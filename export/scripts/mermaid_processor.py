#!/usr/bin/env python3
"""
Mermaid Diagram Processor
แปลง Mermaid diagrams ใน markdown เป็น SVG images สำหรับ PDF
"""

import re
import subprocess
import tempfile
from pathlib import Path
from typing import List, Tuple

class MermaidProcessor:
    """ประมวลผล Mermaid diagrams"""
    
    def __init__(self, output_dir: Path = None):
        """
        Initialize Mermaid Processor
        
        Args:
            output_dir: โฟลเดอร์สำหรับเก็บ SVG ที่สร้าง
        """
        if output_dir is None:
            output_dir = Path(__file__).parent.parent / "assets" / "diagrams"
        
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # ตรวจสอบว่ามี mmdc (mermaid-cli) หรือไม่
        self.has_mmdc = self._check_mmdc()
    
    def _check_mmdc(self) -> bool:
        """ตรวจสอบว่ามี mermaid-cli ติดตั้งหรือไม่"""
        try:
            result = subprocess.run(
                ["mmdc", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
    
    def extract_mermaid_blocks(self, markdown_text: str) -> List[Tuple[str, str]]:
        """
        ดึง Mermaid code blocks จาก markdown
        
        Args:
            markdown_text: เนื้อหา markdown
        
        Returns:
            List of (mermaid_code, block_id)
        """
        # Pattern สำหรับ Mermaid code blocks
        pattern = r'```mermaid\n(.*?)```'
        matches = re.finditer(pattern, markdown_text, re.DOTALL)
        
        blocks = []
        for i, match in enumerate(matches):
            mermaid_code = match.group(1).strip()
            block_id = f"diagram_{i+1}"
            blocks.append((mermaid_code, block_id))
        
        return blocks
    
    def render_mermaid_to_svg(self, mermaid_code: str, output_file: Path) -> bool:
        """
        แปลง Mermaid code เป็น SVG
        
        Args:
            mermaid_code: Mermaid diagram code
            output_file: path สำหรับบันทึก SVG
        
        Returns:
            True ถ้าสำเร็จ, False ถ้าล้มเหลว
        """
        if not self.has_mmdc:
            print("⚠️  ไม่พบ mermaid-cli (mmdc)")
            print("   ติดตั้งด้วย: npm install -g @mermaid-js/mermaid-cli")
            return False
        
        # สร้างไฟล์ชั่วคราวสำหรับ Mermaid code
        with tempfile.NamedTemporaryFile(
            mode='w',
            suffix='.mmd',
            delete=False,
            encoding='utf-8'
        ) as temp_file:
            temp_file.write(mermaid_code)
            temp_path = Path(temp_file.name)
        
        try:
            # รัน mmdc เพื่อแปลงเป็น SVG
            result = subprocess.run(
                [
                    "mmdc",
                    "-i", str(temp_path),
                    "-o", str(output_file),
                    "-t", "neutral",  # theme
                    "-b", "transparent",  # background
                ],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                return True
            else:
                print(f"❌ Error rendering Mermaid: {result.stderr}")
                return False
        
        except subprocess.TimeoutExpired:
            print("❌ Timeout rendering Mermaid diagram")
            return False
        
        finally:
            # ลบไฟล์ชั่วคราว
            temp_path.unlink(missing_ok=True)
    
    def process_markdown(self, markdown_text: str) -> str:
        """
        ประมวลผล markdown โดยแปลง Mermaid blocks เป็น images
        
        Args:
            markdown_text: เนื้อหา markdown
        
        Returns:
            markdown ที่แปลง Mermaid blocks เป็น image tags แล้ว
        """
        if not self.has_mmdc:
            print("⚠️  ข้าม Mermaid processing (ไม่มี mmdc)")
            return markdown_text
        
        # ดึง Mermaid blocks
        blocks = self.extract_mermaid_blocks(markdown_text)
        
        if not blocks:
            return markdown_text
        
        print(f"📊 พบ Mermaid diagrams {len(blocks)} รายการ")
        
        # แปลงแต่ละ block
        processed_text = markdown_text
        
        for mermaid_code, block_id in blocks:
            svg_file = self.output_dir / f"{block_id}.svg"
            
            print(f"   • กำลังสร้าง {block_id}.svg...")
            
            if self.render_mermaid_to_svg(mermaid_code, svg_file):
                # แทนที่ Mermaid block ด้วย image tag
                original_block = f"```mermaid\n{mermaid_code}\n```"
                image_tag = f'![{block_id}]({svg_file})'
                
                processed_text = processed_text.replace(original_block, image_tag)
                print(f"     ✓ สำเร็จ")
            else:
                print(f"     ✗ ล้มเหลว")
        
        return processed_text


def install_mermaid_cli():
    """แนะนำวิธีติดตั้ง mermaid-cli"""
    print("\n" + "=" * 60)
    print("  การติดตั้ง Mermaid CLI")
    print("=" * 60)
    print()
    print("Mermaid CLI ใช้สำหรับแปลง Mermaid diagrams เป็น SVG")
    print()
    print("วิธีติดตั้ง:")
    print("  1. ติดตั้ง Node.js (ถ้ายังไม่มี):")
    print("     https://nodejs.org/")
    print()
    print("  2. ติดตั้ง Mermaid CLI:")
    print("     npm install -g @mermaid-js/mermaid-cli")
    print()
    print("  3. ทดสอบว่าติดตั้งสำเร็จ:")
    print("     mmdc --version")
    print()


if __name__ == "__main__":
    # ทดสอบ
    processor = MermaidProcessor()
    
    if not processor.has_mmdc:
        install_mermaid_cli()
    else:
        print("✅ Mermaid CLI พร้อมใช้งาน")
        
        # ทดสอบด้วย diagram ง่ายๆ
        test_mermaid = """
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[OK]
    B -->|No| D[Cancel]
    C --> E[End]
    D --> E
"""
        
        test_file = processor.output_dir / "test_diagram.svg"
        if processor.render_mermaid_to_svg(test_mermaid, test_file):
            print(f"✅ ทดสอบสร้าง diagram สำเร็จ: {test_file}")
        else:
            print("❌ ทดสอบสร้าง diagram ล้มเหลว")
