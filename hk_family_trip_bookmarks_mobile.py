import streamlit as st
from streamlit.components.v1 import html as st_html
import os

# --- ページ設定 ---
st.set_page_config(
    page_title="",
    layout="wide"
)

st.title("香港 家族旅行ブックマーク")

# --- HTML ファイル ---
html_file = "hk_family_trip_bookmarks_mobile.html"

if not os.path.exists(html_file):
    st.error(f"{html_file} が見つかりません。Python と同じフォルダに置いてください。")
else:
    with open(html_file, "r", encoding="utf-8") as f:
        html_code = f.read()

    # --- スマホ対応の埋め込み ---
    # 高さは十分に大きめに設定、スクロール可能
    st_html(
        html_code,
        height=2500,  # 必要に応じて増減可能
        scrolling=True
    )
