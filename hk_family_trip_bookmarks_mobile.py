import streamlit as st
import os
from streamlit.components.v1 import html as st_html

st.set_page_config(page_title="", layout="wide")

html_file = "hk_family_trip_bookmarks_mobile.html"

if not os.path.exists(html_file):
    st.error(f"{html_file} が見つかりません。Python と同じフォルダに置いてください。")
else:
    # HTMLファイルの絶対パス
    file_path = os.path.abspath(html_file)

    # file:// URL に変換（ブラウザで開くため）
    file_url = f"file://{file_path}"

    # HTML埋め込み＋自動リダイレクト
    auto_open_html = f"""
    <html>
      <head>
        <meta http-equiv="refresh" content="0;url={file_url}">
      </head>
      <body>
        <p>ブラウザでHTMLを開いています… <a href="{file_url}">こちらをクリック</a> もし自動で開かない場合</p>
      </body>
    </html>
    """

    st_html(auto_open_html, height=100)
