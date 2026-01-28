# WIPrecastLabel - ระบบ Precast Pro Labeler

## ภาพรวม

โปรเจกต์นี้เป็นระบบจัดการและติดตามชิ้นส่วนคอนกรีตสำเร็จรูป (Precast Concrete) ด้วย QR Code พร้อมระบบ export เอกสารเป็น PDF

## 📚 เอกสาร

- 📘 [คู่มือการใช้งาน](docs/USER_MANUAL.md) - คู่มือสำหรับผู้ใช้ทุก Role
- 📗 [คู่มือขั้นตอนการทำงาน](docs/WORKFLOW_GUIDE.md) - Workflow และ SOP สำหรับพนักงาน

## 🚀 การ Export PDF

### ติดตั้ง Dependencies

```bash
# สร้าง virtual environment (แนะนำ)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux

# ติดตั้ง Python packages
pip install -r requirements.txt
```

### ดาวน์โหลด Fonts

ดาวน์โหลด fonts จาก Google Fonts และแตกไฟล์ลงใน `export/fonts/`:

1. **IBM Plex Sans Thai**: https://fonts.google.com/specimen/IBM+Plex+Sans+Thai
   - ดาวน์โหลด: Regular (400), Medium (500), SemiBold (600), Bold (700)
   - วางใน: `export/fonts/IBMPlexSansThai/`

2. **Sarabun**: https://fonts.google.com/specimen/Sarabun
   - ดาวน์โหลด: Light (300), Regular (400), Medium (500), SemiBold (600), Bold (700)
   - วางใน: `export/fonts/Sarabun/`

3. **Inter**: https://fonts.google.com/specimen/Inter
   - ดาวน์โหลด: Regular (400), Medium (500), SemiBold (600), Bold (700)
   - วางใน: `export/fonts/Inter/`

หรือใช้ script helper:

```bash
# TODO: สร้าง script ดาวน์โหลด fonts อัตโนมัติ
python export/scripts/download_fonts.py
```

### Export เอกสารเป็น PDF

```bash
# Export คู่มือการใช้งาน
python export/scripts/export_pdf.py \
  --input docs/USER_MANUAL.md \
  --output output/USER_MANUAL.pdf \
  --title "คู่มือการใช้งาน Precast Pro Labeler" \
  --author "WIPrecastLabel Team" \
  --version "1.0"

# Export คู่มือขั้นตอนการทำงาน
python export/scripts/export_pdf.py \
  --input docs/WORKFLOW_GUIDE.md \
  --output output/WORKFLOW_GUIDE.pdf \
  --title "คู่มือขั้นตอนการทำงาน" \
  --author "WIPrecastLabel Team" \
  --version "1.0"

# Export ทั้ง 2 ไฟล์พร้อมกัน
python export/scripts/export_pdf.py --all
```

## 📁 โครงสร้างโปรเจกต์

```
WIPrecastLabel/
├── docs/                       # เอกสาร markdown ต้นฉบับ
│   ├── USER_MANUAL.md
│   └── WORKFLOW_GUIDE.md
│
├── export/                     # ระบบ export PDF
│   ├── scripts/               # Python scripts
│   │   ├── export_pdf.py     # Main export script
│   │   ├── emoji_mapper.py   # แปลง emoji → Lucide icons
│   │   └── cover_generator.py # สร้างหน้าปก
│   │
│   ├── templates/             # HTML templates
│   │   ├── base.html
│   │   ├── cover.html
│   │   └── toc.html
│   │
│   ├── styles/                # CSS stylesheets
│   │   ├── main.css          # Typography & layout
│   │   ├── print.css         # Print-specific styles
│   │   ├── diagrams.css      # Code blocks & diagrams
│   │   └── lucide.css        # Icon styles
│   │
│   ├── fonts/                 # Web fonts (ไม่ commit ใน git)
│   └── assets/                # รูปภาพและ icons
│
├── output/                     # PDF ที่ export (ไม่ commit ใน git)
├── requirements.txt
└── README.md
```

## 🎨 คุณสมบัติ PDF

- ✅ **หน้าปก** พร้อมโลโก้และข้อมูลเอกสาร
- ✅ **สารบัญ** พร้อม page numbers
- ✅ **Header/Footer** ทุกหน้า
- ✅ **Fonts**:
  - ภาษาไทย: IBM Plex Sans Thai (หัวข้อ) + Sarabun (เนื้อหา)
  - ภาษาอังกฤษ: Inter
- ✅ **Icons**: แปลง emoji เป็น Lucide icons
- ✅ **Diagrams**: รองรับ ASCII diagrams และ code blocks
- ✅ **Page Breaks**: อัตโนมัติที่หัวข้อหลัก

## ❓ Troubleshooting

### WeasyPrint ติดตั้งไม่ได้

WeasyPrint ต้องการ dependencies ของระบบ:

**macOS:**
```bash
brew install python cairo pango gdk-pixbuf libffi
```

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-dev python3-pip python3-cffi \
  libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
  libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

### Fonts ไม่แสดงใน PDF

ตรวจสอบว่า:
1. ดาวน์โหลด fonts ครบถ้วนแล้ว
2. วางไฟล์ในโฟลเดอร์ที่ถูกต้อง (`export/fonts/`)
3. Path ใน CSS ถูกต้อง

### Diagrams แสดงผลไม่ดี

ลอง:
1. ปรับ font size ใน `diagrams.css`
2. เปลี่ยน monospace font
3. ปรับ page margins

## 📝 License

© 2026 WIPrecastLabel Team. All rights reserved.
