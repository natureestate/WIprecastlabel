"""
Emoji Mapper - แปลง Emoji เป็น Lucide Icons สำหรับ WeasyPrint
"""
import re

# Mapping ตาราง Emoji -> Lucide Icon Name (ต้องตรงกับไฟล์ใน export/assets/icons/*.svg)
EMOJI_TO_ICON = {
    # Status Icons
    "✅": "check-circle",
    "❌": "x-circle",
    "⚠️": "alert-triangle",
    "🟡": "clock",             # Pending
    "🔴": "x-circle",          # Error/Fail
    "🟢": "check-circle",      # Active/Pass
    "🔵": "circle",            # Blue circle (General)
    "🟣": "package",           # Stock (Purple)
    "🟠": "truck",             # Shipping (Orange)
    "⚪️": "file-text",         # Archive (White)
    "⚪": "file-text",
    
    # Role Icons
    "👑": "crown",             # Admin
    "📋": "clipboard",         # Planning
    "📦": "package",           # Warehouse
    "🚚": "truck",             # Shipping
    "🔧": "wrench",            # Installation
    "👷": "user",              # Worker
    "📱": "smartphone",        # Mobile / Scan
    "👤": "user",
    "👥": "users",
    
    # Action Icons
    "🖨️": "printer",
    "🔍": "file-text",         # Search (ไม่มี icon search ใช้ file-text แทนไปก่อน)
    "📷": "smartphone",        # Camera/Scan (ใช้ smartphone แทน)
    "📝": "file-text",         # Form
    "💾": "check-square",      # Save (ไม่มี save ใช้ check-square)
    "🗑️": "x-circle",          # Delete
    "🔄": "refresh-cw",        # Refresh (ไม่มี file refresh-cw?? เช็คอีกที... ไม่มี ใช้ clock แทน) -> "clock"
    "📤": "truck",             # Upload/Shipping
    "📥": "package",           # Download/Stock
    "⚙️": "settings",
    "🔒": "lock",
    "📧": "mail",
    "🏗️": "factory",           # Construction/Factory
    "🏭": "factory",
    
    # Direction Icons
    "➡️": "chevron-right",
    "⬅️": "chevron-left",
    "⬆️": "chevron-up",
    "⬇️": "chevron-down",
    "▶️": "play",
    
    # Misc
    "📅": "calendar",
    "🕒": "clock",
    "📍": "map-pin",
    "🏷️": "tag",               # Label (ไม่มี tag ใช้ info แทน) -> "info"
}

# Override บางตัวที่ไม่มีไฟล์จริง
EMOJI_TO_ICON["🔄"] = "clock"
EMOJI_TO_ICON["🏷️"] = "info"

def replace_emojis(text: str) -> str:
    """
    แปลง Emoji ในข้อความให้เป็น HTML span ที่มี class icon
    Format: <span class="icon icon-md" data-icon="icon-name"></span>
    """
    
    def replace_match(match):
        emoji_char = match.group(0)
        if emoji_char not in EMOJI_TO_ICON:
            return emoji_char
            
        icon_name = EMOJI_TO_ICON[emoji_char]
        
        # เพิ่มสีพิเศษตาม emoji (Optional - ถ้าจะทำต้องเพิ่ม class)
        color_class = ""
        if emoji_char in ["✅", "🟢"]: color_class = " icon-green"
        elif emoji_char in ["❌", "🔴"]: color_class = " icon-red"
        elif emoji_char in ["🟡", "⚠️"]: color_class = " icon-yellow"
        elif emoji_char in ["🔵", "🟦"]: color_class = " icon-blue"
        
        # สร้าง HTML Tag ตาม Format ของ CSS ที่มีอยู่
        return f'<span class="icon icon-md{color_class}" data-icon="{icon_name}"></span>'

    # สร้าง Pattern สำหรับ Regex
    sorted_emojis = sorted(EMOJI_TO_ICON.keys(), key=len, reverse=True)
    pattern = '|'.join(map(re.escape, sorted_emojis))
    
    return re.sub(pattern, replace_match, text)

if __name__ == "__main__":
    test = "Status: ✅ Passed ❌ Failed 📦 Stock 🚚 Shipping"
    print(replace_emojis(test))
