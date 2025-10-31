import streamlit as st
from pathlib import Path

st.set_page_config(page_title="香港 家族旅行", layout="wide")

# ヘッダ・フッタ非表示
st.markdown(
    """
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# HTMLファイルを読み込む
html_file = Path(__file__).parent / "hk_family_trip_bookmarks_mobile.html"
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# スマホ対応用にリンクをすべて target="_blank" に置換
import re
html_content_fixed = re.sub(r'<a ', '<a target="_blank" ', html_content)

# HTMLをそのまま表示
st.markdown(html_content_fixed, unsafe_allow_html=True)
