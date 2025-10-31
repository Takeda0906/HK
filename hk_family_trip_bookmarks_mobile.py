# app.py
import streamlit as st
from pathlib import Path

#st.set_page_config(page_title="香港 家族旅行", layout="wide")

# Streamlit のヘッダ・フッタ非表示（全画面表示向け）
hide_streamlit_style = """
    <style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# HTMLファイルパス
html_file = Path(__file__).parent / "hk_family_trip_bookmarks_mobile.html"

# HTML読み込み
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# iframeで表示
st.markdown(
    f"""
    <iframe 
        srcdoc="{html_content.replace('"', '&quot;')}" 
        style="border:none; width:100%; height:100vh;" 
        sandbox="allow-scripts allow-same-origin allow-popups allow-forms">
    </iframe>
    """,
    unsafe_allow_html=True
)
