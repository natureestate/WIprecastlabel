from pathlib import Path

# List of icons matches download_icons.py
ICONS = [
    "check-circle", "x-circle", "square", "check-square", 
    "clipboard", "mail", "smartphone", "package", "printer", 
    "file-text", "bar-chart", "trending-up", "trending-down", 
    "calendar", "map-pin", "paperclip", "crown", "user", 
    "users", "wrench", "factory", "lock", "lock-open", 
    "key", "truck", "car", "circle", "alert-triangle", 
    "info", "lightbulb", "play", "pause", "chevron-down", 
    "chevron-up", "chevron-right", "chevron-left", "clock", 
    "timer", "building-2", "building", "settings", "hammer"
]

CSS_HEADER = """/**
 * Lucide CSS - Styles for Lucide Icons
 * Generated automatically. Do not edit manually.
 */

/* =========================================
   ICON BASE STYLES
   ========================================= */

.icon {
    display: inline-block;
    vertical-align: middle;
    width: 1em;
    height: 1em;
    margin: 0 4px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
}

/* =========================================
   ICON SIZES
   ========================================= */

.icon-sm { width: 12px; height: 12px; }
.icon-md { width: 16px; height: 16px; }
.icon-lg { width: 20px; height: 20px; }
.icon-xl { width: 24px; height: 24px; }

/* =========================================
   ICON MAPPINGS
   ========================================= */
"""

def generate_css():
    css_content = CSS_HEADER
    
    # Absolute path to icons
    icon_base_path = "file:///Users/macbooknow/WIPrecastLabel/export/assets/icons"
    
    for icon in sorted(ICONS):
        css_content += f"""
.icon[data-icon="{icon}"] {{
    background-image: url('{icon_base_path}/{icon}.svg');
}}
"""

    # Add color classes using filters (targeted for black SVG to color)
    # Values approximated from https://codepen.io/sosuke/pen/Pjoqqp
    css_content += """
/* =========================================
   ICON COLORS
   ========================================= */

.icon-green {
    filter: invert(60%) sepia(53%) saturate(2878%) hue-rotate(100deg) brightness(95%) contrast(80%);
}

.icon-yellow {
    filter: invert(79%) sepia(61%) saturate(527%) hue-rotate(360deg) brightness(102%) contrast(96%);
}

.icon-red {
    filter: invert(38%) sepia(77%) saturate(2476%) hue-rotate(336deg) brightness(95%) contrast(90%);
}

.icon-blue {
    filter: invert(42%) sepia(93%) saturate(1352%) hue-rotate(200deg) brightness(98%) contrast(93%);
}
"""

    output_path = Path("/Users/macbooknow/WIPrecastLabel/export/styles/lucide.css")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(css_content)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_css()
