import re

from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''


class ParseItemLocator:

    NAME_LOCATOR = "article.product_pod h3 a"
    PRICE_LOCATOR = "article.product_pod p.price_color"
    RATING_LOCATOR = "article.product_pod p.star-rating"


class ParsedItem:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def name(self):
        locator = ParseItemLocator.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs["href"]
        return item_name

    @property
    def price(self):
        locator = ParseItemLocator.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        print(matcher.group(0))
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = ParseItemLocator.RATING_LOCATOR
        start_rating_tag = self.soup.select_one(locator)
        classes = start_rating_tag.attrs["class"]
        rating_classes = [r for r in classes if r != "star-rating"]
        return rating_classes[0]


item = ParsedItem(ITEM_HTML)

print(item.name)
print(item.price)
print(item.rating)

