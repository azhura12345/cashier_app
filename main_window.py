# main_window.py

from PyQt5 import QtWidgets
from ui.main_ui import Ui_MainWindow
from ui.product_ui import Ui_layoutProduct
from widgets.product_item import ProductItemWidget
from models.product import get_products_by_category

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load halaman produk default
        self.load_category_products("Minuman")

    def load_category_products(self, category_name):
        # Clear isi container kategori
        for i in reversed(range(self.ui.categoryContainer.count())):
            widget_to_remove = self.ui.categoryContainer.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)

        # Buat halaman produk
        self.productPage = QtWidgets.QWidget()
        self.productUI = Ui_layoutProduct()
        self.productUI.setupUi(self.productPage)

        # Ambil data produk
        products = get_products_by_category(category_name)

        # Tambahkan produk ke grid
        for idx, product in enumerate(products):
            item_widget = ProductItemWidget(product, parent=self.productPage)
            row = idx // 4
            col = idx % 4
            self.productUI.productLayout.addWidget(item_widget, row, col)

        # Tambahkan ke container kategori
        self.ui.categoryContainer.addWidget(self.productPage)
