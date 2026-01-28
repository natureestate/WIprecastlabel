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
        แปลง markdown เป็น HTML
        
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
            'toc',
            'nl2br',  # New line to <br>
            'sane_lists',
        ])
        
        # แปลง markdown → HTML
        html_content = md.convert(markdown_text)
        
        # Extract TOC
        toc_items = self._extract_toc_from_html(html_content)
        
        return html_content, toc_items
    
    def _extract_toc_from_html(self, html: str) -> list:
        """
        ดึงรายการ TOC จาก HTML
        
        Args:
            html: HTML content
        
        Returns:
            รายการ TOC
        """
        toc_items = []
        
        # ค้นหา headings (h1, h2, h3)
        heading_pattern = r'<h([1-3])[^>]*>([^<]+)</h\1>'
        matches = re.finditer(heading_pattern, html)
        
        for match in matches:
            level = int(match.group(1))
            title = match.group(2).strip()
            
            # ข้าม "สารบัญ" ตัวเอง
            if title.lower() not in ['สารบัญ', 'table of contents']:
                toc_items.append({
                    "title": title,
                    "level": level,
                    "page": "..."  # จะถูกแทนที่ด้วย page number จริงโดย CSS
                })
        
        return toc_items
    
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
        
        # สร้าง PDF
        html = HTML(string=html_content, base_url=str(self.project_root))
        html.write_pdf(
            output_path,
            stylesheets=css_files,
            font_config=self.font_config
        )
        
        print(f"✅ Export สำเร็จ: {output_path}")
        print(f"   ขนาดไฟล์: {output_path.stat().st_size / 1024:.1f} KB")
    
    def process_file(
        self,
        input_file: Path,
        output_file: Path,
        title: str = None,
        subtitle: str = "",
        version: str = "1.0",
        author: str = "WIPrecastLabel Team",
        front_cover_image: Path = None,
        back_cover_image: Path = None
    ):
        """
        ประมวลผลไฟล์ markdown และ export เป็น PDF
        
        Args:
            input_file: ไฟล์ markdown ต้นฉบับ
            output_file: ไฟล์ PDF ปลายทาง
            title: ชื่อเอกสาร
            subtitle: คำอธิบาย
            version: เวอร์ชัน
            author: ผู้แต่ง
        """
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
        
        # 4. แปลง markdown → HTML
        print("4️⃣ แปลง markdown → HTML...")
        content_html, toc_items = self.convert_markdown_to_html(markdown_text)
        
        # 5. สร้าง complete HTML
        print("5️⃣ สร้าง HTML ฉบับสมบูรณ์...")
        complete_html = self.create_complete_html(
            content_html=content_html,
            toc_items=toc_items,
            title=title,
            subtitle=subtitle,
            version=version,
            author=author,
            front_cover_image=front_cover_image,
            back_cover_image=back_cover_image
        )
        
        # 6. Export PDF
        print("6️⃣ Export PDF...")
        self.export_to_pdf(complete_html, output_file)
        
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
