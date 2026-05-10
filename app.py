"""
Nuclear Radiation Interactive Educational App
الإشعاع النووي - برنامج تعليمي تفاعلي
Author: Israa Youssuf Samara
Grade 12 Physics
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import streamlit.components.v1 as components
import random
import math

# ═══════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════
st.set_page_config(
    page_title="الإشعاع النووي | Nuclear Radiation",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ═══════════════════════════════════════════
# GLOBAL CSS
# ═══════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Tajawal:wght@300;400;500;700;800&family=Space+Mono:wght@400;700&display=swap');

:root {
    --bg-primary: #020212;
    --bg-secondary: #06081e;
    --bg-card: rgba(8, 12, 45, 0.85);
    --accent-blue: #00d4ff;
    --accent-green: #00ff88;
    --accent-purple: #b347ff;
    --accent-orange: #ff6b35;
    --accent-yellow: #ffd700;
    --text-primary: #e4e8f5;
    --text-secondary: #7880a0;
    --border-color: rgba(0, 212, 255, 0.18);
}

html, body, [class*="css"] {
    font-family: 'Tajawal', sans-serif !important;
}

.stApp {
    background: var(--bg-primary);
    background-image:
        radial-gradient(ellipse at 15% 15%, rgba(0, 212, 255, 0.06) 0%, transparent 55%),
        radial-gradient(ellipse at 85% 85%, rgba(179, 71, 255, 0.06) 0%, transparent 55%);
    min-height: 100vh;
}

::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--bg-secondary); }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, var(--accent-blue), var(--accent-purple)); border-radius: 4px; }

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0.5rem !important; max-width: 1200px !important; }

/* ★ إخفاء الشريط الجانبي بالكامل */
[data-testid="stSidebar"] { display: none !important; }
[data-testid="stSidebarCollapsedControl"] { display: none !important; }

.card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 20px;
    backdrop-filter: blur(12px);
    margin-bottom: 16px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent-blue), transparent);
    opacity: 0; transition: opacity 0.3s;
}
.card:hover { border-color: rgba(0, 212, 255, 0.4); transform: translateY(-2px); }
.card:hover::before { opacity: 1; }
.card-green { border-color: rgba(0, 255, 136, 0.2); }
.card-green:hover { border-color: rgba(0, 255, 136, 0.5); }
.card-green::before { background: linear-gradient(90deg, transparent, var(--accent-green), transparent); }
.card-purple { border-color: rgba(179, 71, 255, 0.2); }
.card-purple:hover { border-color: rgba(179, 71, 255, 0.5); }
.card-purple::before { background: linear-gradient(90deg, transparent, var(--accent-purple), transparent); }
.card-orange { border-color: rgba(255, 107, 53, 0.2); }
.card-orange:hover { border-color: rgba(255, 107, 53, 0.5); }
.card-orange::before { background: linear-gradient(90deg, transparent, var(--accent-orange), transparent); }

.eq-box {
    background: rgba(0, 0, 0, 0.55);
    border: 1px solid rgba(0, 212, 255, 0.35);
    border-left: 4px solid var(--accent-blue);
    border-radius: 10px;
    padding: 14px 18px;
    font-family: 'Space Mono', monospace;
    font-size: 1rem;
    color: var(--accent-blue);
    text-align: center;
    margin: 12px 0;
    letter-spacing: 0.05em;
    direction: ltr;
    word-break: break-all;
    overflow-x: auto;
}
.eq-box-green { border-color: rgba(0, 255, 136, 0.35); border-left-color: var(--accent-green); color: var(--accent-green); }
.eq-box-purple { border-color: rgba(179, 71, 255, 0.35); border-left-color: var(--accent-purple); color: var(--accent-purple); }
.eq-box-orange { border-color: rgba(255, 107, 53, 0.35); border-left-color: var(--accent-orange); color: var(--accent-orange); }

.sec-title { font-family: 'Tajawal', sans-serif; font-size: 1.5rem; font-weight: 800; color: var(--accent-blue); margin: 6px 0 4px; direction: rtl; text-align: right; }
.sec-subtitle { color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 20px; direction: rtl; text-align: right; }

.tip-box { background: rgba(0, 212, 255, 0.06); border: 1px solid rgba(0, 212, 255, 0.25); border-radius: 10px; padding: 12px 14px; margin: 8px 0; direction: rtl; text-align: right; color: var(--text-primary); font-size: 0.9rem; }
.tip-box strong { color: var(--accent-blue); }
.success-tip { background: rgba(0, 255, 136, 0.06); border-color: rgba(0, 255, 136, 0.25); }
.success-tip strong { color: var(--accent-green); }
.warning-tip { background: rgba(255, 107, 53, 0.06); border-color: rgba(255, 107, 53, 0.25); }
.warning-tip strong { color: var(--accent-orange); }
.purple-tip { background: rgba(179, 71, 255, 0.06); border-color: rgba(179, 71, 255, 0.25); }
.purple-tip strong { color: var(--accent-purple); }

.stButton > button {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.15), rgba(179, 71, 255, 0.15)) !important;
    color: var(--accent-blue) !important;
    border: 1px solid rgba(0, 212, 255, 0.4) !important;
    border-radius: 10px !important;
    font-family: 'Tajawal', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    padding: 10px 20px !important;
    transition: all 0.3s !important;
    width: 100% !important;
    white-space: normal !important;
    line-height: 1.5 !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.3), rgba(179, 71, 255, 0.3)) !important;
    transform: translateY(-2px) !important;
}

[data-testid="metric-container"] { background: var(--bg-card) !important; border: 1px solid var(--border-color) !important; border-radius: 12px !important; padding: 12px !important; }
[data-testid="metric-container"] [data-testid="stMetricLabel"] { color: var(--text-secondary) !important; font-family: 'Tajawal', sans-serif !important; }
[data-testid="metric-container"] [data-testid="stMetricValue"] { color: var(--accent-blue) !important; font-family: 'Orbitron', sans-serif !important; }

.stTabs [data-baseweb="tab-list"] { background: rgba(6, 8, 30, 0.9) !important; border-radius: 12px !important; padding: 4px !important; gap: 2px !important; overflow-x: auto !important; flex-wrap: nowrap !important; }
.stTabs [data-baseweb="tab"] { color: var(--text-secondary) !important; font-family: 'Tajawal', sans-serif !important; font-size: 0.82rem !important; border-radius: 8px !important; padding: 8px 10px !important; white-space: nowrap !important; flex-shrink: 0 !important; }
.stTabs [aria-selected="true"] { background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)) !important; color: white !important; }

p, li, h1, h2, h3, h4, h5, h6, label { direction: rtl; text-align: right; color: var(--text-primary) !important; }
.stMarkdown { direction: rtl; }
.stSelectbox > label, .stSlider > label, .stRadio > label, .stNumberInput > label { color: var(--text-secondary) !important; font-family: 'Tajawal', sans-serif !important; direction: rtl; text-align: right; }

.styled-table { width: 100%; border-collapse: collapse; font-family: 'Tajawal', sans-serif; direction: rtl; font-size: 0.8rem; }
.styled-table th { background: linear-gradient(135deg, rgba(0, 212, 255, 0.2), rgba(179, 71, 255, 0.2)); color: var(--accent-blue); padding: 8px 6px; text-align: center; font-size: 0.78rem; font-weight: 700; border: 1px solid rgba(0, 212, 255, 0.2); }
.styled-table td { padding: 6px 5px; text-align: center; border: 1px solid rgba(255, 255, 255, 0.06); color: var(--text-primary); font-size: 0.78rem; background: rgba(5, 8, 30, 0.5); }
.td-alpha { color: var(--accent-orange) !important; font-weight: 700 !important; }
.td-beta { color: var(--accent-blue) !important; font-weight: 700 !important; }
.td-gamma { color: var(--accent-purple) !important; font-weight: 700 !important; }

.page-header { background: linear-gradient(135deg, rgba(0, 212, 255, 0.08), rgba(179, 71, 255, 0.08)); border: 1px solid rgba(0, 212, 255, 0.15); border-radius: 14px; padding: 16px 20px; margin-bottom: 20px; display: flex; align-items: center; gap: 12px; direction: rtl; }
.page-icon { font-size: 1.8rem; }
.glow-divider { height: 1px; background: linear-gradient(90deg, transparent, var(--accent-blue), transparent); margin: 22px 0; border: none; }
.ar-text { color: var(--text-primary); font-family: 'Tajawal', sans-serif; font-size: 0.92rem; direction: rtl; text-align: right; line-height: 1.8; }
.highlight-blue { color: var(--accent-blue); font-weight: 700; }
.highlight-green { color: var(--accent-green); font-weight: 700; }
.highlight-purple { color: var(--accent-purple); font-weight: 700; }
.highlight-orange { color: var(--accent-orange); font-weight: 700; }
.highlight-yellow { color: var(--accent-yellow); font-weight: 700; }

/* ★ شريط التنقل العلوي */
.top-nav {
    background: rgba(6, 8, 30, 0.95);
    border: 1px solid rgba(0, 212, 255, 0.2);
    border-radius: 14px;
    padding: 8px;
    margin-bottom: 20px;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}
.top-nav::-webkit-scrollbar { height: 3px; }
.top-nav::-webkit-scrollbar-thumb { background: rgba(0,212,255,0.3); border-radius: 3px; }

.nav-btn {
    display: inline-block;
    padding: 8px 14px;
    margin: 3px;
    border-radius: 10px;
    font-family: 'Tajawal', sans-serif;
    font-size: 0.82rem;
    font-weight: 700;
    cursor: pointer;
    border: 1px solid rgba(0, 212, 255, 0.15);
    background: rgba(0, 212, 255, 0.05);
    color: var(--text-secondary);
    transition: all 0.25s;
    white-space: nowrap;
    -webkit-tap-highlight-color: transparent;
}
.nav-btn:hover, .nav-btn:active {
    background: rgba(0, 212, 255, 0.2);
    color: var(--accent-blue);
    border-color: rgba(0, 212, 255, 0.5);
    transform: translateY(-1px);
}
.nav-btn-active {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.3), rgba(179, 71, 255, 0.3)) !important;
    color: var(--accent-blue) !important;
    border-color: rgba(0, 212, 255, 0.6) !important;
    box-shadow: 0 0 15px rgba(0, 212, 255, 0.2);
}

/* ★ بطاقات التنقل في الصفحة الرئيسية */
.nav-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 18px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s;
    -webkit-tap-highlight-color: transparent;
}
.nav-card:hover, .nav-card:active {
    border-color: rgba(0, 212, 255, 0.5);
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.25);
    transform: translateY(-3px);
}
.nav-card-icon { font-size: 2rem; margin-bottom: 8px; }
.nav-card-title { font-weight: 800; font-size: 0.9rem; color: var(--text-primary); margin-bottom: 4px; }
.nav-card-desc { font-size: 0.75rem; color: var(--text-secondary); line-height: 1.4; }

@media (max-width: 768px) {
    .sec-title { font-size: 1.25rem !important; }
    .eq-box { font-size: 0.82rem !important; padding: 10px 12px !important; }
    .tip-box { font-size: 0.82rem !important; padding: 10px 12px !important; }
    .card { padding: 14px; border-radius: 12px; }
    .page-header { padding: 12px 14px; flex-wrap: wrap; }
    .styled-table { font-size: 0.7rem; }
    .nav-btn { padding: 7px 10px; font-size: 0.75rem; }
    .nav-card { padding: 14px; }
    .nav-card-icon { font-size: 1.6rem; }
    .nav-card-title { font-size: 0.82rem; }
}
@media (max-width: 480px) {
    .sec-title { font-size: 1.1rem !important; }
    .eq-box { font-size: 0.75rem !important; }
    .tip-box { font-size: 0.78rem !important; }
    .card { padding: 12px; }
    .nav-btn { padding: 6px 8px; font-size: 0.72rem; margin: 2px; }
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════════
defaults = {
    "coin_count": 50,
    "coin_history": [(0, 50)],
    "attempt_num": 0,
    "quiz_answers": {},
    "quiz_submitted": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ═══════════════════════════════════════════
# ★ التنقل العلوي (بدلاً من الشريط الجانبي)
# ═══════════════════════════════════════════
PAGES = [
    ("🏠", "الصفحة الرئيسية", "home"),
    ("👨‍🔬", "العلماء", "scientists"),
    ("⚛️", "أنواع الإشعاعات", "types"),
    ("🔄", "أنواع الاضمحلال", "decay"),
    ("🎲", "نمذجة الاضمحلال", "modeling"),
    ("⏱️", "عمر النصف", "halflife"),
    ("🔗", "سلاسل الاضمحلال", "series"),
    ("🔬", "التكنولوجيا", "tech"),
    ("📝", "مراجعة الدرس", "review"),
]

# إنشاء أزرار التنقل
nav_html = '<div class="top-nav">'
for icon, label, key in PAGES:
    is_active = st.session_state.get("current_page", "home") == key
    cls = "nav-btn nav-btn-active" if is_active else "nav-btn"
    nav_html += f'<a href="?page={key}" class="{cls}" onclick="event.preventDefault(); window.location.href=\'?page={key}\';">{icon} {label}</a>'
nav_html += '</div>'
st.markdown(nav_html, unsafe_allow_html=True)

# قراءة الصفحة الحالية من URL parameters
query_params = st.query_params
current_page = query_params.get("page", "home")

# حفظ في session state
st.session_state["current_page"] = current_page

# ═══════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════
def page_header(icon, title_ar, subtitle_ar=""):
    st.markdown(f"""
    <div class="page-header">
        <span class="page-icon">{icon}</span>
        <div>
            <div class="sec-title">{title_ar}</div>
            {f'<div class="sec-subtitle">{subtitle_ar}</div>' if subtitle_ar else ''}
        </div>
    </div>
    """, unsafe_allow_html=True)

def section_label(text, color="blue"):
    c = {"blue": "var(--accent-blue)", "green": "var(--accent-green)", "purple": "var(--accent-purple)", "orange": "var(--accent-orange)", "yellow": "var(--accent-yellow)"}.get(color, "var(--accent-blue)")
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:8px;margin:20px 0 10px;direction:rtl;">
        <div style="flex:1;height:1px;background:linear-gradient(90deg,{c}20,transparent);"></div>
        <div style="color:{c};font-family:'Tajawal',sans-serif;font-weight:700;font-size:1rem;white-space:nowrap;">{text}</div>
        <div style="width:7px;height:7px;border-radius:50%;background:{c};box-shadow:0 0 10px {c};flex-shrink:0;"></div>
    </div>
    """, unsafe_allow_html=True)

