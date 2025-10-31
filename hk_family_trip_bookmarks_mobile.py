import streamlit as st

# HTMLファイルを読み込む
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# StreamlitでHTMLを表示
st.components.v1.html(html_content, height=800, scrolling=True)
