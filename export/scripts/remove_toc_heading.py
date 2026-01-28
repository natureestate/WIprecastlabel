#!/usr/bin/env python3
"""
สคริปต์ลบ heading "สารบัญ" ออกจาก markdown
เพื่อป้องกันสารบัญซ้ำใน PDF
"""

import re
from pathlib import Path

def remove_toc_heading(markdown_text: str) -> str:
    """
    ลบ heading "สารบัญ" ออกจาก markdown
    
    Args:
        markdown_text: เนื้อหา markdown
    
    Returns:
        markdown ที่ลบ heading "สารบัญ" แล้ว
    """
    # Pattern สำหรับหา heading "สารบัญ"
    patterns = [
        r'^#\s*สารบัญ\s*$',
        r'^##\s*สารบัญ\s*$',
        r'^###\s*สารบัญ\s*$',
    ]
    
    result = markdown_text
    
    for pattern in patterns:
        result = re.sub(pattern, '', result, flags=re.MULTILINE)
    
    # ลบบรรทัดว่างที่เกิน 2 บรรทัดติดกัน
    result = re.sub(r'\n{3,}', '\n\n', result)
    
    return result


def process_file(input_file: Path, output_file: Path = None):
    """
    ประมวลผลไฟล์ markdown
    
    Args:
        input_file: ไฟล์ต้นฉบับ
        output_file: ไฟล์ปลายทาง (ถ้าไม่ระบุจะเขียนทับไฟล์เดิม)
    """
    # อ่านไฟล์
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # ลบ heading "สารบัญ"
    processed = remove_toc_heading(content)
    
    # บันทึกไฟล์
    if output_file is None:
        output_file = input_file
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(processed)
    
    print(f"✅ ลบ heading 'สารบัญ' จาก {input_file.name}")


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent.parent
    
    # ประมวลผลทั้ง 2 ไฟล์
    files = [
        project_root / "docs" / "USER_MANUAL.md",
        project_root / "docs" / "WORKFLOW_GUIDE.md",
    ]
    
    for file in files:
        if file.exists():
            process_file(file)
