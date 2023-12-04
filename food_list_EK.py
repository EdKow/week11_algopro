class food():
    def __init__(self, foodname, pounds):
        self.__foodname = foodname
        self.__weight = pounds
        self.__standpriceEK()
        self.__calcpriceEK()

    def GetnameEK(self):
        return self.__foodname
    def GetweightEK(self):
        return self.__weight
    def GetcalcpriceEK(self):
        return self.__calcedprice
    def GetstandardpriceEK(self):
        return self.__standardprice
    def __standpriceEK(self):
        foodname = self.__foodname.lower()
        
        if foodname == "dry cured iberian ham":
            self.__standardprice = 177.80
        elif foodname == "wagyu steaks":
            self.__standardprice = 450.00
        elif foodname == "matsutake mushrooms":
            self.__standardprice = 272.00
        elif foodname == "kopi luwak coffee":
            self.__standardprice = 306.5
        elif foodname == "moose cheese":
            self.__standardprice = 487.20
        elif foodname == "white truffles":
            self.__standardprice = 3600.00
        elif foodname == "blue fin tuna":
            self.__standardprice = 3603.00
        elif foodname == "le bonnotte potatoes":
            self.__standardprice = 270.81
        else:
            self.__standardprice:0.00
        
    def __calcpriceEK(self):
        self.__calcedprice = self.__weight*self.__standardprice
        return self.__calcedprice
