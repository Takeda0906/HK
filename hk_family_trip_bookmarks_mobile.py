import streamlit as st
from streamlit.components.v1 import html as st_html

# ページ設定
st.set_page_config(
    page_title="家族旅行ブックマーク",
    layout="wide"
)

# HTMLファイル読み込み（UTF-8保存前提）
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# HTMLを直接埋め込む（スマホリンク対応）
responsive_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    overflow: auto;  /* Streamlit側でスクロール */
  }}
  #content-wrapper {{
    width: 100%;
    min-height: 100vh;
    box-sizing: border-box;
  }}
</style>
</head>
<body>
<div id="content-wrapper">
{html_code}
</div>

<script>
// 高さ自動調整（画像ロードや画面リサイズに対応）
function adjustHeight() {{
    const wrapper = document.getElementById('content-wrapper');
    wrapper.style.minHeight = wrapper.scrollHeight + 'px';
}}

window.addEventListener('load', adjustHeight);
window.addEventListener('resize', adjustHeight);
const images = document.images;
for (let img of images) {{
    img.addEventListener('load', adjustHeight);
}}
</script>
</body>
</html>
"""

# Streamlitに埋め込み
st_html(responsive_html, height=2000, scrolling=True)
