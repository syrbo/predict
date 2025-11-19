# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1095, 472)
        self.tableWidget = QTableWidget(Widget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        font = QFont()
        font.setBold(False)
        font.setStrikeOut(False)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(15, 80, 611, 331))
        self.comboBox = QComboBox(Widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 40, 171, 31))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(17, 39, 71, 31))
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 40, 351, 31))
        self.tableWidget_2 = QTableWidget(Widget)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(640, 40, 441, 371))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(640, 10, 161, 21))
        self.label_user = QLabel(Widget)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setGeometry(QRect(640, 420, 251, 21))
        self.label_user.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setBold(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_user.setFont(font1)
        self.label_user.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_user.setScaledContents(False)
        self.label_role = QLabel(Widget)
        self.label_role.setObjectName(u"label_role")
        self.label_role.setGeometry(QRect(910, 420, 171, 21))
        self.version = QLabel(Widget)
        self.version.setObjectName(u"version")
        self.version.setGeometry(QRect(20, 420, 161, 21))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0424\u043e\u0440\u043c\u0430 \u0441\u043a\u043b\u0430\u0434\u0441\u043a\u043e\u0433\u043e \u0440\u0435\u0436\u0438\u043c\u0430", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"\u0426\u0435\u043d\u0430", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"\u041a\u043e\u043b-\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"\u0413\u0430\u0440\u0430\u043d\u0442\u0438\u044f", None));
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"...\u0430\u0440\u0442\u0438\u043a\u0443\u043b\u0443", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"...\u0438\u043c\u0435\u043d\u0438", None))

        self.label.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0442\u043e\u0432\u0430\u0440\u0430:", None))
        self.label_user.setText("")
        self.label_role.setText(QCoreApplication.translate("Widget", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0440\u043e\u043b\u044c: ", None))
        self.version.setText("")
    # retranslateUi

