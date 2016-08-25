import re


def words(string):
    check_word = re.findall(r'\b(?:[A-Za-z]*|[0-9]*)-?[A-Za-z]+\b', string)
    if len(check_word) == 0:
        return None
    else:
        return check_word

def phone_number(phone_nu):
    try:
        check_numbers = re.search(r'\(*([\d]{3})\)*[-\s\.]*([\d]{3})[-\s\.]*([\d]{4})', phone_nu).groups()
        phone_dict = {}
        phone_dict['area_code'] = check_numbers[0]
        phone_dict['number'] = check_numbers[1]+'-'+check_numbers[2]
        return phone_dict
    except:
        return None


def money(mo):
    try:
        check_money = re.search(r'^(\$)([0-9]{1,3}(?:,?[0-9]{3})*(?:\.[0-9]{2})?)$', mo).groups()
        money_dict = {}
        money_dict['currency'] = check_money[0]
        dmoney = check_money[1].replace(',', '')
        money_dict['amount'] = float(dmoney)
        return money_dict
    except:
        return None


def zipcode(zipe):
    try:
        check_zip = re.search(r"^(\d{5})\-?(\d{4})?$", zipe).groups()
        zip_dict = {}
        zip_dict['plus4'] = check_zip[1]
        zip_dict['zip'] = check_zip[0]
        return zip_dict
    except:
        return None

def date(date1):
    try:
        check_date = re.match(r'([0-9]{1,4})[\/-]([0-9]{1,2})[\/-]([0-9]{1,4})', date1).groups()
        date = {}
        if len(check_date[0]) == 4:
            date['year'] = int(check_date[0])
            date['month'] = int(check_date[1].lstrip("0"))
            date['day'] = int(check_date[2].lstrip("0"))
        else:
            date['year'] = int(check_date[2])
            date['month'] = int(check_date[0].lstrip("0"))
            date['day'] = int(check_date[1].lstrip("0"))
        return date
    except:
        return None
