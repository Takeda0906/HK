import streamlit as st
import os
from streamlit.components.v1 import html as st_html

# --- ページ設定 ---
st.set_page_config(page_title="香港 家族旅行ブックマーク", layout="wide")

#st.title("香港 家族旅行ブックマーク")

# --- HTML ファイル ---
html_file = "hk_family_trip_bookmarks_mobile.html"

if not os.path.exists(html_file):
    st.error(f"{html_file} が見つかりません。Python スクリプトと同じフォルダに置いてください。")
else:
    # HTML ファイルの絶対パスを取得
    file_path = os.path.abspath(html_file)

    # file:// URL に変換
    file_url = f"file://{file_path}"

    # --- 自動リダイレクト用 HTML ---
    auto_open_html = f"""
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>自動リダイレクト</title>
        <!-- 0秒で HTML をブラウザで開く -->
        <meta http-equiv="refresh" content="0;url={file_url}">
        <style>
          body {{
            font-family: sans-serif;
            text-align: center;
            padding-top: 50px;
          }}
        </style>
      </head>
      <body>
        <p>ブラウザでHTMLを開いています…</p>
        <p>もし自動で開かない場合は <a href="{file_url}" target="_blank">こちらをクリック</a></p>
      </body>
    </html>
    """

    # --- Streamlit に埋め込み ---
    st_html(auto_open_html, height=150)
