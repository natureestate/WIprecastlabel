#!/usr/bin/env python3
"""
สคริปต์ดาวน์โหลดและติดตั้งฟอนต์ TH Sarabun ใหม่
ดาวน์โหลดจาก Google Fonts และติดตั้งให้พร้อมใช้งาน
"""

import os
import requests
import zipfile
import shutil
from pathlib import Path

# กำหนด paths
SCRIPT_DIR = Path(__file__).parent
FONTS_DIR = SCRIPT_DIR.parent / "fonts"
SARABUN_DIR = FONTS_DIR / "Sarabun"

# URL สำหรับดาวน์โหลด TH Sarabun จาก Google Fonts
SARABUN_URL = "https://fonts.google.com/download?family=Sarabun"

def download_sarabun():
    """ดาวน์โหลดและติดตั้ง TH Sarabun"""
    
    print("=" * 60)
    print("  ดาวน์โหลดและติดตั้งฟอนต์ TH Sarabun")
    print("=" * 60)
    print()
    
    # ลบโฟลเดอร์เก่า (ถ้ามี)
    if SARABUN_DIR.exists():
        print(f"🗑️  ลบโฟลเดอร์เก่า: {SARABUN_DIR}")
        shutil.rmtree(SARABUN_DIR)
    
    # สร้างโฟลเดอร์ใหม่
    SARABUN_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📁 สร้างโฟลเดอร์: {SARABUN_DIR}")
    
    # ดาวน์โหลด zip file
    zip_path = FONTS_DIR / "Sarabun.zip"
    
    print(f"\n🔽 กำลังดาวน์โหลดจาก Google Fonts...")
    
    try:
        # ดาวน์โหลดโดยตรงจาก GitHub (Google Fonts repository)
        # เพราะ Google Fonts API ต้องการ API key
        github_url = "https://github.com/cadsondemak/Sarabun/archive/refs/heads/master.zip"
        
        response = requests.get(github_url, stream=True)
        response.raise_for_status()
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print("✅ ดาวน์โหลดเสร็จสิ้น")
        
        # แตกไฟล์ zip
        print("\n📦 กำลังแตกไฟล์...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(FONTS_DIR / "temp_sarabun")
        
        # ค้นหาและย้ายไฟล์ .ttf
        print("\n📝 กำลังติดตั้งฟอนต์...")
        temp_dir = FONTS_DIR / "temp_sarabun"
        
        # ค้นหาไฟล์ .ttf ทั้งหมด
        ttf_files = list(temp_dir.rglob("*.ttf"))
        
        installed_count = 0
        for ttf_file in ttf_files:
            # เลือกเฉพาะไฟล์จากโฟลเดอร์ fonts/
            if "fonts" in str(ttf_file).lower() or "ttf" in str(ttf_file).lower():
                dest = SARABUN_DIR / ttf_file.name
                shutil.copy2(ttf_file, dest)
                print(f"  ✓ {ttf_file.name}")
                installed_count += 1
        
        # ลบไฟล์ชั่วคราว
        print("\n🗑️  ลบไฟล์ชั่วคราว...")
        shutil.rmtree(temp_dir)
        zip_path.unlink()
        
        print("\n" + "=" * 60)
        print("  ✅ ติดตั้งเสร็จสิ้น!")
        print("=" * 60)
        
        print(f"\n📝 ติดตั้งฟอนต์ทั้งหมด {installed_count} ไฟล์:")
        fonts = sorted(SARABUN_DIR.glob("*.ttf"))
        for font in fonts:
            print(f"  • {font.name}")
        
        print(f"\n📁 ตำแหน่ง: {SARABUN_DIR}")
        
    except Exception as e:
        print(f"\n❌ เกิดข้อผิดพลาด: {e}")
        
        # ลองดาวน์โหลดจาก alternative source
        print("\n💡 ลองดาวน์โหลดจาก alternative source...")
        download_from_alternative_source()

def download_from_alternative_source():
    """ดาวน์โหลดจาก alternative source (fonts.google.com API)"""
    
    # ใช้ Google Fonts API v2
    api_url = "https://fonts.googleapis.com/css2?family=Sarabun:wght@100;200;300;400;500;600;700;800&display=swap"
    
    print(f"🔽 กำลังดาวน์โหลดจาก Google Fonts API...")
    
    try:
        # ดาวน์โหลด CSS เพื่อหา URL ของฟอนต์
        response = requests.get(api_url)
        response.raise_for_status()
        
        css_content = response.text
        
        # Extract font URLs จาก CSS
        import re
        font_urls = re.findall(r'url\((https://[^)]+\.ttf)\)', css_content)
        
        print(f"📝 พบฟอนต์ {len(font_urls)} ไฟล์")
        
        # ดาวน์โหลดแต่ละไฟล์
        for i, url in enumerate(font_urls, 1):
            filename = f"Sarabun-{i}.ttf"
            dest = SARABUN_DIR / filename
            
            print(f"  {i}/{len(font_urls)} ดาวน์โหลด {filename}...")
            
            font_response = requests.get(url)
            font_response.raise_for_status()
            
            with open(dest, 'wb') as f:
                f.write(font_response.content)
        
        print("\n✅ ดาวน์โหลดเสร็จสิ้น!")
        
    except Exception as e:
        print(f"❌ ไม่สามารถดาวน์โหลดได้: {e}")
        print("\n💡 กรุณาดาวน์โหลดฟอนต์ Sarabun ด้วยตนเองจาก:")
        print("   https://fonts.google.com/specimen/Sarabun")
        print(f"   แล้ววางไฟล์ .ttf ไว้ที่: {SARABUN_DIR}")

def main():
    """ฟังก์ชันหลัก"""
    print("\n" + "=" * 60)
    print("  TH Sarabun Font Installer")
    print("=" * 60)
    print()
    
    # ตรวจสอบว่ามีฟอนต์อยู่แล้วหรือไม่
    if SARABUN_DIR.exists() and list(SARABUN_DIR.glob("*.ttf")):
        print(f"⚠️  พบฟอนต์ TH Sarabun อยู่แล้วที่: {SARABUN_DIR}")
        fonts = list(SARABUN_DIR.glob("*.ttf"))
        print(f"   จำนวน: {len(fonts)} ไฟล์")
        
        response = input("\nต้องการดาวน์โหลดใหม่หรือไม่? (y/N): ")
        if response.lower() != 'y':
            print("ยกเลิกการดาวน์โหลด")
            return
    
    download_sarabun()
    
    print("\n✨ สำเร็จ! ตอนนี้สามารถใช้ฟอนต์ TH Sarabun ใน PDF ได้แล้ว")
    print("💡 ลอง export PDF ใหม่อีกครั้งครับ")

if __name__ == "__main__":
    main()
