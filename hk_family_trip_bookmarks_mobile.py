import streamlit as st
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import socket
import time

st.set_page_config(page_title="香港家族旅行ブックマーク", layout="wide")

# Streamlit のヘッダー・フッターを非表示
st.markdown("""
<style>
header {display: none;}
footer {display: none;}
.css-18e3th9 {padding: 0px;}
</style>
""", unsafe_allow_html=True)

st.title("香港家族旅行ブックマーク (スマホ対応)")

# HTML ファイルのディレクトリをサーバー用に指定
html_dir = os.path.abspath(".")  # HTML があるフォルダ

# 簡易サーバー起動関数
def start_server():
    os.chdir(html_dir)
    port = 8000
    handler = SimpleHTTPRequestHandler
    httpd = HTTPServer(("", port), handler)
    httpd.serve_forever()

# サーバーをバックグラウンドで起動
thread = threading.Thread(target=start_server, daemon=True)
thread.start()

# 少し待ってサーバーが起動するのを待機
time.sleep(1)

# スマホからアクセスするためのローカルIP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
server_url = f"http://{local_ip}:8000/hk_family_trip_bookmarks_mobile.html"

# HTML を直接 iframe で埋め込む
st.markdown(f"""
<iframe src="{server_url}" width="100%" height="1200px" style="border:none;"></iframe>
""", unsafe_allow_html=True)

st.info(f"スマホからもアクセス可能:\n{server_url}")
