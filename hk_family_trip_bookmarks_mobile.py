import streamlit as st
from streamlit.components.v1 import html as st_html

# ページ設定
st.set_page_config(page_title="家族旅行ブックマーク", layout="wide")

# タイトル
#st.subheader("家族旅行ブックマーク")

# HTMLファイルを読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# --- 高さ自動調整 + スクロール対応 ---
auto_resize_wrapper = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  html, body {{
    margin: 0;
    padding: 0;
    height: 100%;
    overflow: auto;  /* ← スクロール許可に変更 */
  }}
  iframe {{
    border: none;
    width: 100%;
    min-height: 100vh;
  }}
</style>
</head>
<body>
  <iframe id="embedded" srcdoc="{html_code.replace('"', '&quot;')}"></iframe>

  <script>
    const iframe = document.getElementById('embedded');
    function resizeIframe() {{
      try {{
        const doc = iframe.contentDocument || iframe.contentWindow.document;
        const newHeight = doc.documentElement.scrollHeight || doc.body.scrollHeight;
        iframe.style.height = newHeight + 'px';
      }} catch (e) {{
        console.log('resize error:', e);
      }}
    }}
    iframe.addEventListener('load', () => {{
      resizeIframe();
      // 再描画後も更新（画像やCSS遅延対策）
      setTimeout(resizeIframe, 1000);
      setTimeout(resizeIframe, 3000);
    }});
    window.addEventListener('resize', resizeIframe);
  </script>
</body>
</html>
"""

# Streamlitに埋め込み
st_html(auto_resize_wrapper, height=2000, scrolling=True)
