"""
Cover Generator - สร้างหน้าปกสำหรับ PDF

ไฟล์นี้สร้าง HTML สำหรับหน้าปกของเอกสาร PDF
พร้อมโลโก้, ชื่อเอกสาร, และข้อมูลต่างๆ
"""

from datetime import datetime
from pathlib import Path


def create_cover_html(
    title: str,
    subtitle: str = "",
    version: str = "1.0",
    date: str = None,
    author: str = "WIPrecastLabel Team",
    logo_path: str = None,
    cover_image_path: str = None
) -> str:
    """
    สร้าง HTML สำหรับหน้าปก
    
    Args:
        title: ชื่อเอกสารหลัก
        subtitle: คำอธิบายเอกสาร
        version: เวอร์ชันเอกสาร
        date: วันที่ (ถ้าไม่ระบุจะใช้วันที่ปัจจุบัน)
        author: ผู้แต่ง/บริษัท
        logo_path: path ของโลโก้ (ถ้ามี)
        cover_image_path: path ของรูปภาพพื้นหลังหน้าปก (ถ้ามี)
    
    Returns:
        HTML string ของหน้าปก
    """
    if date is None:
        date = datetime.now().strftime("%d %B %Y")
    
    # Background Image HTML
    bg_html = ""
    if cover_image_path and Path(cover_image_path).exists():
        bg_html = f'<img src="{cover_image_path}" class="cover-bg" alt="Cover Background">'

    # Logo HTML (ถ้ามี)
    logo_html = ""
    if logo_path and Path(logo_path).exists():
        logo_html = f'<img src="{logo_path}" alt="Logo" class="cover-logo">'
    else:
        # ใช้ placeholder ถ้าไม่มีโลโก้
        logo_html = '<div class="cover-logo-placeholder">WI</div>'
    
    html = f"""
    <div class="cover-page">
        {bg_html}
        <div class="cover-content">
            {logo_html}
            
            <h1 class="cover-title">{title}</h1>
            
            {f'<p class="cover-subtitle">{subtitle}</p>' if subtitle else ''}
            
            <div class="cover-metadata">
                <div class="cover-meta-item">
                    <span class="meta-label">เวอร์ชัน:</span>
                    <span class="meta-value">{version}</span>
                </div>
                <div class="cover-meta-item">
                    <span class="meta-label">วันที่:</span>
                    <span class="meta-value">{date}</span>
                </div>
                <div class="cover-meta-item">
                    <span class="meta-label">จัดทำโดย:</span>
                    <span class="meta-value">{author}</span>
                </div>
            </div>
        </div>
    </div>
    """
    
    return html


def create_back_cover_html(image_path: str = None) -> str:
    """
    สร้าง HTML สำหรับปกหลัง
    
    Args:
        image_path: path ของรูปภาพปกหลัง
        
    Returns:
        HTML string ของปกหลัง
    """
    if not image_path or not Path(image_path).exists():
        return ""
        
    html = f"""
    <div class="back-cover-page">
        <img src="{image_path}" class="back-cover-bg" alt="Back Cover">
    </div>
    """
    return html


def create_toc_html(toc_items: list) -> str:
    """
    สร้าง HTML สำหรับสารบัญ
    
    Args:
        toc_items: รายการ TOC ในรูปแบบ [{"title": "...", "level": 1, "page": 1}, ...]
    
    Returns:
        HTML string ของสารบัญ
    """
    toc_html = """
    <div class="toc-page">
        <h1 class="toc-title">สารบัญ</h1>
        <div class="toc-list">
    """
    
    for item in toc_items:
        level = item.get("level", 1)
        title = item.get("title", "")
        page = item.get("page", "")
        
        indent_class = f"toc-level-{level}"
        
        toc_html += f"""
            <div class="toc-item {indent_class}">
                <span class="toc-text">{title}</span>
                <span class="toc-dots"></span>
                <span class="toc-page-number">{page}</span>
            </div>
        """
    
    toc_html += """
        </div>
    </div>
    """
    
    return toc_html


if __name__ == "__main__":
    # ทดสอบสร้างหน้าปก
    cover = create_cover_html(
        title="คู่มือการใช้งาน Precast Pro Labeler",
        subtitle="ระบบจัดการและติดตามชิ้นส่วนคอนกรีตสำเร็จรูป",
        version="1.0",
        author="WIPrecastLabel Team"
    )
    # print(cover)
    
    # ทดสอบสร้างสารบัญ
    toc_items = [
        {"title": "ภาพรวมระบบ", "level": 1, "page": 3},
        {"title": "การเข้าสู่ระบบ", "level": 1, "page": 5},
        {"title": "ขั้นตอนการ Login", "level": 2, "page": 5},
        {"title": "บทบาทและสิทธิ์ผู้ใช้", "level": 1, "page": 7},
    ]
    toc = create_toc_html(toc_items)
    # print(toc)
