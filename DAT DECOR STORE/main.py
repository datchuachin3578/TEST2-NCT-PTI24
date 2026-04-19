import json
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsColorizeEffect, QMessageBox
from PyQt5.QtCore import QEvent, QTimer, QPoint
from PyQt5.QtGui import QColor
from hover_effect import addHoverEffect
from sidebar_ui import Ui_MainWindow
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        
        #CAC BIEN GLOBAL
        self.All = False
        self.store = True
        self.log = False
        self.res = False
        self.out = True
        self.Cart = False
        self.buyed = False
        self.Checkbox = False
        self.register_users = {}
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.countitem = 0
        self.Rmtotal = False
        self.admin = False
        self.selected_row = -1
        
        #PAPE TRONG STORE
        self.Room = False
        self.Table = False
        self.Light = False
        self.Mange = False
        #CHECK CAC PAGE PRODUCT (DEATAILPG)
        self.Kesach = False
        self.Den = False
        self.Giuong = False
        self.Cay = False

        self.Gau = False
        self.Decal = False
        self.Dongho = False
        self.Hopbut = False

        self.Neon = False
        self.Sao = False
        self.Bay = False
        self.Phg = False
        # Ẩn widget con trước
        self.ui.sb_widget.hide()
        self.ui.sb_acc.hide()
        self.ui.sb_out.hide()
        self.ui.stacked_tong.setCurrentIndex(0)
        self.ui.stacked_store.setCurrentWidget(self.ui.all)
        # Button chuyển trang
        self.ui.list_name.clicked.connect(self.checkRow)
        '''SIDE_BAR MAIN'''
        self.ui.bt_search.clicked.connect(self.search)
        self.ui.bt_home.clicked.connect(self.all)
        self.ui.bt_all.clicked.connect(self.all)
        self.ui.bt_logo.clicked.connect(self.all)
        self.ui.bt_room.clicked.connect(self.room)
        self.ui.bt_table.clicked.connect(self.table)
        self.ui.bt_light.clicked.connect(self.light)
        self.ui.bt_mange.clicked.connect(self.mange)
        self.ui.bt_login.clicked.connect(self.login)
        self.ui.bt_res.clicked.connect(self.resg)
        self.ui.bt_cart.clicked.connect(self.cartft)

        '''BACK PAGE'''
        self.ui.back1.clicked.connect(self.backroom)
        self.ui.back1_2.clicked.connect(self.backroom)
        self.ui.back1_3.clicked.connect(self.backroom)
        self.ui.back1_4.clicked.connect(self.backroom)
        self.ui.back1_5.clicked.connect(self.backtable)
        self.ui.back1_6.clicked.connect(self.backtable)
        self.ui.back1_7.clicked.connect(self.backtable)
        self.ui.back1_8.clicked.connect(self.backtable)
        self.ui.back1_9.clicked.connect(self.backlight)
        self.ui.back1_10.clicked.connect(self.backlight)
        self.ui.back1_11.clicked.connect(self.backlight)
        self.ui.back1_12.clicked.connect(self.backlight)

        '''MANAGER PAGE'''
        self.ui.pb_add_2.clicked.connect(self.AddItem)
        self.ui.pb_delete_2.clicked.connect(self.deleteItem)
        self.ui.le_price.returnPressed.connect(self.AddItem)
        #SLIDE IMAGE
        self.start_auto_slide()

        '''LOGIN PAGE'''
        self.ui.bt_login1.clicked.connect(self.login)
        self.ui.bt_log.clicked.connect(self.CheckLogin)
        '''REGISTER PAGE'''
        self.ui.bt_res1.clicked.connect(self.resg)
        self.ui.bt_sup.clicked.connect(self.CheckRegister)
        '''CHECK ACCOUNT LOGIN/REGISTER'''
        self.ui.bt_account.clicked.connect(self.checkAcc)
        self.ui.bt_out.clicked.connect(self.Out)
        self.ui.le_retype_password.returnPressed.connect(self.CheckRegister)
        self.ui.le_lgpassword.returnPressed.connect(self.CheckLogin)
        '''CART PAGE'''
        self.ui.pb_delete.clicked.connect(self.DeleteItem)
        self.ui.pb_add.clicked.connect(self.cartft)
        self.ui.pb_buy.clicked.connect(self.buy)
        #BUTTON PRODUCT
        '''KỆ SÁCH PAGE'''
        self.ui.bt_kesach.clicked.connect(self.kesach)
        self.ui.bt_preks.clicked.connect(self.preks)
        self.ui.bt_nextks.clicked.connect(self.nextks)
        self.ui.bt_addks.setCheckable(True)
        self.ui.bt_addks.clicked.connect(self.cartft)
        self.ui.bt_buyks.clicked.connect(self.bdl)
        '''ĐÈN PAGE'''
        self.ui.bt_den.clicked.connect(self.den)
        self.ui.bt_preden.clicked.connect(self.preden)
        self.ui.bt_nextden.clicked.connect(self.nextden)
        self.ui.bt_addd.setCheckable(True)
        self.ui.bt_addd.clicked.connect(self.cartft)
        self.ui.bt_buyd.clicked.connect(self.bdl)
        '''ĐỆM GIƯỜNG PAGE'''
        self.ui.bt_giuong.clicked.connect(self.giuong)
        self.ui.bt_preg.clicked.connect(self.preg)
        self.ui.bt_nextg.clicked.connect(self.nextg)
        self.ui.bt_addg.setCheckable(True)
        self.ui.bt_addg.clicked.connect(self.cartft)
        self.ui.bt_buyg.clicked.connect(self.bdl)
        '''CAY PAGE'''
        self.ui.bt_cay.clicked.connect(self.cay)
        self.ui.bt_prec.clicked.connect(self.prec)
        self.ui.bt_nextc.clicked.connect(self.nextc)
        self.ui.bt_addc.setCheckable(True)
        self.ui.bt_addc.clicked.connect(self.cartft)
        self.ui.bt_buyc.clicked.connect(self.bdl)

        '''GẤU PAGE'''
        self.ui.bt_gau.clicked.connect(self.gau)
        self.ui.bt_pregau.clicked.connect(self.pregau)
        self.ui.bt_nextgau.clicked.connect(self.nextgau)
        self.ui.bt_addgau.setCheckable(True)
        self.ui.bt_addgau.clicked.connect(self.cartft)
        self.ui.bt_buygau.clicked.connect(self.bdl)
        '''DECAL PAGE'''
        self.ui.bt_decal.clicked.connect(self.decal)
        self.ui.bt_predecal.clicked.connect(self.predecal)
        self.ui.bt_nextdecal.clicked.connect(self.nextdecal)
        self.ui.bt_adddecal.setCheckable(True)
        self.ui.bt_adddecal.clicked.connect(self.cartft)
        self.ui.bt_buydecal.clicked.connect(self.bdl)
        '''ĐỒNG HỒ PAGE'''
        self.ui.bt_dongho.clicked.connect(self.dongho)
        self.ui.bt_predongho.clicked.connect(self.predongho)
        self.ui.bt_nextdongho.clicked.connect(self.nextdongho)
        self.ui.bt_adddongho.setCheckable(True)
        self.ui.bt_adddongho.clicked.connect(self.cartft)
        self.ui.bt_buydongho.clicked.connect(self.bdl)
        '''HỘP BÚT PAGE'''
        self.ui.bt_hopbut.clicked.connect(self.hopbut)
        self.ui.bt_prehopbut.clicked.connect(self.prehopbut)
        self.ui.bt_nexthopbut.clicked.connect(self.nexthopbut)
        self.ui.bt_addhopbut.setCheckable(True)
        self.ui.bt_addhopbut.clicked.connect(self.cartft)
        self.ui.bt_buyhopbut.clicked.connect(self.bdl)

        '''NEON PAGE'''
        self.ui.bt_neon.clicked.connect(self.neon)
        self.ui.bt_preneon.clicked.connect(self.preneon)
        self.ui.bt_nextneon.clicked.connect(self.nextneon)
        self.ui.bt_addneon.setCheckable(True)
        self.ui.bt_addneon.clicked.connect(self.cartft)
        self.ui.bt_buyneon.clicked.connect(self.bdl)
        '''SAO PAGE'''
        self.ui.bt_sao.clicked.connect(self.sao)
        self.ui.bt_presao.clicked.connect(self.presao)
        self.ui.bt_nextsao.clicked.connect(self.nextsao)
        self.ui.bt_addsao.setCheckable(True)
        self.ui.bt_addsao.clicked.connect(self.cartft)
        self.ui.bt_buysao.clicked.connect(self.bdl)
        '''BAY PAGE'''
        self.ui.bt_bay.clicked.connect(self.bay)
        self.ui.bt_prebay.clicked.connect(self.prebay)
        self.ui.bt_nextbay.clicked.connect(self.nextbay)
        self.ui.bt_addbay.setCheckable(True)
        self.ui.bt_addbay.clicked.connect(self.cartft)
        self.ui.bt_buybay.clicked.connect(self.bdl)
        '''PHG PAGE'''
        self.ui.bt_phg.clicked.connect(self.phg)
        self.ui.bt_prephg.clicked.connect(self.prephg)
        self.ui.bt_nextphg.clicked.connect(self.nextphg)
        self.ui.bt_addphg.setCheckable(True)
        self.ui.bt_addphg.clicked.connect(self.cartft)
        self.ui.bt_buyphg.clicked.connect(self.bdl)

        #ENTER INPUT ĐỂ CHUYỂN TỚI TRANG CHỨC NĂNG CART

        self.ui.bt_luutk.clicked.connect(self.checkbox)
        
        #ADD EFFECT_HOVER
        from hover_effect import addHoverEffect
        # gắn hover vào từng nút

        addHoverEffect(self.ui.bt_room) 
        addHoverEffect(self.ui.bt_table)
        addHoverEffect(self.ui.bt_light)
        addHoverEffect(self.ui.bt_mange)
        addHoverEffect(self.ui.bt_all)
        addHoverEffect(self.ui.bt_products)
        addHoverEffect(self.ui.bt_home)
        addHoverEffect(self.ui.bt_about)
        addHoverEffect(self.ui.bt_search)
        addHoverEffect(self.ui.bt_account)
        addHoverEffect(self.ui.bt_cart)
        addHoverEffect(self.ui.bt_contact)
        addHoverEffect(self.ui.bt_login)
        addHoverEffect(self.ui.bt_res)
        addHoverEffect(self.ui.bt_log)
        addHoverEffect(self.ui.bt_sup)
        addHoverEffect(self.ui.bt_out)
        addHoverEffect(self.ui.bt_info)
        #HOVER EFECT CART_PAGE
        addHoverEffect(self.ui.pb_showweb)
        addHoverEffect(self.ui.pb_edit)
        addHoverEffect(self.ui.pb_delete)
        addHoverEffect(self.ui.pb_add)
        addHoverEffect(self.ui.pb_buy)
        #HOVER EFECT ALL PAGE
        addHoverEffect(self.ui.stacked_img) 
        #HOVER EFFECT bt_buy PRODUCT
        addHoverEffect(self.ui.bt_kesach)
        addHoverEffect(self.ui.bt_den)
        addHoverEffect(self.ui.bt_cay)
        addHoverEffect(self.ui.bt_giuong)
        addHoverEffect(self.ui.bt_den)
        addHoverEffect(self.ui.bt_gau)
        addHoverEffect(self.ui.bt_decal)
        addHoverEffect(self.ui.bt_dongho)
        addHoverEffect(self.ui.bt_hopbut)
        addHoverEffect(self.ui.bt_sao)
        addHoverEffect(self.ui.bt_neon)
        addHoverEffect(self.ui.bt_bay)
        addHoverEffect(self.ui.bt_phg)

        #HOVER EFFECT DEATAIL_PAGE
        '''KE SACH PAGE'''
        addHoverEffect(self.ui.bt_buyks)
        addHoverEffect(self.ui.bt_addks)
        addHoverEffect(self.ui.bt_preks)
        addHoverEffect(self.ui.bt_nextks)
        '''DEN PAGE'''
        addHoverEffect(self.ui.bt_buyd)
        addHoverEffect(self.ui.bt_addd)
        addHoverEffect(self.ui.bt_preden)
        addHoverEffect(self.ui.bt_nextden)
        '''GIUONG PAGE'''
        addHoverEffect(self.ui.bt_buyg)
        addHoverEffect(self.ui.bt_addg)
        addHoverEffect(self.ui.bt_preg)
        addHoverEffect(self.ui.bt_nextg)
        '''CAY PAGE'''
        addHoverEffect(self.ui.bt_buyc)
        addHoverEffect(self.ui.bt_addc)
        addHoverEffect(self.ui.bt_prec)
        addHoverEffect(self.ui.bt_nextc)
        '''ROOM PAGE'''
        addHoverEffect(self.ui.bt_den)

        #BUTTON BLOCK
        addHoverEffect(self.ui.bl1)
        addHoverEffect(self.ui.bl2)
        addHoverEffect(self.ui.bl3)
        addHoverEffect(self.ui.bl4)
        addHoverEffect(self.ui.bl5)
        addHoverEffect(self.ui.bl6)
        addHoverEffect(self.ui.bl7)
        addHoverEffect(self.ui.bl8)
        addHoverEffect(self.ui.bl9)
        addHoverEffect(self.ui.bl10)
        addHoverEffect(self.ui.bl11)
        addHoverEffect(self.ui.bl12)

        #BUTTON BACK
        addHoverEffect(self.ui.back1)
        addHoverEffect(self.ui.back1_2)
        addHoverEffect(self.ui.back1_3)
        addHoverEffect(self.ui.back1_4)
        addHoverEffect(self.ui.back1_5)
        addHoverEffect(self.ui.back1_6)
        addHoverEffect(self.ui.back1_7)
        addHoverEffect(self.ui.back1_8)
        addHoverEffect(self.ui.back1_9)
        addHoverEffect(self.ui.back1_10)
        addHoverEffect(self.ui.back1_11)
        addHoverEffect(self.ui.back1_12)

        '''GAU PAGE'''
        addHoverEffect(self.ui.bt_buygau)
        addHoverEffect(self.ui.bt_addgau)
        addHoverEffect(self.ui.bt_pregau)
        addHoverEffect(self.ui.bt_nextgau)
        '''DECAL PAGE'''
        addHoverEffect(self.ui.bt_buydecal)
        addHoverEffect(self.ui.bt_adddecal)
        addHoverEffect(self.ui.bt_predecal)
        addHoverEffect(self.ui.bt_nextdecal)
        '''DONGHO PAGE'''
        addHoverEffect(self.ui.bt_buydongho)
        addHoverEffect(self.ui.bt_adddongho)
        addHoverEffect(self.ui.bt_predongho)
        addHoverEffect(self.ui.bt_nextdongho)
        '''HOPBUT PAGE'''
        addHoverEffect(self.ui.bt_buyhopbut)
        addHoverEffect(self.ui.bt_addhopbut)
        addHoverEffect(self.ui.bt_prehopbut)
        addHoverEffect(self.ui.bt_nexthopbut)

        '''NEON PAGE'''
        addHoverEffect(self.ui.bt_buyneon)
        addHoverEffect(self.ui.bt_addneon)
        addHoverEffect(self.ui.bt_preneon)
        addHoverEffect(self.ui.bt_nextneon)
        '''SAO PAGE'''
        addHoverEffect(self.ui.bt_buysao)
        addHoverEffect(self.ui.bt_addsao)
        addHoverEffect(self.ui.bt_presao)
        addHoverEffect(self.ui.bt_nextsao)
        '''BAY PAGE'''
        addHoverEffect(self.ui.bt_buybay)
        addHoverEffect(self.ui.bt_addbay)
        addHoverEffect(self.ui.bt_prebay)
        addHoverEffect(self.ui.bt_nextbay)
        '''PHG PAGE'''
        addHoverEffect(self.ui.bt_buyphg)
        addHoverEffect(self.ui.bt_addphg)
        addHoverEffect(self.ui.bt_prephg)
        addHoverEffect(self.ui.bt_nextphg)
        
        addHoverEffect(self.ui.pb_add_2)
        addHoverEffect(self.ui.pb_delete_2)

        self.ui.bt_res1.setStyleSheet("""
            QPushButton {
                border: 0px;
                color: rgb(0, 0, 0);
                font: 75 20pt "8514oem";
                background: 0
            }
            QPushButton:hover {
                text-decoration: underline;
            }
            """)
        self.ui.bt_login1.setStyleSheet("""
            QPushButton {
                border: 0px;
                color: rgb(0, 0, 0);
                font: 75 20pt "8514oem";
                background: 0
            }
            QPushButton:hover {
                text-decoration: underline;
            }
            QPushButton:pressed {
                background-color: 0;     
            }
            """)

                # ============= TIMER CHO 2 MENU HOVER =============
        #Count thời gian cho sb_widget
        self.closetimer = QTimer(self)
        self.closetimer.setSingleShot(True)# Timer chỉ chạy 1 lần rồi tự dừng #Vì ta chỉ muốn ẩn menu 1 lần khi chuột rời đi, không cần lặp lại.
        self.closetimer.setInterval(50)# Đặt thời gian delay = 200 milliseconds (0.2 giây)
        self.closetimer.timeout.connect(self.ui.sb_widget.hide)
        #Count thời gian cho sb_acc
        self.close_timer = QTimer(self)        
        self.close_timer.setSingleShot(True)
        self.close_timer.setInterval(50)
        self.close_timer.timeout.connect(self.ui.sb_acc.hide)
        #Count thời gian cho sb_out
        self.close_timero = QTimer(self)        
        self.close_timero.setSingleShot(True)
        self.close_timero.setInterval(1000)
        self.close_timero.timeout.connect(self.ui.sb_out.hide)
        #Cai event cho cac widgets
        self.ui.bt_account.installEventFilter(self)
        self.ui.sb_acc.installEventFilter(self)
        self.ui.bt_products.installEventFilter(self)
        self.ui.sb_widget.installEventFilter(self)
        self.ui.bt_out.installEventFilter(self)
        self.ui.sb_out.installEventFilter(self)
        
    '''sidebar'''
    def eventFilter(self, obj, event): #eventFilter hàm trong Qtdes (bắt buộc đúng cú pháp), obj; loại widget đang xảy ra(di chuột vào bt_product => obj = bt_products), event: loại sự kiện xảy ra 
        if event.type() not in (QEvent.Enter, QEvent.Leave): #QEvent.Enter = chuột vừa vào vùng của widget, QEvent.Leave = chuột vừa rời khỏi vùng của widget
            return super().eventFilter(obj, event)

        # ============= MENU ACCOUNT =============
        if self.out == True:
            if obj in (self.ui.bt_account, self.ui.sb_acc): #obj xảy ra với bt_account hoặc là sb_acc
                if event.type() == QEvent.Enter: #thì loại event sẽ là chuột chạm vào bt_account hoặc sb_acc
                    self.close_timer.stop() #từ đó => KHÔNG count thời gian nhả chuột khỏi obj
                    if obj == self.ui.bt_account:   #Nếu obj chính bằng bt_account THÌ ---------#
                        self.ui.sb_acc.move(1130, 70)   # vị trí của widget                     #
                        self.ui.sb_acc.show()       #THÌ Hiện lên widget khi chuột trỏ tới obj<=#
                elif event.type() == QEvent.Leave: #Nếu loại event là chuột không trỏ tới obj
                    self.close_timer.start()    #THÌ Count thời gian sau khi nhả chuột khỏi obj
            else:
                self.checkAcc()
        #==========SB_OUT==============================
        if self.out == False:
            if obj in (self.ui.bt_out, self.ui.sb_out):
                if event.type() == QEvent.Enter:
                    self.close_timero.stop()
                    if obj == self.ui.bt_out:
                        self.ui.sb_out.move(1130, 70)   # vị trí của bạn
                        self.ui.sb_out.show()
                elif event.type() == QEvent.Leave:
                    self.close_timero.start()
        # ============= MENU PRODUCTS =============
        if obj in (self.ui.bt_products, self.ui.sb_widget):
            if event.type() == QEvent.Enter:
                self.closetimer.stop()
                if obj == self.ui.bt_products:
                    self.ui.sb_widget.move(540, -5)   # vị trí của bạn
                    self.ui.sb_widget.show()
            elif event.type() == QEvent.Leave:
                self.closetimer.start()

        return super().eventFilter(obj, event)
        
    #===========================================================================================#
    #TỔNG GIÁ/SẢN PHẨM
    
    def update_total(self):
        self.total = 0

        # luôn lấy giá mới nhất
        self.price_map = self.build_price_map()

        for i in range(self.ui.list_item.count()):
            name = self.ui.list_item.item(i).text()

            if name in self.price_map:
                self.total += self.price_map[name]

        self.ui.lb_total.setText(f"{self.total:,} VNĐ")
        self.ui.lb_totalsp.setText(f"{self.countitem}")
    def bdl(self):
        msgBox = QMessageBox()

        if self.out == True:
            msgBox.warning(self, "*_*", "Cần đăng nhập để mua hàng!")
            self.login()
            return

        # ===== xác định sản phẩm =====
        product_map = {
            "kệ sách": self.Kesach,
            "đèn ngủ": self.Den,
            "đệm giường": self.Giuong,
            "cây giả": self.Cay,
            
            "tượng gấu": self.Gau,
            "decal": self.Decal,
            "đồng hồ cát": self.Dongho,
            "hộp bút": self.Hopbut,

            "neon": self.Neon,
            "sao": self.Sao,
            "led": self.Bay,
            "đèn phg": self.Phg,
        }

        product_name = None

        for name, status in product_map.items():
            if status:
                product_name = name
                break

        if not product_name:
            msgBox.warning(self, "Lỗi", "Không xác định được sản phẩm")
            return

        # ===== load giá mới nhất =====
        price_map = self.build_price_map()

        if product_name in price_map:
            price = price_map[product_name]
        else:
            msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
            return

        # ===== hiển thị =====
        self.ui.lb_bill.setText(f"Bạn đã thanh toán thành công số tiền {price:,} VNĐ")

        self.ui.stacked_tong.setCurrentWidget(self.ui.page_buyed)
        self.ui.list_item.clear()
        self.countitem = 0
        self.update_total()

        # reset trạng thái
        self.Kesach = False
        self.Den = False
        self.Giuong = False
        self.Cay = False
        
    def buyindt(self):
        if self.out == False:
            self.countitem = 1
            if self.countitem >= 1:
                self.update_total()
                self.countitem = 0
                self.ui.stacked_tong.setCurrentWidget(self.ui.page_buyed)
                self.ui.list_item.clear()
        msgBox = QMessageBox()
        if self.out == True:
            msgBox.warning(self, "*_*", "Cần đăng nhập để mua hàng!")
            self.login()
    def buy(self):
        msgBox = QMessageBox()
        if self.out == False:
            if self.countitem >= 1:
                self.Rmtotal = True
                self.ui.stacked_tong.setCurrentWidget(self.ui.page_buyed)
                self.ui.list_item.clear()
                self.ui.list_tien.clear()
                self.ui.lb_bill.setText(f"Bạn đã thanh toán thành công {self.total:,} VNĐ")
                self.countitem = 0
                self.update_total()
            else:
                msgBox.warning(self, "*_*", "Chưa có sản phẩm trong giỏ hàng")
        else:
            self.cart()
    def cart(self): #Set cho page_cart = True
        msgBox = QMessageBox()
        if self.out == True:
            msgBox.warning(self, "*_*", "Cần đăng nhập để vào giỏ hàng!")
            self.login()

    #======================================LIST CART=============================================
    def load_price_data(self):
        try: 
            with open("./Json/cart_data.json", "r") as file:
                cart_data = json.load(file)
        except(FileNotFoundError):
            cart_data = []
        return cart_data
    
    def build_price_map(self):
        price_map = {}
        data = self.load_price_data()
        for item in data:
            try:
                price_map[item["name"]] = int(item["price"]) * 1000
            except:
                continue
        return price_map
    
    def cartft(self,sender):
        msgBox = QMessageBox()
        self.name = self.ui.le_input.text()
        c_len = len(self.name)
        sender = self.sender()   #Biết nút nào bấm vào
        if self.out == False:
            self.Rmtotal = False
            if c_len >= 1:
                self.ui.list_item.addItem(self.name)
                self.ui.le_input.clear()
                self.ui.le_input.setFocus()
                self.countitem += 1
                msgBox.information(self, "Thong bao", f'Da them {self.name} vao list thanh cong')
            # Nếu bấm nút "ADD Kệ sách"
            # ===== ADD KỆ SÁCH =====
            if sender == self.ui.bt_addks:
                self.name = "kệ sách"   # ⚠️ phải trùng JSON

                # load giá mới nhất
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm KỆ SÁCH vào giỏ hàng")
                self.ui.bt_addks.setChecked(False)
            # ===== ADD ĐÈN NGỦ =====
            if sender == self.ui.bt_addd:
                self.name = "đèn ngủ"   # ⚠️ phải trùng JSON

                # load giá mới nhất
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm KỆ SÁCH vào giỏ hàng")
                self.ui.bt_addd.setChecked(False)
            # ===== ADD ĐỆM GIƯỜNG =====
            if sender == self.ui.bt_addg:
                self.name = "đệm giường"  # phải trùng JSON

                # load giá mới nhất
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm ĐỆM GIƯỜNG vào giỏ hàng")
                self.ui.bt_addg.setChecked(False)
            # ===== ADD CÂY GIẢ =====
            if sender == self.ui.bt_addc:
                self.name = "cây giả"  # phải trùng JSON

                # load giá mới nhất
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm CÂY GIẢ vào giỏ hàng")
                self.ui.bt_addc.setChecked(False)
            # ===== ADD TƯỢNG BEARBRICK =====
            if sender == self.ui.bt_addgau:
                self.name = "tượng gấu"  # phải trùng JSON

                #load lại giá mới nhất từ JSON
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm TƯỢNG BEARBRICK vào giỏ hàng")
                self.ui.bt_addgau.setChecked(False)
                
            # ===== ADD DECAL =====
            if sender == self.ui.bt_adddecal:
                self.name = "decal"  # phải trùng JSON

                #load lại giá mới nhất từ JSON
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm DECAL vào giỏ hàng")
                self.ui.bt_adddecal.setChecked(False)    
            # ===== ADD ĐỒNG HỒ =====
            if sender == self.ui.bt_adddongho:
                self.name = "đồng hồ cát"  # phải trùng JSON

                #load lại giá mới nhất từ JSON
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm ĐỒNG HỒ vào giỏ hàng")
                self.ui.bt_adddongho.setChecked(False)    
            # ===== ADD HỘP BÚT=====
            if sender == self.ui.bt_addhopbut:
                self.name = "hộp bút"  # phải trùng JSON

               #load lại giá mới nhất từ JSON
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm HỘP BÚT vào giỏ hàng")
                self.ui.bt_addhopbut.setChecked(False)

            # ===== ADD NEON =====
            if sender == self.ui.bt_addneon:
                self.name = "đèn neon"  # phải trùng JSON
                
               #load lại giá mới nhất từ JSON
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm ĐÈN NEON vào giỏ hàng")
                self.ui.bt_addneon.setChecked(False)    
            # ===== ADD SAO =====
            if sender == self.ui.bt_addsao:
                self.name = "đèn sao" # phải trùng JSON

                #load lại giá mới nhất từ JSON
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm ĐÈN SAO vào giỏ hàng")
                self.ui.bt_addsao.setChecked(False)
            # ===== ADD BAY =====
            if sender == self.ui.bt_addbay:
                self.name = "đèn led"  # phải trùng JSON
                
                #load lại giá mới nhất từ JSON
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm ĐÈN LED vào giỏ hàng")
                self.ui.bt_addbay.setChecked(False)
            # ===== ADD ĐÈN PHG =====
            if sender == self.ui.bt_addphg:
                self.name = "đèn phg"  # phải trùng JSON

                #load lại giá mới nhất từ JSON
                self.price_map = self.build_price_map()

                # kiểm tra tồn tại
                if self.name not in self.price_map:
                    msgBox.warning(self, "Lỗi", "Không tìm thấy giá sản phẩm")
                    return

                price = self.price_map[self.name]

                # thêm vào list
                self.ui.list_item.addItem(self.name)

                self.ui.list_tien.addItem(f"{price:,} VNĐ")

                self.countitem += 1
                self.update_total()

                msgBox.information(self, "!", "Đã thêm ĐÈN PHI HÀNH GIA vào giỏ hàng")
                self.ui.bt_addphg.setChecked(False)
                
            if self.ui.bt_cart.clicked:
                self.Cart = True
                self.checkpage()
        else:
            self.cart()
    def DeleteItem(self):
        msgBox = QMessageBox()

        row = self.ui.list_item.currentRow()

        if row != -1:
            # lấy tên sản phẩm TRƯỚC khi xóa
            item = self.ui.list_item.item(row)
            ten_san_pham = item.text()

            self.ui.list_item.takeItem(row)
            self.ui.list_tien.takeItem(row)

            self.countitem -= 1
            self.update_total()

            msgBox.information(self, "Thông báo", f'Bạn đã xóa "{ten_san_pham}"')
        else:
            msgBox.warning(self, "Lỗi", "Chưa chọn sản phẩm")

    #=====================================MANGE SAN PHAM PAGE======================================================
    
    def load_price_data(self):
        try: 
            with open("./Json/price_data.json", "r") as file:
                price_data = json.load(file)
        except(FileNotFoundError):
            price_data = []
        return price_data

    # Hàm lưu dữ liệu - Mã hoá 
    def save_price_data(self, price_data):
        with open("./Json/price_data.json", "w") as file:
            json.dump(price_data, file)

    # Hàm thêm dữ liệu 
    def AddItem(self):
        # Lấy dữ liệu nhập trên giao diện
        name = self.ui.le_name.text()
        price = self.ui.le_price.text()

        
        # Kiểm tra dữ liệu nhập vào có phải nguyên dương hay không 
        if not price.isdigit() or int(price) <= 0:
            self.ui.le_price.clear()
            QMessageBox.warning(self, "Lỗi", "Giá tiền phải nguyên dương")
            return
        
        
        if name and price:
            data = self.load_price_data()

            if self.selected_row != -1:
                data[self.selected_row] = {"name": name, "price": price}

                # update UI
                self.ui.list_name.item(self.selected_row).setText(name)
                self.ui.list_price.item(self.selected_row).setText(price)

                QMessageBox.information(self, "Thông báo", "Cập nhật thành công")

                self.selected_row = -1  # reset mode

            else:
                data.append({"name": name, "price": price})

                self.ui.list_name.addItem(name)
                self.ui.list_price.addItem(price)

                QMessageBox.information(self, "Thông báo", f"Thêm {name} thành công")

            self.save_price_data(data)

            self.ui.le_name.clear()
            self.ui.le_price.clear()
            
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin")
                     

    # Hàm đọc dữ liệu 
    def readpriceData(self):
        data = self.load_price_data()
        for dataItem in data:
            self.ui.list_name.addItem(dataItem["name"])
            self.ui.list_price.addItem(str(dataItem["price"]))

    def checkRow(self):
        self.selected_row = self.ui.list_name.currentRow()

        if self.selected_row != -1:
            name_item = self.ui.list_name.currentItem().text()
            price_item = self.ui.list_price.item(self.selected_row).text()

            self.ui.le_name.setText(name_item)
            self.ui.le_price.setText(price_item)
    # Hàm xoá dữ liệu 
    def deleteItem(self):
        #Chọn tên muốn xoá
        self.selected_row = self.ui.list_name.currentRow()
        
        # list: index và item {0, 1, 2, 3} không có -1
        # Đã được chọn
        if self.selected_row != -1:
            # Xoá sản phẩm ra khỏi list/ trên giao diện
            self.ui.list_name.takeItem(self.selected_row)
            self.ui.list_price.takeItem(self.selected_row)

            # Update lại data json
            data = self.load_price_data()
            del data[self.selected_row]
            self.save_price_data(data)
            self.selected_row = -1
            # Gọi hàm tính tổng tiền
            QMessageBox.information(self, "Thông báo", "Đã sản phẩm thành công")
           
    # Hàm tính tổng tiền
    def calculate_total(self):
        total = 0
        data = self.load_data()
        for key_price in data:
            total += int(key_price["price"])
        self.ui.lb_priceTotal.setText(f"Tổng giá tiền là: {total} $")

    '''TU DONG CHUYEN WIDGETS'''
    def start_auto_slide(self):
        self.slider_timer = QTimer(self)
        self.slider_timer.timeout.connect(self.next_slide)
        self.slider_timer.start(1000)   # đổi slide mỗi 1 giây
    def next_slide(self):
        stacked = self.ui.stacked_img
        stacked.setCurrentIndex(
            (stacked.currentIndex() + 1) % stacked.count()) #lặp cho tới khi hết sẽ quay về ảnh 1
        
    def search(self):
        msgBox = QMessageBox()
        msgBox.information(self, "*_*", "Tính năng tìm kiếm chưa khả dụng :(")
        self.ui.search_text.clear()
    def Out(self):
        self.ui.stacked_tong.setCurrentWidget(self.ui.page_log)
        self.ui.sb_out.close()
        self.ui.list_item.clear()
        self.admin = False
        self.Rmtotal = True
        self.countitem = 0
        self.update_total()
        self.out = True
    def checkAcc(self):
        if self.out == True:
            next
        else:
            self.ui.sb_out.move(1130, 70)   # vị trí của bạn
            self.ui.sb_out.show()
            self.close_timero.start()
    def login(self):
        self.store = False
        self.res = False
        self.log = True
        self.ui.stacked_tong.setCurrentWidget(self.ui.page_log)
        self.checkpage()
    def resg(self):
        self.store = False
        self.log = False
        self.res = True
        self.ui.stacked_tong.setCurrentWidget(self.ui.page_res)
        self.load_data()
        self.checkpage()
    def room(self):
        self.store = True
        self.log = False 
        self.res = False
        self.ui.stacked_store.setCurrentWidget(self.ui.room)
        #+KỆ SÁCH
        nameks = "kệ sách"
        if nameks:
            data = self.load_price_data()
            for user in data:
                if user["name"] == nameks:
                    self.priceks = self.ui.label_13.setText(user["price"] + ".000")
                    self.priceks = self.ui.label_6.setText("Giá: " + user["price"] +".000" + " VND")
        #ĐÈN NGỦ
        named = "đèn ngủ"
        if named:
            data = self.load_price_data()
            for user in data:
                if user["name"] == named:
                    self.priceks = self.ui.label_277.setText(user["price"] + ".000")
                    self.priceks = self.ui.label_23.setText("Giá: " + user["price"] +".000" + " VND")
        #ĐỆM GIƯỜNG
        nameg = "đệm giường"
        if nameg:
            data = self.load_price_data()
            for user in data:
                if user["name"] == nameg:
                    self.priceks = self.ui.label_280.setText(user["price"] + ".000")
                    self.priceks = self.ui.label_12.setText("Giá: " + user["price"] +".000" + " VND")
        #CÂY GIẢ
        namec = "cây giả"
        if namec:
            data = self.load_price_data()
            for user in data:
                if user["name"] == namec:
                    self.priceks = self.ui.label_283.setText(user["price"] + ".000")
                    self.priceks = self.ui.label_18.setText("Giá: " + user["price"] +".000" + " VND")
        self.checkpage()
    def table(self):
        self.store = True
        self.log = False
        self.res = False
        self.ui.stacked_store.setCurrentWidget(self.ui.table)
        #gau
        nameg = "tượng gấu"
        if nameg:
            data = self.load_price_data()
            for user in data:
                if user["name"] == nameg:
                    self.priceg = self.ui.label_26.setText(user["price"] + ".000")
                    self.priceg = self.ui.label_41.setText("Giá: " + user["price"] +".000" + " VND")
        #decal
        namedc = "decal"
        if namedc:
            data = self.load_price_data()
            for user in data:
                if user["name"] == namedc:
                    self.pricedc = self.ui.label_298.setText(user["price"] + ".000")
                    self.pricedc = self.ui.label_35.setText("Giá: " + user["price"] +".000" + " VND")
        #dongho
        namedh = "đồng hồ cát"
        if namedh:
            data = self.load_price_data()
            for user in data:
                if user["name"] == namedh:
                    self.pricedh = self.ui.label_301.setText(user["price"] + ".000")
                    self.pricedh = self.ui.label_47.setText("Giá: " + user["price"] +".000" + " VND")
        #hopbut
        namehb = "hộp bút"
        if namehb:
            data = self.load_price_data()
            for user in data:
                if user["name"] == namehb:
                    self.pricehb = self.ui.label_304.setText(user["price"] + ".000")
                    self.pricehb = self.ui.label_53.setText("Giá: " + user["price"] +".000" + " VND")
        self.checkpage()
    def light(self):
        self.store = True
        self.log = False
        self.res = False
        self.ui.stacked_store.setCurrentWidget(self.ui.light)
        #neon
        nameneon = "đèn neon"
        if nameneon:
            data = self.load_price_data()
            for user in data:
                if user["name"] == nameneon:
                    self.priceneon = self.ui.label_59.setText(user["price"] + ".000")
                    self.priceneon = self.ui.label_75.setText("Giá: " + user["price"] +".000" + " VND")
        #sao
        namesao = "đèn sao"
        if namesao:
            data = self.load_price_data()
            for user in data:
                if user["name"] == namesao:
                    self.pricedc = self.ui.label_299.setText(user["price"] + ".000")
                    self.pricedc = self.ui.label_81.setText("Giá: " + user["price"] +".000" + " VND")
        #led
        nameled = "đèn led"
        if nameled:
            data = self.load_price_data()
            for user in data:
                if user["name"] == nameled:
                    self.priceled = self.ui.label_305.setText(user["price"] + ".000")
                    self.priceled = self.ui.label_87.setText("Giá: " + user["price"] +".000" + " VND")
        #phg
        namephg = "đèn phg"
        if namephg:
            data = self.load_price_data()
            for user in data:
                if user["name"] == namephg:
                    self.pricephg = self.ui.label_320.setText(user["price"] + ".000")
                    self.pricephg = self.ui.label_93.setText("Giá: " + user["price"] +".000" + " VND")
        self.checkpage()
    def mange(self):
        self.Mange = True
        if self.admin == True:
            self.store = True
            self.log = False
            self.res = False
            self.checkpage()
        else:
            QMessageBox.information(self, "Lỗi", "Bạn chưa có quyền admin")
    def all(self):
        self.store = True
        self.log = False
        self.res = False
        self.Mange = False
        self.ui.stacked_store.setCurrentWidget(self.ui.all)
        self.checkpage()
    def backroom(self): #Chuyen tu page detail sang trang truoc do
        self.Room = True
        self.checkpage()
    def backtable(self): #Chuyen tu page detail sang trang truoc do
        self.Table = True
        self.checkpage()
    def backlight(self): #Chuyen tu page detail sang trang truoc do
        self.Light = True
        self.checkpage()
        
    #TAO BIEN CHECK CAC STACKED_WIDGETS
    def checkpage(self):
        if self.Mange == True:
            if self.admin == True:
                    self.ui.stacked_tong.setCurrentWidget(self.ui.page_store)
                    self.ui.stacked_store.setCurrentWidget(self.ui.mange)
                    self.Mange = False
            
        if self.res == True:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_res)
            self.res = False
        if self.log == True:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_log)
            self.log = False
        if self.store == True:
            self.Kesach = False
            self.Den = False
            self.Giuong = False
            self.Cay = False

            self.Gau = False
            self.Decal = False
            self.Dongho = False
            self.Hopbut = False

            self.Neon = False
            self.Sao = False
            self.Bay = False
            self.Phg = False
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_store)
        if self.Cart == True:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_cart)
            if self.countitem <=0:
                self.total = 0
                self.update_total()
            self.Cart = False
        if self.All == True:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_store)
            self.ui.stacked_store.setCurrentWidget(self.ui.all)
            self.Room = False
        if self.Room == True:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_store)
            self.ui.stacked_store.setCurrentWidget(self.ui.room)
            self.Room = False
        if self.Table == True:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_store)
            self.ui.stacked_store.setCurrentWidget(self.ui.table)
            self.Table =False
        if self.Light == True:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_store)
            self.ui.stacked_store.setCurrentWidget(self.ui.light)
            self.Light = False
    #KIEM TRA LOGIN
    def load_data(self):
        try:
            with open("./Json/user_data.json", "r") as file:
                data = json.load(file)
        except(FileNotFoundError):
            data = []
        return data
    def CheckLogin(self):
        # Lấy dữ liệu từ line edit
        userName = self.ui.le_user_name.text()
        password = self.ui.le_lgpassword.text()
        
        # Kiểm tra tài khoản
        if userName and password:
            data = self.load_data()
            if "ad" == userName and "ad123" == password:
                    QMessageBox.information(self, "Thông báo", "Đăng nhập thành công")
                    # Chuyển trang
                    self.store = True
                    self.log = False
                    self.res = False
                    self.out = False
                    self.admin = True
                    self.ui.stacked_store.setCurrentWidget(self.ui.all)
                    self.ui.le_user_name.clear()
                    self.ui.le_lgpassword.clear()
                    self.readpriceData()
                    self.checkpage()
                    return
            for user in data:

                if user["user_name"] == userName and user["password"] == password:
                    QMessageBox.information(self, "Thông báo", "Đăng nhập thành công")
                    # Chuyển trang
                    self.store = True
                    self.log = False
                    self.res = False
                    self.out = False
                    self.admin = False
                    self.ui.stacked_store.setCurrentWidget(self.ui.all)
                    self.checkpage()
                    if self.Checkbox == False:
                        self.ui.le_user_name.clear()
                        self.ui.le_lgpassword.clear()
                        return
                    else:
                        self.ui.le_lgpassword.clear()
                        return
                
            QMessageBox.warning(self, "Lỗi", "Tài khoản không đúng, vui lòng nhập lại !")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin")

    #TAO USER_DATA.json
    # Hàm đọc dữ liệu từ người dùng về file Json - Giải mã 
    def load_data(self):
        try:
            with open("./Json/user_data.json", "r") as file:
                data = json.load(file)
        except(FileNotFoundError):
            data = []
        return data
    
    # Hàm lưu dữ liệu người dùng - Mã hoá
    def save_data(self, data):
        with open("./Json/user_data.json", "w") as file:
            json.dump(data, file)

    def CheckRegister(self):
        # Lấy giá trị đã nhập trong line edit
        userName = self.ui.le_User_name.text()
        password = self.ui.le_password.text()
        RetypePass = self.ui.le_retype_password.text()
        lenPass = len(password)
        lenUserName = len(userName)
        Msg = QMessageBox()

        # Lập trình bảo mật 
        if not userName and not password and not RetypePass:
            Msg.warning(self, "Thông báo lỗi", "Cần điền đầy đủ thông tin !")
            return
        elif lenPass < 6 and lenUserName < 6:
            Msg.warning(self, "Thông báo lỗi", " Tên tk và mk phải ít nhất 6 ký tự")
            return
        elif password != RetypePass:
            Msg.warning(self, "Thông báo lỗi", "Mk chưa trùng khớp")
            password = self.ui.le_password.clear()
            RetypePass = self.ui.le_retype_password.clear()
            return
        elif userName == password:
            Msg.warning(self, "Thông báo lỗi", "Tên TK không được trùng với MK")
            userName = self.ui.le_User_name.clear()
            password = self.ui.le_password.clear()
            RetypePass = self.ui.le_retype_password.clear()
            return
        
        # lập trình đăng ký và lưu tài khoản
        # Biến số gọi hàm tải dữ liệu 
        data = self.load_data()
        for user in data:
            if user["user_name"] == userName:
                Msg.warning(self, "Lỗi", "Tài khoản đã tồn tại")
                return
            
        data.append({"user_name": userName, "password": password})
        self.save_data(data)
        Msg.information(self, "Thông báo", "Đăng Ký thành công")
        self.store = False
        self.log = True
        self.res = False
        self.ui.stacked_store.setCurrentWidget(self.ui.page_log)
        self.checkpage()
        self.ui.le_User_name.clear()
        self.ui.le_password.clear()
        self.ui.le_retype_password.clear()

    def stacked_tong(self):
        self.ui.stacked_tong.setCurrentWidget(self.ui.detailpg)
        self.stacked_detail()
    def stacked_detail(self):
    #ROOM1️⃣
        if self.Kesach == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.kesachpg)
            

        if self.Den == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.denpg)

        if self.Giuong == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.giuongpg)
        if self.Cay == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.caypg)
    #TABLE2️⃣
        if self.Gau == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.gaupg)

        if self.Decal == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.decalpg)

        if self.Dongho == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.donghopg)

        if self.Hopbut == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.hopbutpg)

    #LIGHT3️⃣
        if self.Neon == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.neonpg)

        if self.Sao == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.saopg)
            self.Sao = False
        if self.Bay == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.baypg)

        if self.Phg == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.phgpg)

    #1️⃣
    #PAGE KE SACH#
    def kesach(self):
        self.Kesach = True
        self.stacked_tong()  
    '''ĐỔI IMAGE PRODUCT'''
    def nextks(self):
        stacked = self.ui.stacked_kesach
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def preks(self):
        stacked = self.ui.stacked_kesach
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count())
    #PAGE DEN#
    def den(self):
        self.Den = True
        self.stacked_tong()
    def nextden(self):
        stacked = self.ui.stacked_den 
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def preden(self):
        stacked = self.ui.stacked_den
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong stacked_store
    #PAGE GIUONG#
    def giuong(self):
        self.Giuong = True
        self.stacked_tong()
    def nextg(self):
        stacked = self.ui.stacked_giuong
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def preg(self):
        stacked = self.ui.stacked_giuong
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong stacked_store
    #PAGE CAY#
    def cay(self):
        self.Cay = True
        self.stacked_tong()
    def nextc(self):
        stacked = self.ui.stacked_cay
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def prec(self):
        stacked = self.ui.stacked_cay
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong stacked_store

    #2️⃣
    #PAGE GAU#
    def gau(self):
        self.Gau = True
        self.stacked_tong()  
    '''ĐỔI IMAGE PRODUCT'''
    def nextgau(self):
        stacked = self.ui.stacked_gau
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def pregau(self):
        stacked = self.ui.stacked_gau
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count())
    #PAGE DECAL#
    def decal(self):
        self.Decal = True
        self.stacked_tong()
    def nextdecal(self):
        stacked = self.ui.stacked_decal 
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def predecal(self):
        stacked = self.ui.stacked_decal
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong stacked_store
    #PAGE DONGHO#
    def dongho(self):
        self.Dongho = True
        self.stacked_tong()
    def nextdongho(self):
        stacked = self.ui.stacked_dongho
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def predongho(self):
        stacked = self.ui.stacked_dongho
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong stacked_store
    #PAGE HOPBUT#
    def hopbut(self):
        self.Hopbut = True
        self.stacked_tong()
    def nexthopbut(self):
        stacked = self.ui.stacked_hopbut
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def prehopbut(self):
        stacked = self.ui.stacked_hopbut
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong stacked_store
    
    #3️⃣
    #PAGE NEON#
    def neon(self):
        self.Neon = True
        self.stacked_tong()  
    '''ĐỔI IMAGE PRODUCT'''
    def nextneon(self):
        stacked = self.ui.stacked_neon
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def preneon(self):
        stacked = self.ui.stacked_neon
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count())
    #PAGE SAO#
    def sao(self):
        self.Sao = True
        self.stacked_tong()
    def nextsao(self):
        stacked = self.ui.stacked_sao
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def presao(self):
        stacked = self.ui.stacked_sao
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong stacked_store
    #PAGE BAY#
    def bay(self):
        self.Bay = True
        self.stacked_tong()
    def nextbay(self):
        stacked = self.ui.stacked_bay
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def prebay(self):
        stacked = self.ui.stacked_bay
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong stacked_store
    #PAGE PHG#
    def phg(self):
        self.Phg = True
        self.stacked_tong()
    def nextphg(self):
        stacked = self.ui.stacked_phg
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())
    def prephg(self):
        stacked = self.ui.stacked_phg
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong stacked_store
    

        #kiểm tra lưu tk
    def checkbox(self):
        if self.ui.bt_luutk.isChecked():
            self.Checkbox = True
            self.login()
        else:
            self.Checkbox = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
