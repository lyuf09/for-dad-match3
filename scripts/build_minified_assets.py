from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CSS_DIR = ROOT / 'assets' / 'css'
JS_DIR = ROOT / 'assets' / 'js'


def minify_css(text: str) -> str:
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s*([{}:;,>])\s*', r'\1', text)
    text = re.sub(r';}', '}', text)
    return text.strip() + '\n'


def minify_js(text: str) -> str:
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        lines.append(line)
    return ' '.join(lines).strip() + '\n'


def build_dir(source_dir: Path, suffix: str, minify):
    for path in source_dir.glob(f'*.{suffix}'):
        if path.name.endswith(f'.min.{suffix}'):
            continue
        out = path.with_name(path.stem + f'.min.{suffix}')
        out.write_text(minify(path.read_text()))
        print(f'Wrote {out.relative_to(ROOT)}')


if __name__ == '__main__':
    build_dir(CSS_DIR, 'css', minify_css)
    build_dir(JS_DIR, 'js', minify_js)
