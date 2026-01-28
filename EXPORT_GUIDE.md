# คำแนะนำการ Export PDF

## 📋 ขั้นตอนการเตรียมระบบ

### 1. ติดตั้ง Python Dependencies

```bash
# สร้าง virtual environment (แนะนำ)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux

# ติดตั้ง packages
pip install -r requirements.txt
```

> **หมายเหตุ**: ถ้า WeasyPrint ติดตั้งไม่ได้ ให้ติดตั้ง system dependencies ก่อน:
>
> **macOS:**
> ```bash
> brew install python cairo pango gdk-pixbuf libffi
> ```

### 2. ดาวน์โหลด Fonts

```bash
# วิธีที่ 1: ใช้ script อัตโนมัติ (แนะนำ)
python export/scripts/download_fonts.py

# วิธีที่ 2: ดาวน์โหลดด้วยตนเอง
# ไปที่ Google Fonts และดาวน์โหลด:
# - IBM Plex Sans Thai
# - Sarabun
# - Inter
# จากนั้นแตกไฟล์ลงใน export/fonts/
```

### 3. ทดสอบระบบ

```bash
# ทดสอบ export ไฟล์เดียว
python export/scripts/export_pdf.py \
  --input docs/USER_MANUAL.md \
  --output output/TEST.pdf \
  --title "ทดสอบระบบ" \
  --version "0.1"
```

---

## 🚀 Export PDF

### Export ทั้ง 2 ไฟล์พร้อมกัน (แนะนำ)

```bash
python export/scripts/export_pdf.py --all
```

### Export ไฟล์ทีละไฟล์

```bash
# USER_MANUAL.pdf
python export/scripts/export_pdf.py \
  --input docs/USER_MANUAL.md \
  --output output/USER_MANUAL.pdf \
  --title "คู่มือการใช้งาน Precast Pro Labeler" \
  --subtitle "ระบบจัดการและติดตามชิ้นส่วนคอนกรีตสำเร็จรูป" \
  --version "1.0" \
  --author "WIPrecastLabel Team"

# WORKFLOW_GUIDE.pdf
python export/scripts/export_pdf.py \
  --input docs/WORKFLOW_GUIDE.md \
  --output output/WORKFLOW_GUIDE.pdf \
  --title "คู่มือขั้นตอนการทำงาน" \
  --subtitle "Workflow และ SOP สำหรับพนักงานทุกแผนก" \
  --version "1.0" \
  --author "WIPrecastLabel Team"
```

---

## ✅ ตรวจสอบผลลัพธ์

หลัง export เสร็จ ให้ตรวจสอบ:

1. ✓ หน้าปก - มีชื่อเอกสาร, เวอร์ชัน, วันที่, ผู้แต่ง
2. ✓ สารบัญ - มีรายการหัวข้อและหมายเลขหน้า
3. ✓ Header - มีชื่อระบบและชื่อ section
4. ✓ Footer - มีหมายเลขหน้าและ copyright
5. ✓ Fonts - ภาษาไทยใช้ Sarabun/IBM Plex Sans Thai, อังกฤษใช้ Inter
6. ✓ Icons - emoji แปลงเป็น icons แล้ว
7. ✓ Diagrams - ASCII diagrams แสดงผลถูกต้อง
8. ✓ Tables - ตารางสวยงามและอ่านง่าย
9. ✓ Page Breaks - แต่ละ section ขึ้นหน้าใหม่

---

## 📁 ไฟล์ Output

PDF จะถูกสร้างใน `output/`:
- `output/USER_MANUAL.pdf`
- `output/WORKFLOW_GUIDE.pdf`

> **สำคัญ**: Folder `output/` และไฟล์ `*.pdf` จะไม่ถูก commit ใน Git (ถูก ignore ใน `.gitignore`)

---

## 🔧 Troubleshooting

### ปัญหา: WeasyPrint ติดตั้งไม่ได้

**แก้ไข:**
```bash
# macOS
brew install python cairo pango gdk-pixbuf libffi
pip install weasyprint
```

### ปัญหา: Fonts ไม่แสดงใน PDF

**แก้ไข:**
1. ตรวจสอบว่าดาวน์โหลด fonts ครบแล้ว: `ls export/fonts/`
2. ตรวจสอบว่า path ใน CSS ถูกต้อง
3. ลองดาวน์โหลด fonts ใหม่

### ปัญหา: Diagrams แสดงผลไม่ดี

**แก้ไข:**
1. ปรับ font size ใน `export/styles/diagrams.css`
2. ลอง font อื่น เช่น `Consolas`, `Monaco`
3. ปรับ page margins

### ปัญหา: Memory Error

**แก้ไข:**
Export ทีละไฟล์แทนการ export ทั้งหมด

---

## 💡 Tips

- ใช้ `--all` flag สำหรับ export ครั้งเดียวเสร็จ
- ปรับ `--version` ทุกครั้งที่อัพเดทเอกสาร
- เก็บ PDF เวอร์ชันต่างๆ ด้วยการเปลี่ยนชื่อไฟล์ เช่น `USER_MANUAL_v1.0.pdf`
- ถ้าต้องการเก็บ PDF ใน Git ให้ลบ `*.pdf` ออกจาก `.gitignore`
