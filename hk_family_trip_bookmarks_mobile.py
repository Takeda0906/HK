import streamlit as st

# Streamlit のヘッダやフッタを非表示（全画面風に）
hide_streamlit_style = """
<style>
#/* Streamlit のヘッダ＆フッタ非表示 */
#header {visibility: hidden;}
#footer {visibility: hidden;}

/* サイドバーの余白を取り除く */
.css-1d391kg {padding-top: 0rem !important;}

/* body の余白を詰める */
[data-testid="stAppViewContainer"] > .main {
    padding: 0 !important;
    margin: 0 !important;
}

/* iframe 内でスクロールできるように */
iframe {
    height: 100vh !important;
    width: 100% !important;
    border: none;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# HTMLを読み込む
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# HTMLを全画面で表示（スクロール可能）
st.components.v1.html(html_content, height=1000, scrolling=True)
