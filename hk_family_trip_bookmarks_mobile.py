import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="香港家族旅行ブックマーク", layout="wide")

# Streamlit のヘッダー・フッターを非表示に
hide_streamlit_style = """
<style>
/* ヘッダー非表示 */
header {display: none;}
/* フッター非表示 */
footer {display: none;}
/* ページ余白をなくす */
.css-18e3th9 {padding: 0px;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# HTMLファイル読み込み
with open("hk_family_trip_bookmarks_mobile.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# JavaScriptでリンクを必ず新しいタブで開くようにする
html_with_js = f"""
{html_content}
<script>
document.querySelectorAll('a').forEach(a => {{
    a.setAttribute('target', '_blank');
}});
</script>
"""

# HTMLを埋め込み表示（スクロール可能に）
components.html(
    html_with_js,
    height=1000,   # スクロール可能にする高さ
    scrolling=True
)
