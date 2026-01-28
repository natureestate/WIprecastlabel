"""
Emoji Mapper - แปลง Emoji เป็น Lucide Icons

ไฟล์นี้ทำหน้าที่แปลง emoji ที่ใช้ในเอกสาร markdown 
เป็น SVG icons จาก Lucide Icons เพื่อให้แสดงผลสวยงามใน PDF
"""

import re
from pathlib import Path

# Mapping จาก Emoji ไปยัง Lucide Icon Name
EMOJI_TO_LUCIDE = {
    # Status & Checkmarks
    "✅": "check-circle",
    "❌": "x-circle",
    "☐": "square",
    "☑": "check-square",
    "□": "square",
    
    # Objects
    "📋": "clipboard",
    "📧": "mail",
    "📱": "smartphone",
    "📦": "package",
    "🖨️": "printer",
    "📄": "file-text",
    "📊": "bar-chart",
    "📈": "trending-up",
    "📉": "trending-down",
    "📅": "calendar",
    "📌": "map-pin",
    "📎": "paperclip",
    
    # People & Roles
    "👑": "crown",
    "👤": "user",
    "👥": "users",
    "🔧": "wrench",
    "🏭": "factory",
    
    # Security & Access
    "🔒": "lock",
    "🔓": "lock-open",
    "🔑": "key",
    
    # Transportation
    "🚚": "truck",
    "🚛": "truck",
    "🚗": "car",
    
    # Status Indicators
    "🟢": "circle",  # Will be colored green in CSS
    "🟡": "circle",  # Will be colored yellow in CSS
    "🔴": "circle",  # Will be colored red in CSS
    "⚠️": "alert-triangle",
    "ℹ️": "info",
    "💡": "lightbulb",
    
    # Actions
    "▶": "play",
    "⏸": "pause",
    "⏹": "square",
    "⏺": "circle",
    "▼": "chevron-down",
    "▲": "chevron-up",
    "►": "chevron-right",
    "◄": "chevron-left",
    
    # Time
    "⏰": "clock",
    "⏱": "timer",
    
    # Building & Construction
    "🏗️": "building-2",
    "🏢": "building",
    
    # Tools
    "⚙️": "settings",
    "🔨": "hammer",
}


def get_icon_svg(icon_name: str, size: str = "md", color: str = None) -> str:
    """
    สร้าง HTML สำหรับแสดง Lucide icon
    
    Args:
        icon_name: ชื่อ icon จาก Lucide
        size: ขนาด icon (sm, md, lg)
        color: สีของ icon (ถ้ามี)
    
    Returns:
        HTML string ของ icon
    """
    color_class = f" icon-{color}" if color else ""
    
    # สำหรับ PDF export เราใช้ inline SVG หรือ CSS icon class
    return f'<span class="icon icon-{size}{color_class}" data-icon="{icon_name}"></span>'


def replace_emojis(text: str) -> str:
    """
    แทนที่ emoji ทั้งหมดในข้อความด้วย Lucide icons
    
    Args:
        text: ข้อความที่มี emoji
    
    Returns:
        ข้อความที่แทนที่ emoji ด้วย icon HTML
    """
    result = text
    
    # แทนที่ emoji ตาม mapping
    for emoji, icon_name in EMOJI_TO_LUCIDE.items():
        if emoji in result:
            # ตรวจสอบว่าเป็น status circle หรือไม่
            color = None
            if emoji == "🟢":
                color = "green"
            elif emoji == "🟡":
                color = "yellow"
            elif emoji == "🔴":
                color = "red"
            
            icon_html = get_icon_svg(icon_name, size="md", color=color)
            result = result.replace(emoji, icon_html)
    
    return result


def process_markdown_file(input_path: Path, output_path: Path = None) -> str:
    """
    ประมวลผลไฟล์ markdown และแทนที่ emoji ทั้งหมด
    
    Args:
        input_path: path ของไฟล์ markdown ต้นฉบับ
        output_path: path สำหรับบันทึกไฟล์ผลลัพธ์ (ถ้าไม่ระบุจะ return string)
    
    Returns:
        เนื้อหา markdown ที่แทนที่ emoji แล้ว
    """
    # อ่านไฟล์ต้นฉบับ
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # แทนที่ emoji
    processed_content = replace_emojis(content)
    
    # บันทึกไฟล์ถ้าระบุ output_path
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)
    
    return processed_content


if __name__ == "__main__":
    # ทดสอบ emoji mapper
    test_text = """
    ✅ Completed
    ❌ Failed
    📋 Document
    🚚 Shipping
    🔧 Installation
    🟢 Active
    🟡 Pending
    🔴 Suspended
    """
    
    print("Original:")
    print(test_text)
    print("\nProcessed:")
    print(replace_emojis(test_text))
