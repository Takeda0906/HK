import streamlit as st

# HTMLファイルの読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# HTMLを表示
st.markdown(
    html_content,
    unsafe_allow_html=True  # HTMLレンダリングを許可
)

# ページ全体をスマホ表示に最適化
st.markdown(
    """
    <style>
    /* 全画面幅にする */
    .reportview-container .main {
        padding: 0;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
