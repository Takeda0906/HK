
# Streamlit のヘッダやフッタを CSS で非表示にして、"見た目上"の全画面化
hide_streamlit_style = """
<style>
/* Streamlit のヘッダ＆フッタ非表示 */
.reportview-container .main header {display: none;}
footer {display: none;}
/* サイドバーの余白を取り除く */
.css-1d391kg {padding-top: 0rem;}
/* body の余白を詰める（必要に応じてセレクタ調整） */
[data-testid="stAppViewContainer"] > .main {padding: 0;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# HTML を読み込む
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 画面高さに合わせたいけど、st.components.v1.html は固定 height を要求するため、
# スマホの高さに合わせて余裕を持たせた値を指定（例：1000px や 2000px）。必要なら JS で調整。
# スクロールは有効化しておく
components_html(html_content, height=1200, scrolling=True)
