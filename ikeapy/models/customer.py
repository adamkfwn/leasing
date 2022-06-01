class Customer():
    def __init__(self, customer_id, customer_name, customer_address, customer_phonenr):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__customer_address = customer_address
        self.__customer_phonenr = customer_phonenr

    #customer tabel Getters:
    def getCustomerID(self):
        return self.__customer_id

    def getCustomerName(self):
        return self.__customer_name

    def getCustomerADD(self):
        return self.__customer_address

    def getCustomerTLF(self):
        return self.__customer_phonenr