import streamlit as st
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import socket

st.set_page_config(page_title="香港家族旅行ブックマーク", layout="wide")

# Streamlit ヘッダー・フッター非表示
st.markdown("""
<style>
header {display: none;}
footer {display: none;}
.css-18e3th9 {padding: 0px;}
</style>
""", unsafe_allow_html=True)

st.title("香港家族旅行ブックマーク (スマホ対応)")

# HTML ファイルのディレクトリをサーバー用に指定
html_dir = os.path.abspath(".")  # 同一フォルダ

# 簡易サーバー起動関数
def start_server():
    os.chdir(html_dir)
    port = 8000
    handler = SimpleHTTPRequestHandler
    httpd = HTTPServer(("", port), handler)
    httpd.serve_forever()

# サーバーをバックグラウンドで起動（Thread）
thread = threading.Thread(target=start_server, daemon=True)
thread.start()

# スマホからアクセスするための IP アドレス取得
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
server_url = f"http://{local_ip}:8000/hk_family_trip_bookmarks_mobile.html"

st.markdown(f"""
下のボタンを押すとスマホでもフルスクリーンで表示可能です。

[スマホでHTMLを開く]({server_url})
""")

st.info(f"スマホのブラウザから次のURLにアクセスしてください:\n{server_url}")
