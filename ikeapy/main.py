from PyQt5 import QtWidgets, uic
from Controllers import FurnitureController as FCC
class MyWindow(QtWidgets.QMainWindow):

    listOfFurniture = []

    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('ikea.UI', self)
        self.run()

    def init(self):
        global listOfFurniture
        listOfFurniture = FCC.IKEAController.getCustomer()

        for x in listOfFurniture:
            self.twFurniture.addItem(x.getFurnitureName())

        #mangler self


 #   def furnitureSelected(self):
  #      try:

   # def order(self):

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()