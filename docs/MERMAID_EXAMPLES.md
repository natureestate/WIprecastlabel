# ตัวอย่าง Mermaid Diagrams สำหรับ USER_MANUAL.md

## 1. Main Workflow Diagram

```mermaid
graph TD
    Start([เริ่มต้น]) --> Planning[ฝ่ายวางแผน<br/>PLANNING]
    Planning --> Print[1. พิมพ์ฉลาก<br/>PENDING]
    Print --> Activate[2. Scan & Activate<br/>ACTIVATED]
    Activate --> Produce[3. หล่อชิ้นงาน<br/>PRODUCED]
    
    Produce --> QC[ฝ่าย QC<br/>ตรวจสอบคุณภาพ]
    QC --> QCDecision{ผ่าน QC?}
    
    QCDecision -->|ผ่าน| QCPass[QC PASSED]
    QCDecision -->|ไม่ผ่าน| QCFail[QC FAILED]
    QCFail --> Fix[แก้ไข/ทำใหม่]
    Fix --> QC
    
    QCPass --> Warehouse[ฝ่ายคลัง<br/>WAREHOUSE]
    Warehouse --> InStock[5. รับเข้าคลัง<br/>IN_STOCK]
    
    InStock --> Shipping[ฝ่ายจัดส่ง<br/>SHIPPING]
    Shipping --> Ship[6. จัดส่ง<br/>SHIPPING]
    Ship --> Delivered[7. ส่งถึง<br/>DELIVERED]
    
    Delivered --> Installation[ฝ่ายติดตั้ง<br/>INSTALLATION]
    Installation --> Installing[8. กำลังติดตั้ง<br/>INSTALLING]
    Installing --> Installed[9. ติดตั้งเสร็จ<br/>INSTALLED]
    Installed --> Archive[10. จบงาน<br/>ARCHIVED]
    Archive --> End([สิ้นสุด])
    
    style Start fill:#e3f2fd
    style End fill:#e3f2fd
    style Planning fill:#fff3e0
    style QC fill:#f3e5f5
    style Warehouse fill:#e8f5e9
    style Shipping fill:#fce4ec
    style Installation fill:#e0f2f1
    style QCPass fill:#c8e6c9
    style QCFail fill:#ffcdd2
```

## 2. Planning Flow

```mermaid
flowchart TD
    Start([เริ่มต้น]) --> HasOrder{มีคำสั่งผลิต<br/>ใหม่?}
    HasOrder -->|ไม่มี| End([รอคำสั่ง])
    HasOrder -->|มี| Login[1. Login เข้าระบบ]
    
    Login --> PrintPage[2. ไปหน้าพิมพ์ฉลาก]
    PrintPage --> FillInfo[3. กรอกข้อมูล<br/>• ชื่อลูกค้า<br/>• ชื่อโครงการ<br/>• สถานที่หล่อ]
    
    FillInfo --> AddItems[4. เพิ่มรายการ<br/>• ประเภทชิ้นงาน<br/>• จำนวน<br/>• Running Number]
    
    AddItems --> SelectTemplate[5. เลือกเทมเพลต<br/>• Default<br/>• Custom<br/>• Saved]
    
    SelectTemplate --> Customize{ต้องการ<br/>ปรับแต่ง?}
    Customize -->|ใช่| Edit[6. ปรับแต่ง<br/>• ลาก-วาง<br/>• แก้ไขข้อความ<br/>• ปรับสี/ฟอนต์]
    Customize -->|ไม่| PrintPDF[7. กดพิมพ์ PDF]
    Edit --> PrintPDF
    
    PrintPDF --> Attach[8. พิมพ์และติดฉลาก<br/>ที่แบบหล่อ]
    Attach --> Cast[9. หล่อชิ้นงานเสร็จ<br/>Scan QR Code]
    Cast --> ActivateBtn[10. กด Activate<br/>pending → activated]
    ActivateBtn --> SendQC[11. ส่งต่อให้ QC<br/>ตรวจสอบ]
    SendQC --> Done([เสร็จสิ้น])
    
    style Start fill:#e3f2fd
    style Done fill:#e3f2fd
    style End fill:#ffebee
    style PrintPDF fill:#fff9c4
    style ActivateBtn fill:#c8e6c9
```

## 3. QC Flow

```mermaid
flowchart TD
    Start([เริ่มต้น]) --> HasWork{มีชิ้นงาน<br/>รอตรวจ QC?}
    HasWork -->|ไม่มี| End([รอชิ้นงาน])
    HasWork -->|มี| Login[1. Login เข้าระบบ]
    
    Login --> ScanPage[2. ไปหน้า Scan]
    ScanPage --> ScanQR[3. Scan QR Code<br/>บนชิ้นงาน]
    
    ScanQR --> ViewInfo[4. ดูข้อมูลชิ้นงาน<br/>• ประเภท<br/>• ขนาด<br/>• วันที่หล่อ]
    
    ViewInfo --> Inspect[5. ตรวจสอบคุณภาพ<br/>• ขนาด<br/>• รูปร่าง<br/>• ความแข็งแรง<br/>• รอยแตกร้าว]
    
    Inspect --> Decision{ผ่าน QC?}
    
    Decision -->|ผ่าน| Pass[6a. กด QC Pass]
    Decision -->|ไม่ผ่าน| Fail[6b. กด QC Fail]
    
    Fail --> Note[7. กรอกหมายเหตุ<br/>เหตุผลที่ไม่ผ่าน]
    Note --> Return[8. ส่งกลับให้แก้ไข]
    Return --> End
    
    Pass --> SendWarehouse[9. ส่งต่อให้ Warehouse<br/>รับเข้าคลัง]
    SendWarehouse --> Done([เสร็จสิ้น])
    
    style Start fill:#e3f2fd
    style Done fill:#e3f2fd
    style End fill:#ffebee
    style Pass fill:#c8e6c9
    style Fail fill:#ffcdd2
```

## วิธีใช้:

1. คัดลอก Mermaid code ด้านบน
2. แทนที่ ASCII art diagrams ใน USER_MANUAL.md
3. Export PDF ใหม่

Mermaid จะถูกแปลงเป็น SVG อัตโนมัติและแสดงผลสวยงามใน PDF!
