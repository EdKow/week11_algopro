from food_list_EK import food

def flist():
    food_list = []
    while True:
        amount = int(input("How many Items will you order today? "))
        if amount <= 0:
            print("Number of items must be at least 1.")
            amount = int(input("How many Items will you order today? "))
        elif amount >= 1:
            break
    
    itemnum = 0
    for x in range(amount):
        itemnum += 1
        print (f"item #{itemnum}-")
        foodname = input("Enter food: ")
        pounds = int(input("Enter amount of pounds: "))
    food_list.append(food(foodname, pounds))
    return food_list



def displaylist(list):
    for x in list:
        print("Here is the summary of the items purchased.")

        print("---------------------------------------")

        print(f"item: {x.Getname()}")

        print(f"amount: {x.Getweight()}")

        print(f"Price Per Pound: {x.Getstandardprice()}")

        print(f"Price of order: {x.Getcalcprice()}")

def totalcost(list):
    total = []
    for item in list:
        total.append(item.Getcalcprice())
    return sum(total)


def main():
    list = flist()
    displaylist(list)
    return totalcost(list)


print(f"Total Cost: {main()}")



