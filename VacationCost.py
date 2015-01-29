
# Taking a Vacation 
# Computate the cost 

# hotel cost(assume $40/night)
def hotel_cost(nights):
	 return 40 * nights

# flight cost
def flight_cost(city):
	if city == "Charlotte":
		return 183

	elif city == "Tampa":
		return 220

	elif city == "Pittsburgh":
		return 222

	elif city == "Los Angeles":
		return 475

# car rental cost
def car_rental_cost(days):
	if days >= 7:
		return 40*days-50
	elif days >= 3 and days < 7:
		return 40*days-20
	else:
		return 40*days

#total cost
def trip_cost(city,days,spending_money):
	 return car_rental_cost(days)+hotel_cost(days)+flight_cost(city)+spending_money


# calculate your vacation cost
trip_city = raw_input("choose your trip city(Charlotte, Tampa, Pittsburgh or Los Angeles) :")
trip_days = raw_input("how many days you are going to stay?")
trip_length = int(trip_days)
money = raw_input("how much money you plan to spent during this trip :)")
money = int(money)
totalCost = trip_cost(trip_city, trip_length,money)
print "The total cost of your lovely trip will be %s, Bon Voyage & Happy Shopping! " %totalCost


