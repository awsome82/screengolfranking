import json
from datetime import datetime

with open("data.json", encoding="utf-8") as f:
    d = json.load(f)

MEDAL = {1: "🥇", 2: "🥈", 3: "🥉"}

def rows(items, show_count=False):
    html = ""
    for item in items:
        r    = item["rank"]
        name = item["name"]
        medal = MEDAL.get(r, f'<span class="rank-num">{r}</span>')
        extra = f'<span class="count">{item["count"]}회</span>' if show_count else ""
        html += f"""
        <tr>
          <td class="rank-cell">{medal}</td>
          <td class="name-cell">{name}</td>
          <td>{extra}</td>
        </tr>"""
    return html

def table_card(title, items, show_count=False):
    return f"""
    <div class="card">
      <div class="card-title">{title}</div>
      <table>
        <tbody>{rows(items, show_count)}</tbody>
      </table>
    </div>"""

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1a7f4b">
<title>⛳ {d['course']} 랭킹</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #f0f4f0;
    color: #1a1a1a;
    padding-bottom: 2rem;
  }}

  header {{
    background: linear-gradient(135deg, #1a7f4b, #2ecc71);
    color: white;
    padding: 1.2rem 1rem 1rem;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  }}

  header h1 {{ font-size: 1.2rem; font-weight: 700; }}
  header p  {{ font-size: 0.78rem; opacity: 0.85; margin-top: 0.2rem; }}

  .tabs {{
    display: flex;
    background: #fff;
    border-bottom: 2px solid #e0e0e0;
    position: sticky;
    top: 62px;
    z-index: 99;
    overflow-x: auto;
    scrollbar-width: none;
  }}
  .tabs::-webkit-scrollbar {{ display: none; }}

  .tab {{
    flex: 1;
    min-width: 80px;
    padding: 0.7rem 0.5rem;
    text-align: center;
    font-size: 0.82rem;
    font-weight: 600;
    color: #888;
    cursor: pointer;
    border-bottom: 3px solid transparent;
    white-space: nowrap;
    transition: all 0.2s;
  }}
  .tab.active {{
    color: #1a7f4b;
    border-bottom-color: #1a7f4b;
  }}

  .section {{ display: none; padding: 0.8rem; }}
  .section.active {{ display: block; }}

  .grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.7rem;
  }}

  .card {{
    background: #fff;
    border-radius: 14px;
    padding: 0.9rem 0.8rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
  }}

  .card-title {{
    font-size: 0.82rem;
    font-weight: 700;
    color: #1a7f4b;
    margin-bottom: 0.6rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid #e8f5e9;
  }}

  table {{ width: 100%; border-collapse: collapse; }}

  td {{
    padding: 0.35rem 0.2rem;
    font-size: 0.88rem;
    vertical-align: middle;
  }}

  .rank-cell {{ width: 28px; text-align: center; }}
  .rank-num  {{
    display: inline-block;
    width: 20px; height: 20px;
    background: #f0f0f0;
    border-radius: 50%;
    font-size: 0.72rem;
    font-weight: 700;
    line-height: 20px;
    text-align: center;
    color: #666;
  }}
  .name-cell {{ font-weight: 600; }}
  .count     {{ font-size: 0.78rem; color: #888; }}

  tr:not(:last-child) td {{
    border-bottom: 1px solid #f5f5f5;
  }}

  .stats {{
    display: flex;
    gap: 0.7rem;
    margin-bottom: 0.8rem;
  }}
  .stat-box {{
    flex: 1;
    background: #fff;
    border-radius: 12px;
    padding: 0.7rem;
    text-align: center;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
  }}
  .stat-val {{ font-size: 1.4rem; font-weight: 700; color: #1a7f4b; }}
  .stat-lbl {{ font-size: 0.72rem; color: #888; margin-top: 0.1rem; }}
</style>
</head>
<body>

<header>
  <h1>⛳ {d['course']} 랭킹</h1>
  <p>업데이트: {d['updated_at']} &nbsp;|&nbsp; {d['valid_rounds']}라운드 · {d['unique_players']}명</p>
</header>

<div class="tabs">
  <div class="tab active" onclick="show('general', this)">일반스코어</div>
  <div class="tab"        onclick="show('handicap', this)">핸디캡</div>
  <div class="tab"        onclick="show('played',   this)">최다플레이</div>
</div>

<div id="general" class="section active">
  <div class="grid">
    {table_card("🏌️ 남자 일반스코어 TOP12", d['general_M'])}
    {table_card("🏌️‍♀️ 여자 일반스코어 TOP12", d['general_F'])}
  </div>
</div>

<div id="handicap" class="section">
  <div class="grid">
    {table_card("🏌️ 남자 핸디캡 TOP12", d['handicap_M'])}
    {table_card("🏌️‍♀️ 여자 핸디캡 TOP12", d['handicap_F'])}
  </div>
</div>

<div id="played" class="section">
  <div class="stats">
    <div class="stat-box">
      <div class="stat-val">{d['valid_rounds']}</div>
      <div class="stat-lbl">총 라운드</div>
    </div>
    <div class="stat-box">
      <div class="stat-val">{d['unique_players']}</div>
      <div class="stat-lbl">참여 인원</div>
    </div>
  </div>
  <div class="grid">
    {table_card("🏌️ 남자 최다플레이 TOP10", d['played_M'], show_count=True)}
    {table_card("🏌️‍♀️ 여자 최다플레이 TOP10", d['played_F'], show_count=True)}
  </div>
</div>

<script>
  function show(id, el) {{
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    el.classList.add('active');
  }}
</script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html 생성 완료")
