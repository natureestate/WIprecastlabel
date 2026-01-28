# 🎉 ระบบ Export PDF พร้อมใช้งาน!

## ✅ สิ่งที่เสร็จแล้ว (90%)

### 📂 โครงสร้างโปรเจกต์
```
WIPrecastLabel/
├── docs/                  ← เอกสาร markdown (ย้ายมาจาก root แล้ว)
├── export/
│   ├── scripts/          ← Python scripts ครบ 4 ไฟล์
│   ├── styles/           ← CSS stylesheets ครบ 4 ไฟล์
│   └── fonts/            ⚠️ ต้องดาวน์โหลด (ดูด้านล่าง)
├── output/               ← PDF จะถูกสร้างที่นี่
└── venv/                 ← Python dependencies ติดตั้งแล้ว
```

### 🐍 Python Scripts
✅ `export_pdf.py` - Main export script  
✅ `emoji_mapper.py` - แปลง emoji → icons  
✅ `cover_generator.py` - สร้างหน้าปก & สารบัญ  
✅ `download_fonts.py` - Helper ดาวน์โหลด fonts  

### 🎨 CSS Stylesheets
✅ `main.css` - Typography, layout, colors  
✅ `print.css` - Page setup, headers, footers  
✅ `diagrams.css` - Code blocks & diagrams  
✅ `lucide.css` - Icon styles  

### 📦 Dependencies
✅ Python packages ติดตั้งใน venv แล้ว:
- weasyprint 68.0
- markdown 3.10.1
- pygments 2.19.2
- jinja2 3.1.6

---

## ⏳ ต้องทำก่อนใช้งาน

### 1️⃣ ดาวน์โหลด Fonts (MANUAL)

**คุณต้องดาวน์โหลดเองจาก Google Fonts:**

1. **IBM Plex Sans Thai**  
   🔗 https://fonts.google.com/specimen/IBM+Plex+Sans+Thai  
   📁 วางไฟล์ `.ttf` ใน: `export/fonts/IBMPlexSansThai/`

2. **Sarabun**  
   🔗 https://fonts.google.com/specimen/Sarabun  
   📁 วางไฟล์ `.ttf` ใน: `export/fonts/Sarabun/`

3. **Inter**  
   🔗 https://fonts.google.com/specimen/Inter  
   📁 วางไฟล์ `.ttf` (จากโฟลเดอร์ `static/`) ใน: `export/fonts/Inter/`

> 📖 **รายละเอียดเพิ่มเติม**: อ่าน [`FONTS_DOWNLOAD.md`](FONTS_DOWNLOAD.md)

---

## 🚀 วิธีใช้งาน

### ขั้นตอน 1: Activate Virtual Environment
```bash
source venv/bin/activate
```

### ขั้นตอน 2: Export PDF
```bash
# Export ทั้ง 2 ไฟล์พร้อมกัน (แนะนำ)
python export/scripts/export_pdf.py --all

# หรือ export ทีละไฟล์
python export/scripts/export_pdf.py \
  --input docs/USER_MANUAL.md \
  --output output/USER_MANUAL.pdf \
  --title "คู่มือการใช้งาน Precast Pro Labeler" \
  --version "1.0"
```

### ขั้นตอน 3: เปิดดู PDF
```bash
open output/USER_MANUAL.pdf
open output/WORKFLOW_GUIDE.pdf
```

---

## 📚 เอกสารอ้างอิง

- 📘 [`README.md`](README.md) - ภาพรวมโปรเจกต์
- 📗 [`EXPORT_GUIDE.md`](EXPORT_GUIDE.md) - คำแนะนำ export แบบละเอียด
- 📙 [`FONTS_DOWNLOAD.md`](FONTS_DOWNLOAD.md) - วิธีดาวน์โหลด fonts

---

## 🎨 คุณสมบัติ PDF

เมื่อ export เสร็จ PDF จะมี:

- ✅ **หน้าปก** พร้อมชื่อเอกสาร, เวอร์ชัน, วันที่, ผู้แต่ง
- ✅ **สารบัญ** พร้อมหมายเลขหน้า
- ✅ **Header** ทุกหน้า (ชื่อระบบ + section)
- ✅ **Footer** ทุกหน้า (หมายเลขหน้า + copyright)
- ✅ **Fonts สวยงาม**:
  - หัวข้อ: IBM Plex Sans Thai
  - เนื้อหาไทย: Sarabun
  - เนื้อหาอังกฤษ: Inter
- ✅ **Icons** แทน emoji
- ✅ **Code blocks** และ diagrams สวยงาม
- ✅ **Page breaks** อัตโนมัติ

---

## 🔧 Troubleshooting

### ปัญหา: Fonts ไม่แสดง
**แก้ไข**: ตรวจสอบว่าดาวน์โหลดและวางไฟล์ถูกที่แล้ว (`ls export/fonts/*/`)

### ปัญหา: ModuleNotFoundError
**แก้ไข**: Activate venv ก่อน (`source venv/bin/activate`)

### ปัญหา: Diagrams แสดงผลไม่ดี
**แก้ไข**: ปรับ font-size ใน `export/styles/diagrams.css`

---

## 💡 Tips

- ใช้ `--all` flag เพื่อ export ครั้งเดียวเสร็จ
- ปรับ `--version` ทุกครั้งที่อัพเดทเอกสาร
- PDF จะไม่ถูก commit ใน Git (ถูก ignore แล้ว)
- ถ้าต้องการเก็บ PDF ใน Git ให้ลบ `*.pdf` ออกจาก `.gitignore`

---

## 📞 ต้องการความช่วยเหลือ?

อ่านเอกสารเพิ่มเติม:
1. [`EXPORT_GUIDE.md`](EXPORT_GUIDE.md) - คำแนะนำละเอียด
2. [`FONTS_DOWNLOAD.md`](FONTS_DOWNLOAD.md) - วิธีดาวน์โหลด fonts
3. [`README.md`](README.md) - ภาพรวมและ troubleshooting

---

**🎯 ทำตามนี้เลย:**

```bash
# 1. ดาวน์โหลด fonts (manual - ดูใน FONTS_DOWNLOAD.md)
# 2. Activate venv
source venv/bin/activate

# 3. Export PDF
python export/scripts/export_pdf.py --all

# 4. เปิดดู
open output/*.pdf
```

**แค่นี้ก็พร้อมใช้งานแล้ว!** 🚀
