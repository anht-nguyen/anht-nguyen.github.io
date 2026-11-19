"""Check local page links, fragments, and assets after a Jekyll build (stdlib only)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])


root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
pages = {p: Document(p.read_text(encoding="utf-8")) for p in root.rglob("*.html")}
errors = []
if not pages:
    errors.append("No generated HTML found. Run the Jekyll build first.")
for source, document in pages.items():
    for link in document.links:
        url = urlsplit(link)
        # Academic Pages also emits absolute links to this site's own domain.
        if (url.scheme or url.netloc) and url.netloc != "anht-nguyen.github.io":
            continue
        path = unquote(url.path)
        target = ((root / path.lstrip("/")) if path.startswith("/") else (source.parent / path)).resolve() if path else source
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            errors.append(f"{source.relative_to(root)}: missing {link}")
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f"{source.relative_to(root)}: missing fragment {link}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Checked internal links, fragments, and assets across {len(pages)} HTML pages.")
