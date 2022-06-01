import DBConnection as DB
from models import furniture as FPY
from models import customer as CPY

class IKEAController():

    @staticmethod
    def getFurnitureName():
        try:
            listOfFurniture = []

            conn = DB.DBConnection.getConnection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM ikea.furniture")
            for row in cur:
                furniturename= FPY.Furniture(row[0], row[1]) #furniture_id, furniture_name
                listOfFurniture.append(furniturename)
            return listOfFurniture
        except Exception as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def getCustomer(customerID):
        try:
            listOfCustomer = []

            conn = DB.DBConnection.getConnection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM ikea.customer WHERE customerID = %s", (customerID))
            for row in cur:
                customers = CPY.customer(row[0], row[1],row[2],row[3]) #customer_id, customer_name, customer_address, customer_phonenr
                listOfCustomer.append(customers)
            return listOfCustomer
        except Exception as e:
            print(e)
        finally:
            conn.close()