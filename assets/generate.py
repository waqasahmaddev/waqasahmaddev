"""Builds the profile images (banner + 3 link cards) as self-contained SVGs.

Usage:  python assets/generate.py <geist.woff2> <jetbrains-mono.woff2>

The fonts are embedded as data URIs, because an SVG shown through <img> cannot load
files from the network. Nothing here calls a third-party service.
"""
import base64
import pathlib
import sys

geist_path, mono_path = sys.argv[1], sys.argv[2]
out = pathlib.Path(__file__).parent


def b64(path):
    return base64.b64encode(pathlib.Path(path).read_bytes()).decode()


GEIST = b64(geist_path)
MONO = b64(mono_path)

BG, PANEL, LINE, LINE2 = '#0b0e13', '#0e1218', '#1d232d', '#2a313c'
INK, INK2, DIM, FAINT = '#e6eaf0', '#a3adbc', '#7c8696', '#4c5563'
MINT, CORAL, CORAL_INK, BLUE, BLUE_INK = '#3ee6b4', '#ff7a59', '#1a0c07', '#7aa2ff', '#0a1230'

FONTS = f"""
@font-face{{font-family:G;src:url(data:font/woff2;base64,{GEIST}) format('woff2');font-weight:100 900}}
@font-face{{font-family:M;src:url(data:font/woff2;base64,{MONO}) format('woff2');font-weight:100 800}}
.m{{font-family:M,ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
.g{{font-family:G,'Segoe UI',Helvetica,Arial,sans-serif}}
"""


