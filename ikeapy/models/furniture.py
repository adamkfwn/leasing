class Furniture():
#møbel constructor
    def __init__(self, furniture_id, furniture_name, furniture_price, monthly_price, Sellable_online, contract_id):
        self.__furniture_id = furniture_id
        self.__furniture_name = furniture_name
        self.__furniture_price = furniture_price
        self.__monthly_price = monthly_price
        self.__Sellable_online = Sellable_online
        self.__contract_id = contract_id
#setter til møbel navn
    def setFurnitureName(self, furniture_name):
        self.__furniture_name = furniture_name

#møbel tabel- getters

    def getFurnitureID(self):
        return self.__furniture_id

    def getFurnitureName(self):
        return self.__furniture_name

    def getFurniturePrice(self):
        return self.__furniture_price

    def getContractType(self):
        return self.__contract_type

    def getMonthlyPrice(self):
        return self.__monthly_price

    def getStatus(self):
        return self.__Sellable_online

    def getContract(self):
        return self.__contract_id




