"""
Emoji Mapper - ปล่อยให้ emoji แสดงผลตามปกติ

ไฟล์นี้เดิมทำหน้าที่แปลง emoji แต่ตอนนี้ไม่แปลงแล้ว
เพราะฟอนต์สมัยใหม่รองรับ emoji อยู่แล้ว
"""

def replace_emojis(text: str) -> str:
    """
    ไม่แปลง emoji - ปล่อยให้ฟอนต์รองรับ emoji แสดงผลเอง
    
    Args:
        text: ข้อความที่มี emoji
    
    Returns:
        ข้อความเดิม (ไม่แปลง)
    """
    # ไม่ต้องแปลง emoji เพราะฟอนต์สมัยใหม่รองรับ emoji อยู่แล้ว
    # การแปลงเป็น HTML tags จะทำให้ WeasyPrint แสดงผลไม่ถูกต้อง
    return text


if __name__ == "__main__":
    # ทดสอบ
    test_text = """
    ✅ Completed
    ❌ Failed
    📋 Document
    🚚 Shipping
    """
    
    print("Original:")
    print(test_text)
    print("\nProcessed (ไม่เปลี่ยนแปลง):")
    print(replace_emojis(test_text))
