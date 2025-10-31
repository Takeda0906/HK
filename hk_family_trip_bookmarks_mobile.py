import streamlit as st
import streamlit.components.v1 as components

# HTMLファイル読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# aタグに target="_blank" がなければ付与する簡易処理
import re
html_content = re.sub(r'<a (?!.*target=)', '<a target="_blank" ', html_content)

# 埋め込み表示
components.html(
    html_content,
    height=800,
    scrolling=True
)
