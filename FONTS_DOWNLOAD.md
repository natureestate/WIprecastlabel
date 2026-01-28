# วิธีดาวน์โหลด Fonts สำหรับ PDF Export

เนื่องจาก Google Fonts API อาจไม่สามารถดาวน์โหลดอัตโนมัติได้ ให้ทำตามขั้นตอนด้านล่าง:

## 📥 ดาวน์โหลด Fonts

### 1. IBM Plex Sans Thai

1. ไปที่: https://fonts.google.com/specimen/IBM+Plex+Sans+Thai
2. คลิกปุ่ม "Download family" หรือ "Get font"
3. คลิก "Download all"
4. แตกไฟล์ ZIP ที่ดาวน์โหลดมา
5. คัดลอกไฟล์ `.ttf` ทั้งหมดไปยัง:
   ```
   export/fonts/IBMPlexSansThai/
   ```

**ไฟล์ที่ต้องการ:**
- `IBMPlexSansThai-Regular.ttf` (400)
- `IBMPlexSansThai-Medium.ttf` (500)
- `IBMPlexSansThai-SemiBold.ttf` (600)
- `IBMPlexSansThai-Bold.ttf` (700)

---

### 2. Sarabun

1. ไปที่: https://fonts.google.com/specimen/Sarabun
2. คลิกปุ่ม "Download family"
3. แตกไฟล์ ZIP
4. คัดลอกไฟล์ `.ttf` ไปยัง:
   ```
   export/fonts/Sarabun/
   ```

**ไฟล์ที่ต้องการ:**
- `Sarabun-Light.ttf` (300)
- `Sarabun-Regular.ttf` (400)
- `Sarabun-Medium.ttf` (500)
- `Sarabun-SemiBold.ttf` (600)
- `Sarabun-Bold.ttf` (700)

---

### 3. Inter

1. ไปที่: https://fonts.google.com/specimen/Inter
2. คลิกปุ่ม "Download family"
3. แตกไฟล์ ZIP
4. คัดลอกไฟล์ `.ttf` จากโฟลเดอร์ `static/` ไปยัง:
   ```
   export/fonts/Inter/
   ```

**ไฟล์ที่ต้องการ:**
- `Inter-Regular.ttf` (400)
- `Inter-Medium.ttf` (500)
- `Inter-SemiBold.ttf` (600)
- `Inter-Bold.ttf` (700)

---

## ✅ ตรวจสอบว่าครบถ้วน

หลังคัดลอกไฟล์แล้ว ตรวจสอบโครงสร้างให้เหมือนนี้:

```
export/fonts/
├── IBMPlexSansThai/
│   ├── IBMPlexSansThai-Regular.ttf
│   ├── IBMPlexSansThai-Medium.ttf
│   ├── IBMPlexSansThai-SemiBold.ttf
│   └── IBMPlexSansThai-Bold.ttf
├── Sarabun/
│   ├── Sarabun-Light.ttf
│   ├── Sarabun-Regular.ttf
│   ├── Sarabun-Medium.ttf
│   ├── Sarabun-SemiBold.ttf
│   └── Sarabun-Bold.ttf
└── Inter/
    ├── Inter-Regular.ttf
    ├── Inter-Medium.ttf
    ├── Inter-SemiBold.ttf
    └── Inter-Bold.ttf
```

ใช้คำสั่งนี้เพื่อตรวจสอบ:
```bash
ls -la export/fonts/*/
```

---

## 🚀 พร้อมใช้งานแล้ว!

หลังจากดาวน์โหลด fonts ครบแล้ว คุณสามารถ export PDF ได้ทันที:

```bash
# Activate virtual environment (ถ้ายังไม่ได้ activate)
source venv/bin/activate

# Export ทั้ง 2 ไฟล์
python export/scripts/export_pdf.py --all
```
