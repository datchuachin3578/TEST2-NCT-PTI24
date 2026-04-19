from PyQt5.QtWidgets import QGraphicsColorizeEffect
from PyQt5.QtGui import QColor

def addHoverEffect(widget, strength=0.35):

    effect = QGraphicsColorizeEffect()
    effect.setColor(QColor(255, 255, 255))  # màu sáng trắng
    effect.setStrength(0)                   # mặc định không sáng
    widget.setGraphicsEffect(effect)

    # Lưu hàm enter/leave cũ nếu có
    old_enter = widget.enterEvent
    old_leave = widget.leaveEvent

    # Hàm khi hover vào
    def enterEvent(event):
        effect.setStrength(strength)
        try:
            old_enter(event)
        except:
            pass

    # Hàm khi rời chuột
    def leaveEvent(event):
        effect.setStrength(0)
        try:
            old_leave(event)
        except:
            pass

    # Gán lại sự kiện
    widget.enterEvent = enterEvent
    widget.leaveEvent = leaveEvent