def tip(text, kind="blue"):
    cls = {"blue": "tip-box", "green": "tip-box success-tip", "orange": "tip-box warning-tip", "purple": "tip-box purple-tip"}.get(kind, "tip-box")
    st.markdown(f'<div class="{cls}">{text}</div>', unsafe_allow_html=True)

def eq(text, kind="blue"):
    cls = {"blue": "eq-box", "green": "eq-box eq-box-green", "purple": "eq-box eq-box-purple", "orange": "eq-box eq-box-orange"}.get(kind, "eq-box")
    st.markdown(f'<div class="{cls}">{text}</div>', unsafe_allow_html=True)

def glow_div():
    st.markdown('<hr class="glow-divider">', unsafe_allow_html=True)

# ═══════════════════════════════════════════
# PAGE 1: HOME
# ═══════════════════════════════════════════
def show_home():
    # شعار وعنوان
    st.markdown("""
    <div style="text-align:center;padding:16px 8px 20px;">
        <div style="font-size:3rem;margin-bottom:6px;">⚛️</div>
        <div style="font-family:'Orbitron',sans-serif;font-size:0.7rem;letter-spacing:3px;color:rgba(0,212,255,0.7);margin-bottom:4px;">NUCLEAR RADIATION</div>
        <div style="font-family:'Tajawal',sans-serif;font-size:2rem;font-weight:800;color:#00d4ff;text-shadow:0 0 25px rgba(0,212,255,0.5);">الإشعاع النووي</div>
        <div style="font-size:0.8rem;color:#556;margin-top:4px;">الدرس الثاني — الاضمحلال الإشعاعي</div>
        <div style="font-size:0.72rem;color:#334;margin-top:8px;">إعداد: Israa Youssuf Samara ✦ الفيزياء — الصف الثاني عشر</div>
    </div>
    """, unsafe_allow_html=True)

    # رسوم الذرة المتحركة
    components.html("""
    <!DOCTYPE html><html><head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Tajawal:wght@700;800&display=swap');
    *{margin:0;padding:0;box-sizing:border-box;}
    body{background:transparent;overflow:hidden;}
    .scene{width:100%;height:200px;position:relative;display:flex;align-items:center;justify-content:center;}
    canvas#bg{position:absolute;top:0;left:0;width:100%;height:100%;}
    .atom{position:relative;width:120px;height:120px;}
    .nucleus{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:30px;height:30px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff9a5c,#ff3d00 60%,#cc2000);box-shadow:0 0 0 4px rgba(255,80,0,0.15),0 0 25px rgba(255,80,0,0.6);animation:pulse-nuc 2.5s ease-in-out infinite;z-index:5;}
    .orbit{position:absolute;top:50%;left:50%;border-radius:50%;border:1.5px solid rgba(0,212,255,0.3);}
    .o1{width:50px;height:50px;margin:-25px 0 0 -25px;animation:spin 3.2s linear infinite;}
    .o2{width:80px;height:80px;margin:-40px 0 0 -40px;animation:spin 5s linear infinite reverse;border-style:dashed;}
    .o3{width:115px;height:115px;margin:-57px 0 0 -57px;animation:spin 7s linear infinite;transform:rotateX(70deg);}
    .electron{position:absolute;width:7px;height:7px;border-radius:50%;top:-3px;left:calc(50% - 3px);}
    .e-blue{background:#00d4ff;box-shadow:0 0 8px rgba(0,212,255,0.9);}
    .e-green{background:#00ff88;box-shadow:0 0 8px rgba(0,255,136,0.9);}
    .e-purple{background:#b347ff;box-shadow:0 0 8px rgba(179,71,255,0.9);}
    @keyframes spin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
    @keyframes pulse-nuc{0%,100%{box-shadow:0 0 0 4px rgba(255,80,0,0.15),0 0 25px rgba(255,80,0,0.6)}50%{box-shadow:0 0 0 7px rgba(255,80,0,0.2),0 0 40px rgba(255,80,0,0.9);transform:translate(-50%,-50%) scale(1.1)}}
    .badges{display:flex;gap:6px;flex-wrap:wrap;justify-content:center;margin-top:8px;}
    .badge{padding:3px 8px;border-radius:20px;font-size:0.65rem;font-family:'Orbitron',sans-serif;font-weight:700;}
    .b-alpha{background:rgba(255,107,53,0.2);color:#ff6b35;border:1px solid rgba(255,107,53,0.5);}
    .b-beta{background:rgba(0,212,255,0.2);color:#00d4ff;border:1px solid rgba(0,212,255,0.5);}
    .b-gamma{background:rgba(179,71,255,0.2);color:#b347ff;border:1px solid rgba(179,71,255,0.5);}
    </style></head><body>
    <div class="scene">
        <canvas id="bg"></canvas>
        <div class="atom"><div class="nucleus"></div><div class="orbit o1"><div class="electron e-blue"></div></div><div class="orbit o2"><div class="electron e-green"></div></div><div class="orbit o3"><div class="electron e-purple"></div></div></div>
        <div class="badges"><span class="badge b-alpha">α Alpha</span><span class="badge b-beta">β Beta</span><span class="badge b-gamma">γ Gamma</span></div>
    </div>
    <script>
    var cv=document.getElementById('bg'),cx=cv.getContext('2d');
    function rs(){cv.width=cv.parentElement.offsetWidth;cv.height=cv.parentElement.offsetHeight;}
    rs();window.addEventListener('resize',rs);
    var ps=[];for(var i=0;i<25;i++)ps.push({x:Math.random()*cv.width,y:Math.random()*cv.height,r:Math.random()*1.2+0.3,vx:(Math.random()-0.5)*0.3,vy:(Math.random()-0.5)*0.3,a:Math.random()*0.4+0.1,c:['#00d4ff','#b347ff','#00ff88','#ff6b35'][Math.floor(Math.random()*4)]});
    function an(){cx.clearRect(0,0,cv.width,cv.height);for(var i=0;i<ps.length;i++){var p=ps[i];p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>cv.width)p.vx*=-1;if(p.y<0||p.y>cv.height)p.vy*=-1;cx.beginPath();cx.arc(p.x,p.y,p.r,0,Math.PI*2);cx.fillStyle=p.c+Math.floor(p.a*255).toString(16).padStart(2,'0');cx.fill();}requestAnimationFrame(an);}
    an();
    </script></body></html>
    """, height=220)

    # بطاقات التنقل الرئيسية
    section_label("تصفح أقسام الدرس", "blue")
    nav_cards = [
        ("👨‍🔬", "العلماء والاكتشافات", "بيكريل، كوري، رذرفورد، فيلار", "scientists"),
        ("⚛️", "أنواع الإشعاعات", "مقارنة ألفا وبيتا وغاما + محاكاة النفاذ", "types"),
        ("🔄", "أنواع الاضمحلال", "ألفا، β⁻، β⁺، غاما + معادلات", "decay"),
        ("🎲", "نمذجة الاضمحلال", "تجربة العملات المعدنية", "modeling"),
        ("⏱️", "عمر النصف والنشاطية", "العلاقات الرياضية + مسائل", "halflife"),
        ("🔗", "سلاسل الاضمحلال", "U-238, Th-232, Ac-235", "series"),
        ("🔬", "الربط بالتكنولوجيا", "تطبيقات حقيقية في الطب والصناعة", "tech"),
        ("📝", "مراجعة الدرس", "أسئلة MCQ + مسائل", "review"),
    ]
    for row_start in range(0, len(nav_cards), 2):
        cols = st.columns(2)
        for j in range(2):
            idx = row_start + j
            if idx < len(nav_cards):
                icon, title, desc, key = nav_cards[idx]
                with cols[j]:
                    st.markdown(f"""
                    <a href="?page={key}" style="text-decoration:none;" onclick="event.preventDefault(); window.location.href='?page={key}';">
                        <div class="nav-card">
                            <div class="nav-card-icon">{icon}</div>
                            <div class="nav-card-title">{title}</div>
                            <div class="nav-card-desc">{desc}</div>
                        </div>
                    </a>
                    """, unsafe_allow_html=True)

    glow_div()
    section_label("الفكرة الرئيسية", "blue")
    tip("""<strong>تبعث النوى غير المستقرة إشعاعات بطاقات مختلفة.</strong>
    <br>اكتشف <strong>بيكريل</strong> 1896 أن أملاح اليورانيوم تبعث إشعاعاً تلقائياً.
    اكتشفت <strong>كوري</strong> البولونيوم والراديوم.
    ميّز <strong>رذرفورد</strong> ألفا وبيتا. واكتشف <strong>فيلار</strong> غاما.""")
    section_label("نواتج التعلم", "green")
    for it in ["المقارنة بين ألفا وبيتا وغاما", "وصف التغيرات النووية", "تحليل رسوم تناقص النوى", "توضيح النشاطية وعمر النصف", "تحليل سلاسل الاضمحلال"]:
        st.markdown(f'<div style="display:flex;align-items:center;gap:8px;margin:5px 0;direction:rtl;"><div style="color:var(--accent-green);font-size:0.85rem;">✦</div><div style="color:var(--text-primary);font-size:0.88rem;">{it}</div></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════
# PAGE 2: SCIENTISTS
# ═══════════════════════════════════════════
def show_scientists():
    page_header("👨‍🔬", "العلماء والاكتشافات", "رحلة اكتشاف الإشعاع النووي")
    components.html("""
    <!DOCTYPE html><html><head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;800&family=Orbitron:wght@700&display=swap');
    *{margin:0;padding:0;box-sizing:border-box;}
    body{background:transparent;font-family:'Tajawal',sans-serif;padding:4px;}
    .tl{position:relative;max-width:100%;margin:0 auto;padding:8px 0;}
    .tl::before{content:'';position:absolute;right:18px;top:0;bottom:0;width:2px;background:linear-gradient(180deg,transparent,#00d4ff,#b347ff,transparent);}
    .ev{display:flex;align-items:flex-start;margin:14px 0;position:relative;direction:rtl;}
    .dot{position:absolute;right:12px;top:18px;width:14px;height:14px;border-radius:50%;background:#00d4ff;box-shadow:0 0 12px #00d4ff;z-index:2;}
    .cd{width:calc(100% - 42px);margin-right:36px;background:rgba(8,12,45,0.9);border:1px solid rgba(0,212,255,0.25);border-radius:12px;padding:14px;transition:all 0.3s;}
    .cd:hover{border-color:rgba(0,212,255,0.6);box-shadow:0 0 15px rgba(0,212,255,0.25);}
    .yr{font-family:'Orbitron',sans-serif;font-size:0.8rem;font-weight:700;color:#00d4ff;margin-bottom:4px;}
    .nm{font-size:0.9rem;font-weight:800;color:#e4e8f5;margin-bottom:4px;}
    .ds{font-size:0.78rem;color:rgba(180,190,220,0.85);line-height:1.6;direction:rtl;text-align:right;}
    .av{font-size:1.5rem;margin-bottom:4px;display:block;}
    @media(min-width:700px){.tl::before{left:50%;right:auto;transform:translateX(-50%);}.ev .cd{width:calc(50% - 42px);margin-right:calc(50% + 18px);}.ev:nth-child(even) .cd{margin-right:0;margin-left:calc(50% + 18px);}.ev:nth-child(even){justify-content:flex-end;}.dot{right:auto;left:50%;transform:translateX(-50%);}}
    </style></head><body>
    <div class="tl">
        <div class="ev"><div class="dot"></div><div class="cd"><span class="av">🧑‍🔬</span><div class="yr">1896</div><div class="nm">هنري بيكريل</div><div class="ds">اكتشف أن أملاح اليورانيوم تؤثر في الألواح الفوتوغرافية دون تحفيز — أول اكتشاف للنشاط الإشعاعي.</div></div></div>
        <div class="ev"><div class="dot" style="background:#b347ff;box-shadow:0 0 12px #b347ff;"></div><div class="cd" style="border-color:rgba(179,71,255,0.25);"><span class="av">👩‍🔬</span><div class="yr" style="color:#b347ff;">1898</div><div class="nm">ماري وبيير كوري</div><div class="ds">اكتشفا <strong style="color:#b347ff;">البولونيوم</strong> و<strong style="color:#b347ff;">الراديوم</strong>، وابتكرت ماري مصطلح "النشاط الإشعاعي".</div></div></div>
        <div class="ev"><div class="dot" style="background:#00ff88;box-shadow:0 0 12px #00ff88;"></div><div class="cd" style="border-color:rgba(0,255,136,0.25);"><span class="av">⚗️</span><div class="yr" style="color:#00ff88;">1899</div><div class="nm">إرنست رذرفورد</div><div class="ds">ميّز بين <strong style="color:#ff6b35;">ألفا (α)</strong> و<strong style="color:#00d4ff;">بيتا (β)</strong> حسب قدرتهما على النفاذ.</div></div></div>
        <div class="ev"><div class="dot" style="background:#ffd700;box-shadow:0 0 12px #ffd700;"></div><div class="cd" style="border-color:rgba(255,215,0,0.25);"><span class="av">💡</span><div class="yr" style="color:#ffd700;">1900</div><div class="nm">بول فيلار</div><div class="ds">اكتشف <strong style="color:#b347ff;">أشعة غاما (γ)</strong> الكهرمغناطيسية عالية النفاذ.</div></div></div>
        <div class="ev"><div class="dot" style="background:#ff6b35;box-shadow:0 0 12px #ff6b35;"></div><div class="cd" style="border-color:rgba(255,107,53,0.25);"><span class="av">🔬</span><div class="yr" style="color:#ff6b35;">1911</div><div class="nm">النموذج النووي</div><div class="ds">أثبت رذرفورد عبر تجربة تشتت ألفا وجود نواة موجبة صغيرة مركزية.</div></div></div>
    </div></body></html>
    """, height=520)
    glow_div()
    for col,(ic,tt,ds,cl,clr) in zip(st.columns(3),[("🔴","α ALPHA","نوى الهيليوم","card card-orange","--accent-orange"),("🔵","β BETA","إلكترون/بوزيترون","card","--accent-blue"),("🟣","γ GAMMA","فوتونات EM","card card-purple","--accent-purple")]):
        with col:
            st.markdown(f'<div class="{cl}" style="text-align:center;"><div style="font-size:2rem;">{ic}</div><div style="color:var({clr});font-family:\'Orbitron\',sans-serif;font-size:0.9rem;font-weight:700;margin:6px 0;">{tt}</div><div style="color:var(--text-secondary);font-size:0.8rem;">{ds}</div></div>',unsafe_allow_html=True)

# ═══════════════════════════════════════════
# PAGE 3: RADIATION TYPES
# ═══════════════════════════════════════════
def show_radiation_types():
    page_header("⚛️","أنواع الإشعاعات ومقارنتها","قدرة النفاذ والتأيين")
    section_label("محاكاة النفاذ عبر المواد — اضغط الأزرار!","orange")
    components.html("""
    <!DOCTYPE html><html><head><style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    *{margin:0;padding:0;box-sizing:border-box;}body{background:transparent;}
    .controls{display:flex;gap:8px;justify-content:center;padding:10px 4px;flex-wrap:wrap;}
    .btn{padding:10px 18px;border-radius:8px;cursor:pointer;font-family:'Tajawal',sans-serif;font-size:0.9rem;font-weight:700;border:none;min-width:90px;-webkit-tap-highlight-color:transparent;}
    .btn:active{filter:brightness(1.5);}
    .ba{background:rgba(255,107,53,0.3);color:#ff6b35;border:2px solid #ff6b35;}
    .bb{background:rgba(0,212,255,0.3);color:#00d4ff;border:2px solid #00d4ff;}
    .bg2{background:rgba(179,71,255,0.3);color:#b347ff;border:2px solid #b347ff;}
    .ball{background:rgba(255,215,0,0.2);color:#ffd700;border:2px solid #ffd700;}
    .cw{width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;}
    canvas{display:block;max-width:100%;height:auto;border-radius:10px;}
    </style></head><body>
    <div class="controls">
        <button class="btn ba" onclick="fire('alpha')">🔴 ألفا</button>
        <button class="btn bb" onclick="fire('beta')">🔵 بيتا</button>
        <button class="btn bg2" onclick="fire('gamma')">🟣 غاما</button>
        <button class="btn ball" onclick="fireAll()">⚡ الكل</button>
    </div>
    <div class="cw"><canvas id="c" width="780" height="240"></canvas></div>
    <script>
    var c=document.getElementById('c'),ctx=c.getContext('2d'),W=780,H=240,SX=55;
    var BS=[{x:200,w:16,label:'ورق',lc:'#c9a878',bc:'rgba(139,119,95,0.8)'},{x:360,w:30,label:'ألمنيوم',lc:'#8ab4c8',bc:'rgba(140,180,200,0.7)'},{x:540,w:60,label:'رصاص',lc:'#7080a0',bc:'rgba(80,90,110,0.85)'}];
    var MX={alpha:BS[0].x-2,beta:BS[1].x-2,gamma:W+10};
    var parts=[],anim=null;
    function draw(){ctx.clearRect(0,0,W,H);var bg=ctx.createLinearGradient(0,0,W,0);bg.addColorStop(0,'rgba(2,2,18,0.95)');bg.addColorStop(1,'rgba(5,5,25,0.95)');ctx.fillStyle=bg;ctx.fillRect(0,0,W,H);ctx.strokeStyle='rgba(0,212,255,0.04)';ctx.lineWidth=1;for(var x=0;x<W;x+=40){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke();}for(var y=0;y<H;y+=40){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
    var cy=H/2;ctx.fillStyle='rgba(255,80,0,0.12)';ctx.beginPath();ctx.arc(SX,cy,24,0,Math.PI*2);ctx.fill();ctx.strokeStyle='rgba(255,80,0,0.4)';ctx.lineWidth=2;ctx.beginPath();ctx.arc(SX,cy,24,0,Math.PI*2);ctx.stroke();ctx.fillStyle='#ff6b35';ctx.beginPath();ctx.arc(SX,cy,14,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff8';ctx.font='bold 9px Orbitron';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('☢',SX,cy);ctx.fillStyle='rgba(200,200,220,0.5)';ctx.font='9px Tajawal';ctx.fillText('مصدر مشع',SX,cy+34);
    for(var i=0;i<BS.length;i++){var b=BS[i];ctx.fillStyle=b.bc;ctx.fillRect(b.x,16,b.w,H-32);ctx.strokeStyle=b.lc+'cc';ctx.lineWidth=1.5;ctx.strokeRect(b.x,16,b.w,H-32);ctx.fillStyle=b.lc;ctx.font='bold 8px Tajawal';ctx.textAlign='center';ctx.fillText(b.label,b.x+b.w/2,H-4);}
    var dx=BS[2].x+BS[2].w+8;ctx.fillStyle='rgba(0,255,136,0.03)';ctx.fillRect(dx,20,W-dx-8,H-40);ctx.strokeStyle='rgba(0,255,136,0.15)';ctx.lineWidth=1;ctx.setLineDash([3,3]);ctx.strokeRect(dx,20,W-dx-8,H-40);ctx.setLineDash([]);ctx.fillStyle='rgba(0,255,136,0.5)';ctx.font='8px Tajawal';ctx.fillText('كاشف',dx+(W-dx-8)/2,cy);
    for(var i=0;i<parts.length;i++){var p=parts[i];ctx.save();ctx.globalAlpha=p.alpha;if(p.trail.length>1){ctx.beginPath();ctx.moveTo(p.trail[0].x,p.trail[0].y);for(var j=1;j<p.trail.length;j++)ctx.lineTo(p.trail[j].x,p.trail[j].y);ctx.strokeStyle=p.color+'44';ctx.lineWidth=2;ctx.stroke();}var gr=ctx.createRadialGradient(p.x,p.y,0,p.x,p.y,p.r*2);gr.addColorStop(0,'#fff');gr.addColorStop(0.3,p.color);gr.addColorStop(1,p.color+'00');ctx.fillStyle=gr;ctx.beginPath();ctx.arc(p.x,p.y,p.r*2,0,Math.PI*2);ctx.fill();ctx.fillStyle=p.color;ctx.shadowColor=p.color;ctx.shadowBlur=10;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fill();ctx.restore();if(p.stopped&&p.sl){ctx.fillStyle=p.color;ctx.font='bold 8px Tajawal';ctx.textAlign='center';ctx.fillText(p.sl,p.x,p.y-14);}}}
    function spawn(type){var cfg={alpha:{color:'#ff6b35',r:6,speed:3,sl:'توقف!',mx:MX.alpha},beta:{color:'#00d4ff',r:4,speed:4,sl:'توقف!',mx:MX.beta},gamma:{color:'#b347ff',r:3,speed:5,sl:null,mx:MX.gamma}};var cc=cfg[type];parts.push({x:SX+18,y:H/2+(Math.random()-0.5)*6,vx:cc.speed,vy:(Math.random()-0.5)*0.8,r:cc.r,color:cc.color,alpha:1,mx:cc.mx,stopped:false,sl:cc.sl,trail:[]});}
    function fire(type){spawn(type);if(!anim)loop();}
    function fireAll(){spawn('alpha');spawn('beta');spawn('gamma');if(!anim)loop();}
    function loop(){for(var i=0;i<parts.length;i++){var p=parts[i];if(p.stopped){p.alpha=Math.max(0,p.alpha-0.01);continue;}p.trail.push({x:p.x,y:p.y});if(p.trail.length>18)p.trail.shift();p.x+=p.vx;p.y+=p.vy;if(p.x>=p.mx){p.stopped=true;p.x=p.mx;}}var np=[];for(var i=0;i<parts.length;i++)if(parts[i].alpha>0)np.push(parts[i]);parts=np;draw();if(parts.length>0)anim=requestAnimationFrame(loop);else{anim=null;draw();}}
    draw();
    </script></body></html>
    """,height=310)
    glow_div()
    section_label("جدول مقارنة","purple")
    st.markdown("""<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;"><table class="styled-table"><thead><tr><th>الخاصية</th><th class="td-alpha">ألفا α</th><th class="td-beta">بيتا β</th><th class="td-gamma">غاما γ</th></tr></thead><tbody><tr><td><strong>الطبيعة</strong></td><td class="td-alpha">نوى هيليوم</td><td class="td-beta">إلكترون</td><td class="td-gamma">فوتونات EM</td></tr><tr><td><strong>الشحنة</strong></td><td class="td-alpha">+2e</td><td class="td-beta">±e</td><td class="td-gamma">صفر</td></tr><tr><td><strong>التأيين</strong></td><td class="td-alpha">كبيرة جداً</td><td class="td-beta">متوسطة</td><td class="td-gamma">ضعيفة</td></tr><tr><td><strong>النفاذ</strong></td><td class="td-alpha">ضعيفة (ورق)</td><td class="td-beta">متوسطة (Al)</td><td class="td-gamma">كبيرة (Pb)</td></tr><tr><td><strong>المغناطيسي</strong></td><td class="td-alpha">ينحرف (+)</td><td class="td-beta">ينحرف (±)</td><td class="td-gamma">لا ينحرف</td></tr></tbody></table></div>""",unsafe_allow_html=True)
    glow_div()
    section_label("طاقة الإشعاع مقابل المسافة","green")
    x=np.linspace(0,10,300)
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=x,y=100*np.exp(-x/0.6),name='α',line=dict(color='#ff6b35',width=3),fill='tozeroy',fillcolor='rgba(255,107,53,0.08)'))
    fig.add_trace(go.Scatter(x=x,y=80*np.exp(-x/2.5),name='β',line=dict(color='#00d4ff',width=3),fill='tozeroy',fillcolor='rgba(0,212,255,0.08)'))
    fig.add_trace(go.Scatter(x=x,y=60*np.exp(-x/8),name='γ',line=dict(color='#b347ff',width=3),fill='tozeroy',fillcolor='rgba(179,71,255,0.08)'))
    fig.update_layout(template="plotly_dark",height=280,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font=dict(family="Tajawal",color="#e4e8f5",size=11),xaxis=dict(title="المسافة",gridcolor='rgba(255,255,255,0.04)',color='#7880a0'),yaxis=dict(title="الطاقة %",gridcolor='rgba(255,255,255,0.04)',color='#7880a0'),legend=dict(bgcolor='rgba(0,0,0,0.4)',font=dict(size=11)),margin=dict(l=10,r=10,t=10,b=10))
    st.plotly_chart(fig,use_container_width=True)

