import os
from datetime import datetime

SITE_URL = "https://cardsnark.cc"
EXTENSIONS = {".html"}  # add .xml, .css, .js etc if needed

def find_files(base):
    for root, dirs, files in os.walk(base):
        for name in files:
            if os.path.splitext(name)[-1].lower() in EXTENSIONS:
                path = os.path.join(root, name)
                yield os.path.relpath(path, base).replace("\\", "/")

def lastmod(filepath):
    dt = datetime.utcfromtimestamp(os.path.getmtime(filepath))
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def make_sitemap(output="sitemap.xml"):
    here = os.getcwd()
    urls = []
    for file_path in find_files(here):
        file_url = f"{SITE_URL}/{file_path.lstrip('./')}".replace("//", "/")
        file_url = file_url.replace(":/", "://")  # correct double slash
        if file_url.endswith("404.html"):  # skip error pages
            continue
        mod = lastmod(file_path)
        urls.append(f"""  <url>
    <loc>{file_url}</loc>
    <lastmod>{mod}</lastmod>
  </url>""")
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>
'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'
        + "
".join(urls) +
        '
</urlset>
'
    )
    with open(output, "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"Sitemap written to {output}")

if __name__ == "__main__":
    make_sitemap()
