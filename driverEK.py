from food_list_EK import food

def flist():
    food_list = list()
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


flist()

