from PyQt5 import QtWidgets, uic
from Controllers import FurnitureController as FCC
class MyWindow(QtWidgets.QMainWindow):

    listOfFurniture = []

    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('ikea.UI', self)
        self.init()

    def init(self):
        global listOfFurniture
        listOfFurniture = FCC.IKEAController.getFurnitureName()

        for x in listOfFurniture:
            self.cbFurniture.addItem(x.getFurnitureName())

        self.twFurniture.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Item ID"))
        self.twFurniture.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Item Name"))
        self.twFurniture.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Item Price"))
        self.twFurniture.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Monthly Price"))
        self.twFurniture.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("Sellable Online"))
        self.twFurniture.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("Contract ID"))


        self.cbFurniture.currentIndexChanged.connect(self.furnitureSelected)

        self.funnitureSelected

    def furnitureSelected(self):
        cbFurnitureIndex = self.cbFurniture.currentIndex()
        selectedFurniture = listOfFurniture[cbFurnitureIndex]
        #furnitureID =selectedFurniture.getFurnitureID()
        customerID =selectedFurniture.getCustomerID()

        listOfCustomer = FCC.FurnitureController.getCustomer(customerID)


        self.twFurniture.setRowCount(2)
        for row_number, row_data in enumerate(listOfCustomer):
            self.twFurniture.insertRow(row_number)
            self.twFurniture.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data.getFurnitureID()))
            self.twFurniture.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data.getFurnitureName()))
            self.twFurniture.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data.getFurniturePrice()))
            self.twFurniture.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data.getContractType()))
            self.twFurniture.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data.getMonthlyPrice()))
            self.twFurniture.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data.getStatus()))
            self.twFurniture.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data.getContract()))

    def order(self):
        self.lb0rderStatus.hide()
        self.lb0rdered.show


    def main(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = MyWindow()
        window.show()
        sys.exit(app.exec_())

