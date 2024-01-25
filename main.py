from bs4 import BeautifulSoup

SIMPLE_HTML = """<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolar. lorem Consesteur edipsum</p>
<p>another p without class</p>
<p>sdfjhdsfksdhf</p>
<ul>
<li>Rolf</li>
<li>Charlie</li>
<li>Jen</li>
<li>Jose</li>
</ul>
</body>
</html>
"""

simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")


def find_title():
    print(simple_soup.find("h1"))
    print(simple_soup.find("h1").string)


def find_list_items():
    list_item = [item.string for item in simple_soup.find_all("li")]
    print(list_item)


def find_subtitle():
    paragraph = simple_soup.find("p", {"class": "subtitle"})
    print(paragraph.string)


def find_other_parag():
    paragraphs = simple_soup.find_all("p")
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get("class", [])]
    print(other_paragraph)


find_title()
find_list_items()
find_subtitle()
find_other_parag()
