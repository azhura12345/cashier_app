# ui/product_ui.py

from PyQt5 import QtCore, QtWidgets

class Ui_layoutProduct(object):
    def setupUi(self, layoutProduct):
        layoutProduct.setObjectName("layoutProduct")
        layoutProduct.resize(800, 600)

        self.verticalLayout = QtWidgets.QVBoxLayout(layoutProduct)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        # Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(layoutProduct)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # Widget konten scroll
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # Grid layout untuk produk
        self.productLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.productLayout.setContentsMargins(10, 10, 10, 10)
        self.productLayout.setSpacing(15)
        self.productLayout.setObjectName("productLayout")

        # Set widget konten ke scroll area
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Tambahkan scroll area ke layout utama
        self.verticalLayout.addWidget(self.scrollArea)