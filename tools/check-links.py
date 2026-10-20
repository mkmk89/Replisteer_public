"""Checks the internal links of the built documentation site: every link and image must point to an existing file,
and every #anchor to an existing id on its page.

Usage: python3 tools/check-links.py docs/public [/Replisteer_public/]
The second argument is the path the site is served under (the path of its base URL).
Exits with 1 when a link is broken.
"""
import html
import os
import re
import sys
from urllib.parse import unquote, urljoin, urlparse


def main(root, base):
    pages = {}
    for directory, _, files in os.walk(root):
        for name in files:
            if name.endswith(".html"):
                path = os.path.join(directory, name)
                relative = os.path.relpath(path, root).replace(os.sep, "/")
                url = base + (relative[: -len("index.html")] if relative.endswith("index.html") else relative)
                with open(path, encoding="utf-8") as file:
                    pages[url] = file.read()

    ids = {url: set(re.findall(r'\bid="?([^"\s>]+)', content)) for url, content in pages.items()}
    problems, checked = set(), 0
    for url, content in pages.items():
        for match in re.finditer(r'\b(?:href|src)="?([^"\s>]+)', content):
            link = html.unescape(match.group(1))
            if link.startswith(("http://", "https://", "mailto:", "data:", "javascript:")):
                continue
            checked += 1
            target = urlparse(urljoin("https://site" + url, link))
            path = unquote(target.path)
            if not path.startswith(base):
                problems.add((url, link, "outside the site"))
                continue
            local = os.path.join(root, path[len(base):])
            if not (os.path.isfile(local) or os.path.isfile(os.path.join(local, "index.html"))):
                problems.add((url, link, "missing page or file"))
            elif target.fragment and path in ids and target.fragment not in ids[path]:
                problems.add((url, link, "missing anchor"))

    print(f"{len(pages)} pages, {checked} internal links, {len(problems)} broken")
    for page, link, reason in sorted(problems):
        print(f"  {page}: {link} ({reason})")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "/Replisteer_public/"))
