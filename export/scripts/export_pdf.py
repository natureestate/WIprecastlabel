#!/usr/bin/env python3
"""
Export PDF - แปลง Markdown เป็น PDF ด้วย WeasyPrint

ไฟล์นี้เป็น main script สำหรับแปลงเอกสาร markdown เป็น PDF
พร้อมหน้าปก, สารบัญ, header/footer, และ custom fonts
"""

import argparse
import re
import sys
from pathlib import Path
from datetime import datetime

try:
    import markdown
    from markdown.extensions import tables, fenced_code, codehilite, toc
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
    import pypdf
    import io
except ImportError as e:
    print(f"❌ Error: Missing required library: {e}")
    print("กรุณาติดตั้ง dependencies ด้วย: pip install -r requirements.txt")
    sys.exit(1)

# Import modules อื่นๆ
from emoji_mapper import replace_emojis
from cover_generator import create_cover_html, create_toc_html, create_back_cover_html
from mermaid_processor import MermaidProcessor


class PDFExporter:
    """คลาสหลักสำหรับ export PDF"""
    
    def __init__(self, project_root: Path = None):
        """
        Initialize PDF Exporter
        
        Args:
            project_root: root directory ของโปรเจกต์
        """
        if project_root is None:
            project_root = Path(__file__).parent.parent.parent
        
        self.project_root = Path(project_root)
        self.export_dir = self.project_root / "export"
        self.templates_dir = self.export_dir / "templates"
        self.styles_dir = self.export_dir / "styles"
        self.fonts_dir = self.export_dir / "fonts"
        self.assets_dir = self.export_dir / "assets"
        
        # Font configuration สำหรับ WeasyPrint
        self.font_config = FontConfiguration()
        
        # Mermaid processor สำหรับแปลง diagrams
        self.mermaid_processor = MermaidProcessor(
            output_dir=self.assets_dir / "diagrams"
        )
    
    def load_markdown(self, filepath: Path) -> str:
        """
        โหลดไฟล์ markdown
        
        Args:
            filepath: path ของไฟล์ markdown
        
        Returns:
            เนื้อหา markdown
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    def convert_markdown_to_html(self, markdown_text: str) -> tuple:
        """
        แปลง markdown เป็น HTML และสร้าง TOC พร้อม ID ที่ตรงกัน
        
        Args:
            markdown_text: เนื้อหา markdown
        
        Returns:
            tuple (html_content, toc_items)
        """
        # Extensions สำหรับ markdown
        md = markdown.Markdown(extensions=[
            'tables',
            'fenced_code',
            'codehilite',
            'nl2br',
            'sane_lists',
            # เอา 'toc' ออกเพื่อจัดการ ID เองให้ชัวร์
        ])
        
        # แปลง markdown → HTML ดิบ
        raw_html = md.convert(markdown_text)
        
        # Process Headings: เติม ID และสร้างรายการ TOC
        # ใช้เทคนิคนี้เพื่อการันตีว่า ID ในเนื้อหากับ TOC ตรงกันแน่นอน
        html_content, toc_items = self._inject_ids_and_extract_toc(raw_html)
        
        return html_content, toc_items
    
    def _inject_ids_and_extract_toc(self, html: str) -> tuple:
        """
        เติม ID ให้ heading tags และดึงข้อมูลสำหรับ TOC
        """
        toc_items = []
        counter = 0
        
        def replace_header(match):
            nonlocal counter
            counter += 1
            
            level = int(match.group(1)) # capture group 1: ระดับ (1-3)
            # group 2 คือ attributes เก่า (ทิ้งไป)
            text_content = match.group(3) # capture group 3: เนื้อหาข้างใน
            
            # สร้าง ID ใหม่ที่ unique แน่นอน
            heading_id = f"section-{counter}"
            
            # Clean title สำหรับแสดงในสารบัญ (ลบ html tags)
            clean_title = re.sub(r'<[^>]+>', '', text_content).strip()
            
            # เพิ่มลงรายการ TOC (ข้าม heading ที่เป็น title 'สารบัญ')
            if clean_title.lower() not in ['สารบัญ', 'table of contents']:
                toc_items.append({
                    "title": clean_title,
                    "level": level,
                    "id": heading_id
                })
            
            # คืนค่า tag ใหม่ที่มี id ใส่เข้าไป
            return f'<h{level} id="{heading_id}">{text_content}</h{level}>'

        # Regex: <h(1-3) ... > ... </h(1-3)>
        # flags=re.DOTALL เพื่อให้ครอบคลุมกรณี heading มีหลายบรรทัด
        pattern = r'<h([1-3])(.*?)>(.*?)</h\1>'
        new_html = re.sub(pattern, replace_header, html, flags=re.DOTALL)
        
        return new_html, toc_items
    
    def create_complete_html(
        self,
        content_html: str,
        toc_items: list,
        title: str,    
        version: str,
        author: str,
        subtitle: str = "",
        front_cover_image: Path = None,
        back_cover_image: Path = None
    ) -> str:
        """
        สร้าง HTML ฉบับสมบูรณ์พร้อมหน้าปก, สารบัญ, และเนื้อหา
        
        Args:
            content_html: HTML ของเนื้อหาหลัก
            toc_items: รายการสารบัญ
            title: ชื่อเอกสาร
            version: เวอร์ชัน
            author: ผู้แต่ง
            subtitle: คำอธิบาย
        
        Returns:
            HTML ฉบับสมบูรณ์
        """
        # สร้างหน้าปก
        cover_html = create_cover_html(
            title=title,
            subtitle=subtitle,
            version=version,
            author=author,
            cover_image_path=str(front_cover_image) if front_cover_image else None
        )
        
        # สร้างปกหลัง
        back_cover_html = create_back_cover_html(
            image_path=str(back_cover_image) if back_cover_image else None
        )
        
        # สร้างสารบัญ
        toc_html = create_toc_html(toc_items)
        
        # Load CSS files
        css_files = [
            self.styles_dir / "main.css",
            self.styles_dir / "print.css",
            self.styles_dir / "diagrams.css",
            self.styles_dir / "lucide.css",
        ]
        
        css_links = "\n".join([
            f'<link rel="stylesheet" href="{css_file}">'
            for css_file in css_files
        ])
        
        # สร้าง complete HTML
        complete_html = f"""
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {css_links}
</head>
<body>
    <!-- หน้าปก -->
    {cover_html}
    
    <!-- สารบัญ -->
    {toc_html}
    
    <!-- เนื้อหาหลัก -->
    <div class="main-content">
        {content_html}
    </div>
    
    <!-- ปกหลัง -->
    {back_cover_html}
