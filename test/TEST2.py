from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
from PyQt6 import QtWidgets
import sys
import json

# Giao diện cart
class Cart(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./App/UI/Cart.ui", self)

        # Tạo sự kiện nhấn nút Add
        self.pb_add.clicked.connect(self.AddItem)
        # Tạo sự kiến nhấn tút delete
        self.pb_delete.clicked.connect(self.deleteItem)

        self.list_name.clicked.connect(self.checkRow)
        # Gọi hàm đọc dữ liệu
        self.readData()

        #SET chọn hang trong list_name
        self.selected_row = -1
    # Hàm tải dữ liệu - Giải mã (load)
    def load_data(self):
        try: 
            with open("./test/data.json", "r") as file:
                data = json.load(file)
        except(FileNotFoundError):
            data = []
        return data
    
    # Hàm lưu dữ liệu - Mã hoá 
    def save_data(self, data):
        with open("./test/data.json", "w") as file:
            json.dump(data, file)

    # Hàm thềm dữ liệu 
    def AddItem(self):
        name = self.le_name.text()
        price = self.le_price.text()

        if not price.isdigit() or int(price) <= 0:
            self.le_price.clear()
            QMessageBox.warning(self, "Lỗi", "Giá tiền phải nguyên dương")
            return

        if name and price:
            data = self.load_data()

            if self.selected_row != -1:
                data[self.selected_row] = {"name": name, "price": price}

                # update UI
                self.list_name.item(self.selected_row).setText(name)
                self.list_price.item(self.selected_row).setText(price)

                QMessageBox.information(self, "Thông báo", "Cập nhật thành công")

                self.selected_row = -1  # reset mode

            else:
                data.append({"name": name, "price": price})

                self.list_name.addItem(name)
                self.list_price.addItem(price)

                QMessageBox.information(self, "Thông báo", f"Thêm {name} thành công")

            self.save_data(data)

            self.le_name.clear()
            self.le_price.clear()

        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin")
        # Hàm đọc dữ liệu 
    def readData(self):
        data = self.load_data()
        for dataItem in data:
            self.list_name.addItem(dataItem["name"])
            self.list_price.addItem(str(dataItem["price"]))

    def checkRow(self):
        self.selected_row = self.list_name.currentRow()

        if self.selected_row != -1:
            name_item = self.list_name.currentItem().text()
            price_item = self.list_price.item(self.selected_row).text()

            self.le_name.setText(name_item)
            self.le_price.setText(price_item)
    # Hàm xoá dữ liệu 
    def deleteItem(self):
        # Chọn tên muốn xoá 
        selected_row = self.list_name.currentRow()
        
        # list: index và item {0, 1, 2, 3} không có -1
        # Đã được chọn 
        if selected_row != -1:
            # Xoá sản phẩm ra khỏi list/ trên giao diện
            self.list_name.takeItem(selected_row)
            self.list_price.takeItem(selected_row)

            # Update lại data json
            data = self.load_data()
            del data[selected_row]
            self.save_data(data)
            QMessageBox.information(self, "Thông báo", "Đã sản phẩm thành công")

# Gọi giao diện 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    CartPage = Cart()
    CartPage.show()
    sys.exit(app.exec())