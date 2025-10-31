import streamlit as st
from streamlit.components.v1 import html as st_html
import os

# --- ページ設定 ---
st.set_page_config(
    page_title="",
    layout="wide"
)

# --- HTML ファイル読み込み ---
html_file = "hk_family_trip_bookmarks_mobile.html"
if not os.path.exists(html_file):
    st.error(f"{html_file} が見つかりません。Python スクリプトと同じフォルダに置いてください。")
else:
    with open(html_file, "r", encoding="utf-8") as f:
        html_code = f.read()

    # --- Streamlit に HTML を直接埋め込み ---
    st_html(
        html_code,
        height=2000,       # 初期高さ。iframe 内のスクロールで調整可能
        scrolling=True
    )
