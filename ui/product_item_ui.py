# /cashier_app/ui/product_item_ui.py

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProductItem(object):
    def setupUi(self, ProductItem):
        ProductItem.setObjectName("ProductItem")
        ProductItem.resize(200, 300)

        self.verticalLayout = QtWidgets.QVBoxLayout(ProductItem)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame = QtWidgets.QFrame(ProductItem)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("""
            QFrame#frame {
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: white;
            }
        """)

        self.frameLayout = QtWidgets.QVBoxLayout(self.frame)
        self.frameLayout.setObjectName("frameLayout")

        self.imagePrd = QtWidgets.QLabel(self.frame)
        self.imagePrd.setFixedSize(120, 120)
        self.imagePrd.setScaledContents(True)
        self.frameLayout.addWidget(self.imagePrd, alignment=QtCore.Qt.AlignCenter)

        self.namePrdLabel = QtWidgets.QLabel("Product Name", self.frame)
        self.namePrdLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.frameLayout.addWidget(self.namePrdLabel)

        self.priceLabelItem = QtWidgets.QLabel("$0.00", self.frame)
        self.priceLabelItem.setAlignment(QtCore.Qt.AlignCenter)
        self.frameLayout.addWidget(self.priceLabelItem)

        self.discLabelItem = QtWidgets.QLabel("$0.00", self.frame)
        self.discLabelItem.setAlignment(QtCore.Qt.AlignCenter)
        self.discLabelItem.setStyleSheet("color: red; text-decoration: line-through;")
        self.frameLayout.addWidget(self.discLabelItem)

        self.inStockLabel = QtWidgets.QLabel("In Stock", self.frame)
        self.inStockLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.frameLayout.addWidget(self.inStockLabel)

        # Tambahan ini ⬇️
        self.sizeFrame = QtWidgets.QFrame(self.frame)
        self.sizeFrame.setObjectName("sizeFrame")
        self.sizeLayout = QtWidgets.QHBoxLayout(self.sizeFrame)
        self.sizeLayout.setContentsMargins(0, 0, 0, 0)
        self.sizeLayout.setSpacing(5)

        self.wLabel = QtWidgets.QLabel("W : --", self.sizeFrame)
        self.dLabel = QtWidgets.QLabel("D : --", self.sizeFrame)
        self.hLabel = QtWidgets.QLabel("H : --", self.sizeFrame)

        self.sizeLayout.addWidget(self.wLabel)
        self.sizeLayout.addWidget(self.dLabel)
        self.sizeLayout.addWidget(self.hLabel)

        self.frameLayout.addWidget(self.sizeFrame)
        # ⬆️ Tambahan selesai

        self.addCartButton = QtWidgets.QPushButton("Add to Cart", self.frame)
        self.frameLayout.addWidget(self.addCartButton)

        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(ProductItem)
        QtCore.QMetaObject.connectSlotsByName(ProductItem)

    def retranslateUi(self, ProductItem):
        _translate = QtCore.QCoreApplication.translate
        ProductItem.setWindowTitle(_translate("ProductItem", "Product Item"))
