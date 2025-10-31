import streamlit as st
from pathlib import Path

# ページ設定
st.set_page_config(page_title="家族旅行ブックマーク", layout="wide")

# HTML読み込み（UTF-8）
html_file = Path("hk_family_trip_bookmarks_mobile.html")
with html_file.open("r", encoding="utf-8") as f:
    html_code = f.read()

# Streamlit に直接埋め込み（iframeなし）
# スクロールと高さ自動調整対応
st.markdown(f"""
<div id="bookmark-wrapper" style="width:100%;">
{html_code}
</div>

<script>
// 高さ自動調整（画像ロードやリサイズ対応）
function adjustHeight() {{
    const wrapper = document.getElementById('bookmark-wrapper');
    wrapper.style.minHeight = wrapper.scrollHeight + 'px';
}}

window.addEventListener('load', adjustHeight);
window.addEventListener('resize', adjustHeight);

const images = document.images;
for (let img of images) {{
    img.addEventListener('load', adjustHeight);
}}
</script>
""", unsafe_allow_html=True)
