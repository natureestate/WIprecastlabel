# คู่มือการใช้งาน Precast Pro Labeler

1. [ภาพรวมระบบ](#1-ภาพรวมระบบ)
2. [การเข้าสู่ระบบ](#2-การเข้าสู่ระบบ)
3. [บทบาทและสิทธิ์ผู้ใช้](#3-บทบาทและสิทธิ์ผู้ใช้)
4. [ขั้นตอนการทำงานหลัก (Main Workflow)](#4-ขั้นตอนการทำงานหลัก-main-workflow)
5. [คู่มือสำหรับแต่ละ Role](#5-คู่มือสำหรับแต่ละ-role)
6. [สถานะชิ้นงาน (Status Flow)](#6-สถานะชิ้นงาน-status-flow)
7. [คู่มือการใช้งานแต่ละหน้า](#7-คู่มือการใช้งานแต่ละหน้า)
8. [FAQ และการแก้ไขปัญหา](#8-faq-และการแก้ไขปัญหา)

---

## 1. ภาพรวมระบบ

### 1.1 Precast Pro Labeler คืออะไร?

**Precast Pro Labeler** เป็นระบบจัดการและติดตามชิ้นส่วนคอนกรีตสำเร็จรูป (Precast Concrete) ด้วย QR Code ออกแบบมาเพื่อ:

- ✅ สร้างและพิมพ์ฉลาก QR Code สำหรับชิ้นงาน
- ✅ ติดตามสถานะชิ้นงานตั้งแต่ผลิตจนถึงติดตั้ง
- ✅ Scan QR Code เพื่ออัปเดตสถานะได้ทุกที่ทุกเวลา
- ✅ ดูรายงานและประวัติการดำเนินการ
- ✅ ให้ลูกค้าตรวจสอบสถานะชิ้นงานผ่าน QR Code

### 1.2 ความต้องการของระบบ

| รายการ | ความต้องการ |
|--------|-------------|
| Browser | Chrome, Firefox, Safari, Edge (เวอร์ชันล่าสุด) |
| อุปกรณ์ | Desktop, Tablet, Smartphone |
| Internet | จำเป็นต้องมีการเชื่อมต่อ Internet |
| กล้อง | สำหรับ Scan QR Code (บนมือถือ) |

### 1.3 การติดตั้งแอปบนมือถือ (PWA)

1. เปิดเว็บไซต์ผ่าน Chrome บนมือถือ
2. กดที่เมนู (⋮) → "Add to Home Screen" หรือ "ติดตั้งแอป"
3. แอปจะปรากฏบนหน้าจอเหมือนแอปทั่วไป

---

## 2. การเข้าสู่ระบบ

### 2.1 ขั้นตอนการ Login

1. กรอก **Email** ที่ลงทะเบียนไว้
2. กรอก **Password**
3. กดปุ่ม **"เข้าสู่ระบบ"**

### 2.2 สถานะบัญชีผู้ใช้

| สถานะ | คำอธิบาย | การเข้าถึง |
|-------|----------|------------|
| 🟡 Pending | รอการอนุมัติจาก Admin | ดูได้เฉพาะหน้า Scan (View-only) |
| 🟢 Active | บัญชีใช้งานปกติ | เข้าถึงตาม Role ที่กำหนด |
| 🔴 Suspended | บัญชีถูกระงับ | ไม่สามารถเข้าใช้งานได้ |

---

## 3. บทบาทและสิทธิ์ผู้ใช้

### 3.1 ตารางสิทธิ์ตาม Role

| หน้า/ฟังก์ชัน | Admin | Planning | QC | Warehouse | Shipping | Installation |
|--------------|:-----:|:--------:|:--:|:---------:|:--------:|:------------:|
| พิมพ์ฉลาก | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| ประวัติการพิมพ์ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Scan & Confirm | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Tracking Dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| จัดการผู้ใช้ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Activate ชิ้นงาน | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| QC Pass/Fail | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| รับเข้าคลัง | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ |
| จัดส่ง | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| ติดตั้ง | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |

### 3.2 รายละเอียดแต่ละ Role

#### 👑 Admin (ผู้ดูแลระบบ)
- เข้าถึงได้ทุกหน้าและทุกฟังก์ชัน
- จัดการผู้ใช้ (เพิ่ม, แก้ไข, อนุมัติ, ระงับ)
- ดู Tracking Dashboard
- กำหนด Custom Permissions

#### 📋 Planning (ฝ่ายวางแผน)
- สร้างและพิมพ์ฉลาก QR Code
- Activate ชิ้นงานใหม่หลังจากหล่อเสร็จ
- ดูประวัติการพิมพ์

#### ✅ QC (ฝ่ายตรวจสอบคุณภาพ)
- ตรวจสอบคุณภาพชิ้นงาน
- เปลี่ยนสถานะ QC Pass หรือ QC Fail
- บันทึกหมายเหตุกรณีไม่ผ่าน QC

#### 📦 Warehouse (ฝ่ายคลังสินค้า)
- รับชิ้นงานที่ผ่าน QC เข้าคลัง
- เปลี่ยนสถานะเป็น In Stock

#### 🚚 Shipping (ฝ่ายจัดส่ง)
- จัดส่งชิ้นงานไปยังหน้างาน
- เปลี่ยนสถานะ Shipping → Delivered

#### 🔧 Installation (ฝ่ายติดตั้ง)
- ติดตั้งชิ้นงานที่หน้างาน
- เปลี่ยนสถานะ Installing → Installed

---

## 4. ขั้นตอนการทำงานหลัก (Main Workflow)

### 4.1 Workflow Diagram

<div class="flow-container">
    
    <!-- Planning -->
    <div class="flow-step step-planning">
        <span class="step-title">📋 ฝ่ายวางแผน (Planning)</span>
    </div>

    <div class="flow-step step-planning">
        <span class="step-title">🖨️ 1. พิมพ์ฉลาก (Print Label)</span>
        <span class="step-meta">Status: PENDING 🟡</span>
    </div>

    <div class="flow-step step-planning">
        <span class="step-title">📷 2. Scan & Activate</span>
        <span class="step-desc">ติดฉลากที่ชิ้นงานจริงและเปิดใช้งาน</span>
        <span class="step-meta">Status: ACTIVATED 🟢</span>
    </div>

    <div class="flow-step step-planning">
        <span class="step-title">🏗️ 3. หล่อชิ้นงาน (Casting)</span>
        <span class="step-meta">Status: PRODUCED 🔵</span>
    </div>

    <!-- QC -->
    <div class="flow-step step-qc">
        <span class="step-title">🔍 ฝ่ายตรวจสอบคุณภาพ (QC)</span>
    </div>

    <div class="flow-step step-decision">
        <span class="step-title">⚖️ ตรวจสอบคุณภาพ (QC Inspect)</span>
    </div>

    <div class="flow-step step-fail">
        <span class="step-title">❌ กรณีไม่ผ่าน (QC FAILED)</span>
        <span class="step-desc">ส่งซ่อม/แก้ไขงาน</span>
    </div>

    <div class="flow-step step-pass">
        <span class="step-title">✅ กรณีผ่าน (QC PASSED)</span>
    </div>

    <!-- Warehouse -->
    <div class="flow-step step-warehouse">
        <span class="step-title">📦 ฝ่ายคลังสินค้า (Warehouse)</span>
    </div>

    <div class="flow-step step-warehouse">
        <span class="step-title">📥 5. รับเข้าสต็อก (Stock In)</span>
        <span class="step-meta">Status: IN_STOCK 🟣</span>
    </div>

    <!-- Shipping -->
    <div class="flow-step step-shipping">
        <span class="step-title">🚚 ฝ่ายจัดส่ง (Shipping)</span>
    </div>

    <div class="flow-step step-shipping">
        <span class="step-title">📤 6. จัดส่งสินค้า (Shipping)</span>
        <span class="step-meta">Status: SHIPPING 🟠</span>
    </div>

    <div class="flow-step step-shipping">
        <span class="step-title">📍 7. ส่งถึงหน่วยงาน (Delivered)</span>
        <span class="step-meta">Status: DELIVERED 🔵</span>
    </div>

    <!-- Installation -->
    <div class="flow-step step-installation">
        <span class="step-title">🔧 ฝ่ายติดตั้ง (Installation)</span>
    </div>

    <div class="flow-step step-installation">
        <span class="step-title">🏗️ 8. กำลังติดตั้ง (Installing)</span>
        <span class="step-meta">Status: INSTALLING 🚧</span>
    </div>

    <div class="flow-step step-installation">
        <span class="step-title">✅ 9. ติดตั้งเสร็จสิ้น (Installed)</span>
        <span class="step-meta">Status: INSTALLED 🏁</span>
    </div>

    <div class="flow-step step-installation">
        <span class="step-title">💾 10. จบงาน (Archive)</span>
        <span class="step-meta">Status: ARCHIVED ⚪️</span>
    </div>

</div>

### 4.2 Timeline การทำงาน

*(Timeline Diagram ถูกแทนที่ด้วยรายละเอียดใน Flow ด้านบนแล้ว)*

---

## 5. คู่มือสำหรับแต่ละ Role

### 5.1 คู่มือสำหรับ Planning (ฝ่ายวางแผน)

#### งานหลัก: พิมพ์ฉลากและ Activate ชิ้นงาน

<div class="flow-container">
    <div class="flow-step step-planning">
        <span class="step-title">📋 1. มีคำสั่งผลิต</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">🔒 2. Login เข้าระบบ</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">🖨️ 3. ไปหน้าพิมพ์ฉลาก</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">📝 4. กรอกข้อมูล & เพิ่มรายการ</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">🏷️ 5. กดพิมพ์ PDF & ติดฉลากที่แบบหล่อ</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">📷 6. หล่อเสร็จ -> Scan QR Code</span>
    </div>
    <div class="flow-step step-planning">
        <span class="step-title">🟢 7. กด Activate</span>
    </div>
</div>

#### ขั้นตอนละเอียด: การพิมพ์ฉลาก

| ขั้นตอน | การดำเนินการ | หมายเหตุ |
|---------|-------------|----------|
| 1 | เปิดหน้า **พิมพ์ฉลาก** (หน้าแรก) | - |
| 2 | กรอก **ชื่อลูกค้า** | เช่น "บริษัท ABC จำกัด" |
| 3 | กรอก **ชื่อโครงการ** | เช่น "อาคาร XYZ" |
| 4 | กรอก **สถานที่หล่อ** | เช่น "โรงงาน A" |
| 5 | กดปุ่ม **"+ เพิ่มรายการ"** | - |
| 6 | เลือก **ประเภทชิ้นงาน** | เช่น "เสาเข็ม", "พื้น", "ผนัง" |
| 7 | กรอก **จำนวน** | จำนวนชิ้นที่ต้องการพิมพ์ |
| 8 | ระบบจะสร้าง **Running Number** อัตโนมัติ | เช่น "ABC-001", "ABC-002" |
| 9 | เลือก **เทมเพลต** ที่ต้องการ | Default / Custom / Saved |
| 10 | ปรับแต่งด้วย **Visual Editor** (ถ้าต้องการ) | ลาก-วาง, แก้ไขข้อความ |
| 11 | กดปุ่ม **"พิมพ์ PDF"** | ระบบจะสร้าง PDF |
| 12 | **พิมพ์** และนำไปติดที่แบบหล่อ | - |

---

### 5.2 คู่มือสำหรับ QC (ฝ่ายตรวจสอบคุณภาพ)

#### งานหลัก: ตรวจสอบคุณภาพและบันทึกผล

<div class="flow-container">
    <div class="flow-step step-qc">
        <span class="step-title">📥 1. รับแจ้งงานรอตรวจ</span>
    </div>
    <div class="flow-step step-qc">
        <span class="step-title">📷 2. Scan QR Code</span>
    </div>
    <div class="flow-step step-qc">
        <span class="step-title">🔍 3. ตรวจสอบคุณภาพ</span>
        <span class="step-desc">ขนาด, รูปร่าง, ผิว</span>
    </div>
    <div class="flow-step step-decision">
        <span class="step-title">⚖️ ผลการตรวจ?</span>
    </div>
    <div class="flow-step step-pass">
        <span class="step-title">✅ กรณีผ่าน (QC PASS)</span>
    </div>
    <div class="flow-step step-fail">
        <span class="step-title">❌ กรณีไม่ผ่าน (QC FAIL)</span>
        <span class="step-desc">ระบุเหตุผล -> ส่งแก้</span>
    </div>
</div>


#### รายการตรวจสอบ QC

- ☐ 1. ขนาดถูกต้องตามแบบ (±5mm)
- ☐ 2. รูปร่างไม่บิดเบี้ยว
- ☐ 3. ไม่มีรอยแตกร้าว
- ☐ 4. ผิวเรียบสม่ำเสมอ
- ☐ 5. เหล็กเสริมไม่โผล่
- ☐ 6. ตำแหน่งเหล็กยึดถูกต้อง

---

### 5.3 คู่มือสำหรับ Warehouse (ฝ่ายคลังสินค้า)

#### งานหลัก: รับชิ้นงานเข้าคลัง

<div class="flow-container">
    <div class="flow-step step-warehouse">
        <span class="step-title">📷 1. Scan QR Code</span>
        <span class="step-desc">ต้องเป็น QC Passed</span>
    </div>
    <div class="flow-step step-warehouse">
        <span class="step-title">📥 2. กด "รับเข้าคลัง"</span>
        <span class="step-desc">Status: In Stock 🟣</span>
    </div>
    <div class="flow-step step-warehouse">
        <span class="step-title">📦 3. จัดเก็บ & บันทึกตำแหน่ง</span>
    </div>
</div>

---

### 5.4 คู่มือสำหรับ Shipping (ฝ่ายจัดส่ง)

#### งานหลัก: จัดส่งชิ้นงานไปยังหน้างาน

<div class="flow-container">
    <div class="flow-step step-shipping">
        <span class="step-title">📋 1. รับใบสั่งจัดส่ง & หยิบของ</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">truck 2. Scan -> กด "จัดส่ง"</span>
        <span class="step-desc">Status: Shipping 🟠</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">🚚 3. ขนส่งถึงหน้างาน</span>
    </div>
    <div class="flow-step step-shipping">
        <span class="step-title">📍 4. Scan -> กด "ส่งถึงแล้ว"</span>
        <span class="step-desc">Status: Delivered 🔵</span>
    </div>
</div>

---

### 5.5 คู่มือสำหรับ Installation (ฝ่ายติดตั้ง)

#### งานหลัก: ติดตั้งชิ้นงานที่หน้างาน

<div class="flow-container">
    <div class="flow-step step-installation">
        <span class="step-title">📥 1. รับชิ้นงาน</span>
        <span class="step-desc">รับจาก Shipping ตรวจสอบสภาพ</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">🏗️ 2. เตรียมติดตั้ง</span>
        <span class="step-desc">เช็คพื้นที่และเครื่องมือ</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">📷 3. Scan "Delivered"</span>
        <span class="step-desc">ยืนยันว่าถึงหน้างานแล้ว</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">🚧 4. กด "กำลังติดตั้ง"</span>
        <span class="step-desc">Status -> Installing 🚧</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">🔧 5. ดำเนินการติดตั้ง</span>
        <span class="step-desc">ตามแบบและมาตรฐาน</span>
    </div>
    <div class="flow-step step-installation">
        <span class="step-title">🏁 6. สแกนอีกครั้ง -> กด "ติดตั้งเสร็จ"</span>
        <span class="step-desc">Status -> Installed ✅</span>
    </div>
</div>

---

### 5.6 คู่มือสำหรับ Admin (ผู้ดูแลระบบ)

#### งานหลัก: จัดการระบบ, ผู้ใช้, และติดตามภาพรวม

<div class="flow-container">
    <div class="flow-step step-admin">
        <span class="step-title">👑 Admin Dashboard</span>
    </div>
    
    <!-- User Management -->
    <div class="flow-step step-admin">
        <span class="step-title">👥 A. จัดการผู้ใช้ (Users)</span>
    </div>
    <div class="flow-step step-pass">
        <span class="step-title">✅ อนุมัติผู้ใช้ใหม่</span>
        <span class="step-desc">ตรวจสอบและกด Approve</span>
    </div>
    <div class="flow-step step-admin">
        <span class="step-title">🔒 กำหนดสิทธิ์ (Role)</span>
        <span class="step-desc">Admin, Planning, QC, etc.</span>
    </div>
    <div class="flow-step step-fail">
        <span class="step-title">🚫 ระงับบัญชี</span>
        <span class="step-desc">กรณีลาออกหรือทำผิดกฎ</span>
    </div>

    <!-- Tracking -->
    <div class="flow-step step-admin">
        <span class="step-title">📊 B. Tracking Dashboard</span>
    </div>
    <div class="flow-step step-admin">
        <span class="step-title">🔍 ค้นหาและกรอง</span>
        <span class="step-desc">ดูสถานะชิ้นงานทุกชิ้น</span>
    </div>
    <div class="flow-step step-admin">
        <span class="step-title">🔄 แก้ไขสถานะ</span>
        <span class="step-desc">กรณีพนักงานทำผิดขั้นตอน</span>
    </div>
    <div class="flow-step step-admin">
        <span class="step-title">💾 Report & Archive</span>
        <span class="step-desc">ดูรายงานและจบงาน</span>
    </div>
</div>

---

## 6. สถานะชิ้นงาน (Status Flow)

### 6.1 รายละเอียดแต่ละสถานะ

| สถานะ | รหัส | ความหมาย | สี | Role ที่เปลี่ยน |
|-------|------|----------|-----|----------------|
| รอดำเนินการ | `pending` | สร้างจากการพิมพ์ฉลาก รอ Activate | ⚪ เทา | - |
| เปิดใช้งาน | `activated` | Planning Scan และ Activate แล้ว | 🔵 ฟ้า | Planning |
| ผลิตเสร็จ | `produced` | หล่อชิ้นงานเสร็จแล้ว | 🟣 ม่วง | Planning |
| ผ่าน QC | `qc_passed` | ตรวจสอบคุณภาพผ่าน | 🟢 เขียว | QC |
| ไม่ผ่าน QC | `qc_failed` | ตรวจสอบคุณภาพไม่ผ่าน | 🔴 แดง | QC |
| ในคลัง | `in_stock` | รับเข้าคลังแล้ว รอจัดส่ง | 🟡 เหลือง (ทอง) | Warehouse |
| กำลังจัดส่ง | `shipping` | อยู่ระหว่างขนส่ง | 🟠 ส้ม | Shipping |
| ส่งถึงแล้ว | `delivered` | ถึงหน้างานแล้ว รอติดตั้ง | 🔵 น้ำเงินเข้ม | Shipping |
| กำลังติดตั้ง | `installing` | อยู่ระหว่างติดตั้ง | 🚧 ลายขวาง | Installation |
| ติดตั้งเสร็จ | `installed` | ติดตั้งเรียบร้อย | ✅ เขียวเข้ม | Installation |
| เก็บถาวร | `archived` | จบงานแล้ว | ⚫ ดำ | Admin |

---

## 7. คู่มือการใช้งานแต่ละหน้า

### 7.1 หน้า Home / พิมพ์ฉลาก
*   **สำหรับ:** Admin, Planning
*   **หน้าที่:** สร้าง Project, เพิ่มรายการชิ้นงาน, พิมพ์ฉลาก QR Code
*   **ฟีเจอร์:** Visual Editor สำหรับปรับแต่งฉลาก

### 7.2 หน้า Scan & Confirm (PWA)
*   **สำหรับ:** ทุก Role (Production)
*   **หน้าที่:** สแกน QR Code เพื่อดูข้อมูลและเปลี่ยนสถานะ
*   **การทำงาน:** ปุ่ม Action จะเปลี่ยนไปตามสถานะปัจจุบันและสิทธิ์ของผู้ใช้

### 7.3 หน้า Tracking Dashboard
*   **สำหรับ:** Admin
*   **หน้าที่:** ดูภาพรวมสถานะชิ้นงานทั้งหมด
*   **ฟีเจอร์:** กราฟสรุป, ตารางรายการ, ตัวกรอง (Filter), และ Timeline

### 7.4 หน้า Public Status
*   **สำหรับ:** ลูกค้า (ไม่ต้อง Login)
*   **หน้าที่:** ตรวจสอบความคืบหน้าของชิ้นงาน
*   **ฟีเจอร์:** สแกน QR Code เพื่อดูสถานะ, รูปถ่าย, และวันที่ติดตั้ง

---

## 8. FAQ และการแก้ไขปัญหา

### 8.1 คำถามที่พบบ่อย

1.  **Q: ลืมรหัสผ่านทำอย่างไร?**
    *   A: ติดต่อ Admin เพื่อให้ Reset รหัสผ่านชั่วคราว (ยังไม่มีระบบกู้คืนเองทางอีเมลในเวอร์ชันนี้)

2.  **Q: Scan QR Code ไม่ติด?**
    *   A: ตรวจสอบแสงสว่าง, เช็ดเลนส์กล้อง, หรือกดปุ่ม "ระบุรหัสด้วยตนเอง" เพื่อพิมพ์รหัสชิ้นงานแทน

3.  **Q: ทำไมกดปุ่มเปลี่ยนสถานะไม่ได้? (ปุ่มเป็นสีเทา)**
    *   A: คุณอาจไม่มีสิทธิ์ในขั้นตอนนั้น (เช่น Warehouse จะกด QC Pass ไม่ได้) หรือข้ามขั้นตอน (เช่น จะ Shipping ก่อนเข้า Stock ไม่ได้)

4.  **Q: พิมพ์ฉลากแล้วไม่มีอะไรเกิดขึ้น?**
    *   A: โปรดตรวจสอบว่า Browser ของคุณบล็อก Pop-up หรือไม่ ให้กด Allow Pop-up สำหรับเว็บไซต์นี้

5.  **Q: ใช้บน iPhone/iPad ได้ไหม?**
    *   A: ได้ โดยใช้ Safari หรือ Chrome และสามารถกด "Add to Home Screen" เพื่อติดตั้งเป็นแอปได้

### 8.2 การติดต่อ Support

หากพบปัญหาการใช้งาน กรุณาติดต่อทีม IT Support:
*   **Email:** support@barcode.co.th
*   **Line:** @PrecastSupport

---

## เวอร์ชัน

| เวอร์ชัน | วันที่ | การเปลี่ยนแปลง |
|---------|--------|---------------|
| 1.0 | 28/01/2026 | เวอร์ชันแรก |
| 1.1 | 29/01/2026 | ปรับปรุง Workflow Diagram และเพิ่มคู่มือ Admin |

---

*เอกสารนี้จัดทำโดย Barcode Precast*
*สำหรับคู่มือการใช้งานระบบ Precast Pro Labeler*
*อัปเดตล่าสุด: 29 มกราคม 2026*
