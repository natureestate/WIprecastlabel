#!/usr/bin/env python3
"""
สคริปต์ดาวน์โหลดฟอนต์ Monospace สำหรับ ASCII Art
ใช้ IBM Plex Mono Thai ที่รองรับภาษาไทยและมี fixed-width spacing
"""

import os
import requests
import zipfile
from pathlib import Path

# กำหนด path
SCRIPT_DIR = Path(__file__).parent
FONTS_DIR = SCRIPT_DIR.parent / "fonts"
MONO_FONT_DIR = FONTS_DIR / "IBMPlexMonoThai"

# URL สำหรับดาวน์โหลด IBM Plex Mono Thai
IBM_PLEX_MONO_THAI_URL = "https://github.com/IBM/plex/releases/download/v6.4.0/TrueType.zip"

def download_ibm_plex_mono_thai():
    """ดาวน์โหลดและติดตั้ง IBM Plex Mono Thai"""
    
    print("🔽 กำลังดาวน์โหลด IBM Plex Mono Thai...")
    
    # สร้างโฟลเดอร์
    MONO_FONT_DIR.mkdir(parents=True, exist_ok=True)
    
    # ดาวน์โหลด zip file
    zip_path = FONTS_DIR / "IBMPlexMono.zip"
    
    try:
        response = requests.get(IBM_PLEX_MONO_THAI_URL, stream=True)
        response.raise_for_status()
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print("✅ ดาวน์โหลดเสร็จสิ้น")
        
        # แตกไฟล์ zip
        print("📦 กำลังแตกไฟล์...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # แตกเฉพาะไฟล์ IBM Plex Mono Thai
            for file in zip_ref.namelist():
                if 'IBM-Plex-Mono' in file and file.endswith('.ttf'):
                    # แตกไฟล์ไปยังโฟลเดอร์ปลายทาง
                    zip_ref.extract(file, FONTS_DIR)
                    
                    # ย้ายไฟล์ไปยังโฟลเดอร์ที่ต้องการ
                    source = FONTS_DIR / file
                    dest = MONO_FONT_DIR / Path(file).name
                    source.rename(dest)
                    print(f"  ✓ {Path(file).name}")
        
        # ลบไฟล์ zip
        zip_path.unlink()
        
        # ลบโฟลเดอร์ชั่วคราว
        temp_dir = FONTS_DIR / "TrueType"
        if temp_dir.exists():
            import shutil
            shutil.rmtree(temp_dir)
        
        print(f"\n✅ ติดตั้ง IBM Plex Mono Thai เรียบร้อยแล้ว")
        print(f"📁 ตำแหน่ง: {MONO_FONT_DIR}")
        
        # แสดงรายการไฟล์ที่ติดตั้ง
        fonts = list(MONO_FONT_DIR.glob("*.ttf"))
        print(f"\n📝 ติดตั้งฟอนต์ทั้งหมด {len(fonts)} ไฟล์:")
        for font in sorted(fonts):
            print(f"  • {font.name}")
            
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        if zip_path.exists():
            zip_path.unlink()
        raise

def main():
    """ฟังก์ชันหลัก"""
    print("=" * 60)
    print("  ดาวน์โหลดฟอนต์ Monospace สำหรับ ASCII Art")
    print("=" * 60)
    print()
    
    # ตรวจสอบว่ามีฟอนต์อยู่แล้วหรือไม่
    if MONO_FONT_DIR.exists() and list(MONO_FONT_DIR.glob("*.ttf")):
        print(f"⚠️  พบฟอนต์ IBM Plex Mono Thai อยู่แล้วที่: {MONO_FONT_DIR}")
        response = input("ต้องการดาวน์โหลดใหม่หรือไม่? (y/N): ")
        if response.lower() != 'y':
            print("ยกเลิกการดาวน์โหลด")
            return
    
    download_ibm_plex_mono_thai()
    
    print("\n" + "=" * 60)
    print("  เสร็จสิ้น!")
    print("=" * 60)

if __name__ == "__main__":
    main()
