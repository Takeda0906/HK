import streamlit as st
from streamlit.components.v1 import html as st_html

# ページ設定
st.set_page_config(page_title="家族旅行ブックマーク", layout="wide")

# HTMLファイルを読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# --- Blob URLでiframe読み込み（文字化け防止＆スマホリンク対応） ---
auto_resize_wrapper = f"""
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
    // HTML文字列をUTF-8でBlob化
    const htmlString = `{html_code.replace('`', '\\`')}`;
    const blob = new Blob([htmlString], {{ type: "text/html;charset=utf-8" }});
    const blobUrl = URL.createObjectURL(blob);

    // iframe生成
    const iframe = document.createElement("iframe");
    iframe.src = blobUrl;
    iframe.sandbox = "allow-same-origin allow-scripts allow-popups allow-forms";
    iframe.style.width = "100%";
    iframe.style.minHeight = "100vh";
    iframe.style.border = "none";
    document.body.appendChild(iframe);

    // 高さ自動調整
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

# Streamlitに埋め込み
st_html(auto_resize_wrapper, height=2000, scrolling=True)