# ═══════════════════════════════════════════
# PAGE 4: DECAY TYPES
# ═══════════════════════════════════════════
def show_decay_types():
    page_header("🔄","أنواع الاضمحلال الإشعاعي","ألفا · بيتا · غاما")
    tabs=st.tabs(["🔴 ألفا","🔵 بيتا","🟣 غاما","📊 ملخص"])
    with tabs[0]:
        section_label("اضمحلال ألفا","orange")
        st.markdown('<div class="ar-text">تنبعث من <strong class="highlight-orange">النوى الثقيلة (Z>82)</strong>. تخسر 2 بروتون + 2 نيوترون:</div>',unsafe_allow_html=True)
        eq("ᴬ_Z X → ᴬ⁻⁴_(Z-2) Y + ⁴₂He","orange")
        eq("²³⁸₉₂U → ²³⁴₉₀Th + ⁴₂He","orange")
        tip("<strong>Z يقل 2 | A يقل 4</strong>","orange")
        tip("<strong>تطبيق:</strong> أجهزة إنذار الحريق — أمريسيوم-241 يطلق ألفا يُأيّن الهواء. الدخان يمتص الألفا → ينقطع التيار → الإنذار!","orange")
        components.html("""<!DOCTYPE html><html><head><style>*{margin:0;padding:0;box-sizing:border-box;}body{background:transparent;display:flex;align-items:center;justify-content:center;}canvas{display:block;max-width:100%;height:auto;border-radius:10px;}</style></head><body><canvas id="c" width="280" height="280"></canvas><script>var c=document.getElementById('c'),ctx=c.getContext('2d'),t=0,phase=0,ax=0;function dn(x,y,l,g){ctx.save();if(g){ctx.shadowColor='rgba(255,107,53,0.7)';ctx.shadowBlur=20;}var gr=ctx.createRadialGradient(x-8,y-8,2,x,y,30);gr.addColorStop(0,'#ff9a5c');gr.addColorStop(0.6,'#cc2000');gr.addColorStop(1,'#7a0000');ctx.fillStyle=gr;ctx.beginPath();ctx.arc(x,y,30,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;ctx.fillStyle='#fff';ctx.font='bold 10px monospace';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(l,x,y);ctx.restore();}function da(x,y){ctx.save();ctx.shadowColor='#ff6b35';ctx.shadowBlur=15;var gr=ctx.createRadialGradient(x,y,0,x,y,12);gr.addColorStop(0,'#fff');gr.addColorStop(0.3,'#ff6b35');gr.addColorStop(1,'rgba(255,107,53,0)');ctx.fillStyle=gr;ctx.beginPath();ctx.arc(x,y,12,0,Math.PI*2);ctx.fill();ctx.fillStyle='#ff6b35';ctx.beginPath();ctx.arc(x,y,7,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff';ctx.font='bold 8px monospace';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('α',x,y);ctx.restore();}function draw(){ctx.clearRect(0,0,280,280);ctx.fillStyle='rgba(2,2,18,0.95)';ctx.fillRect(0,0,280,280);ctx.fillStyle='rgba(255,107,53,0.8)';ctx.font='bold 11px Tajawal,sans-serif';ctx.textAlign='center';ctx.fillText('اضمحلال ألفا',140,18);if(phase===0){dn(140,130,'²³⁸U',true);var r=Math.sin(t*0.05)*6+40;ctx.strokeStyle='rgba(255,107,53,'+(0.25-r*0.003)+')';ctx.lineWidth=1.5;ctx.setLineDash([4,4]);ctx.beginPath();ctx.arc(140,130,r,0,Math.PI*2);ctx.stroke();ctx.setLineDash([]);}else if(phase===1){var p=Math.min(ax/160,1);dn(140,155,'²³⁴Th',false);da(140+p*110,130-p*50);if(p>=1)phase=2;}else{ctx.fillStyle='rgba(0,255,136,0.6)';ctx.font='9px Tajawal,sans-serif';ctx.textAlign='center';ctx.fillText('²³⁴Th',85,45);ctx.fillText('α',210,45);dn(90,130,'²³⁴Th',false);da(210,110);ctx.fillStyle='rgba(0,255,136,0.8)';ctx.font='bold 10px Tajawal,sans-serif';ctx.fillText('Z: 92→90  A: 238→234',140,245);}t++;if(phase===0&&t===100){phase=1;ax=0;}if(phase===1)ax+=3.5;if(phase===2&&t===230){t=0;phase=0;ax=0;}requestAnimationFrame(draw);}draw();</script></body></html>""",height=290)
    with tabs[1]:
        section_label("بيتا السالبة β⁻","blue")
        st.markdown('<div class="ar-text">نوى ذات <strong class="highlight-blue">فائض نيوترونات</strong>:</div>',unsafe_allow_html=True)
        eq("¹₀n → ¹₁p + ⁰₋₁e + v̄","blue");eq("ᴬ_Z X → ᴬ_(Z+1) Y + ⁰₋₁e","blue");eq("¹⁴₆C → ¹⁴₇N + ⁰₋₁e","blue")
        tip("<strong>Z+1 | A ثابت</strong> — تطبيق: التأريخ بالكربون-14","blue")
        glow_div();section_label("بيتا الموجبة β⁺","green")
        eq("¹₁p → ¹₀n + ⁰₊₁e + ν","green");eq("ᴬ_Z X → ᴬ_(Z-1) Y + ⁰₊₁e","green")
        tip("<strong>Z-1 | A ثابت</strong> — تطبيق: PET Scan بالفلور-18","green")
        glow_div();section_label("ابنِ معادلة بيتا!","blue")
        c1,c2=st.columns(2)
        with c1:pZ=st.number_input("Z",1,100,6,key="bz");pA=st.number_input("A",1,250,14,key="ba")
        with c2:bt=st.radio("النوع",["β⁻ سالبة","β⁺ موجبة"],key="btype")
        dZ=+1 if "β⁻" in bt else -1;eq(f"ᴬ_Z X → {pA}_{pZ+dZ} Y + {('⁰₋₁e' if dZ==1 else '⁰₊₁e')}","blue" if dZ==1 else "green")
    with tabs[2]:
        section_label("اضمحلال غاما γ","purple")
        st.markdown('<div class="ar-text">النواة في <strong class="highlight-purple">حالة إثارة*</strong> تطلق فوتونات.<br><strong class="highlight-yellow">لا يتغير Z ولا A!</strong></div>',unsafe_allow_html=True)
        eq("ᴬ_Z X* → ᴬ_Z X + γ","purple")
        tip("تطبيق: فحص عيوب اللحام الصناعي","purple")
        fig=go.Figure();fig.add_shape(type="line",x0=0.2,x1=0.8,y0=4.4,y1=4.4,line=dict(color="#ff6b35",width=3,dash="dot"));fig.add_annotation(x=0.85,y=4.4,text="¹²₆C* (إثارة)\n4.4 MeV",showarrow=False,font=dict(color="#ff6b35",size=10,family="Tajawal"),xanchor="left");fig.add_shape(type="line",x0=0.2,x1=0.8,y0=0,y1=0,line=dict(color="#00ff88",width=3));fig.add_annotation(x=0.85,y=0,text="¹²₆C (استقرار)\n0 MeV",showarrow=False,font=dict(color="#00ff88",size=10,family="Tajawal"),xanchor="left");fig.add_annotation(x=0.5,y=2.2,ax=0.5,ay=4.2,arrowcolor="#b347ff",arrowwidth=3,arrowhead=2,text="");fig.add_annotation(x=0.5,y=2.2,text="γ=4.4 MeV",showarrow=False,font=dict(color="#b347ff",size=12,family="Orbitron"));fig.update_layout(template="plotly_dark",height=280,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',showlegend=False,xaxis=dict(showgrid=False,showticklabels=False,range=[0,1.4]),yaxis=dict(title="الطاقة (MeV)",range=[-0.8,5.2],gridcolor='rgba(255,255,255,0.04)',color='#7880a0'),font=dict(family="Tajawal",size=11),margin=dict(l=10,r=10,t=25,b=10),title=dict(text="مستويات طاقة ¹²₆C",font=dict(color="#b347ff",size=12)));st.plotly_chart(fig,use_container_width=True)
    with tabs[3]:
        section_label("ملخص","blue")
        st.markdown("""<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;"><table class="styled-table"><thead><tr><th>النوع</th><th>الجسيم</th><th>ΔZ</th><th>ΔA</th></tr></thead><tbody><tr><td class="td-alpha">ألفا</td><td class="td-alpha">⁴₂He</td><td class="td-alpha">−2</td><td class="td-alpha">−4</td></tr><tr><td class="td-beta">β⁻</td><td class="td-beta">⁰₋₁e</td><td class="td-beta">+1</td><td class="td-beta">0</td></tr><tr><td class="td-beta">β⁺</td><td class="td-beta">⁰₊₁e</td><td class="td-beta">−1</td><td class="td-beta">0</td></tr><tr><td class="td-gamma">غاما</td><td class="td-gamma">γ</td><td class="td-gamma">0</td><td class="td-gamma">0</td></tr></tbody></table></div>""",unsafe_allow_html=True)

# ═══════════════════════════════════════════
# PAGE 5: MODELING
# ═══════════════════════════════════════════
def show_modeling():
    page_header("🎲", "نمذجة الاضمحلال بالعملات", "التجربة 1")
    section_label("الفكرة", "blue")
    tip("<strong>كل عملة = نواة مشعة.</strong> الصورة = لم تضمحل | الكتابة = اضمحلت. احتمال الاضمحلال = ½ ← عمر نصف واحد!", "blue")

    col1, col2 = st.columns([1, 1])

    with col1:
        ic = st.slider("عدد العملات N₀", 10, 200, 50, key="init_coins")
        dp = st.slider("احتمال الاضمحلال", 0.3, 0.7, 0.5, 0.05, key="prob")

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🎲 إلقاء", key="one_throw"):
                if st.session_state.attempt_num == 0:
                    st.session_state.coin_count = ic
                    st.session_state.coin_history = [(0, ic)]
                rem = sum(1 for _ in range(st.session_state.coin_count) if random.random() > dp)
                st.session_state.attempt_num += 1
                st.session_state.coin_count = rem
                st.session_state.coin_history.append((st.session_state.attempt_num, rem))

        with c2:
            if st.button("🔄 إعادة", key="reset_throw"):
                st.session_state.coin_count = ic
                st.session_state.coin_history = [(0, ic)]
                st.session_state.attempt_num = 0

        if st.button("⚡ تلقائي كامل", key="auto_run"):
            cnt = ic
            hist = [(0, cnt)]
            for i in range(1, 12):
                cnt = sum(1 for _ in range(cnt) if random.random() > dp)
                hist.append((i, cnt))
                if cnt < 2:
                    break
            st.session_state.coin_history = hist
            st.session_state.coin_count = cnt
            st.session_state.attempt_num = len(hist) - 1

        if st.session_state.coin_history:
            N0 = st.session_state.coin_history[0][1]
            Nn = st.session_state.coin_count
            n = st.session_state.attempt_num
            m1, m2 = st.columns(2)
            m1.metric("N₀", f"{N0}")
            m2.metric(f"N (بعد {n})", f"{Nn}")

    with col2:
        if st.session_state.coin_history:
            al = [h[0] for h in st.session_state.coin_history]
            cl = [h[1] for h in st.session_state.coin_history]
            N0 = cl[0]
            tx = np.linspace(0, max(al[-1] + 1, 8), 200)
            ty = N0 * (1 - dp) ** tx
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=tx, y=ty, mode='lines', name='النظرية', line=dict(color='rgba(0,212,255,0.5)', width=2, dash='dash')))
            fig.add_trace(go.Scatter(x=al, y=cl, mode='lines+markers', name='التجربة', line=dict(color='#00ff88', width=3), marker=dict(color='#00ff88', size=8)))
            fig.update_layout(template="plotly_dark", height=300, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(family="Tajawal", color="#e4e8f5", size=10), xaxis=dict(title="n", gridcolor='rgba(255,255,255,0.04)', color='#7880a0'), yaxis=dict(title="N", gridcolor='rgba(255,255,255,0.04)', color='#7880a0'), legend=dict(bgcolor='rgba(0,0,0,0.4)', font=dict(size=9)), margin=dict(l=5, r=5, t=5, b=5))
            st.plotly_chart(fig, use_container_width=True)

            th = math.log(2) / math.log(1 / (1 - dp))
            tip(f"<strong>عمر النصف النظري:</strong> ≈ {th:.2f} محاولة", "green")
            
