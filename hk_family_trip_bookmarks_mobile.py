import streamlit as st
import os
import webbrowser

st.set_page_config(page_title="香港家族旅行ブックマーク", layout="wide")

# Streamlit ヘッダー・フッターを非表示
st.markdown("""
<style>
header {display: none;}
footer {display: none;}
.css-18e3th9 {padding: 0px;}
</style>
""", unsafe_allow_html=True)

st.title("香港家族旅行ブックマーク")

# HTMLファイルの絶対パス
file_path = os.path.abspath("hk_family_trip_bookmarks_mobile.html")
file_url = f"file://{file_path}"

st.markdown("""
スマホで HTML を完全に表示・リンクも使いたい場合は、下のボタンを押してブラウザで開いてください。
""")

# ボタンでブラウザを開く
if st.button("HTML をブラウザで開く"):
    # ローカルPCからなら自動で開く
    webbrowser.open(file_url)
    st.success("ブラウザで開きました！")
    st.markdown(f"[もし自動で開かない場合はここをタップ]({file_url})")
