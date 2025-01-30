import sys
import json
import os
from PyQt5 import QtWidgets, uic

PRODUCTS_DB = 'products.json'
RECEIPT_DB = 'data/creo_data_receipt.json'

os.makedirs('data', exist_ok=True)

#Creooooooooooooooooooooooooooooooooooooooooooooooo

def load_products():
    with open(PRODUCTS_DB, 'r') as f:
        return json.load(f)

def save_receipt(user_name, cart):
    receipt = {
        "user": user_name,
        "items": cart
    }
    if os.path.exists(RECEIPT_DB):
        with open(RECEIPT_DB, 'r') as f:
            data = json.load(f)
    else:
        data = []
    data.append(receipt)
    with open(RECEIPT_DB, 'w') as f:
        json.dump(data, f, indent=4)

class CreoApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.landing_page = uic.loadUi('creo-0.ui')
        self.main_page = uic.loadUi('creo-1.ui')
        self.cart_page = uic.loadUi('creo-2.ui')
        self.stacked_widget.addWidget(self.landing_page)
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.cart_page)
        self.setup_ui_connections()
        self.user_name = ''
        self.cart = []
        self.products = load_products()
        self.setup_product_buttons()

    def setup_ui_connections(self):
        self.landing_page.continue_btn.clicked.connect(self.handle_continue)
        self.main_page.cart1_btn.clicked.connect(self.show_cart)
        self.main_page.logout_btn.clicked.connect(self.logout)
        self.cart_page.back_btn.clicked.connect(self.back_to_main)
        self.cart_page.remove_btn.clicked.connect(self.remove_item)
        self.cart_page.search_btn.clicked.connect(self.search_item)
        self.cart_page.checkout_btn.clicked.connect(self.checkout)

    def handle_continue(self):
        self.user_name = self.landing_page.name_bar.text()
        if not self.user_name:
            QtWidgets.QMessageBox.warning(self, 'Input Error', 'Please enter your name.')
        else:
            self.stacked_widget.setCurrentWidget(self.main_page)

    def setup_product_buttons(self):
        for btn_name, product in self.products.items():
            button = getattr(self.main_page, btn_name, None)
            if button:
                button.clicked.connect(lambda checked, p=product: self.add_to_cart(p))

    def add_to_cart(self, product):
        for item in self.cart:
            if item["name"] == product["name"]:
                item["quantity"] += 1  
                break
        else:
            product_copy = product.copy()
            product_copy["quantity"] = 1
            self.cart.append(product_copy)

        QtWidgets.QMessageBox.information(self, 'Item Added', f'{product["name"]} added to cart!')

    def show_cart(self):
        self.cart_page.product_table.setRowCount(len(self.cart))
        for row, item in enumerate(self.cart):
            self.cart_page.product_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item["quantity"])))  # Quantity
            self.cart_page.product_table.setItem(row, 1, QtWidgets.QTableWidgetItem(item["name"]))  # Name
            self.cart_page.product_table.setItem(row, 2, QtWidgets.QTableWidgetItem(f'₱{item["price"]:.2f}'))  # Price

        self.update_total_price()
        self.stacked_widget.setCurrentWidget(self.cart_page)

    def back_to_main(self):
        self.stacked_widget.setCurrentWidget(self.main_page)

    def remove_item(self):
        selected_row = self.cart_page.product_table.currentRow()
        if selected_row >= 0:
            self.cart.pop(selected_row)
            self.show_cart()

    def search_item(self):
        # Search for an item in the cart
        search_text = self.cart_page.search_bar.text().lower()
        for row in range(self.cart_page.product_table.rowCount()):
            item_name = self.cart_page.product_table.item(row, 1).text().lower()
            if search_text in item_name:
                self.cart_page.product_table.selectRow(row)
                return
        QtWidgets.QMessageBox.warning(self, 'Search', f'No item found matching "{search_text}".')

    def update_total_price(self):
        total_price = sum(item["price"] * item["quantity"] for item in self.cart)
        total_items = sum(item["quantity"] for item in self.cart)
        self.cart_page.price_text.setText(f'({total_items}) ₱{total_price:.2f}')

    def checkout(self):
        if not self.cart:
            QtWidgets.QMessageBox.warning(self, 'Checkout Error', 'Your cart is empty!')
        else:
            total_price = sum(item["price"] * item["quantity"] for item in self.cart)  # Include quantity in total price
            QtWidgets.QMessageBox.information(self, 'Checkout Success', f'Checkout successful by {self.user_name}!\nTotal: ₱{total_price:.2f}')
            save_receipt(self.user_name, self.cart)
            self.cart.clear()
            self.back_to_main()

    def logout(self):
        self.user_name = ''
        self.cart.clear()  
        self.stacked_widget.setCurrentWidget(self.landing_page)  


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CreoApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
