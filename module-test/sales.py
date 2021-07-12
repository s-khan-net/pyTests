def cal_shipping(price, location):
    return price + location

def calc_tax(price):
    return price + (price % 0.18)