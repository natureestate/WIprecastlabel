#!/usr/bin/env python3
"""
Download Fonts - ดาวน์โหลด fonts จาก Google Fonts API

Script นี้ดาวน์โหลด fonts ที่จำเป็นสำหรับ PDF export:
- IBM Plex Sans Thai
- Sarabun  
- Inter
"""

import os
import sys
import urllib.request
from pathlib import Path
import zipfile

# Font URLs (Google Fonts Download API)
FONTS = {
    "IBMPlexSansThai": {
        "url": "https://fonts.google.com/download?family=IBM%20Plex%20Sans%20Thai",
        "dir": "IBMPlexSansThai"
    },
    "Sarabun": {
        "url": "https://fonts.google.com/download?family=Sarabun",
        "dir": "Sarabun"
    },
    "Inter": {
        "url": "https://fonts.google.com/download?family=Inter",
        "dir": "Inter"
    }
}


def download_font(font_name: str, font_info: dict, fonts_dir: Path):
    """
    ดาวน์โหลดและแตกไฟล์ font
    
    Args:
        font_name: ชื่อ font
        font_info: ข้อมูล font (url, dir)
        fonts_dir: directory สำหรับเก็บ fonts
    """
    print(f"\n📥 กำลังดาวน์โหลด {font_name}...")
    
    # สร้าง directory
    font_dir = fonts_dir / font_info["dir"]
    font_dir.mkdir(parents=True, exist_ok=True)
    
    # ดาวน์โหลด zip file
    zip_path = fonts_dir / f"{font_name}.zip"
    
    try:
        print(f"   กำลังดาวน์โหลดจาก Google Fonts...")
        urllib.request.urlretrieve(font_info["url"], zip_path)
        
        # แตกไฟล์
        print(f"   กำลังแตกไฟล์...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(font_dir)
        
        # ลบ zip file
        zip_path.unlink()
        
        print(f"   ✅ ดาวน์โหลด {font_name} สำเร็จ!")
        
    except Exception as e:
        print(f"   ❌ เกิดข้อผิดพลาด: {e}")
        print(f"   กรุณาดาวน์โหลดด้วยตนเองจาก: {font_info['url']}")


def main():
    """Main function"""
    # หา fonts directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    fonts_dir = project_root / "export" / "fonts"
    
    print("=" * 60)
    print("🔤 Font Downloader สำหรับ WIPrecastLabel PDF Export")
    print("=" * 60)
    
    # สร้าง fonts directory
    fonts_dir.mkdir(parents=True, exist_ok=True)
    
    # ดาวน์โหลดแต่ละ font
    for font_name, font_info in FONTS.items():
        download_font(font_name, font_info, fonts_dir)
    
    print("\n" + "=" * 60)
    print("✨ เสร็จสมบูรณ์!")
    print("=" * 60)
    print(f"\nFonts ถูกดาวน์โหลดไปยัง: {fonts_dir}")
    print("\nหมายเหตุ:")
    print("- ถ้าดาวน์โหลดไม่สำเร็จ กรุณาดาวน์โหลดด้วยตนเองจาก Google Fonts")
    print("- IBM Plex Sans Thai: https://fonts.google.com/specimen/IBM+Plex+Sans+Thai")
    print("- Sarabun: https://fonts.google.com/specimen/Sarabun")
    print("- Inter: https://fonts.google.com/specimen/Inter")


if __name__ == "__main__":
    main()