# ═══════════════════════════════════════════
# PAGE 6: HALF-LIFE
# ═══════════════════════════════════════════
def show_half_life():
    page_header("⏱️","عمر النصف والنشاطية","العلاقات الرياضية")
    tabs=st.tabs(["📐 عمر النصف","⚡ النشاطية","🔢 مسائل"])
    with tabs[0]:
        section_label("تعريف عمر النصف","blue");tip("<strong>t½</strong> = الزمن لاضمحلال نصف النوى.","blue")
        eq("N/N₀ = (½)^(t/t½)","blue");eq("t½ = 0.693/λ","green")
        section_label("محاكاة تفاعلية","blue")
        N0i=st.number_input("N₀",100,10000,1000,100,key="hl_n0");thi=st.number_input("t½",1.0,100.0,5.0,0.5,key="hl_th");tmx=int(thi*5)
        ta=np.linspace(0,tmx,300);Na=N0i*(0.5)**(ta/thi);fig=go.Figure()
        fig.add_trace(go.Scatter(x=ta,y=Na,mode='lines',line=dict(color='#00d4ff',width=3),fill='tozeroy',fillcolor='rgba(0,212,255,0.05)'))
        for k in range(1,6):xv=k*thi
        if xv<=tmx:yv=N0i*(0.5)**k;fig.add_trace(go.Scatter(x=[xv],y=[yv],mode='markers',marker=dict(color='#ffd700',size=8,symbol='diamond'),showlegend=False));fig.add_annotation(x=xv,y=yv+N0i*0.03,text=f"t={k}t½\nN={int(yv)}",font=dict(size=8,color="#ffd700",family="Tajawal"),showarrow=False)
        fig.update_layout(template="plotly_dark",height=280,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font=dict(family="Tajawal",color="#e4e8f5",size=10),xaxis=dict(title="t",gridcolor='rgba(255,255,255,0.04)',color='#7880a0'),yaxis=dict(title="N",gridcolor='rgba(255,255,255,0.04)',color='#7880a0'),margin=dict(l=5,r=5,t=5,b=5));st.plotly_chart(fig,use_container_width=True)
    with tabs[1]:
        section_label("النشاطية A","orange");tip("<strong>A = λ·N</strong> (اضمحلالات/ثانية)","orange");eq("A = λ · N","orange");eq("A/A₀ = (½)^(t/t½)","orange")
    with tabs[2]:
        section_label("مسألة: الغاليوم-67","blue");st.markdown('<div class="ar-text">λ=2.4×10⁻⁶, A₀=4680 Bq. أوجد t حتى A=1170 Bq.</div>',unsafe_allow_html=True);eq("A/A₀=1/4=(½)² → t=2t½","blue");eq("t=5.8×10⁵ s ≈ 6.7 days","blue")
        glow_div();section_label("مسألة: الكوبالت-60","green");st.markdown('<div class="ar-text">t½=5.27y, A₀=0.200μCi. أوجد N₀ و A(3t½).</div>',unsafe_allow_html=True);eq("N₀=1.77×10¹² نواة","green");eq("A(3t½)=A₀/8=0.025 μCi","green")