</body>
</html>
        """
        
        return complete_html
    
    def export_to_pdf(
        self,
        html_content: str,
        output_path: Path
    ):
        """
        Export HTML เป็น PDF
        
        Args:
            html_content: HTML ฉบับสมบูรณ์
            output_path: path สำหรับบันทึก PDF
        """
        print(f"📄 กำลัง export PDF...")
        
        # สร้าง output directory ถ้ายังไม่มี
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Load CSS files
        css_files = [
            CSS(str(self.styles_dir / "main.css"), font_config=self.font_config),
            CSS(str(self.styles_dir / "print.css"), font_config=self.font_config),
            CSS(str(self.styles_dir / "diagrams.css"), font_config=self.font_config),
            CSS(str(self.styles_dir / "lucide.css"), font_config=self.font_config),
        ]
        
        # Create HTML document
        doc = HTML(string=html_content, base_url=str(self.project_root)).render(
            stylesheets=css_files,
            font_config=self.font_config
        )
        
        # Write PDF
        doc.write_pdf(output_path)
        
        return output_path
        
    def _export_to_pdf_bytes(self, html_content: str) -> bytes:
        """Export PDF to bytes (for pass 1)"""
        css_files = [
            CSS(str(self.styles_dir / "main.css"), font_config=self.font_config),
            CSS(str(self.styles_dir / "print.css"), font_config=self.font_config),
            CSS(str(self.styles_dir / "diagrams.css"), font_config=self.font_config),
            CSS(str(self.styles_dir / "lucide.css"), font_config=self.font_config),
        ]
        
        doc = HTML(string=html_content, base_url=str(self.project_root)).render(
            stylesheets=css_files,
            font_config=self.font_config
        )
        
        return doc.write_pdf()

    def _extract_page_numbers_from_pdf(self, pdf_bytes: bytes) -> dict:
        """Extract page numbers from PDF bookmarks"""
        pdf = pypdf.PdfReader(io.BytesIO(pdf_bytes))
        page_map = {}
        
        def _process_outline(outlines):
            for item in outlines:
                if isinstance(item, list):
                    _process_outline(item)
                else:
                    # pypdf outline item: {'/Title': '...', '/Page': IndirectObject(...), ...}
                    try:
                        title = item.title
                        
                        # Get page number
                        page_index = pdf.get_destination_page_number(item)
                        if page_index is not None:
                             # Page index is 0-based, display page is 1-based
                             # แต่เราต้องการ ID, ไม่ใช่ Title. 
                             # WeasyPrint สร้าง Named Destination จาก ID ของ Heading
                             # แต่ pypdf outline ไม่เก็บ Named Dest. ง่ายๆ
                             # Trick: เราจะใช้ "Title" แมพกลับไปหา ID จาก toc_items ที่เรามีอยู่แล้ว
                             # ดังนั้นเก็บ {title: page_num} ไว้ก่อน
                             page_map[title.strip()] = page_index + 1
                    except Exception as e:
                        print(f"⚠️ Warning extract outline: {e}")
                        continue
                        
        if pdf.outline:
            _process_outline(pdf.outline)
            
        return page_map

    def _update_toc_items_with_pages(self, toc_items: list, page_map: dict):
        """Update toc_items with page numbers from page_map"""
        for item in toc_items:
            title = item["title"].replace('&amp;', '&') # Decode html entity if needed
            if title in page_map:
                item["page"] = page_map[title]
            else:
                 # ลอง fuzzy matching หรือดู parent
                 pass

    def process_file(
        self,
        input_file: Path,
        output_file: Path,
        title: str = None,
        subtitle: str = None,
        version: str = "1.0",
        author: str = "WI Precast Label Team",
        front_cover_image: Path = None,
        back_cover_image: Path = None
    ):
        """ประมวลผลไฟล์เดียว (2-Pass Rendering)"""
        print(f"\n{'='*60}")
        print(f"📖 กำลังประมวลผล: {input_file.name}")
        print(f"{'='*60}\n")
        
        # ใช้ชื่อไฟล์เป็น title ถ้าไม่ระบุ
        if title is None:
            title = input_file.stem.replace('_', ' ').title()
        
        # 1. โหลด markdown
        print("1️⃣ โหลดไฟล์ markdown...")
        markdown_text = self.load_markdown(input_file)
        
        # 2. แทนที่ emoji
        print("2️⃣ แปลง emoji → Lucide icons...")
        markdown_text = replace_emojis(markdown_text)
        
        # 3. ประมวลผล Mermaid diagrams
        print("3️⃣ ประมวลผล Mermaid diagrams...")
        markdown_text = self.mermaid_processor.process_markdown(markdown_text)
        
        # 4. แปลง markdown → HTML และได้ TOC (ยังไม่มีเลขหน้า)
        print("4️⃣ แปลง markdown → HTML...")
        content_html, toc_items = self.convert_markdown_to_html(markdown_text)
        
        # --- PASS 1: Generate Temporary PDF to find page numbers ---
        print("🔄 Pass 1: คำนวณเลขหน้า...")
        
        # สร้าง HTML สำหรับ Pass 1 (TOC ไม่มีเลขหน้า)
        temp_html = self.create_complete_html(
            content_html=content_html,
            toc_items=toc_items,
            title=title,
            subtitle=subtitle,
            version=version,
            author=author,
            front_cover_image=front_cover_image,
            back_cover_image=back_cover_image
        )
        
        try:
            # Generate PDF Memory
            pdf_bytes = self._export_to_pdf_bytes(temp_html)
            
            # Extract Page Numbers
            page_map = self._extract_page_numbers_from_pdf(pdf_bytes)
            print(f"   ✓ พบจุดอ้างอิง {len(page_map)} จุด")
            
            # Update TOC with real page numbers
            self._update_toc_items_with_pages(toc_items, page_map)
            
        except Exception as e:
            print(f"⚠️  Error calculating page numbers: {e}")
            import traceback
            traceback.print_exc()
            
        # --- PASS 2: Generate Final PDF ---
        print("5️⃣ สร้าง HTML ฉบับสมบูรณ์ (พร้อมเลขหน้าจริง)...")
        final_html = self.create_complete_html(
            content_html=content_html,
            toc_items=toc_items, # ตอนนี้มี page number ครบแล้ว
            title=title,
            subtitle=subtitle,
            version=version,
            author=author,
            front_cover_image=front_cover_image,
            back_cover_image=back_cover_image
        )
        
        # 6. Export Final PDF
        print("6️⃣ Export PDF...")
        self.export_to_pdf(final_html, output_file)
        
        print(f"✅ Export สำเร็จ: {output_file}")
        print(f"   ขนาดไฟล์: {output_file.stat().st_size / 1024:.1f} KB")
        
        print(f"\n{'='*60}")
        
        print("✨ เสร็จสมบูรณ์!")
        print(f"{'='*60}\n")


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Export Markdown เป็น PDF ด้วย WeasyPrint"
    )
    
    parser.add_argument(
        "--input", "-i",
        type=Path,
        help="ไฟล์ markdown ต้นฉบับ"
    )
    
    parser.add_argument(
        "--output", "-o",
        type=Path,
        help="ไฟล์ PDF ปลายทาง"
    )
    
    parser.add_argument(
        "--title", "-t",
        type=str,
        help="ชื่อเอกสาร"
    )
    
    parser.add_argument(
        "--subtitle", "-s",
        type=str,
        default="",
        help="คำอธิบายเอกสาร"
    )
    
    parser.add_argument(
        "--version", "-v",
        type=str,
        default="1.0",
        help="เวอร์ชันเอกสาร"
    )
    
    parser.add_argument(
        "--author", "-a",
        type=str,
        default="WIPrecastLabel Team",
        help="ผู้แต่ง/บริษัท"
    )
    
    parser.add_argument(
        "--all",
        action="store_true",
        help="Export เอกสารทั้งหมด (USER_MANUAL และ WORKFLOW_GUIDE)"
    )
    
    args = parser.parse_args()
    
    # สร้าง exporter
    exporter = PDFExporter()
    
    # เตรียม path ของรูปปก
    front_cover = exporter.assets_dir / "front-cover.png"
    back_cover = exporter.assets_dir / "back-cover.png"
    
    # Function to append timestamp to filename
    def append_timestamp(path: Path) -> Path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return path.with_name(f"{path.stem}_{timestamp}{path.suffix}")

    # Export ทั้งหมด
    if args.all:
        print("🚀 Export เอกสารทั้งหมด...\n")
        
        files_to_export = [
            {
                "input": exporter.project_root / "docs" / "USER_MANUAL.md",
                "output": exporter.project_root / "output" / "USER_MANUAL.pdf",
                "title": "คู่มือการใช้งาน Precast Pro Labeler",
                "subtitle": "ระบบจัดการและติดตามชิ้นส่วนคอนกรีตสำเร็จรูป",
            },
            {
                "input": exporter.project_root / "docs" / "WORKFLOW_GUIDE.md",
                "output": exporter.project_root / "output" / "WORKFLOW_GUIDE.pdf",
                "title": "คู่มือขั้นตอนการทำงาน",
                "subtitle": "Workflow และ SOP สำหรับพนักงานทุกแผนก",
            },
        ]
        
        for file_info in files_to_export:
            # Append timestamp to output path
            output_file = append_timestamp(file_info["output"])
            
            exporter.process_file(
                input_file=file_info["input"],
                output_file=output_file,
                title=file_info["title"],
                subtitle=file_info["subtitle"],
                version=args.version,
                author=args.author,
                front_cover_image=front_cover,
                back_cover_image=back_cover
            )
    
    # Export ไฟล์เดียว
    elif args.input and args.output:
        # Append timestamp to output path
        output_file = append_timestamp(args.output)
        
        exporter.process_file(
            input_file=args.input,
            output_file=output_file,
            title=args.title,
            subtitle=args.subtitle,
            version=args.version,
            author=args.author,
            front_cover_image=front_cover,
            back_cover_image=back_cover
        )
    
    else:
        parser.print_help()
        print("\n❌ Error: กรุณาระบุ --input และ --output หรือใช้ --all")
        sys.exit(1)


if __name__ == "__main__":
    main()
