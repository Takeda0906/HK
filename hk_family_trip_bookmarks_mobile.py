import streamlit as st
from streamlit.components.v1 import html as st_html
import base64

st.set_page_config(page_title="家族旅行ブックマーク", layout="wide")

# HTMLファイル読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Base64に変換
html_base64 = base64.b64encode(html_code.encode("utf-8")).decode()

# Blob URLを生成してiframeで読み込む
html_wrapper = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  html, body {{
    margin: 0;
    padding: 0;
    height: 100%;
    overflow: auto;
  }}
  iframe {{
    border: none;
    width: 100%;
    min-height: 100vh;
  }}
</style>
</head>
<body>
  <script>
    // Base64データをBlobに変換し、一時URLを作成
    const blob = new Blob([atob("{html_base64}")], {{ type: "text/html" }});
    const blobUrl = URL.createObjectURL(blob);

    // iframe生成
    const iframe = document.createElement("iframe");
    iframe.src = blobUrl;
    iframe.sandbox = "allow-same-origin allow-scripts allow-popups allow-forms";
    iframe.style.width = "100%";
    iframe.style.border = "none";
    iframe.style.minHeight = "100vh";
    document.body.appendChild(iframe);

    // 自動高さ調整
    function resizeIframe() {{
      try {{
        const doc = iframe.contentDocument || iframe.contentWindow.document;
        const newHeight = doc.documentElement.scrollHeight || doc.body.scrollHeight;
        iframe.style.height = newHeight + "px";
      }} catch (e) {{
        console.log("resize error:", e);
      }}
    }}

    iframe.addEventListener("load", () => {{
      resizeIframe();
      setTimeout(resizeIframe, 1000);
      setTimeout(resizeIframe, 3000);
    }});
    window.addEventListener("resize", resizeIframe);
  </script>
</body>
</html>
"""

# Streamlitで埋め込み
st_html(html_wrapper, height=2000, scrolling=True)