# ═══════════════════════════════════════════
# PAGE 7: DECAY SERIES
# ═══════════════════════════════════════════
def show_decay_series():
    page_header("🔗","سلاسل الاضمحلال الطبيعي","Natural Decay Series")
    section_label("ما هي السلاسل الإشعاعية؟","blue");tip("<strong>اضمحلالات متسلسلة</strong> تبدأ بنظير ثقيل وتنتهي برصاص مستقر.","blue")
    for col,(n,s,e,t,c) in zip(st.columns(3),[("سلسلة اليورانيوم","²³⁸U","²⁰⁶Pb","4.47×10⁹y","#ff6b35"),("سلسلة الثوريوم","²³²Th","²⁰⁸Pb","1.41×10¹⁰y","#00d4ff"),("سلسلة الأكتينيوم","²³⁵U","²⁰⁷Pb","7.04×10⁸y","#b347ff")]):
        with col:st.markdown(f'<div class="card" style="text-align:center;border-color:{c}44;"><div style="color:{c};font-weight:800;font-size:0.85rem;">{n}</div><div style="font-family:monospace;font-size:0.8rem;margin:4px 0;">{s}→{e}</div><div style="color:var(--text-secondary);font-size:0.72rem;">{t}</div></div>',unsafe_allow_html=True)
    glow_div();section_label("سلسلة U-238 على مخطط N-Z","orange")
    u238=[(92,146,"²³⁸U","α"),(90,144,"²³⁴Th","β⁻"),(91,143,"²³⁴Pa","β⁻"),(92,142,"²³⁴U","α"),(90,140,"²³⁰Th","α"),(88,138,"²²⁶Ra","α"),(86,136,"²²²Rn","α"),(84,134,"²¹⁸Po","α"),(82,132,"²¹⁴Pb","β⁻"),(83,131,"²¹⁴Bi","β⁻"),(84,130,"²¹⁴Po","α"),(82,128,"²¹⁰Pb","β⁻"),(83,127,"²¹⁰Bi","β⁻"),(84,126,"²¹⁰Po","α"),(82,124,"²⁰⁶Pb","stable")]
    fig=go.Figure();fig.add_trace(go.Scatter(x=np.arange(80,94),y=np.arange(80,94)*1.53-2,mode='lines',line=dict(color='rgba(0,255,136,0.08)',width=18),name='نطاق الاستقرار',showlegend=True))
    for i in range(len(u238)-1):z1,n1=u238[i][0],u238[i][1];z2,n2=u238[i+1][0],u238[i+1][1];dt=u238[i][3];color='#ff6b35' if dt=='α' else '#00d4ff';fig.add_annotation(x=z2,y=n2,ax=z1,ay=n1,arrowcolor=color,arrowwidth=2,arrowhead=2,showarrow=True,text="",xref='x',yref='y',axref='x',ayref='y')
    cm={'α':'#ff6b35','β⁻':'#00d4ff','stable':'#00ff88'}
    for z,n,name,dt in u238:c=cm.get(dt,'#888');sz=18 if name=="²³⁸U" else(15 if name=="²⁰⁶Pb" else 11);fig.add_trace(go.Scatter(x=[z],y=[n],mode='markers+text',marker=dict(color=c,size=sz,line=dict(color='white',width=1)),text=[name],textposition='top right',textfont=dict(size=9,color=c,family="monospace"),name=name,showlegend=False,hovertemplate=f"<b>{name}</b> Z={z} N={n}<extra></extra>"))
    fig.add_trace(go.Scatter(x=[None],y=[None],mode='markers',marker=dict(color='#ff6b35',size=10),name='α',showlegend=True));fig.add_trace(go.Scatter(x=[None],y=[None],mode='markers',marker=dict(color='#00d4ff',size=10),name='β⁻',showlegend=True));fig.add_trace(go.Scatter(x=[None],y=[None],mode='markers',marker=dict(color='#00ff88',size=10),name='مستقر',showlegend=True))
    fig.update_layout(template="plotly_dark",height=420,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font=dict(family="Tajawal",color="#e4e8f5",size=10),xaxis=dict(title="Z",range=[79,94],gridcolor='rgba(255,255,255,0.04)',color='#7880a0',dtick=2),yaxis=dict(title="N",range=[120,150],gridcolor='rgba(255,255,255,0.04)',color='#7880a0',dtick=5),legend=dict(bgcolor='rgba(0,0,0,0.5)',bordercolor='rgba(0,212,255,0.2)',x=0.01,y=0.99,font=dict(size=9)),margin=dict(l=5,r=5,t=5,b=5));st.plotly_chart(fig,use_container_width=True)
    glow_div();section_label("المعادلة الإجمالية","orange");eq("²³⁸₉₂U → ²⁰⁶₈₂Pb + 8⁴₂He + 6⁰₋₁e + 6v̄","orange");tip("الكتلة: 238=206+32 ✓ | الذري: 92=82+16−6=92 ✓","green")
    glow_div();section_label("مثال 11 — الثوريوم-232","blue");eq("n=(232-208)/4=6 α | m=82+12-90=4 β⁻","blue")

