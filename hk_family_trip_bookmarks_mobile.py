import streamlit as st
import streamlit.components.v1 as components

# HTMLファイルの読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# HTMLを埋め込み表示
components.html(
    html_content,
    height=800,          # スクロール可能にする高さ
    scrolling=True       # スクロールを有効にする
)
