import streamlit as st
from streamlit.components.v1 import html as st_html

st.set_page_config(page_title="香港 家族旅行ブックマーク", layout="wide")

st.title("香港 家族旅行ブックマーク")

html_content = """
<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
#<title>香港旅行</title>
<meta name="description" content="家族旅行（3泊4日／ディズニー含む）向けのスマホ用ブックマークリスト。公式サイトへワンタップで移動できます。">
<style>
:root{--bg:#ffffff;--card:#f8fafc;--accent:#ff5a5f;--muted:#6b7280;--border:#e6eef6}
*{box-sizing:border-box}
html,body{height:100%;margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,'Hiragino Kaku Gothic ProN',Meiryo,Arial;background:linear-gradient(180deg,#f7fbff 0%,#ffffff 100%);color:#0f1724}
.wrap{max-width:720px;margin:0 auto;padding:18px}
header{display:flex;gap:12px;align-items:center}
.logo{width:56px;height:56px;border-radius:12px;background:linear-gradient(135deg,var(--accent),#ff7b5a);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:18px}
h1{margin:0;font-size:18px}
p.lead{margin:6px 0 14px;color:var(--muted);font-size:13px}
.card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:12px;margin-bottom:14px}
.section-title{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.section-title h2{margin:0;font-size:15px}
.list{display:grid;gap:8px}
.item{display:flex;justify-content:space-between;align-items:center;padding:10px;border-radius:10px;background:#fff;border:1px solid var(--border)}
.meta{display:flex;flex-direction:column;gap:3px}
.title{font-weight:600;font-size:15px}
.subtitle{font-size:12px;color:var(--muted)}
.actions{display:flex;gap:8px;align-items:center}
.btn{display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:10px;text-decoration:none;background:var(--accent);color:#fff;font-weight:600;font-size:13px}
.btn.secondary{background:#fff;color:var(--accent);border:1px solid var(--border)}
footer{padding:12px 0;text-align:center;color:var(--muted);font-size:13px}
.hint{font-size:13px;color:var(--muted);margin-top:8px}
.copy{font-size:12px;color:var(--muted);text-align:center;margin-top:6px}
@media (max-width:420px){.wrap{padding:14px}.logo{width:48px;height:48px}}
</style>
</head>
<body>
<div class="wrap">
<header>
<div class="logo">HK</div>
<div>
<h1>香港 家族旅行ブックマーク</h1>
<p class="lead">3泊4日（ディズニー含む）。タップで公式ページを開けます。ホーム画面に追加すると便利です。</p>
</div>
</header>

<section class="card">
<div class="section-title">
<h2>使い方</h2>
<span class="subtitle">スマホ向け</span>
</div>
<div class="hint">このページをブラウザで開き、ブラウザメニューから「ホーム画面に追加」をしてください。渡航中にすぐ開けます。</div>
</section>

<section class="card">
<div class="section-title">
<h2>🍽 レストラン（おすすめ）</h2>
<span class="subtitle">ワンタップで公式サイトへ</span>
</div>
<div class="list">
"""  # ここまでヘッダと開始タグ

# レストランリストを追加
restaurants = [
    {"name":"Hutong（フートン）","desc":"ハーバービューの北方中華・<br>テイスティングあり","url":"https://hutong.com.hk/"},
    {"name":"Tim Ho Wan（添好運）","desc":"ミシュラン点心・カジュアルで名物多数","url":"https://www.timhowan.com/menu/"},
    {"name":"T’ang Court（唐閣）","desc":"The Langham内の高級広東料理","url":"https://www.langhamhotels.com/en/the-langham/hong-kong/dine/tang-court/"},
    {"name":"Mott 32","desc":"モダンチャイニーズ（人気店）","url":"https://mott32.com/"},
    {"name":"Ho Lee Fook","desc":"SOHOのカジュアル中華","url":"https://blacksheeprestaurants.com/restaurants/ho-lee-fook/"},
    {"name":"Grand Majestic Sichuan","desc":"四川料理の人気店","url":"https://blacksheeprestaurants.com/restaurants/grand-majestic-sichuan/"},
    {"name":"WING","desc":"創作中国料理","url":"https://wingrestaurant.hk/"},
    {"name":"Jean‑Pierre","desc":"（参考）フレンチ","url":"https://blacksheeprestaurants.com/restaurants/jean-pierre/"},
    {"name":"BELON","desc":"（参考）モダンフレンチ","url":"https://blacksheeprestaurants.com/restaurants/belon/"},
    {"name":"Associazione Chianti","desc":"（参考）トスカーナ料理","url":"https://blacksheeprestaurants.com/restaurants/associazione-chianti/"},
]

for r in restaurants:
    html_content += f"""
    <div class="item">
      <div class="meta"><div class="title">{r['name']}</div><div class="subtitle">{r['desc']}</div></div>
      <div class="actions"><a class="btn" href="{r['url']}" target="_blank" rel="noopener">公式</a></div>
    </div>
    """

# ホテルリストを追加
html_content += """
</div>
</section>

<section class="card">
<div class="section-title">
<h2>🏨 ホテル（おすすめ）</h2>
<span class="subtitle">家族向け・立地別に選べます</span>
</div>
<div class="list">
"""

hotels = [
    {"name":"The Mira Hong Kong","desc":"尖沙咀・買い物に便利","url":"https://www.themirahotel.com/hong-kong/en/"},
    {"name":"The Langham, Hong Kong","desc":"サービス充実の高級ホテル","url":"https://www.langhamhotels.com/en/the-langham/hong-kong/"},
    {"name":"Hong Kong Disneyland Hotel","desc":"ディズニー公式ホテル（子供に人気）","url":"https://www.hongkongdisneyland.com/hotels/"},
    {"name":"Rosewood Hong Kong","desc":"ラグジュアリー滞在","url":"https://www.rosewoodhotels.com/en/hong-kong"},
    {"name":"Four Seasons Hong Kong","desc":"中環・景色とスパが魅力","url":"https://www.fourseasons.com/hongkong/"},
    {"name":"Mandarin Oriental","desc":"伝統ある名門ホテル","url":"https://www.mandarinoriental.com/en/hong-kong/victoria-harbour"},
    {"name":"Kerry Hotel Hong Kong","desc":"ファミリー向け・海沿い","url":"https://www.shangri-la.com/en/hongkong/kerry/"},
    {"name":"The Royal Garden","desc":"プールあり・家族旅行向け","url":"https://www.rghk.com.hk/en/index.php"},
    {"name":"EAST Hong Kong","desc":"モダンでコスパ良し","url":"https://www.easthotels.com/en/hongkong/"},
    {"name":"Disney Explorers Lodge","desc":"ディズニー直営のもう一つの選択肢","url":"https://www.hongkongdisneyland.com/hotels/disney-explorers-lodge/"},
]

for h in hotels:
    html_content += f"""
    <div class="item">
      <div class="meta"><div class="title">{h['name']}</div><div class="subtitle">{h['desc']}</div></div>
      <div class="actions"><a class="btn" href="{h['url']}" target="_blank" rel="noopener">公式</a></div>
    </div>
    """

# HTML閉じタグ
html_content += """
</div>
</section>

<footer>
<div class="copy">このページは旅行の計画用メモです。サイトの内容や価格は変更される可能性があります。</div>
</footer>
</div>
</body>
</html>
"""

# Streamlit に埋め込む
st_html(html_content, height=2000, scrolling=True)
