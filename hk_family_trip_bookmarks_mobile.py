import streamlit as st
from streamlit.components.v1 import html as st_html

# ページ設定（UIを表示する）
st.set_page_config(page_title="家族旅行ブックマーク", layout="wide")

st.title("📖 家族旅行ブックマーク（モバイル対応）")
st.write("以下のHTMLは自動で高さを調整して全体がスクロール可能です。")

# HTMLファイルを読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# --- ここがポイント ---
# JavaScriptを使ってiframeの高さを自動調整
# Streamlitがiframe経由でHTMLを表示するため、postMessageで親ページへ高さを通知
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
    overflow: hidden;
  }}
  iframe {{
    border: none;
    width: 100%;
  }}
</style>
</head>
<body>
  <iframe id="embedded" srcdoc='{html_code.replace("'", "&apos;")}'></iframe>

  <script>
    const iframe = document.getElementById('embedded');
    function resizeIframe() {{
      try {{
        const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
        const newHeight = iframeDocument.body.scrollHeight;
        iframe.style.height = newHeight + 'px';
      }} catch(e) {{
        console.log('resize error:', e);
      }}
    }}
    iframe.addEventListener('load', resizeIframe);
    window.addEventListener('resize', resizeIframe);
  </script>
</body>
</html>
"""

# Streamlitに埋め込み（高さは一時的に大きめでOK）
st_html(auto_resize_wrapper, height=1000, scrolling=True)
