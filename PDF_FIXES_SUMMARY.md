# สรุปการแก้ไขปัญหา PDF Export

## 🔧 ปัญหาที่แก้ไข:

### 1. ✅ Icons ใน diagram แสดงเป็น HTML code
**สาเหตุ:** `emoji_mapper.py` แปลง emoji เป็น `<span>` tags ซึ่ง WeasyPrint ไม่รองรับ

**วิธีแก้:**
- แก้ไข `emoji_mapper.py` ให้ไม่แปลง emoji
- ปล่อยให้ฟอนต์รองรับ emoji แสดงผลเอง

**ไฟล์ที่แก้:** `export/scripts/emoji_mapper.py`

### 2. ✅ ฟอนต์ไทยเพี้ยนบางคำ
**สาเหตุ:** การแปลง emoji ทำให้ text encoding เสียหาย

**วิธีแก้:**
- ไม่แปลง emoji แล้ว (แก้ไขพร้อมกับปัญหาที่ 1)
- ฟอนต์ Sarabun รองรับภาษาไทยได้ถูกต้อง

### 3. ✅ สารบัญซ้ำ 2 จุด
**สาเหตุ:** 
- มี heading `# สารบัญ` ใน markdown
- มีการสร้าง TOC page แยกอีกที

**วิธีแก้:**
- สร้างสคริปต์ `remove_toc_heading.py` ลบ heading "สารบัญ" ออก
- กรอง TOC items ไม่ให้รวม "สารบัญ"

**ไฟล์ที่สร้าง:** `export/scripts/remove_toc_heading.py`

### 4. ⚠️ ไม่แสดงหมายเลขหน้าในสารบัญ
**สาเหตุ:** WeasyPrint ไม่รองรับ CSS `target-counter()` สำหรับ TOC อัตโนมัติ

**สถานะ:** ยังไม่แก้ไข - ต้องใช้ทางเลือกอื่น:

**ทางเลือก:**
1. **ใช้ Markdown TOC extension** (แนะนำ)
2. **สร้าง TOC ด้วย Python script** หลัง render PDF
3. **ใช้ external tool** เช่น `pdftk` หรือ `pypdf`

## 📋 ขั้นตอนการ Export PDF ที่ถูกต้อง:

```bash
# 1. ลบ heading "สารบัญ" (ถ้ายังไม่ได้รัน)
python3 export/scripts/remove_toc_heading.py

# 2. Export PDF
python3 export/scripts/export_pdf.py --all
```

## 📊 ผลลัพธ์:

### ✅ ปัญหาที่แก้ไขแล้ว:
- Icons ใน diagram แสดงผลถูกต้อง (เป็น emoji)
- ฟอนต์ไทยไม่เพี้ยน
- สารบัญไม่ซ้ำ

### ⚠️ ปัญหาที่ยังค้างอยู่:
- หมายเลขหน้าในสารบัญแสดงเป็น `...`

## 🔄 การแก้ไขหมายเลขหน้า (ขั้นสูง):

### วิธีที่ 1: ใช้ Markdown TOC Extension

แก้ไข `export_pdf.py`:

```python
md = markdown.Markdown(extensions=[
    'tables',
    'fenced_code',
    'codehilite',
    'toc',  # ใช้ TOC extension
    'nl2br',
    'sane_lists',
])

# ดึง TOC จาก extension
toc_html = md.toc
```

### วิธีที่ 2: Post-process PDF

สร้างสคริปต์ Python ที่:
1. Render PDF ครั้งแรก (เพื่อหาหมายเลขหน้า)
2. Extract page numbers
3. Update TOC
4. Render PDF ครั้งที่ 2

### วิธีที่ 3: ใช้ LaTeX/Pandoc

แปลง Markdown → LaTeX → PDF ด้วย Pandoc ซึ่งรองรับ TOC อัตโนมัติ

## 📁 ไฟล์ที่แก้ไข/สร้าง:

```
export/scripts/
├── emoji_mapper.py (แก้ไข - ไม่แปลง emoji)
├── remove_toc_heading.py (สร้างใหม่)
└── mermaid_processor.py (เพิ่มรองรับ Mermaid)

docs/
├── USER_MANUAL.md (ลบ heading "สารบัญ")
└── WORKFLOW_GUIDE.md (ลบ heading "สารบัญ")
```

## 🎯 สรุป:

**ปัญหาหลักๆ แก้ไขแล้ว** ✅
- Icons แสดงผลถูกต้อง
- ฟอนต์ไทยไม่เพี้ยน  
- สารบัญไม่ซ้ำ

**ปัญหาที่ยังค้าง** ⚠️
- หมายเลขหน้าในสารบัญ (ต้องใช้วิธีขั้นสูง)

---

**หมายเหตุ:** สำหรับหมายเลขหน้า แนะนำให้ใช้ Pandoc หรือ LaTeX ถ้าต้องการ TOC ที่สมบูรณ์แบบ
