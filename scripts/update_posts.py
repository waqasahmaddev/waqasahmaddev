"""Writes the latest posts from my own API into README.md.

Usage:  python scripts/update_posts.py <posts.json> <README.md> [limit]

The README must contain the markers <!-- POSTS:START --> and <!-- POSTS:END -->.
If the JSON is missing, empty or broken, the README is left untouched.
"""
import json
import pathlib
import re
import sys

START, END = '<!-- POSTS:START -->', '<!-- POSTS:END -->'

posts_file, readme_file = sys.argv[1], sys.argv[2]
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 3

try:
    posts = json.loads(pathlib.Path(posts_file).read_text(encoding='utf-8'))
except (OSError, ValueError) as error:
    print(f'Could not read posts: {error}')
    sys.exit(0)

if not isinstance(posts, list) or not posts:
    print('No posts found, README left as it is.')
    sys.exit(0)

rows = []
for post in posts[:limit]:
    title, url = post.get('title'), post.get('url')
    if not title or not url or not url.startswith('https://waqasahmaddev.com/'):
        continue
    rows.append(f"- **[{title}]({url})**  \n  <sub>{post.get('date', '')} · {post.get('minutes', '?')} min read</sub>")

if not rows:
    print('No usable posts, README left as it is.')
    sys.exit(0)

readme = pathlib.Path(readme_file)
text = readme.read_bytes().decode('utf-8').replace('\r\n', '\n')
pattern = re.compile(re.escape(START) + r'.*?' + re.escape(END), re.S)
if not pattern.search(text):
    print('Markers not found in README.')
    sys.exit(1)

block = START + '\n' + '\n'.join(rows) + '\n' + END
readme.write_text(pattern.sub(lambda _: block, text), encoding='utf-8', newline='\n')
print(f'Updated {len(rows)} posts.')
