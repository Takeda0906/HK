# app.py
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

#st.set_page_config(page_title="香港 家族旅行", layout="wide")

# Streamlit ヘッダ・フッタ非表示
st.markdown(
    """
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# HTMLファイルのパス
html_file = Path(__file__).parent / "hk_family_trip_bookmarks_mobile.html"

# HTMLを読み込み
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# components.htmlで直接埋め込む
components.html(
    html_content,
    height=1200,  # ページ全体の高さに調整してください
    scrolling=True
)
