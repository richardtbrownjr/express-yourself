import re


def binary(s):
    return re.search(r'^[01]+$', s)


def binary_even(s):
    return re.search(r'[01]+0$', s)


def hex(s):
    # return re.search(r'^\b[0-9A-F]+\b', s)
    return re.search(r'^[A-Fa-f0-9]+$', s)


def word(w):
    return re.match(r'^\w*[-]*[a-z]+$', w)


def words(w, count=None):
    x = re.findall(r'[\w-]+[a-zA-Z]+', w)
    if count is not None:
        return len(x) == count
    else:
        return len(x) > 0


def phone_number(pn):
    return re.search(r"\(?(\d{3})\)?[-.]?\s*(\d{3})[-.]?(\d{4})", pn)


def money(mo):

    #return re.match(r'^\$([0-9]{1,3})(,?[0-9]{3})*(\.[0-9){2})?$', mo)
    return re.search(r'^\$[0-9]{1,3}(?:,?[0-9]{3})*(?:\.[0-9]{2})?$', mo)



def zipcode(zp):
    return re.search(r"^(^\d{5}-\d{4})|(^\d{5})+$", zp)
    # return re.search(r'^(^\d{5}-\d{4})|(^\d{5})+$', string)

def date(gametime):
    # return( [r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4}|\d{2})",
    #               r"(?P<year>\d{4})-?(?P<month>\d{2})-?(?P<day>\d{2})",
    #               r"(?P<day>\d{1,2})\s*(?P<month>[A-Za-z]{3})\s*(?P<year>\d{4})",
    #               r"(?P<month>[A-Za-z]{3})\s*(?P<day>\d{1,2})\s*,?\s*(?P<year>\d{4})"], gametime)
    return re.match(r'[0-9]{1,4}[\/-][0-9]{1,2}[\/-][0-9]{2,4}', gametime)
