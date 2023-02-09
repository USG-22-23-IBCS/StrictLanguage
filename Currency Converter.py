class Currency_Converter:

    def __init__(self):
        self.countries = ["1. Viet Nam",
                          "2. South Korea",
                          "3. Japan",
                          "4. Thailand",
                          "5. China",
                          "6. USA"]
    
        
        self.conversion_rate ={"VND" : 23500,
                               "Won" : 1263,
                               "Yen" : 131,
                               "Bath" : 33.5,
                               "Yuan" : 6.8,
                               "USD" : 1}
        
        self.countries_currencies = {"1" : "VND",
                                     "2" : "Won",
                                     "3" : "Yen",
                                     "4" : "Bath",
                                     "5" : "Yuan",
                                     "6" : "USD"}
        
        
        

    def getCountries(self):
        return self.countries
    
    def getConversionRate(self, country):
        currency = self.countries_currencies.get(country)
        conversionRate = self.conversion_rate.get(currency)
        return conversionRate
        
    def convertUSdollar(self, country, usdAmount):
        conversionRate = self.getConversionRate(country)
        finalAmount = usdAmount*conversionRate
        return finalAmount
    
    def convertCountriesCurrency(self, country1, country2, amount):
        conversionRate1 = self.getConversionRate(country1)
        conversionRate2 = self.getConversionRate(country2)
        conversionOfCountries = conversionRate2/conversionRate1
        finalAmount2 = amount*conversionOfCountries
        return finalAmount2
    
    def printMoney(self, country, amount):
        currency = self.countries_currencies.get(country)
        return str(amount) + " " + currency
   
        
def main():
    C = Currency_Converter()
    while True:
        print("Available countries currency to convert")
        print(*C.getCountries(), sep="\n")
        from_country = input("Please enter which country you want to convert money from\n")
        to_country = input("Please enter which country you want to convert money to\n")
        money = float(input("Please enter how much money you have\n"))
        print("...Calculating...")
        convertedAmount = C.convertCountriesCurrency(from_country, to_country, money)
        print("Here is your " + C.printMoney(to_country, convertedAmount))
        yesOrNo = input("Do you want to continue?\n Yes or No\n")
        if yesOrNo == "No" or "no":
            break
        
        
      
    












































if __name__ == "__main__":
    main()







































