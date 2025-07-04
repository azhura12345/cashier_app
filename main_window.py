# /cashier_app/main_window.py

from PyQt5 import QtWidgets, QtCore, QtGui
from ui.main_ui import Ui_MainWindow
from ui.product_ui import Ui_layoutProduct
from widgets.product_item import ProductItemWidget
from models.product import get_products_by_category, get_all_products

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.productContainer = QtWidgets.QWidget()
        self.productContainerLayout = QtWidgets.QGridLayout(self.productContainer)
        self.ui.verticalLayout_12.addWidget(self.productContainer)

        # Koneksi klik kategori
        self.ui.category1.mousePressEvent = lambda e: self.load_category_products("Living Room")
        self.ui.category2.mousePressEvent = lambda e: self.load_category_products("Bedroom")
        self.ui.category3.mousePressEvent = lambda e: self.load_category_products("Office")
        self.ui.category4.mousePressEvent = lambda e: self.load_category_products("Kitchen")
        self.ui.category5.mousePressEvent = lambda e: self.load_category_products("Dining")
        self.ui.category6.mousePressEvent = lambda e: self.load_category_products("Outdoor")
        self.ui.category7.mousePressEvent = lambda e: self.load_category_products("Decoration")
        self.ui.category8.mousePressEvent = lambda e: self.load_all_products()

        # Kursor jadi tangan saat hover
        for label in [
            self.ui.category1, self.ui.category2, self.ui.category3,
            self.ui.category4, self.ui.category5, self.ui.category6,
            self.ui.category7, self.ui.category8
        ]:
            label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Load default: tampil semua produk
        self.load_all_products()

    def load_all_products(self):
        self.render_products(get_all_products())

    def load_category_products(self, category_name):
        self.render_products(get_products_by_category(category_name))

    def render_products(self, products):
        # Clear container
        for i in reversed(range(self.productContainerLayout.count())):
            widget_to_remove = self.productContainerLayout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)

        # Tambahkan produk ke grid
        for idx, product in enumerate(products):
            item_widget = ProductItemWidget(product, parent=self.productContainer)
            row = idx // 4
            col = idx % 4
            self.productContainerLayout.addWidget(item_widget, row, col)
