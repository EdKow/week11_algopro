class food():
    def __init__(self, foodname, pounds):
        self.__foodname = foodname
        self.__weight = pounds
        self.__standardprice = 0
        self.__calcprice = 0

    def __standprice(self, foodname, price):
        self.__standardprice = price
        if foodname == "Dry Cured Iberian Ham":
            price = 177.80
        elif foodname == "Wagyu Steaks":
            price = 450.00
        elif foodname == "Matsutake Mushrooms":
            price = 272.00
        elif foodname == "Kopi Luwak Coffee":
            price = 306.5
        elif foodname == "Moose Cheese":
            price = 487.20
        elif foodname == "White Truffles":
            price = 3600.00
        elif foodname == "Blue Fin Tuna":
            price = 3603.00
        elif foodname == "Le Bonnotte Potatoes":
            price = 270.81
        else:
            price:0.00
        
    def __calcprice(self):
        tot = self.__weight*self.__standardprice
        return tot
    

    def __str__(self):
        return (f"")