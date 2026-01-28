# คู่มือขั้นตอนการทำงาน (Workflow Guide)
## สำหรับวางผังการทำงานและ Model พนักงาน

---

1. [ภาพรวม Workflow](#1-ภาพรวม-workflow)
2. [แผนผังการทำงานรวม](#2-แผนผังการทำงานรวม)
3. [คู่มือการทำงาน - Planning](#3-คู่มือการทำงาน---planning)
4. [คู่มือการทำงาน - QC](#4-คู่มือการทำงาน---qc)
5. [คู่มือการทำงาน - Warehouse](#5-คู่มือการทำงาน---warehouse)
6. [คู่มือการทำงาน - Shipping](#6-คู่มือการทำงาน---shipping)
7. [คู่มือการทำงาน - Installation](#7-คู่มือการทำงาน---installation)
8. [ตารางความรับผิดชอบ (RACI Matrix)](#8-ตารางความรับผิดชอบ-raci-matrix)
9. [Checklist สำหรับแต่ละ Role](#9-checklist-สำหรับแต่ละ-role)
10. [KPI และเป้าหมาย](#10-kpi-และเป้าหมาย)

---

## 1. ภาพรวม Workflow

### 1.1 วัตถุประสงค์

ระบบ Precast Pro Labeler ออกแบบมาเพื่อ:

1. **ติดตามชิ้นงาน** ตั้งแต่ผลิตจนติดตั้งเสร็จ
2. **ลดความผิดพลาด** ในการส่งมอบชิ้นงาน
3. **เพิ่มความโปร่งใส** ให้ลูกค้าตรวจสอบสถานะได้
4. **บันทึกประวัติ** การดำเนินการทุกขั้นตอน

### 1.2 ผู้มีส่วนเกี่ยวข้อง

| Role | จำนวนแนะนำ | หน้าที่หลัก |
|------|-----------|-------------|
| Admin | 1-2 คน | ดูแลระบบ, จัดการผู้ใช้ |
| Planning | 1-3 คน | พิมพ์ฉลาก, Activate ชิ้นงาน |
| QC | 2-4 คน | ตรวจสอบคุณภาพ |
| Warehouse | 2-3 คน | รับเข้า-ออกคลัง |
| Shipping | 2-4 คน | จัดส่งชิ้นงาน |
| Installation | 3-6 คน | ติดตั้งที่หน้างาน |

---

## 2. แผนผังการทำงานรวม

### 2.1 Master Workflow Diagram

<div class="flow-container">
    <div class="flow-step step-planning">
        <span class="step-title">📋 PHASE 1: PRODUCTION</span>
        <span class="step-desc">ฝ่ายผลิต/วางแผน</span>
    </div>

    <!-- Production Steps -->
    <div class="flow-step step-planning">
        <span class="step-meta">Step 1</span>
        <span class="step-title">📝 รับคำสั่งผลิต</span>
        <span class="step-desc">จาก Sales/Engineer</span>
    </div>
    
    <div class="flow-step step-planning">
        <span class="step-meta">Step 2</span>
        <span class="step-title">🖨️ พิมพ์ฉลาก QR Code</span>
        <span class="step-desc">เตรียม Running Number</span>
    </div>

    <div class="flow-step step-planning">
        <span class="step-meta">Step 3</span>
        <span class="step-title">🏷️ ติดฉลากที่แบบหล่อ</span>
        <span class="step-desc">ก่อนเทคอนกรีต</span>
    </div>
    
    <div class="flow-step step-planning">
        <span class="step-meta">Step 4</span>
        <span class="step-title">🏗️ หล่อชิ้นงาน</span>
        <span class="step-desc">กระบวนการผลิต (Casting)</span>
    </div>

    <div class="flow-step step-planning">
        <span class="step-meta">Step 5</span>
        <span class="step-title">📷 ถอดแบบ & Activate</span>
        <span class="step-desc">Scan QR เพื่อเริ่มเข้าระบบ (Status: Activated 🟢)</span>
    </div>

    <!-- QC Phase -->
    <div class="flow-step step-qc">
        <span class="step-title">🔍 PHASE 2: QUALITY CONTROL</span>
        <span class="step-desc">ฝ่ายตรวจสอบคุณภาพ</span>
    </div>

    <div class="flow-step step-qc">
        <span class="step-meta">Step 6</span>
        <span class="step-title">📷 Scan QR Code</span>
        <span class="step-desc">เพื่อดูข้อมูลชิ้นงาน</span>
    </div>

    <div class="flow-step step-decision">
        <span class="step-title">⚖️ ตรวจสอบคุณภาพ</span>
        <span class="step-desc">ผ่านเกณฑ์มาตรฐานหรือไม่?</span>
    </div>

    <div class="flow-step step-fail">
        <span class="step-title">❌ กรณีไม่ผ่าน (QC FAILED)</span>
        <span class="step-desc">ระบุสาเหตุ -> ส่งซ่อม -> กลับมาตรวจใหม่</span>
    </div>

    <div class="flow-step step-pass">
        <span class="step-title">✅ กรณีผ่าน (QC PASSED)</span>
        <span class="step-desc">คุณภาพสมบูรณ์พร้อมส่งมอบ</span>
    </div>

    <!-- Warehouse Phase -->
    <div class="flow-step step-warehouse">
        <span class="step-title">📦 PHASE 3: STORAGE</span>
        <span class="step-desc">ฝ่ายคลังสินค้า</span>
    </div>

    <div class="flow-step step-warehouse">
        <span class="step-meta">Step 7</span>
        <span class="step-title">📥 Scan รับเข้าคลัง</span>
        <span class="step-desc">Status: In Stock 🟣</span>
    </div>

    <div class="flow-step step-warehouse">
        <span class="step-meta">Step 8</span>
        <span class="step-title">📍 บันทึกตำแหน่งจัดเก็บ</span>
        <span class="step-desc">ระบุ Zone/Row/Shelf</span>
    </div>

    <!-- Shipping Phase -->
    <div class="flow-step step-shipping">
        <span class="step-title">🚚 PHASE 4: DELIVERY</span>
        <span class="step-desc">ฝ่ายจัดส่ง</span>
    </div>

    <div class="flow-step step-shipping">
        <span class="step-meta">Step 9</span>
        <span class="step-title">📋 ได้รับคำสั่งจัดส่ง</span>
        <span class="step-desc">หยิบของจากคลัง</span>
    </div>

    <div class="flow-step step-shipping">
        <span class="step-meta">Step 10</span>
        <span class="step-title">📤 Scan ขึ้นรถ (Shipping)</span>
        <span class="step-desc">Status: Shipping 🟠</span>
    </div>

    <div class="flow-step step-shipping">
        <span class="step-meta">Step 11</span>
        <span class="step-title">🚚 ขนส่งถึงหน้างาน</span>
        <span class="step-desc">เดินทางปลอดภัย</span>
    </div>
    
    <div class="flow-step step-shipping">
        <span class="step-meta">Step 12</span>
        <span class="step-title">📍 Scan ส่งมอบ (Delivered)</span>
        <span class="step-desc">Status: Delivered 🔵</span>
    </div>

    <!-- Installation Phase -->
    <div class="flow-step step-installation">
        <span class="step-title">🔧 PHASE 5: INSTALLATION</span>
        <span class="step-desc">ฝ่ายติดตั้ง</span>
    </div>

    <div class="flow-step step-installation">
        <span class="step-meta">Step 13</span>
        <span class="step-title">📥 รับมอบชิ้นงาน</span>
        <span class="step-desc">ตรวจสอบความถูกต้อง</span>
    </div>

    <div class="flow-step step-installation">
        <span class="step-meta">Step 14</span>
        <span class="step-title">🏗️ Scan เริ่มติดตั้ง</span>
        <span class="step-desc">Status: Installing 🚧</span>
    </div>

    <div class="flow-step step-installation">
        <span class="step-title">Step 15</span>
        <span class="step-title">✅ ติดตั้งเสร็จสิ้น</span>
        <span class="step-desc">Status: Installed 🏁</span>
    </div>

    <div class="flow-step step-pass">
        <span class="step-title">💾 COMPLETION</span>
        <span class="step-desc">จบกระบวนการ (Archive ⚪️)</span>
    </div>
</div>

---

## 3. คู่มือการทำงาน - Planning

### 3.1 ตำแหน่งงาน: พนักงานฝ่ายวางแผน

**หน้าที่หลัก:**
- สร้างและพิมพ์ฉลาก QR Code
- ติดฉลากที่แบบหล่อ
- Activate ชิ้นงานหลังหล่อเสร็จ

### 3.2 ขั้นตอนการทำงาน (Step-by-Step)

#### งาน A: พิมพ์ฉลาก QR Code

<div class="flow-container">
    <div class="flow-step step-planning">
        <span class="step-title">📝 STEP 1: เตรียมข้อมูล</span>
        <span class="step-desc">ตรวจสอบรายละเอียดคำสั่งผลิต</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">🔒 STEP 2: Login เข้าระบบ</span>
        <span class="step-desc">ใช้ Email/Password</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">📋 STEP 3: กรอกข้อมูลโครงการ</span>
        <span class="step-desc">ลูกค้า, ชื่อโครงการ, สถานที่</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">➕ STEP 4: เพิ่มรายการชิ้นงาน</span>
        <span class="step-desc">ระบุประเภทและจำนวน (Auto Run No.)</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">📄 STEP 5: เลือกเทมเพลต</span>
        <span class="step-desc">Default หรือ Custom</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">🎨 STEP 6: ปรับแต่ง (ถ้าจำเป็น)</span>
        <span class="step-desc">ใช้ Visual Editor</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">🖨️ STEP 7: พิมพ์ PDF</span>
        <span class="step-desc">สั่งพิมพ์ออกทางเครื่องพิมพ์</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">🏷️ STEP 8: ติดฉลากที่แบบหล่อ</span>
        <span class="step-desc">ระวังเปียกน้ำ/เปื้อนปูน</span>
    </div>
</div>

#### งาน B: Activate ชิ้นงาน

<div class="flow-container">
    <div class="flow-step step-planning">
        <span class="step-title">🏗️ STEP 1: หล่อเสร็จ</span>
        <span class="step-desc">ถอดแบบแล้ว</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">📱 STEP 2: เปิดหน้า Scan & Activate</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">📷 STEP 3: Scan QR Code</span>
        <span class="step-desc">ชี้กล้องไปที่ฉลาก</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">🔍 STEP 4: ตรวจสอบข้อมูล</span>
        <span class="step-desc">ต้องขึ้นสถานะ Pending</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">🟢 STEP 5: กด Activate</span>
        <span class="step-desc">เปลี่ยนสถานะเป็น Activated</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">➡️ STEP 6: ส่งต่อ QC</span>
    </div>
</div>

### 3.3 เวลาทำงานโดยประมาณ

| งาน | เวลา/ชิ้น |
|-----|----------|
| พิมพ์ฉลาก (10 ชิ้น) | 5-10 นาที |
| ติดฉลาก | 1-2 นาที/ชิ้น |
| Activate | 30 วินาที/ชิ้น |

---

## 4. คู่มือการทำงาน - QC

### 4.1 ตำแหน่งงาน: พนักงานฝ่ายตรวจสอบคุณภาพ

**หน้าที่หลัก:**
- ตรวจสอบคุณภาพชิ้นงานตามมาตรฐาน
- บันทึกผล QC Pass หรือ QC Fail
- บันทึกหมายเหตุกรณีไม่ผ่าน

### 4.2 ขั้นตอนการทำงาน (Step-by-Step)

<div class="flow-container">
    <div class="flow-step step-qc">
        <span class="step-title">📥 STEP 1: รับแจ้งงานรอตรวจ</span>
    </div>
    <div class="flow-step step-qc">
        <span class="step-title">📱 STEP 2: เปิดหน้า Scan</span>
    </div>
    <div class="flow-step step-qc">
        <span class="step-title">📷 STEP 3: Scan QR Code</span>
        <span class="step-desc">สถานะต้องเป็น Activated</span>
    </div>
    <div class="flow-step step-qc">
        <span class="step-title">🔍 STEP 4: ตรวจสอบคุณภาพ</span>
        <span class="step-desc">ขนาด, รูปร่าง, ผิว, เหล็กเสริม</span>
    </div>
    
    <div class="flow-step step-decision">
        <span class="step-title">⚖️ ประเมินผล (Decision)</span>
    </div>

    <!-- Pass -->
    <div class="flow-step step-pass">
        <span class="step-title">✅ STEP 5A: ผ่าน (QC Pass)</span>
        <span class="step-desc">กดปุ่ม Pass -> แจ้ง Warehouse</span>
    </div>

    <!-- Fail -->
    <div class="flow-step step-fail">
        <span class="step-title">❌ STEP 5B: ไม่ผ่าน (QC Fail)</span>
        <span class="step-desc">กดปุ่ม Fail -> ระบุเหตุผล -> ส่งแก้</span>
    </div>
</div>

### 4.3 เกณฑ์การตรวจสอบ QC

| รายการ | เกณฑ์ผ่าน | เกณฑ์ไม่ผ่าน |
|--------|----------|-------------|
| ขนาด | ±5mm จากแบบ | เกิน ±5mm |
| รูปร่าง | ไม่บิดเบี้ยว | บิดเบี้ยวมองเห็นได้ชัด |
| พื้นผิว | เรียบ, รูพรุน <5% | รูพรุน >5% หรือขรุขระ |
| รอยแตก | ไม่มี | มีรอยแตกใดๆ |
| เหล็กเสริม | ไม่โผล่ | มีเหล็กโผล่ |

---

## 5. คู่มือการทำงาน - Warehouse

### 5.1 ตำแหน่งงาน: พนักงานฝ่ายคลังสินค้า

**หน้าที่หลัก:**
- รับชิ้นงานที่ผ่าน QC เข้าคลัง
- จัดเก็บและบันทึกตำแหน่ง
- เตรียมชิ้นงานสำหรับจัดส่ง

### 5.2 ขั้นตอนการทำงาน (Step-by-Step)

<div class="flow-container">
    <div class="flow-step step-warehouse">
        <span class="step-title">📥 STEP 1: รับแจ้งของผ่าน QC</span>
    </div>
    <div class="flow-step step-warehouse">
        <span class="step-title">📱 STEP 2: เปิดหน้า Scan</span>
    </div>
    <div class="flow-step step-warehouse">
        <span class="step-title">📷 STEP 3: Scan QR Code</span>
        <span class="step-desc">สถานะต้องเป็น QC Passed</span>
    </div>
    <div class="flow-step step-warehouse">
        <span class="step-title">🔍 STEP 4: ตรวจสอบสภาพ</span>
        <span class="step-desc">ไม่เสียหายตอนขนย้าย</span>
    </div>
    <div class="flow-step step-warehouse">
        <span class="step-title">🟣 STEP 5: กด "รับเข้าคลัง"</span>
        <span class="step-desc">Status -> In Stock</span>
    </div>
    <div class="flow-step step-warehouse">
        <span class="step-title">📍 STEP 6: จัดเก็บ & บันทึกตำแหน่ง</span>
        <span class="step-desc">Zone / Shelf</span>
    </div>
     <div class="flow-step step-warehouse">
        <span class="step-title">📝 STEP 7: ลงทะเบียนคลัง</span>
    </div>
</div>

---

## 6. คู่มือการทำงาน - Shipping

### 6.1 ตำแหน่งงาน: พนักงานฝ่ายจัดส่ง

**หน้าที่หลัก:**
- รับใบสั่งจัดส่ง
- หยิบชิ้นงานจากคลัง
- ขนส่งและส่งมอบที่หน้างาน

### 6.2 ขั้นตอนการทำงาน (Step-by-Step)

#### PHASE A: เตรียมจัดส่ง (ที่คลัง)

<div class="flow-container">
    <div class="flow-step step-shipping">
        <span class="step-title">📋 STEP 1: รับใบสั่งจัดส่ง</span>
        <span class="step-desc">ตรวจสอบรายการ/สถานที่</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">📦 STEP 2: ไปที่คลัง</span>
        <span class="step-desc">แจ้งเบิกของ</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">🏗️ STEP 3: หยิบชิ้นงาน</span>
        <span class="step-desc">ตามตำแหน่งที่ระบุ</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">📤 STEP 4: Scan "จัดส่ง" (Shipping)</span>
        <span class="step-desc">ทำทีละชิ้นจนครบ</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">🚚 STEP 5: ขนขึ้นรถ</span>
        <span class="step-desc">รัดยึดให้แน่นหนา</span>
    </div>
</div>

#### PHASE B & C: ขนส่งและส่งมอบ

<div class="flow-container">
    <div class="flow-step step-shipping">
        <span class="step-title">🚚 STEP 6: เดินทางไปหน้างาน</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">📍 STEP 7: ถึงหน้างาน</span>
        <span class="step-desc">ติดต่อผู้รับ</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">🔵 STEP 8: Scan "ส่งถึงแล้ว" (Delivered)</span>
        <span class="step-desc">เปลี่ยนสถานะเป็น Delivered</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">📝 STEP 9: ลงนามรับมอบ</span>
        <span class="step-desc">ถ่ายรูปหลักฐาน</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">➡️ STEP 10: ส่งต่อทีมติดตั้ง</span>
    </div>
</div>

---

## 7. คู่มือการทำงาน - Installation

### 7.1 ตำแหน่งงาน: พนักงานฝ่ายติดตั้ง

**หน้าที่หลัก:**
- รับชิ้นงานที่หน้างาน
- ติดตั้งตามแบบและมาตรฐาน
- บันทึกผลการติดตั้ง

### 7.2 ขั้นตอนการทำงาน (Step-by-Step)

<div class="flow-container">
    <div class="flow-step step-installation">
        <span class="step-title">📥 STEP 1: รับชิ้นงาน</span>
        <span class="step-desc">จากทีม Shipping</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">🏗️ STEP 2: เตรียมหน้างาน</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">📷 STEP 3: Scan ก่อนติดตั้ง</span>
        <span class="step-desc">ยืนยันชิ้นงานถูกต้อง</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">🚧 STEP 4: กด "กำลังติดตั้ง"</span>
        <span class="step-desc">Status -> Installing</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">🔧 STEP 5: ดำเนินการติดตั้ง</span>
        <span class="step-desc">ตามแบบวิศวกรรม</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">🔍 STEP 6: ตรวจสอบหลังติดตั้ง</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">📷 STEP 7: Scan หลังติดตั้ง</span>
        <span class="step-desc">เพื่อยืนยันจบงาน</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">🏁 STEP 8: กด "ติดตั้งเสร็จ"</span>
        <span class="step-desc">Status -> Installed</span>
    </div>
    <div class="flow-step step-pass">
        <span class="step-title">💾 STEP 9: บันทึกรายงาน/รูปถ่าย</span>
        <span class="step-desc">ปิดจ็อบ</span>
    </div>
</div>

---

## 8. ตารางความรับผิดชอบ (RACI Matrix)

### 8.1 RACI Legend

| รหัส | ความหมาย | คำอธิบาย |
|------|----------|----------|
| **R** | Responsible | ผู้รับผิดชอบทำงาน (ผู้ลงมือทำ) |
| **A** | Accountable | ผู้รับผิดชอบผลงาน (ผู้อนุมัติ/รับผิดชอบหลัก) |
| **C** | Consulted | ผู้ให้คำปรึกษา (ต้องถามก่อนทำ) |
| **I** | Informed | ผู้ที่ต้องแจ้งให้ทราบ (แจ้งเพื่อทราบ) |

### 8.2 RACI Matrix

| กิจกรรม | Admin | Planning | QC | Warehouse | Shipping | Installation |
|---------|:-----:|:--------:|:--:|:---------:|:--------:|:------------:|
| **พิมพ์ฉลาก** | I | R/A | - | - | - | - |
| **ติดฉลากที่แบบหล่อ** | - | R/A | - | - | - | - |
| **Activate ชิ้นงาน** | I | R/A | I | - | - | - |
| **ตรวจ QC** | I | I | R/A | I | - | - |
| **บันทึก QC Fail** | I | I | R/A | - | - | - |
| **รับเข้าคลัง** | I | - | I | R/A | - | - |
| **จัดเก็บในคลัง** | - | - | - | R/A | - | - |
| **เตรียมจัดส่ง** | I | I | - | C | R/A | I |
| **ขนส่ง** | I | - | - | - | R/A | I |
| **ส่งมอบหน้างาน** | I | - | - | - | R/A | I |
| **ติดตั้ง** | I | - | - | - | - | R/A |
| **บันทึกผลติดตั้ง** | I | - | - | - | - | R/A |
| **Archive ชิ้นงาน** | R/A | I | - | - | - | I |
| **จัดการผู้ใช้** | R/A | - | - | - | - | - |
| **ดู Tracking** | R/A | - | - | - | - | - |

---

## 9. Checklist สำหรับแต่ละ Role

### 9.1 Planning
- [ ] เตรียมข้อมูลโครงการครบถ้วน
- [ ] พิมพ์ฉลากชัดเจน ไม่เบลอ
- [ ] ติดฉลากที่แบบหล่อแน่นหนา
- [ ] Activate ชิ้นงานทันทีหลังถอดแบบ

### 9.2 QC
- [ ] เครื่องมือวัดพร้อมใช้งาน
- [ ] ตรวจสอบตามมาตรฐานทุกจุด
- [ ] บันทึกผลในระบบทันที
- [ ] ถ่ายรูปกรณีพบปัญหา Fail

### 9.3 Warehouse
- [ ] ตรวจสอบสภาพของตอนรับเข้า
- [ ] จัดเก็บในตำแหน่งที่ปลอดภัย
- [ ] อัปเดต Map ตำแหน่งจัดเก็บเสมอ

### 9.4 Shipping
- [ ] เช็ครายการของจัดส่งเทียบกับใบสั่ง
- [ ] รัดชิ้นงานบนรถให้แน่นหนา
- [ ] Scan Delivered ทันทีที่ลงของเสร็จ

### 9.5 Installation
- [ ] ตรวจสอบชิ้นงานก่อนติดตั้ง
- [ ] ติดตั้งตาม Spec อย่างเคร่งครัด
- [ ] Scan Installed เพื่อจบงาน

---

## 10. KPI และเป้าหมาย

### 10.1 KPI รายบุคคล

| Role | KPI | เป้าหมาย | วิธีวัด |
|------|-----|---------|--------|
| **Planning** | จำนวนฉลากที่พิมพ์/วัน | ≥50 ชิ้น | นับจากระบบ |
| **Planning** | Activate ภายใน 24 ชม. หลังหล่อ | ≥95% | ตรวจจาก Timeline |
| **QC** | จำนวนชิ้นที่ตรวจ/วัน | ≥30 ชิ้น | นับจากระบบ |
| **QC** | อัตรา QC Pass | ≥90% | (Pass/Total) x 100 |
| **Warehouse** | เวลารับเข้าคลัง | ภายใน 4 ชม. หลัง QC | ตรวจจาก Timeline |
| **Shipping** | จัดส่งตรงเวลา | ≥95% | (ตรงเวลา/Total) x 100 |
| **Shipping** | ไม่มีความเสียหายระหว่างขนส่ง | 100% | นับ Claim |
| **Installation** | ติดตั้งตรงแผน | ≥90% | (ตรงแผน/Total) x 100 |
| **Installation** | ไม่มีงานแก้ไข | ≥95% | นับงานซ่อม |

### 10.2 KPI รวมทั้งระบบ

| KPI | เป้าหมาย | คำอธิบาย |
|-----|---------|----------|
| Cycle Time (พิมพ์→ติดตั้ง) | ≤14 วัน | เวลาเฉลี่ยทั้ง process |
| อัตราใช้งานระบบ | ≥95% | % ที่ Scan ครบทุกขั้นตอน |
| ความถูกต้องของข้อมูล | ≥99% | ข้อมูลตรงกับชิ้นงานจริง |
| ความพึงพอใจลูกค้า | ≥4.5/5 | จาก Survey |

### 10.3 Dashboard Metrics

#### 📊 สถิติรายวัน
*   ชิ้นงานใหม่วันนี้: XX ชิ้น
*   QC Pass วันนี้: XX ชิ้น
*   จัดส่งวันนี้: XX ชิ้น
*   ติดตั้งเสร็จวันนี้: XX ชิ้น

#### 📈 สถิติรายเดือน
*   ชิ้นงานรวม: XXX ชิ้น
*   อัตรา QC Pass: XX%
*   จัดส่งตรงเวลา: XX%
*   ติดตั้งเสร็จ: XXX ชิ้น

#### ⏱️ เวลาเฉลี่ย (Cycle Time)
*   Pending → Activated: X ชั่วโมง
*   Activated → QC Pass: X วัน
*   QC Pass → In Stock: X ชั่วโมง
*   In Stock → Delivered: X วัน
*   Delivered → Installed: X วัน

---

## เวอร์ชัน

| เวอร์ชัน | วันที่ | การเปลี่ยนแปลง |
|---------|--------|---------------|
| 1.0 | 28/01/2026 | เวอร์ชันแรก |
| 1.1 | 29/01/2026 | ปรับปรุงสำหรับ Vertical Layout |

---

*เอกสารนี้จัดทำโดย Barcode Precast*
*สำหรับวางผังการทำงานและ Model พนักงาน*
*อัปเดตล่าสุด: 29 มกราคม 2026*
