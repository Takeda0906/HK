import streamlit as st
from pathlib import Path

# ページ設定
st.set_page_config(
    page_title="家族旅行ブックマーク",
    layout="wide"
)

# HTMLファイルのパス
html_file = Path("hk_family_trip_bookmarks_mobile.html")

# Streamlit の「静的ファイル」用ディレクトリにコピー（例：現在のディレクトリ）
# ここではそのままパスを iframe src に渡します
iframe_src = html_file.as_posix()  # Windowsなら as_posix() でスラッシュ統一

# iframe で HTML を読み込み、高さ自動調整
st.markdown(f"""
<iframe 
    src="{iframe_src}" 
    style="width:100%; height:1000px; border:none;" 
    id="bookmark-frame"
></iframe>

<script>
// 高さ自動調整（画像ロード・リサイズ対応）
const iframe = document.getElementById('bookmark-frame');
function resizeIframe() {{
    try {{
        iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
    }} catch(e) {{
        console.log('iframe resize error:', e);
    }}
}}

iframe.addEventListener('load', () => {{
    resizeIframe();
    // 画像やCSS読み込み遅延対策
    setTimeout(resizeIframe, 1000);
    setTimeout(resizeIframe, 3000);
}});
window.addEventListener('resize', resizeIframe);
</script>
""", unsafe_allow_html=True)

