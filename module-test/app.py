# from sales import calc_tax, cal_shipping
#same as from sales import * but not good
import sales
import sys

#used by method import only 
# print(calc_tax(1000))
# print(cal_shipping(1000, 420))

print(sales.cal_shipping(1000, 420))
print(sales.calc_tax(1000))

print("python searches these directories for finding the module ->")
print(sys.path)
