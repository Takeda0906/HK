import streamlit as st
from streamlit.components.v1 import html as st_html
import os

st.set_page_config(page_title="香港 家族旅行ブックマーク", layout="wide")
st.title("香港 家族旅行ブックマーク")

html_file = "hk_family_trip_bookmarks_mobile.html"

if not os.path.exists(html_file):
    st.error(f"{html_file} が見つかりません。Python と同じフォルダに置いてください。")
else:
    with open(html_file, "r", encoding="utf-8") as f:
        html_code = f.read()

    # HTML 内のすべてのリンクに onclick を付与して window.open で開く
    # target="_blank" でも動作しない場合に対応
    html_code_with_js = f"""
    <script>
    document.addEventListener("DOMContentLoaded", function() {{
        const links = document.querySelectorAll("a");
        links.forEach(link => {{
            link.setAttribute("target", "_blank");
            link.setAttribute("rel", "noopener");
            link.onclick = function(e) {{
                e.preventDefault();
                window.open(this.href, "_blank");
            }};
        }});
    }});
    </script>
    {html_code}
    """

    # Streamlit に埋め込み
    st_html(html_code_with_js, height=2500, scrolling=True)
