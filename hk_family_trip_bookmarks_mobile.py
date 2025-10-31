import streamlit as st

st.set_page_config(
    page_title="家族旅行プラン",
    layout="wide"
)

# タイトル
#st.markdown("<h2 style='text-align:center;'>家族旅行プラン</h2>", unsafe_allow_html=True)

# HTMLファイルを読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# iframeで埋め込み（高さ自動調整＋スクロール対応）
iframe_code = f"""
    <iframe
        srcdoc="{html_content}"
        style="
            width:100%;
            height:100vh;
            border:none;
            overflow:auto;
        "
        sandbox="allow-same-origin allow-scripts allow-popups allow-forms"
    ></iframe>
"""

# HTMLを埋め込む
st.components.v1.html(iframe_code, height=1000, scrolling=True)
