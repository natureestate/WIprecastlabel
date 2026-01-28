#!/usr/bin/env python3
"""
สคริปต์จัดระเบียบและติดตั้งฟอนต์ TH Sarabun ใหม่
แก้ไขปัญหา path ที่ไม่ถูกต้อง
"""

import shutil
from pathlib import Path

# กำหนด paths
SCRIPT_DIR = Path(__file__).parent
FONTS_DIR = SCRIPT_DIR.parent / "fonts"
SARABUN_DIR = FONTS_DIR / "Sarabun"

def reorganize_sarabun_fonts():
    """จัดระเบียบฟอนต์ Sarabun ให้อยู่ใน path ที่ถูกต้อง"""
    
    print("=" * 60)
    print("  จัดระเบียบฟอนต์ TH Sarabun")
    print("=" * 60)
    print()
    
    # ตรวจสอบว่ามีโฟลเดอร์ Sarabun/Sarabun หรือไม่
    nested_sarabun = SARABUN_DIR / "Sarabun"
    
    if nested_sarabun.exists():
        print(f"🔍 พบโฟลเดอร์ซ้อน: {nested_sarabun}")
        print("📦 กำลังย้ายไฟล์ฟอนต์...")
        
        # ย้ายไฟล์ .ttf ทั้งหมดขึ้นมา 1 ระดับ
        ttf_files = list(nested_sarabun.glob("*.ttf"))
        
        for ttf_file in ttf_files:
            dest = SARABUN_DIR / ttf_file.name
            if dest.exists():
                dest.unlink()  # ลบไฟล์เก่าถ้ามี
            shutil.move(str(ttf_file), str(dest))
            print(f"  ✓ {ttf_file.name}")
        
        # ลบโฟลเดอร์ซ้อน
        print("\n🗑️  ลบโฟลเดอร์ซ้อน...")
        shutil.rmtree(nested_sarabun)
        print("  ✓ ลบเรียบร้อย")
    
    # ลบโฟลเดอร์ IBM_Plex_Sans_Thai ที่อยู่ผิดที่
    wrong_ibm_dir = SARABUN_DIR / "IBM_Plex_Sans_Thai"
    if wrong_ibm_dir.exists():
        print("\n🗑️  ลบโฟลเดอร์ IBM_Plex_Sans_Thai ที่อยู่ผิดที่...")
        shutil.rmtree(wrong_ibm_dir)
        print("  ✓ ลบเรียบร้อย")
    
    # แสดงรายการฟอนต์ที่ติดตั้ง
    print("\n" + "=" * 60)
    print("  ✅ จัดระเบียบเสร็จสิ้น!")
    print("=" * 60)
    
    fonts = sorted(SARABUN_DIR.glob("*.ttf"))
    print(f"\n📝 ฟอนต์ Sarabun ทั้งหมด ({len(fonts)} ไฟล์):")
    for font in fonts:
        print(f"  • {font.name}")
    
    print(f"\n📁 ตำแหน่ง: {SARABUN_DIR}")

def main():
    """ฟังก์ชันหลัก"""
    try:
        reorganize_sarabun_fonts()
        print("\n✨ สำเร็จ! ตอนนี้ path ของฟอนต์ถูกต้องแล้ว")
        print("💡 ลอง export PDF ใหม่อีกครั้งครับ")
    except Exception as e:
        print(f"\n❌ เกิดข้อผิดพลาด: {e}")
        raise

if __name__ == "__main__":
    main()
