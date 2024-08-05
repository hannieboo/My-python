def prod(n):
    sum_price = 0
    for i in range(n):
        price = int(input(f"ราคาสินค้า{i+1}:"))
        sum_price += price
    return sum_price

def tax(total):
    vat = (7/100)*total
    return vat

def change(money,net_price):
    c = money - net_price
    return c 

num = int(input("จำนวนรายการสินค้า:"))
total = prod(num)
print(f"ราคารวม { total }") 
print(f"ภาษีมูลค่าเพิ่ม {tax(total)}")
net_price = total + tax(total)
print("รวมเป็นเงินทั้งสิ้น %.2f"% net_price)
money = int(input("จำนวนเงิน:"))
print("เงินทอน %.2f" % (change(money, net_price)))