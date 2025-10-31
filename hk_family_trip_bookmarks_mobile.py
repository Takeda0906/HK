import streamlit as st
from streamlit.components.v1 import html as st_html
import base64

# ページ設定
st.set_page_config(page_title="家族旅行ブックマーク", layout="wide")

# HTMLファイルを読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Base64エンコード（UTF-8対応で文字化け防止）
html_base64 = base64.b64encode(html_code.encode("utf-8")).decode()

# --- Blob URLでiframe読み込み（スマホリンク対応） ---
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
    // Base64 → UTF-8 デコードして Blob に変換
    const binary = atob("{html_base64}");
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) {{
      bytes[i] = binary.charCodeAt(i);
    }}
    const blob = new Blob([bytes], {{ type: "text/html;charset=utf-8" }});
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
        const newHeight = doc.documentElement.scrollHeight || doc.body.scr