# ═══════════════════════════════════════════
# PAGE 8: TECHNOLOGY
# ═══════════════════════════════════════════
def show_technology():
    page_header("🔬","الربط بالتكنولوجيا","تطبيقات الإشعاع في الحياة")
    for ic,tt,rad,elem,cl,desc,why in [("🔥","أجهزة إنذار الحريق","α","Am-241","card-orange","ألفا تُأيّن الهواء → تيار. الدخان يمتص الألفا → إنذار.","ألفا آمنة + تأيين عالي"),("🏥","علاج السرطان","γ","Co-60","card-purple","غاما تدمر DNA الخلايا السرطانية.","تخترق بعمق ويمكن توجيهها"),("🧬","PET Scan","β⁺","F-18","","β⁺+إلكترون → فوتونان γ → تصوير 3D.","كشف مبكر عن الأورام"),("⚙️","ضبط سُمك المواد","β","مصادر","card-green","β تنفذ ← كاشف يقيس الشدة.","بيتا متوسطة النفاذ مثالية"),("🔍","فحص اللحامات","γ","Ir-192","card-purple","غاما + لوحة فوتوغرافية = صورة الشقوق.","تخترق المعادن السميكة"),("🌍","التأريخ الجيولوجي","α/β⁻","¹⁴C/U","card-orange","¹⁴C للآثار، U/Pb للصخور.","عمر نصف معروف = ساعة طبيعية")]:
        st.markdown(f'<div class="card {cl}"><div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;direction:rtl;"><span style="font-size:1.5rem;">{ic}</span><div><div style="font-weight:800;font-size:0.92rem;">{tt}</div><div style="font-size:0.75rem;color:var(--text-secondary);">{rad} — {elem}</div></div></div><div style="color:var(--text-primary);font-size:0.85rem;line-height:1.65;direction:rtl;">{desc}</div><div style="margin-top:8px;padding:6px 10px;background:rgba(0,212,255,0.05);border-radius:6px;border:1px solid rgba(0,212,255,0.12);"><span style="color:var(--accent-blue);font-weight:700;font-size:0.78rem;">💡 لماذا؟ </span><span style="color:var(--text-secondary);font-size:0.78rem;">{why}</span></div></div>',unsafe_allow_html=True)
    glow_div();section_label("اختبر نفسك","yellow")
    jc={"اختر...":None,"فحص سُمك ورق":"β","علاج ورم":"γ","كشف دخان":"α","فحص لحام":"γ","تأريخ 3000 سنة":"¹⁴C"}
    sel=st.selectbox("اختر مهمة:",list(jc.keys()),key="job_sel")
    if jc.get(sel):eq(f"الأنسب: {jc[sel]}","green")