def banner():
    lines = []

    def line(n, y, delay, body):
        lines.append(
            f'<g class="l" style="animation-delay:{delay}s">'
            f'<text class="m" x="60" y="{y}" font-size="22" fill="{FAINT}">{n}</text>{body}</g>'
        )

    q = '&quot;'
    key = lambda k: f'<tspan fill="{DIM}">{q}{k}{q}:</tspan>'
    sval = lambda v: f'<tspan fill="{MINT}">{q}{v}{q}</tspan>'
    punc = lambda p: f'<tspan fill="{INK2}">{p}</tspan>'

    line(1, 150, 0.1, f'<text class="m" x="110" y="150" font-size="26" fill="{INK2}">{{</text>')
    line(2, 214, 0.35,
         f'<text class="m" x="146" y="214" font-size="26">{key("name")}'
         f'<tspan class="g" font-size="64" font-weight="800" fill="{INK}" letter-spacing="-2" dx="14">'
         f'<tspan fill="{FAINT}">{q}</tspan>Waqas Ahmad<tspan fill="{FAINT}">{q}</tspan></tspan></text>')
    line(3, 266, 0.6,
         f'<text class="m" x="146" y="266" font-size="26">{key("role")} {sval("Software Engineer")}{punc(",")}</text>')
    line(4, 306, 0.85,
         f'<text class="m" x="146" y="306" font-size="26">{key("builds")} {punc("[")}{sval("backend systems")}{punc(",")} '
         f'{sval("web apps")}{punc(",")} {sval("dev tools")}{punc("],")}</text>')
    line(5, 346, 1.1,
         f'<text class="m" x="146" y="346" font-size="26">{key("experience")} {sval("10+ years, mostly .NET")}</text>')
    line(6, 386, 1.35,
         f'<text class="m" x="110" y="386" font-size="26" fill="{INK2}">}}</text>'
         f'<rect class="cur" x="134" y="366" width="13" height="26" fill="{MINT}"/>')

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="430" viewBox="0 0 1200 430" role="img" aria-label="GET /waqas 200 OK. Waqas Ahmad, Software Engineer. Builds backend systems, web apps and dev tools. 10+ years, mostly .NET.">
<style>{FONTS}
.l{{animation:in .4s ease-out backwards}}
@keyframes in{{from{{opacity:0;transform:translateX(-10px)}}to{{opacity:1;transform:none}}}}
.cur{{animation:blink 1.1s steps(1) 1.8s infinite}}
@keyframes blink{{50%{{opacity:0}}}}
.dot{{animation:pulse 2.4s ease-in-out infinite}}
@keyframes pulse{{50%{{opacity:.45}}}}
@media (prefers-reduced-motion:reduce){{.l,.cur,.dot{{animation:none}}}}
</style>
<defs>
<pattern id="d" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{LINE}"/></pattern>
<radialGradient id="glow" cx="1100" cy="30" r="460" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{MINT}" stop-opacity=".16"/><stop offset="1" stop-color="{MINT}" stop-opacity="0"/></radialGradient>
</defs>
<rect x=".5" y=".5" width="1199" height="429" rx="18" fill="{BG}" stroke="{LINE}"/>
<rect x=".5" y=".5" width="1199" height="429" rx="18" fill="url(#d)"/>
<rect x=".5" y=".5" width="1199" height="429" rx="18" fill="url(#glow)"/>
<rect x="48" y="36" width="318" height="44" rx="11" fill="{PANEL}" stroke="{LINE2}"/>
<rect x="58" y="46" width="56" height="24" rx="6" fill="{CORAL}"/>
<text class="m" x="86" y="63" font-size="15" font-weight="700" fill="{CORAL_INK}" text-anchor="middle">GET</text>
<text class="m" x="128" y="64" font-size="19" fill="{INK}">/waqas</text>
<text class="m" x="236" y="64" font-size="19" fill="{MINT}">200 OK</text>
<circle class="dot" cx="928" cy="58" r="12" fill="{MINT}" fill-opacity=".14"/>
<circle cx="928" cy="58" r="6" fill="{MINT}"/>
<text class="m" x="1152" y="65" font-size="20" fill="{INK2}" text-anchor="end">waqasahmaddev.com</text>
{''.join(lines)}
</svg>
"""


def card(name, verb, title, sub):
    badge_fill, badge_ink = (CORAL, CORAL_INK) if verb == 'GET' else (BLUE, BLUE_INK)
    badge_w = 56 if verb == 'GET' else 66
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="400" height="132" viewBox="0 0 400 132" role="img" aria-label="{verb} {title}. {sub}">
<style>{FONTS}
.c{{transition:none}}
</style>
<defs><pattern id="d" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{LINE}"/></pattern></defs>
<rect x=".5" y=".5" width="399" height="131" rx="16" fill="{BG}" stroke="{LINE2}"/>
<rect x=".5" y=".5" width="399" height="131" rx="16" fill="url(#d)"/>
<rect x="24" y="24" width="{badge_w}" height="24" rx="6" fill="{badge_fill}"/>
<text class="m" x="{24 + badge_w / 2}" y="41" font-size="14" font-weight="700" fill="{badge_ink}" text-anchor="middle">{verb}</text>
<text class="m" x="{24 + badge_w + 14}" y="42" font-size="16" fill="{MINT}">200 OK</text>
<path d="M352 42 L370 24 M356 24 H370 V38" fill="none" stroke="{INK2}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
<text class="m" x="24" y="88" font-size="24" font-weight="700" fill="{INK}">{title}</text>
<text class="m" x="24" y="112" font-size="15" fill="{DIM}">{sub}</text>
</svg>
"""


(out / 'banner.svg').write_text(banner(), encoding='utf-8')
(out / 'card-site.svg').write_text(card('site', 'GET', 'waqasahmaddev.com', 'my website'), encoding='utf-8')
(out / 'card-posts.svg').write_text(card('posts', 'GET', '/posts', 'notes on .NET and system design'), encoding='utf-8')
(out / 'card-contact.svg').write_text(card('contact', 'POST', '/contact', 'hello@waqasahmaddev.com'), encoding='utf-8')
for f in sorted(out.glob('*.svg')):
    print(f.name, f.stat().st_size, 'bytes')
