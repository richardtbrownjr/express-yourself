import re

def phone_numbers(pn):
    return re.findall(r'\(\d{3}\)[.-]?\s\d{3}[-.]?\d{4}', pn)