# ═══════════════════════════════════════════
# PAGE 9: REVIEW
# ═══════════════════════════════════════════
def show_review():
    page_header("📝","مراجعة الدرس","أسئلة تقييمية")
    tabs=st.tabs(["📌 MCQ","⚗️ المعادلات","🔢 مسائل"])
    with tabs[0]:
        questions=[("1. الاضمحلال الذي لا يتساوى فيه A للأم والناتج:",["أ. ألفا","ب. بيتا+","جـ. بيتا−","د. غاما"],"أ. ألفا","ألفا يقلل A بـ4"),("2. ليست صحيحة لغاما:",["أ. لا شحنة","ب. تفاعل ضعيف","جـ. تردد منخفض","د. سرعتها=c"],"جـ. تردد منخفض","غاما ترددها عالٍ"),("3. أكبر قدرة تأيين:",["أ. غاما","ب. بيتا","جـ. ألفا","د. سينية"],"جـ. ألفا","كتلة+شحنة كبيرة"),("4. إذا t½(X)=2t½(Y) فإن λ(X):",["أ. ضعف λ(Y)","ب. نفسها","جـ. ربعها","د. نصفها"],"د. نصفها","علاقة عكسية"),("5. ²²⁶₈₈Ra → ? + ⁴₂He:",["أ. ²²²₈₆Rn","ب. ²²²₈₄Po","جـ. ²²⁰₈₆Rn","د. ²²⁴₈₈Ra"],"أ. ²²²₈₆Rn","Z=86, A=222")]
        if "quiz_submitted" not in st.session_state:st.session_state.quiz_submitted=False
        if "quiz_answers" not in st.session_state:st.session_state.quiz_answers={}
        for i,(q,opts,ans,exp) in enumerate(questions):
            with st.expander(q,expanded=(i<2)):st.session_state.quiz_answers[f"q{i}"]=st.radio("",opts,key=f"q{i}",label_visibility="collapsed")
        if st.button("✅ تحقق",key="submit_quiz"):st.session_state.quiz_submitted=True
        if st.session_state.quiz_submitted:
            correct=0
            for i,(_,_,ans,exp) in enumerate(questions):ua=st.session_state.quiz_answers.get(f"q{i}","");ok=ua==ans
            if ok:correct+=1;cls="success-tip" if ok else "warning-tip"
            st.markdown(f'<div class="tip-box {cls}">{"✅" if ok else "❌"} سؤال {i+1}: {ua} | {"صحيح" if ok else f"الصواب: {ans}"}<br><em style="font-size:0.82rem;">{exp}</em></div>',unsafe_allow_html=True)
            sc="#00ff88" if correct>=4 else("#ffd700" if correct>=2 else "#ff6b35");st.markdown(f'<div class="eq-box" style="color:{sc};font-size:1.1rem;">{correct}/{len(questions)} {"🌟" if correct==len(questions) else "👍" if correct>=3 else "📚"}</div>',unsafe_allow_html=True)
    with tabs[1]:
        section_label("أكمل المعادلات","green")
        for i,(q,a,h) in enumerate([("¹₀n → ¹₁p + ? + v̄","⁰₋₁e","β⁻"),("¹₁p → ¹₀n + ? + ν","⁰₊₁e","β⁺"),("²²⁶₈₈Ra → ? + ⁴₂He","²²²₈₆Rn","α"),("²³⁴₉₁Pa* → ²³⁴₉₁Pa + ?","γ","غاما")]):
            eq(f"تمرين {i+1}: {q}","blue")
            if st.button(f"الإجابة {i+1}",key=f"fill{i}"):eq(f"{a}","green");tip(h,"green")
    with tabs[2]:
        section_label("اليود-131","orange");st.markdown('<div class="ar-text">t½=8 أيام. اضمحل 75%.</div>',unsafe_allow_html=True)
        with st.expander("💡 الحل"):eq("يبقى 25% → t=2t½=16 يوم","orange");tip("✅ 16 يوماً","green")
        glow_div();section_label("الثوريوم-228","blue")
        with st.expander("💡 الحل"):eq("t½=0.693/λ=6.03×10⁷s≈1.9y","blue");eq("A=λN=2.91×10¹³ Bq","blue")

# ═══════════════════════════════════════════
# ★ ROUTER — يقرأ الصفحة من URL
# ═══════════════════════════════════════════
if current_page == "scientists":   show_scientists()
elif current_page == "types":      show_radiation_types()
elif current_page == "decay":      show_decay_types()
elif current_page == "modeling":   show_modeling()
elif current_page == "halflife":   show_half_life()
elif current_page == "series":     show_decay_series()
elif current_page == "tech":       show_technology()
elif current_page == "review":     show_review()
else:                              show_home()
