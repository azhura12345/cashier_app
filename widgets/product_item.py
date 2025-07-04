from PyQt5 import QtWidgets, QtGui
from ui.product_item_ui import Ui_ProductItem
import os

class ProductItemWidget(QtWidgets.QWidget):
    def __init__(self, product, add_to_cart_callback=None):
        super().__init__()
        self.ui = Ui_ProductItem()
        self.ui.setupUi(self)

        print(f"[WIDGET] Produk: {product['name']}")

        self.setMinimumSize(220, 300)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        # Nama Produk
        self.ui.namePrdLabel.setText(product["name"])

        # Harga
        self.ui.priceLabelItem.setText(f"${float(product['price']):,.2f}")

        # Diskon
        if product.get("discount"):
            self.ui.discLabelItem.setVisible(True)
            self.ui.discLabelItem.setText(f"${float(product['discount']):,.2f}")
        else:
            self.ui.discLabelItem.setVisible(False)

        # Ukuran
        self.ui.wLabel.setText(f"W : {product['width']}")
        self.ui.dLabel.setText(f"D : {product['depth']}")
        self.ui.hLabel.setText(f"H : {product['height']}")

        # Stok
        if product["stock"] <= 0:
            self.ui.inStockLabel.setText("Out of Stock")
            self.ui.inStockLabel.setStyleSheet("color:red;")
        else:
            self.ui.inStockLabel.setText("In Stock")

        # Gambar
        if product["image_path"]:
            full_path = os.path.join(os.getcwd(), product["image_path"])
            print(f"[DEBUG] Load image path: {full_path}")
            if os.path.exists(full_path):
                pixmap = QtGui.QPixmap(full_path)
                print(f"[DEBUG] pixmap.isNull(): {pixmap.isNull()}")
                if not pixmap.isNull():
                    self.ui.imagePrd.setPixmap(pixmap)
                else:
                    print(f"[WARNING] Pixmap is null → image load failed for {product['name']}")
            else:
                print(f"[WARNING] File tidak ditemukan: {full_path}")

        # Tombol Add to Cart
        if add_to_cart_callback:
            self.ui.addCartButton.clicked.connect(lambda: add_to_cart_callback(product))
