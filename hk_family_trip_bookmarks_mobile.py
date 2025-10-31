import streamlit as st
from streamlit.components.v1 import html as st_html

# ページ設定
st.set_page_config(
    page_title="家族旅行ブックマーク",
    layout="wide"
)

# HTMLファイル読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Streamlitに埋め込み（スマホ対応・全画面・スクロール対応）
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
    height: 100%;
    overflow: hidden; /* スクロールはStreamlit側に任せる */
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
function adjustHeight() {{
    const wrapper = document.getElementById('content-wrapper');
    const newHeight = wrapper.scrollHeight;
    wrapper.style.minHeight = newHeight + 'px';
}}

// 読み込み時・画像読み込み後・リサイズ時に高さ調整
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
# heightは大きめにしてスクロール可能に
st_html(responsive_html, height=2000, scrolling=True)
