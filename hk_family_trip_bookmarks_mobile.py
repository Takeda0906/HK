import streamlit as st
from pathlib import Path

# タイトル
st.title("香港 家族旅行ブックマーク")

# HTMLファイルパス
html_file = Path("hk_family_trip_bookmarks_mobile.html")

if html_file.exists():
    # HTMLを読み込む
    html_content = html_file.read_text(encoding="utf-8")
    
    # Streamlitで表示
    st.components.v1.html(
        html_content,
        height=1200,   # 初期表示高さ。スクロール可能
        scrolling=True
    )
else:
    st.error(f"{html_file} が見つかりません。")
