# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.

items_purchase = {
	"Apple": "$4",
	"Honey": "$3",
	"Fan": "$14",
	"Bananas": "$4",
	"Pan": "$100",
	"Spoon": "$2"
}

wallet = '$100'
money = int(wallet[1:])
# print(money)

can_afford = []

for item in items_purchase:
	price = int(items_purchase[item][1:])
	if price <= money:
		can_afford.append(item)

# Sort the list in alphabetical order. Return “Nothing” if you can’t afford anything from the store.

can_afford.sort()

print(can_afford if can_afford else 'Nothing')