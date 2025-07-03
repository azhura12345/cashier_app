from PyQt5 import QtWidgets, QtGui
from ui.product_item_ui import Ui_ProductItem
import os

class ProductItemWidget(QtWidgets.QWidget):
    def __init__(self, product, add_to_cart_callback=None):
        super().__init__()
        self.ui = Ui_ProductItem()
        self.ui.setupUi(self)

        self.ui.namePrdLabel.setText(product["name"])
        self.ui.priceLabelItem.setText(f"${product['price']:.2f}")

        if product["discount"]:
            self.ui.discLabelItem.setVisible(True)
            self.ui.discLabelItem.setText(f"${product['discount']:.2f}")
        else:
            self.ui.discLabelItem.setVisible(False)

        self.ui.wLabel.setText(f"W : {product['width']}")
        self.ui.dLabel.setText(f"D : {product['depth']}")
        self.ui.hLabel.setText(f"H : {product['height']}")

        if product["stock"] <= 0:
            self.ui.inStockLabel.setText("Out of Stock")
            self.ui.inStockLabel.setStyleSheet("color:red;")
        else:
            self.ui.inStockLabel.setText("In Stock")

        if product["image_path"]:
            full_path = os.path.join(os.getcwd(), product["image_path"])
            if os.path.exists(full_path):
                pixmap = QtGui.QPixmap(full_path)
                if not pixmap.isNull():
                    self.ui.imagePrd.setPixmap(pixmap)

        if add_to_cart_callback:
            self.ui.addCartButton.clicked.connect(lambda: add_to_cart_callback(product))
