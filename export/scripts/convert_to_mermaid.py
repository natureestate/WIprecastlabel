#!/usr/bin/env python3
"""
ASCII to Mermaid Converter Helper
สคริปต์ช่วยแปลง ASCII art diagrams เป็น Mermaid syntax
"""

import re
from pathlib import Path

def convert_user_manual_to_mermaid(input_file: Path, output_file: Path):
    """
    แปลง USER_MANUAL.md โดยแทนที่ ASCII art ด้วย Mermaid diagrams
    
    Args:
        input_file: ไฟล์ USER_MANUAL.md ต้นฉบับ
        output_file: ไฟล์ที่จะบันทึก (มี Mermaid)
    """
    
    print("=" * 60)
    print("  แปลง ASCII Art → Mermaid Diagrams")
    print("=" * 60)
    print()
    
    # อ่านไฟล์ต้นฉบับ
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Main Workflow Diagram (บรรทัด 129-226)
    main_workflow_mermaid = """```mermaid
graph TD
    Start([เริ่มต้น]) --> Planning[ฝ่ายวางแผน<br/>PLANNING]
    Planning --> Print[1. พิมพ์ฉลาก<br/>PENDING]
    Print --> Activate[2. Scan & Activate<br/>ACTIVATED]
    Activate --> Produce[3. หล่อชิ้นงาน<br/>PRODUCED]
    
    Produce --> QC[ฝ่าย QC<br/>ตรวจสอบคุณภาพ]
    QC --> QCDecision{ผ่าน QC?}
    
    QCDecision -->|ผ่าน| QCPass[QC PASSED]
    QCDecision -->|ไม่ผ่าน| QCFail[QC FAILED]
    QCFail --> Fix[แก้ไข/ทำใหม่]
    Fix --> QC
    
    QCPass --> Warehouse[ฝ่ายคลัง<br/>WAREHOUSE]
    Warehouse --> InStock[5. รับเข้าคลัง<br/>IN_STOCK]
    
    InStock --> Shipping[ฝ่ายจัดส่ง<br/>SHIPPING]
    Shipping --> Ship[6. จัดส่ง<br/>SHIPPING]
    Ship --> Delivered[7. ส่งถึง<br/>DELIVERED]
    
    Delivered --> Installation[ฝ่ายติดตั้ง<br/>INSTALLATION]
    Installation --> Installing[8. กำลังติดตั้ง<br/>INSTALLING]
    Installing --> Installed[9. ติดตั้งเสร็จ<br/>INSTALLED]
    Installed --> Archive[10. จบงาน<br/>ARCHIVED]
    
    style Planning fill:#fff3e0
    style QC fill:#f3e5f5
    style Warehouse fill:#e8f5e9
    style Shipping fill:#fce4ec
    style Installation fill:#e0f2f1
    style QCPass fill:#c8e6c9
    style QCFail fill:#ffcdd2
```"""
    
    # หา ASCII art block แรก (Main Workflow)
    # Pattern: ```\n┌──────... ถึง └───────────┘\n```
    ascii_pattern_1 = r'```\n┌──────────────────────────────────────────────────────────────────────────────┐.*?└───────────┘\n```'
    
    # แทนที่ ASCII art ด้วย Mermaid
    content = re.sub(ascii_pattern_1, main_workflow_mermaid, content, count=1, flags=re.DOTALL)
    
    print("✅ แปลง Main Workflow Diagram")
    
    # Planning Flow Diagram
    planning_flow_mermaid = """```mermaid
flowchart TD
    Start([เริ่มต้น]) --> HasOrder{มีคำสั่งผลิต<br/>ใหม่?}
    HasOrder -->|ไม่มี| End([รอคำสั่ง])
    HasOrder -->|มี| Login[1. Login เข้าระบบ]
    
    Login --> PrintPage[2. ไปหน้าพิมพ์ฉลาก]
    PrintPage --> FillInfo[3. กรอกข้อมูล]
    FillInfo --> AddItems[4. เพิ่มรายการ]
    AddItems --> SelectTemplate[5. เลือกเทมเพลต]
    SelectTemplate --> Customize{ต้องการ<br/>ปรับแต่ง?}
    Customize -->|ใช่| Edit[6. ปรับแต่ง]
    Customize -->|ไม่| PrintPDF[7. กดพิมพ์ PDF]
    Edit --> PrintPDF
    PrintPDF --> Attach[8. พิมพ์และติดฉลาก]
    Attach --> Cast[9. หล่อชิ้นงานเสร็จ]
    Cast --> ActivateBtn[10. กด Activate]
    ActivateBtn --> SendQC[11. ส่งต่อให้ QC]
    
    style Start fill:#e3f2fd
    style End fill:#ffebee
    style PrintPDF fill:#fff9c4
    style ActivateBtn fill:#c8e6c9
```"""
    
    # แทนที่ Planning Flow
    ascii_pattern_2 = r'```\n┌────────────────────────────────────────────────────────────────────┐\n│\s+FLOW การทำงานของ PLANNING.*?└─────────────────────┘\n```'
    content = re.sub(ascii_pattern_2, planning_flow_mermaid, content, count=1, flags=re.DOTALL)
    
    print("✅ แปลง Planning Flow Diagram")
    
    # QC Flow Diagram
    qc_flow_mermaid = """```mermaid
flowchart TD
    Start([เริ่มต้น]) --> HasWork{มีชิ้นงาน<br/>รอตรวจ QC?}
    HasWork -->|ไม่มี| End([รอชิ้นงาน])
    HasWork -->|มี| Login[1. Login เข้าระบบ]
    Login --> ScanPage[2. ไปหน้า Scan]
    ScanPage --> ScanQR[3. Scan QR Code]
    ScanQR --> ViewInfo[4. ดูข้อมูลชิ้นงาน]
    ViewInfo --> Inspect[5. ตรวจสอบคุณภาพ]
    Inspect --> Decision{ผ่าน QC?}
    Decision -->|ผ่าน| Pass[6a. กด QC Pass]
    Decision -->|ไม่ผ่าน| Fail[6b. กด QC Fail]
    Fail --> Note[7. กรอกหมายเหตุ]
    Note --> Return[8. ส่งกลับให้แก้ไข]
    Pass --> SendWarehouse[9. ส่งต่อให้ Warehouse]
    
    style Start fill:#e3f2fd
    style End fill:#ffebee
    style Pass fill:#c8e6c9
    style Fail fill:#ffcdd2
```"""
    
    # แทนที่ QC Flow
    ascii_pattern_3 = r'```\n┌────────────────────────────────────────────────────────────────────┐\n│\s+FLOW การทำงานของ QC.*?└───────────────┘\n```'
    content = re.sub(ascii_pattern_3, qc_flow_mermaid, content, count=1, flags=re.DOTALL)
    
    print("✅ แปลง QC Flow Diagram")
    
    # บันทึกไฟล์
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print()
    print("=" * 60)
    print("  ✅ แปลงเสร็จสิ้น!")
    print("=" * 60)
    print(f"\n📄 ไฟล์ใหม่: {output_file}")
    print("\n💡 ขั้นตอนต่อไป:")
    print("   1. ตรวจสอบไฟล์ที่สร้างขึ้น")
    print("   2. Export PDF ด้วย: python3 export/scripts/export_pdf.py --all")
    print("   3. Mermaid diagrams จะถูกแปลงเป็น SVG อัตโนมัติ")


def main():
    """ฟังก์ชันหลัก"""
    project_root = Path(__file__).parent.parent.parent
    
    input_file = project_root / "docs" / "USER_MANUAL.md"
    output_file = project_root / "docs" / "USER_MANUAL_with_mermaid.md"
    
    if not input_file.exists():
        print(f"❌ ไม่พบไฟล์: {input_file}")
        return
    
    # สำรองไฟล์เดิม
    backup_file = project_root / "docs" / "USER_MANUAL_backup.md"
    if not backup_file.exists():
        import shutil
        shutil.copy2(input_file, backup_file)
        print(f"💾 สำรองไฟล์เดิมไว้ที่: {backup_file}\n")
    
    convert_user_manual_to_mermaid(input_file, output_file)


if __name__ == "__main__":
    main()
