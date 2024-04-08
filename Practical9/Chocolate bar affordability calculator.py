#define a function to calculate it
def calculator(total_money,price):
    number=total_money//price
    left=total_money%price
    return number, left

#example
total=184
bar=10
numbers,change = calculator(total,bar)
print(f'Bars:{numbers}, Change left over:{change}')