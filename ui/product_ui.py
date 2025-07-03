# /cashier_app/ui/product_ui.py
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_layoutProduct(object):
    def setupUi(self, layoutProduct):
        layoutProduct.setObjectName("layoutProduct")
        layoutProduct.resize(368, 336)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(layoutProduct)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(layoutProduct)
        self.widget.setStyleSheet("*{\n"
"    background-color:#ffffff;\n"
"    font-family:Segoe UI;\n"
"}\n"
"\n"
"#frameProduct{\n"
"    border-radius: 10px;\n"
"    border:1px solid #dee2e6;\n"
"    box-shadow:0px 4px 8px rgba(0,0,0,0.1);\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"/* Frame Utama Produk */\n"
"#productItem {\n"
"    background-color: #ffffff;\n"
"    \n"
"}\n"
"\n"
"/* Harga Setelah Diskon */\n"
"#discLabelItem {\n"
"    color: #d32f2f;\n"
"    text-decoration: line-through;\n"
"    font-weight: bold;\n"
"    font-size:15px;\n"
"}\n"
"\n"
"#priceLabelItem {\n"
"    font-size:15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Label Ukuran (W, D, H) */\n"
"#sizeFrame QLabel {\n"
"    font-size: 9pt;\n"
"    color: #666666;\n"
"    border:1px solid #dee2e6;\n"
"    background-color:#f8f9fa;\n"
"    border-radius:3px;\n"
"}\n"
"\n"
"/* Button Tambah ke Keranjang */\n"
"#addCartButton {\n"
"    background-color: #212529;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"}\n"
"#addCartButton:pressed {\n"
"    background-color: #495057;\n"
"}\n"
"\n"
"#inStockFrame {\n"
"    background-color: rgba(70,125,78,0.3);\n"
"    min-height:25px;\n"
"    border-radius:5px;\n"
"    border: none;\n"
"}\n"
"#inStockLabel,#inStockIcon{\n"
"    background-color: rgba(70,125,78,0.0);\n"
"}\n"
"\n"
"/* Label \"Out of Stock\" (kalau ada) */\n"
"#stockOffLabel,#stockOffLabelDisc {\n"
"    color: red;\n"
"    font-weight: bold;\n"
"    min-height:20px;\n"
"    padding:1px;\n"
"    border-radius:5px;\n"
"    background-color:rgba(220, 53, 69,0.3);\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameProduct = QtWidgets.QFrame(self.widget)
        self.frameProduct.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameProduct.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameProduct.setObjectName("frameProduct")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameProduct)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.productItem = QtWidgets.QFrame(self.frameProduct)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productItem.sizePolicy().hasHeightForWidth())
        self.productItem.setSizePolicy(sizePolicy)
        self.productItem.setMinimumSize(QtCore.QSize(0, 0))
        self.productItem.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.productItem.setFont(font)
        self.productItem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.productItem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.productItem.setObjectName("productItem")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.productItem)
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.stockOffFrame = QtWidgets.QFrame(self.productItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockOffFrame.sizePolicy().hasHeightForWidth())
        self.stockOffFrame.setSizePolicy(sizePolicy)
        self.stockOffFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stockOffFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stockOffFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stockOffFrame.setObjectName("stockOffFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.stockOffFrame)
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stockOffLabelDisc = QtWidgets.QLabel(self.stockOffFrame)
        self.stockOffLabelDisc.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.stockOffLabelDisc.setFont(font)
        self.stockOffLabelDisc.setObjectName("stockOffLabelDisc")
        self.horizontalLayout_5.addWidget(self.stockOffLabelDisc)
        self.stockOffLabel = QtWidgets.QLabel(self.stockOffFrame)
        self.stockOffLabel.setObjectName("stockOffLabel")
        self.horizontalLayout_5.addWidget(self.stockOffLabel)
        self.verticalLayout_20.addWidget(self.stockOffFrame)
        self.prdItemFrame = QtWidgets.QFrame(self.productItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prdItemFrame.sizePolicy().hasHeightForWidth())
        self.prdItemFrame.setSizePolicy(sizePolicy)
        self.prdItemFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.prdItemFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prdItemFrame.setObjectName("prdItemFrame")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.prdItemFrame)
        self.gridLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.namePrdLabel = QtWidgets.QLabel(self.prdItemFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.namePrdLabel.setFont(font)
        self.namePrdLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.namePrdLabel.setObjectName("namePrdLabel")
        self.gridLayout_14.addWidget(self.namePrdLabel, 3, 0, 1, 1)
        self.imagePrd = QtWidgets.QLabel(self.prdItemFrame)
        self.imagePrd.setMaximumSize(QtCore.QSize(120, 120))
        self.imagePrd.setText("")
        self.imagePrd.setPixmap(QtGui.QPixmap("../../PyhtonTraining/cashier_app/PyQt/images/office chair.jpg"))
        self.imagePrd.setScaledContents(True)
        self.imagePrd.setAlignment(QtCore.Qt.AlignCenter)
        self.imagePrd.setObjectName("imagePrd")
        self.gridLayout_14.addWidget(self.imagePrd, 2, 0, 1, 1)
        self.verticalLayout_20.addWidget(self.prdItemFrame)
        self.frameDescription = QtWidgets.QFrame(self.productItem)
        self.frameDescription.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDescription.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDescription.setObjectName("frameDescription")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frameDescription)
        self.gridLayout_15.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.sizeFrame = QtWidgets.QFrame(self.frameDescription)
        self.sizeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sizeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sizeFrame.setObjectName("sizeFrame")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.sizeFrame)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.wLabel = QtWidgets.QLabel(self.sizeFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.wLabel.setFont(font)
        self.wLabel.setObjectName("wLabel")
        self.horizontalLayout_4.addWidget(self.wLabel)
        self.dLabel = QtWidgets.QLabel(self.sizeFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.dLabel.setFont(font)
        self.dLabel.setObjectName("dLabel")
        self.horizontalLayout_4.addWidget(self.dLabel)
        self.hLabel = QtWidgets.QLabel(self.sizeFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.hLabel.setFont(font)
        self.hLabel.setObjectName("hLabel")
        self.horizontalLayout_4.addWidget(self.hLabel)
        self.gridLayout_16.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.sizeFrame, 0, 3, 1, 2)
        self.discLabelItem = QtWidgets.QLabel(self.frameDescription)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(True)
        self.discLabelItem.setFont(font)
        self.discLabelItem.setObjectName("discLabelItem")
        self.gridLayout_15.addWidget(self.discLabelItem, 0, 1, 1, 1)
        self.priceLabelItem = QtWidgets.QLabel(self.frameDescription)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.priceLabelItem.setFont(font)
        self.priceLabelItem.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.priceLabelItem.setObjectName("priceLabelItem")
        self.gridLayout_15.addWidget(self.priceLabelItem, 0, 0, 1, 1)
        self.inStockFrame = QtWidgets.QFrame(self.frameDescription)
        self.inStockFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inStockFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inStockFrame.setObjectName("inStockFrame")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.inStockFrame)
        self.gridLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.inStockIcon = QtWidgets.QLabel(self.inStockFrame)
        self.inStockIcon.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.inStockIcon.setFont(font)
        self.inStockIcon.setText("")
        self.inStockIcon.setPixmap(QtGui.QPixmap("../../PyhtonTraining/cashier_app/PyQt/icon/tick-circle.png"))
        self.inStockIcon.setScaledContents(True)
        self.inStockIcon.setObjectName("inStockIcon")
        self.gridLayout_17.addWidget(self.inStockIcon, 0, 0, 1, 1)
        self.inStockLabel = QtWidgets.QLabel(self.inStockFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.inStockLabel.setFont(font)
        self.inStockLabel.setObjectName("inStockLabel")
        self.gridLayout_17.addWidget(self.inStockLabel, 0, 1, 1, 1)
        self.gridLayout_15.addWidget(self.inStockFrame, 3, 0, 1, 3)
        self.addCartButton = QtWidgets.QPushButton(self.frameDescription)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.addCartButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../PyhtonTraining/cashier_app/PyQt/icon/cart-shopping-white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addCartButton.setIcon(icon)
        self.addCartButton.setIconSize(QtCore.QSize(50, 15))
        self.addCartButton.setAutoRepeat(False)
        self.addCartButton.setObjectName("addCartButton")
        self.gridLayout_15.addWidget(self.addCartButton, 3, 3, 1, 2)
        self.verticalLayout_20.addWidget(self.frameDescription)
        self.horizontalLayout_3.addWidget(self.productItem)
        self.verticalLayout.addWidget(self.frameProduct)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(layoutProduct)
        QtCore.QMetaObject.connectSlotsByName(layoutProduct)

    def retranslateUi(self, layoutProduct):
        _translate = QtCore.QCoreApplication.translate
        layoutProduct.setWindowTitle(_translate("layoutProduct", "Form"))
        self.stockOffLabelDisc.setText(_translate("layoutProduct", "- 30%"))
        self.stockOffLabel.setText(_translate("layoutProduct", "New"))
        self.namePrdLabel.setText(_translate("layoutProduct", "Dinning Chair"))
        self.wLabel.setText(_translate("layoutProduct", "W : 120"))
        self.dLabel.setText(_translate("layoutProduct", "D : 40"))
        self.hLabel.setText(_translate("layoutProduct", "H : 110"))
        self.discLabelItem.setText(_translate("layoutProduct", "$50"))
        self.priceLabelItem.setText(_translate("layoutProduct", "$30"))
        self.inStockLabel.setText(_translate("layoutProduct", "In Stock"))
        self.addCartButton.setText(_translate("layoutProduct", "Add to Cart"))
