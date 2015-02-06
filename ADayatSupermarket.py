
# A Day at Supermarket
# 1) check the inventory
prices = {"banana":4, "apple":2,"orange":1.5,"pear":3}
stock = {"banana":6, "apple":0,"orange":32,"pear":15}

'''
print list as following format:
apple
price: 2
stock: 0
'''
print "The inventory list:"
for key in prices:
	print key
	print "price: %s" %prices[key]
	print "stock: %s" %stock[key]

# calculate total value of the inventory
total_value = 0
for item in prices:
    total_value += prices[item]*stock[item]
print "Total vale of the inventory is: %s" %total_value

# 2) Go for a shopping
# shop list
shopping_list = ["banana", "orange", "apple"]

# make a purchase and check out
def pay_bill(food):
	bill=0
	for shop_item in food:
		if stock[shop_item]>0:
			bill += prices[shop_item]
			stock[shop_item]-=1
	return bill

print "The shopping bill is: %s" %pay_bill(shopping_list)

