# /cashier_app/main_window.py
from PyQt5 import QtWidgets, QtGui
from ui.main_ui import Ui_MainWindow
from ui.product_item_ui import Ui_layoutProduct
from ui.order_detail_ui import Ui_OrderDetailWidget
from ui.order_item_ui import Ui_orderItemWidget
from models.product import get_products_by_category
from ui.product_item_ui import Ui_ProductItem
from widgets.product_item import ProductItemWidget

import os

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI utama
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup stack halaman (kategori <-> produk)
        self.init_stacked_widget()

        # Hubungkan tombol kategori ke halaman produk
        self.connect_category_buttons()

        # Inisialisasi order detail (keranjang)
        self.init_order_detail()

    def init_stacked_widget(self):
        self.stack = QtWidgets.QStackedWidget()

        # Halaman kategori (scroll area)
        kategori_view = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(kategori_view)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui.scrollArea)

        # Halaman produk
        produk_page = QtWidgets.QWidget()
        produk_ui = Ui_layoutProduct()
        produk_ui.setupUi(produk_page)

        self.product_ui = produk_ui  # biar bisa akses dari method lain
        self.setup_product_events()  # koneksi dummy add to cart

        self.stack.addWidget(kategori_view)  # index 0
        self.stack.addWidget(produk_page)   # index 1

        # Masukkan stack ke layout utama
        for i in reversed(range(self.ui.categoryWidget.layout().count())):
            widget = self.ui.categoryWidget.layout().itemAt(i).widget()
            if widget:
                widget.setParent(None)
        self.ui.categoryWidget.layout().addWidget(self.stack)

        self.stack.setCurrentIndex(0)

    def connect_category_buttons(self):
        self.ui.category1.clicked.connect(lambda: self.show_product_page(1))
        self.ui.category2.clicked.connect(lambda: self.show_product_page(2))
        self.ui.category3.clicked.connect(lambda: self.show_product_page(3))
        self.ui.category4.clicked.connect(lambda: self.show_product_page(4))
        self.ui.category5.clicked.connect(lambda: self.show_product_page(5))
        self.ui.category6.clicked.connect(lambda: self.show_product_page(6))
        self.ui.category7.clicked.connect(lambda: self.show_product_page(7))
        self.ui.category8.clicked.connect(lambda: self.show_product_page(8))
        self.ui.categoryFrameButton.clicked.connect(lambda: self.show_product_page(1))  # All Product

    def show_product_page(self, category_id=1):
        self.stack.setCurrentIndex(1)
        self.load_products_from_db(category_id)

    def make_add_to_cart_callback(self, p):
        return lambda: self.add_item_to_cart(
            product_name=p["name"],
            price=f"${p['price']:.2f}",
            qty=1,
            image_path=p["image_path"]
        )

    def load_products_from_db(self, category_id=1):
        print(f"[DEBUG] Load product for category: {category_id}")
        products = get_products_by_category(category_id)

        # Bersihkan layout sebelum load baru
        for i in reversed(range(self.product_ui.verticalLayout.count())):
            widget = self.product_ui.verticalLayout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        for product in products:
            print(f"[DEBUG] Membuat widget untuk produk: {product['name']}")
            try:
                product_widget = ProductItemWidget(product, self.make_add_to_cart_callback)
                self.product_ui.verticalLayout.addWidget(product_widget)
            except Exception as e:
                print(f"[ERROR] Crash saat buat widget produk {product['name']}:", e)

            product_widget = ProductItemWidget(product, self.make_add_to_cart_callback)
            ui = Ui_ProductItem()
            ui.setupUi(product_widget)

            # Set data...
            ui.namePrdLabel.setText(product["name"])
            ui.priceLabelItem.setText(f"${product['price']:.2f}")

            # Diskon
            if product.get("discount"):
                ui.discLabelItem.setVisible(True)
                ui.discLabelItem.setText(f"${product['discount']:.2f}")
            else:
                ui.discLabelItem.setVisible(False)

            # Stok
            ui.inStockLabel.setText(product.get("in_stock_label", ""))
            if product["stock"] <= 0:
                ui.inStockLabel.setStyleSheet("color:red;")

            # Ukuran
            ui.wLabel.setText(f"W : {product['width']}")
            ui.dLabel.setText(f"D : {product['depth']}")
            ui.hLabel.setText(f"H : {product['height']}")

            # Gambar
            if product["image_path"]:
                full_path = os.path.join(os.getcwd(), product["image_path"])
                if os.path.exists(full_path):
                    ui.imagePrd.setPixmap(QtGui.QPixmap(full_path))
                else:
                    print(f"[WARNING] Image not found: {full_path}")

            # Dalam loop for product in products:
            ui.addCartButton.clicked.connect(self.make_add_to_cart_callback(product))

            self.product_ui.verticalLayout.addWidget(product_widget)

    def show_category_page(self):
        self.stack.setCurrentIndex(0)

    def init_order_detail(self):
        self.order_widget = QtWidgets.QWidget()
        self.order_ui = Ui_OrderDetailWidget()
        self.order_ui.setupUi(self.order_widget)

        if self.ui.widget_2.layout() is None:
            self.ui.widget_2.setLayout(QtWidgets.QVBoxLayout())
        self.ui.widget_2.layout().addWidget(self.order_widget)
        self.ui.widget_2.setVisible(False)

        self.cartItemLayout = QtWidgets.QVBoxLayout()
        self.cartItemLayout.setContentsMargins(0, 0, 0, 0)
        self.cartItemLayout.setSpacing(8)
        self.order_ui.cartItemContainer.setLayout(self.cartItemLayout)

    def show_order_detail(self):
        self.ui.widget_2.setVisible(True)

    def hide_order_detail(self):
        self.ui.widget_2.setVisible(False)

    def add_item_to_cart(self, product_name="Wooden Chair", price="$19", qty=1, image_path=None):
        item_widget = QtWidgets.QWidget()
        item_ui = Ui_orderItemWidget()
        item_ui.setupUi(item_widget)

        item_ui.nameCart3.setText(product_name)
        item_ui.textNumber.setText(str(qty))
        item_ui.priceCart.setText(price)

        if image_path:
            full_path = os.path.join(os.getcwd(), image_path)
            if os.path.exists(full_path):
                item_ui.imageCart.setPixmap(QtGui.QPixmap(full_path))

        self.cartItemLayout.addWidget(item_widget)
        self.show_order_detail()

    def setup_product_events(self):
        try:
            self.product_ui.addCartButton.clicked.connect(lambda: self.add_item_to_cart(
                product_name="Office Chair", price="$55", qty=1
            ))
        except AttributeError:
            print("[ERROR] Tombol addCartButton tidak ditemukan di product_ui")
