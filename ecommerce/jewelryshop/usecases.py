from store.models import Product


WISH_LIST = 'wish-list'
VIEWED_BOOKS = 'viewed-books'
BOOK_IDS = "book_ids"


SECOND = 1
MINUTE = SECOND * 60
HOUR = MINUTE * 60

SHORT_WAIT = SECOND * 3
VERY_LONG_WAIT = MINUTE * 10

SHORT_CACHING_TIME = MINUTE * 30
LONG_CACHING_TIME = HOUR * 2


def testpermission(user, product_id: int = None) -> bool:
    if user.is_authenticated:

        if product_id:
            if product := Product.objects.filter(id=product_id).first():
                if user == product.category:
                    return True
            return False
        else:
            return True
    else:
        return False
    
