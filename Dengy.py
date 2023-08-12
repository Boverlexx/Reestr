# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dengy.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_Dengy(object):
    def setupUi(self, Dengy):
        if not Dengy.objectName():
            Dengy.setObjectName(u"Dengy")
        Dengy.setEnabled(True)
        Dengy.resize(518, 613)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dengy.sizePolicy().hasHeightForWidth())
        Dengy.setSizePolicy(sizePolicy)
        Dengy.setMinimumSize(QSize(518, 570))
        Dengy.setMaximumSize(QSize(518, 613))
        icon = QIcon()
        icon.addFile(u"Image/russian.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dengy.setWindowIcon(icon)
        self.centralwidget = QWidget(Dengy)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(400, 570))
        self.centralwidget.setMaximumSize(QSize(518, 600))
        self.verticalLayout_28 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 600))
        self.tabWidget.setMaximumSize(QSize(16777215, 600))
        self.tabWidget.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.tabWidget.setIconSize(QSize(24, 24))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(0, 550))
        self.tab.setMaximumSize(QSize(16777215, 550))
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.verticalLayout_43 = QVBoxLayout(self.groupBox)
        self.verticalLayout_43.setSpacing(2)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_open_ved = QPushButton(self.groupBox)
        self.pushButton_open_ved.setObjectName(u"pushButton_open_ved")
        sizePolicy.setHeightForWidth(self.pushButton_open_ved.sizePolicy().hasHeightForWidth())
        self.pushButton_open_ved.setSizePolicy(sizePolicy)
        self.pushButton_open_ved.setMinimumSize(QSize(150, 27))
        self.pushButton_open_ved.setMaximumSize(QSize(122, 27))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton_open_ved.setFont(font1)
        self.pushButton_open_ved.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_open_ved.setStyleSheet(u"background-color: rgb(170, 255, 127);")

        self.verticalLayout_5.addWidget(self.pushButton_open_ved, 0, Qt.AlignHCenter)

        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.textEdit)


        self.verticalLayout_43.addLayout(self.verticalLayout_5)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit_book = QLineEdit(self.groupBox)
        self.lineEdit_book.setObjectName(u"lineEdit_book")
        self.lineEdit_book.setFont(font1)
        self.lineEdit_book.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.lineEdit_book)


        self.verticalLayout_43.addLayout(self.horizontalLayout_4)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spinBox_column_start = QSpinBox(self.groupBox)
        self.spinBox_column_start.setObjectName(u"spinBox_column_start")
        sizePolicy.setHeightForWidth(self.spinBox_column_start.sizePolicy().hasHeightForWidth())
        self.spinBox_column_start.setSizePolicy(sizePolicy)
        self.spinBox_column_start.setMinimumSize(QSize(70, 25))
        self.spinBox_column_start.setMaximumSize(QSize(70, 25))
        self.spinBox_column_start.setFont(font1)
        self.spinBox_column_start.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_column_start.setMaximum(99999)

        self.verticalLayout.addWidget(self.spinBox_column_start)

        self.spinBox_column_start_2 = QSpinBox(self.groupBox)
        self.spinBox_column_start_2.setObjectName(u"spinBox_column_start_2")
        sizePolicy.setHeightForWidth(self.spinBox_column_start_2.sizePolicy().hasHeightForWidth())
        self.spinBox_column_start_2.setSizePolicy(sizePolicy)
        self.spinBox_column_start_2.setMinimumSize(QSize(70, 25))
        self.spinBox_column_start_2.setMaximumSize(QSize(70, 25))
        self.spinBox_column_start_2.setFont(font1)
        self.spinBox_column_start_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_column_start_2.setMaximum(99999)

        self.verticalLayout.addWidget(self.spinBox_column_start_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.spinBox_row_start = QSpinBox(self.groupBox)
        self.spinBox_row_start.setObjectName(u"spinBox_row_start")
        sizePolicy.setHeightForWidth(self.spinBox_row_start.sizePolicy().hasHeightForWidth())
        self.spinBox_row_start.setSizePolicy(sizePolicy)
        self.spinBox_row_start.setMinimumSize(QSize(70, 25))
        self.spinBox_row_start.setMaximumSize(QSize(70, 25))
        self.spinBox_row_start.setFont(font1)
        self.spinBox_row_start.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_row_start.setMaximum(99999)

        self.verticalLayout_3.addWidget(self.spinBox_row_start)

        self.spinBox_row_finish = QSpinBox(self.groupBox)
        self.spinBox_row_finish.setObjectName(u"spinBox_row_finish")
        sizePolicy.setHeightForWidth(self.spinBox_row_finish.sizePolicy().hasHeightForWidth())
        self.spinBox_row_finish.setSizePolicy(sizePolicy)
        self.spinBox_row_finish.setMinimumSize(QSize(70, 25))
        self.spinBox_row_finish.setMaximumSize(QSize(70, 25))
        self.spinBox_row_finish.setFont(font1)
        self.spinBox_row_finish.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_row_finish.setMaximum(99999)

        self.verticalLayout_3.addWidget(self.spinBox_row_finish)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_43.addLayout(self.horizontalLayout_3)

        self.line_9 = QFrame(self.groupBox)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line_9)

        self.label_info = QLabel(self.groupBox)
        self.label_info.setObjectName(u"label_info")
        sizePolicy2.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy2)
        self.label_info.setMinimumSize(QSize(0, 30))
        self.label_info.setFont(font1)
        self.label_info.setLayoutDirection(Qt.LeftToRight)
        self.label_info.setStyleSheet(u"background-color: rgb(170, 255, 127);\n"
"color: rgb(85, 0, 255);")
        self.label_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_info.setWordWrap(False)

        self.verticalLayout_43.addWidget(self.label_info)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_34.setSpacing(2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_open_reestr = QPushButton(self.groupBox_2)
        self.pushButton_open_reestr.setObjectName(u"pushButton_open_reestr")
        sizePolicy.setHeightForWidth(self.pushButton_open_reestr.sizePolicy().hasHeightForWidth())
        self.pushButton_open_reestr.setSizePolicy(sizePolicy)
        self.pushButton_open_reestr.setMinimumSize(QSize(150, 27))
        self.pushButton_open_reestr.setMaximumSize(QSize(122, 27))
        self.pushButton_open_reestr.setFont(font1)
        self.pushButton_open_reestr.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_open_reestr.setStyleSheet(u"background-color: rgb(255, 92, 28);")

        self.verticalLayout_6.addWidget(self.pushButton_open_reestr, 0, Qt.AlignHCenter)

        self.textEdit_2 = QTextEdit(self.groupBox_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy2.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy2)
        self.textEdit_2.setMinimumSize(QSize(0, 0))
        self.textEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_2.setFont(font2)
        self.textEdit_2.setStyleSheet(u"background-color: rgb(255, 92, 28);")

        self.verticalLayout_6.addWidget(self.textEdit_2)


        self.verticalLayout_34.addLayout(self.verticalLayout_6)

        self.line_19 = QFrame(self.groupBox_2)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_19)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_27 = QLabel(self.groupBox_2)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setFont(font1)

        self.horizontalLayout_23.addWidget(self.label_27)

        self.lineEdit_book_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_book_3.setObjectName(u"lineEdit_book_3")
        self.lineEdit_book_3.setFont(font1)
        self.lineEdit_book_3.setStyleSheet(u"background-color: rgb(255, 92, 28);")

        self.horizontalLayout_23.addWidget(self.lineEdit_book_3)


        self.verticalLayout_34.addLayout(self.horizontalLayout_23)

        self.line_20 = QFrame(self.groupBox_2)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_20)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_23)

        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_24)


        self.horizontalLayout_21.addLayout(self.verticalLayout_9)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.spinBox_column_start_11 = QSpinBox(self.groupBox_2)
        self.spinBox_column_start_11.setObjectName(u"spinBox_column_start_11")
        sizePolicy.setHeightForWidth(self.spinBox_column_start_11.sizePolicy().hasHeightForWidth())
        self.spinBox_column_start_11.setSizePolicy(sizePolicy)
        self.spinBox_column_start_11.setMinimumSize(QSize(70, 25))
        self.spinBox_column_start_11.setMaximumSize(QSize(70, 25))
        self.spinBox_column_start_11.setFont(font1)
        self.spinBox_column_start_11.setStyleSheet(u"background-color: rgb(255, 92, 28);")
        self.spinBox_column_start_11.setMaximum(99999)

        self.verticalLayout_30.addWidget(self.spinBox_column_start_11)

        self.spinBox_column_start_12 = QSpinBox(self.groupBox_2)
        self.spinBox_column_start_12.setObjectName(u"spinBox_column_start_12")
        sizePolicy.setHeightForWidth(self.spinBox_column_start_12.sizePolicy().hasHeightForWidth())
        self.spinBox_column_start_12.setSizePolicy(sizePolicy)
        self.spinBox_column_start_12.setMinimumSize(QSize(70, 25))
        self.spinBox_column_start_12.setMaximumSize(QSize(70, 25))
        self.spinBox_column_start_12.setFont(font1)
        self.spinBox_column_start_12.setStyleSheet(u"background-color: rgb(255, 92, 28);")
        self.spinBox_column_start_12.setMaximum(99999)

        self.verticalLayout_30.addWidget(self.spinBox_column_start_12)


        self.horizontalLayout_21.addLayout(self.verticalLayout_30)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setFont(font1)

        self.verticalLayout_31.addWidget(self.label_25)

        self.label_26 = QLabel(self.groupBox_2)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setFont(font1)

        self.verticalLayout_31.addWidget(self.label_26)


        self.horizontalLayout_22.addLayout(self.verticalLayout_31)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.spinBox_row_start_6 = QSpinBox(self.groupBox_2)
        self.spinBox_row_start_6.setObjectName(u"spinBox_row_start_6")
        sizePolicy.setHeightForWidth(self.spinBox_row_start_6.sizePolicy().hasHeightForWidth())
        self.spinBox_row_start_6.setSizePolicy(sizePolicy)
        self.spinBox_row_start_6.setMinimumSize(QSize(70, 25))
        self.spinBox_row_start_6.setMaximumSize(QSize(70, 25))
        self.spinBox_row_start_6.setFont(font1)
        self.spinBox_row_start_6.setStyleSheet(u"background-color: rgb(255, 92, 28);")
        self.spinBox_row_start_6.setMaximum(99999)

        self.verticalLayout_32.addWidget(self.spinBox_row_start_6)

        self.spinBox_row_finish_6 = QSpinBox(self.groupBox_2)
        self.spinBox_row_finish_6.setObjectName(u"spinBox_row_finish_6")
        sizePolicy.setHeightForWidth(self.spinBox_row_finish_6.sizePolicy().hasHeightForWidth())
        self.spinBox_row_finish_6.setSizePolicy(sizePolicy)
        self.spinBox_row_finish_6.setMinimumSize(QSize(70, 25))
        self.spinBox_row_finish_6.setMaximumSize(QSize(70, 25))
        self.spinBox_row_finish_6.setFont(font1)
        self.spinBox_row_finish_6.setStyleSheet(u"background-color: rgb(255, 92, 28);")
        self.spinBox_row_finish_6.setMaximum(99999)

        self.verticalLayout_32.addWidget(self.spinBox_row_finish_6)


        self.horizontalLayout_22.addLayout(self.verticalLayout_32)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_22)


        self.verticalLayout_34.addLayout(self.horizontalLayout_20)

        self.label_info_4 = QLabel(self.groupBox_2)
        self.label_info_4.setObjectName(u"label_info_4")
        sizePolicy2.setHeightForWidth(self.label_info_4.sizePolicy().hasHeightForWidth())
        self.label_info_4.setSizePolicy(sizePolicy2)
        self.label_info_4.setMinimumSize(QSize(0, 30))
        self.label_info_4.setFont(font1)
        self.label_info_4.setLayoutDirection(Qt.LeftToRight)
        self.label_info_4.setStyleSheet(u"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_info_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_info_4.setWordWrap(False)

        self.verticalLayout_34.addWidget(self.label_info_4)

        self.line_4 = QFrame(self.groupBox_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_4)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_vnesti = QPushButton(self.tab)
        self.pushButton_vnesti.setObjectName(u"pushButton_vnesti")
        sizePolicy.setHeightForWidth(self.pushButton_vnesti.sizePolicy().hasHeightForWidth())
        self.pushButton_vnesti.setSizePolicy(sizePolicy)
        self.pushButton_vnesti.setMinimumSize(QSize(120, 27))
        self.pushButton_vnesti.setMaximumSize(QSize(120, 27))
        self.pushButton_vnesti.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_vnesti)

        self.pushButton_cancel = QPushButton(self.tab)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        self.pushButton_cancel.setMinimumSize(QSize(120, 27))
        self.pushButton_cancel.setMaximumSize(QSize(120, 27))
        self.pushButton_cancel.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_cancel)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        icon1 = QIcon()
        icon1.addFile(u"Image/PSB.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setMinimumSize(QSize(0, 550))
        self.tab_2.setMaximumSize(QSize(16777215, 550))
        self.verticalLayout_29 = QVBoxLayout(self.tab_2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.verticalLayout_44 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_44.setSpacing(2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.pushButton_open_ved_3 = QPushButton(self.groupBox_5)
        self.pushButton_open_ved_3.setObjectName(u"pushButton_open_ved_3")
        sizePolicy.setHeightForWidth(self.pushButton_open_ved_3.sizePolicy().hasHeightForWidth())
        self.pushButton_open_ved_3.setSizePolicy(sizePolicy)
        self.pushButton_open_ved_3.setMinimumSize(QSize(150, 27))
        self.pushButton_open_ved_3.setMaximumSize(QSize(122, 27))
        self.pushButton_open_ved_3.setFont(font1)
        self.pushButton_open_ved_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_open_ved_3.setStyleSheet(u"background-color: rgb(170, 255, 127);")

        self.verticalLayout_21.addWidget(self.pushButton_open_ved_3, 0, Qt.AlignHCenter)

        self.textEdit_5 = QTextEdit(self.groupBox_5)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setFont(font2)
        self.textEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_21.addWidget(self.textEdit_5)


        self.verticalLayout_44.addLayout(self.verticalLayout_21)

        self.line_11 = QFrame(self.groupBox_5)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_15)

        self.lineEdit_book_5 = QLineEdit(self.groupBox_5)
        self.lineEdit_book_5.setObjectName(u"lineEdit_book_5")
        self.lineEdit_book_5.setFont(font1)
        self.lineEdit_book_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.lineEdit_book_5)


        self.verticalLayout_44.addLayout(self.horizontalLayout_14)

        self.line_12 = QFrame(self.groupBox_5)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_12)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setFont(font1)

        self.verticalLayout_22.addWidget(self.label_16)

        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setFont(font1)

        self.verticalLayout_22.addWidget(self.label_17)


        self.horizontalLayout_16.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.spinBox_column_start_7 = QSpinBox(self.groupBox_5)
        self.spinBox_column_start_7.setObjectName(u"spinBox_column_start_7")
        sizePolicy.setHeightForWidth(self.spinBox_column_start_7.sizePolicy().hasHeightForWidth())
        self.spinBox_column_start_7.setSizePolicy(sizePolicy)
        self.spinBox_column_start_7.setMinimumSize(QSize(70, 25))
        self.spinBox_column_start_7.setMaximumSize(QSize(70, 25))
        self.spinBox_column_start_7.setFont(font1)
        self.spinBox_column_start_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_column_start_7.setMaximum(99999)

        self.verticalLayout_23.addWidget(self.spinBox_column_start_7)

        self.spinBox_column_start_8 = QSpinBox(self.groupBox_5)
        self.spinBox_column_start_8.setObjectName(u"spinBox_column_start_8")
        sizePolicy.setHeightForWidth(self.spinBox_column_start_8.sizePolicy().hasHeightForWidth())
        self.spinBox_column_start_8.setSizePolicy(sizePolicy)
        self.spinBox_column_start_8.setMinimumSize(QSize(70, 25))
        self.spinBox_column_start_8.setMaximumSize(QSize(70, 25))
        self.spinBox_column_start_8.setFont(font1)
        self.spinBox_column_start_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_column_start_8.setMaximum(99999)

        self.verticalLayout_23.addWidget(self.spinBox_column_start_8)


        self.horizontalLayout_16.addLayout(self.verticalLayout_23)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setFont(font1)

        self.verticalLayout_24.addWidget(self.label_18)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setFont(font1)

        self.verticalLayout_24.addWidget(self.label_19)


        self.horizontalLayout_17.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.spinBox_row_start_4 = QSpinBox(self.groupBox_5)
        self.spinBox_row_start_4.setObjectName(u"spinBox_row_start_4")
        sizePolicy.setHeightForWidth(self.spinBox_row_start_4.sizePolicy().hasHeightForWidth())
        self.spinBox_row_start_4.setSizePolicy(sizePolicy)
        self.spinBox_row_start_4.setMinimumSize(QSize(70, 25))
        self.spinBox_row_start_4.setMaximumSize(QSize(70, 25))
        self.spinBox_row_start_4.setFont(font1)
        self.spinBox_row_start_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_row_start_4.setMaximum(99999)

        self.verticalLayout_25.addWidget(self.spinBox_row_start_4)

        self.spinBox_row_finish_4 = QSpinBox(self.groupBox_5)
        self.spinBox_row_finish_4.setObjectName(u"spinBox_row_finish_4")
        sizePolicy.setHeightForWidth(self.spinBox_row_finish_4.sizePolicy().hasHeightForWidth())
        self.spinBox_row_finish_4.setSizePolicy(sizePolicy)
        self.spinBox_row_finish_4.setMinimumSize(QSize(70, 25))
        self.spinBox_row_finish_4.setMaximumSize(QSize(70, 25))
        self.spinBox_row_finish_4.setFont(font1)
        self.spinBox_row_finish_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_row_finish_4.setMaximum(99999)

        self.verticalLayout_25.addWidget(self.spinBox_row_finish_4)


        self.horizontalLayout_17.addLayout(self.verticalLayout_25)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_17)


        self.verticalLayout_44.addLayout(self.horizontalLayout_15)

        self.line_13 = QFrame(self.groupBox_5)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_13)

        self.label_info_3 = QLabel(self.groupBox_5)
        self.label_info_3.setObjectName(u"label_info_3")
        sizePolicy2.setHeightForWidth(self.label_info_3.sizePolicy().hasHeightForWidth())
        self.label_info_3.setSizePolicy(sizePolicy2)
        self.label_info_3.setMinimumSize(QSize(0, 30))
        self.label_info_3.setFont(font1)
        self.label_info_3.setLayoutDirection(Qt.LeftToRight)
        self.label_info_3.setStyleSheet(u"background-color: rgb(170, 255, 127);\n"
"color: rgb(85, 0, 255);")
        self.label_info_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_info_3.setWordWrap(False)

        self.verticalLayout_44.addWidget(self.label_info_3)


        self.verticalLayout_29.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.verticalLayout_39 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_39.setSpacing(2)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.pushButton_open_reestr1_3 = QPushButton(self.groupBox_6)
        self.pushButton_open_reestr1_3.setObjectName(u"pushButton_open_reestr1_3")
        sizePolicy.setHeightForWidth(self.pushButton_open_reestr1_3.sizePolicy().hasHeightForWidth())
        self.pushButton_open_reestr1_3.setSizePolicy(sizePolicy)
        self.pushButton_open_reestr1_3.setMinimumSize(QSize(150, 27))
        self.pushButton_open_reestr1_3.setMaximumSize(QSize(122, 27))
        self.pushButton_open_reestr1_3.setFont(font1)
        self.pushButton_open_reestr1_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_open_reestr1_3.setStyleSheet(u"background-color: rgb(255, 92, 28);")

        self.verticalLayout_26.addWidget(self.pushButton_open_reestr1_3, 0, Qt.AlignHCenter)

        self.textEdit_6 = QTextEdit(self.groupBox_6)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setFont(font2)
        self.textEdit_6.setStyleSheet(u"background-color: rgb(255, 92, 28);")

        self.verticalLayout_26.addWidget(self.textEdit_6)


        self.verticalLayout_39.addLayout(self.verticalLayout_26)

        self.line_23 = QFrame(self.groupBox_6)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_23)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_33 = QLabel(self.groupBox_6)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setFont(font1)

        self.horizontalLayout_28.addWidget(self.label_33)

        self.lineEdit_book_6 = QLineEdit(self.groupBox_6)
        self.lineEdit_book_6.setObjectName(u"lineEdit_book_6")
        self.lineEdit_book_6.setFont(font1)
        self.lineEdit_book_6.setStyleSheet(u"background-color: rgb(255, 92, 28);")

        self.horizontalLayout_28.addWidget(self.lineEdit_book_6)


        self.verticalLayout_39.addLayout(self.horizontalLayout_28)

        self.line_24 = QFrame(self.groupBox_6)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_24)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_34 = QLabel(self.groupBox_6)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setFont(font1)

        self.verticalLayout_27.addWidget(self.label_34)

        self.label_35 = QLabel(self.groupBox_6)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setFont(font1)

        self.verticalLayout_27.addWidget(self.label_35)


        self.horizontalLayout_30.addLayout(self.verticalLayout_27)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.spinBox_column_start_15 = QSpinBox(self.groupBox_6)
        self.spinBox_column_start_15.setObjectName(u"spinBox_column_start_15")
        sizePolicy.setHeightForWidth(self.spinBox_column_start_15.sizePolicy().hasHeightForWidth())
        self.spinBox_column_start_15.setSizePolicy(sizePolicy)
        self.spinBox_column_start_15.setMinimumSize(QSize(70, 25))
        self.spinBox_column_start_15.setMaximumSize(QSize(70, 25))
        self.spinBox_column_start_15.setFont(font1)
        self.spinBox_column_start_15.setStyleSheet(u"background-color: rgb(255, 92, 28);")
        self.spinBox_column_start_15.setMaximum(99999)

        self.verticalLayout_40.addWidget(self.spinBox_column_start_15)

        self.spinBox_column_start_16 = QSpinBox(self.groupBox_6)
        self.spinBox_column_start_16.setObjectName(u"spinBox_column_start_16")
        sizePolicy.setHeightForWidth(self.spinBox_column_start_16.sizePolicy().hasHeightForWidth())
        self.spinBox_column_start_16.setSizePolicy(sizePolicy)
        self.spinBox_column_start_16.setMinimumSize(QSize(70, 25))
        self.spinBox_column_start_16.setMaximumSize(QSize(70, 25))
        self.spinBox_column_start_16.setFont(font1)
        self.spinBox_column_start_16.setStyleSheet(u"background-color: rgb(255, 92, 28);")
        self.spinBox_column_start_16.setMaximum(99999)

        self.verticalLayout_40.addWidget(self.spinBox_column_start_16)


        self.horizontalLayout_30.addLayout(self.verticalLayout_40)


        self.horizontalLayout_29.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(3)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_36 = QLabel(self.groupBox_6)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setFont(font1)

        self.verticalLayout_41.addWidget(self.label_36)

        self.label_37 = QLabel(self.groupBox_6)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setFont(font1)

        self.verticalLayout_41.addWidget(self.label_37)


        self.horizontalLayout_31.addLayout(self.verticalLayout_41)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.spinBox_row_start_8 = QSpinBox(self.groupBox_6)
        self.spinBox_row_start_8.setObjectName(u"spinBox_row_start_8")
        sizePolicy.setHeightForWidth(self.spinBox_row_start_8.sizePolicy().hasHeightForWidth())
        self.spinBox_row_start_8.setSizePolicy(sizePolicy)
        self.spinBox_row_start_8.setMinimumSize(QSize(70, 25))
        self.spinBox_row_start_8.setMaximumSize(QSize(70, 25))
        self.spinBox_row_start_8.setFont(font1)
        self.spinBox_row_start_8.setStyleSheet(u"background-color: rgb(255, 92, 28);")
        self.spinBox_row_start_8.setMaximum(99999)

        self.verticalLayout_42.addWidget(self.spinBox_row_start_8)

        self.spinBox_row_finish_8 = QSpinBox(self.groupBox_6)
        self.spinBox_row_finish_8.setObjectName(u"spinBox_row_finish_8")
        sizePolicy.setHeightForWidth(self.spinBox_row_finish_8.sizePolicy().hasHeightForWidth())
        self.spinBox_row_finish_8.setSizePolicy(sizePolicy)
        self.spinBox_row_finish_8.setMinimumSize(QSize(70, 25))
        self.spinBox_row_finish_8.setMaximumSize(QSize(70, 25))
        self.spinBox_row_finish_8.setFont(font1)
        self.spinBox_row_finish_8.setStyleSheet(u"background-color: rgb(255, 92, 28);")
        self.spinBox_row_finish_8.setMaximum(99999)

        self.verticalLayout_42.addWidget(self.spinBox_row_finish_8)


        self.horizontalLayout_31.addLayout(self.verticalLayout_42)


        self.horizontalLayout_29.addLayout(self.horizontalLayout_31)


        self.verticalLayout_39.addLayout(self.horizontalLayout_29)

        self.line_15 = QFrame(self.groupBox_6)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_15)

        self.label_info_5 = QLabel(self.groupBox_6)
        self.label_info_5.setObjectName(u"label_info_5")
        sizePolicy2.setHeightForWidth(self.label_info_5.sizePolicy().hasHeightForWidth())
        self.label_info_5.setSizePolicy(sizePolicy2)
        self.label_info_5.setMinimumSize(QSize(0, 30))
        self.label_info_5.setFont(font1)
        self.label_info_5.setLayoutDirection(Qt.LeftToRight)
        self.label_info_5.setStyleSheet(u"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_info_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_info_5.setWordWrap(False)

        self.verticalLayout_39.addWidget(self.label_info_5)


        self.verticalLayout_29.addWidget(self.groupBox_6)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_vnesti_3 = QPushButton(self.tab_2)
        self.pushButton_vnesti_3.setObjectName(u"pushButton_vnesti_3")
        sizePolicy.setHeightForWidth(self.pushButton_vnesti_3.sizePolicy().hasHeightForWidth())
        self.pushButton_vnesti_3.setSizePolicy(sizePolicy)
        self.pushButton_vnesti_3.setMinimumSize(QSize(120, 27))
        self.pushButton_vnesti_3.setMaximumSize(QSize(120, 27))
        self.pushButton_vnesti_3.setFont(font1)

        self.horizontalLayout_18.addWidget(self.pushButton_vnesti_3)

        self.pushButton_cancel_3 = QPushButton(self.tab_2)
        self.pushButton_cancel_3.setObjectName(u"pushButton_cancel_3")
        sizePolicy.setHeightForWidth(self.pushButton_cancel_3.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel_3.setSizePolicy(sizePolicy)
        self.pushButton_cancel_3.setMinimumSize(QSize(120, 27))
        self.pushButton_cancel_3.setMaximumSize(QSize(120, 27))
        self.pushButton_cancel_3.setFont(font1)

        self.horizontalLayout_18.addWidget(self.pushButton_cancel_3)


        self.verticalLayout_29.addLayout(self.horizontalLayout_18)

        self.line_14 = QFrame(self.tab_2)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_29.addWidget(self.line_14)

        icon2 = QIcon()
        icon2.addFile(u"Image/calculate.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")

        self.verticalLayout_28.addWidget(self.tabWidget)

        Dengy.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Dengy)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 518, 22))
        Dengy.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Dengy)
        self.statusbar.setObjectName(u"statusbar")
        Dengy.setStatusBar(self.statusbar)

        self.retranslateUi(Dengy)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dengy)
    # setupUi

    def retranslateUi(self, Dengy):
        Dengy.setWindowTitle(QCoreApplication.translate("Dengy", u"\u0414\u0435\u043d\u044c\u0433\u0438", None))
        self.tabWidget.setWindowTitle(QCoreApplication.translate("Dengy", u"\u0414\u0435\u043d\u044c\u0433\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dengy", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0444\u0430\u0439\u043b\u0430 \u0432\u0435\u0434\u043e\u043c\u043e\u0441\u0442\u0438", None))
        self.pushButton_open_ved.setText(QCoreApplication.translate("Dengy", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432\u0435\u0434\u043e\u043c\u043e\u0441\u0442\u044c", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dengy", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dengy", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043a\u043d\u0438\u0433\u0438!!!", None))
        self.lineEdit_book.setText("")
        self.label_2.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u0441 \u2116 \u0441\u0447\u0435\u0442\u043e\u0432", None))
        self.label_6.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u0441 \u0441\u0443\u043c\u043c\u0430\u043c\u0438", None))
        self.label_5.setText(QCoreApplication.translate("Dengy", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.label_info.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Dengy", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0444\u0430\u0439\u043b\u0430 \u0440\u0435\u0435\u0441\u0442\u0440\u0430", None))
        self.pushButton_open_reestr.setText(QCoreApplication.translate("Dengy", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0440\u0435\u0435\u0441\u0442\u0440", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Dengy", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("Dengy", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043a\u043d\u0438\u0433\u0438!!!", None))
        self.lineEdit_book_3.setText("")
        self.label_23.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u0441 \u2116 \u0441\u0447\u0435\u0442\u043e\u0432", None))
        self.label_24.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u0441 \u0441\u0443\u043c\u043c\u0430\u043c\u0438", None))
        self.label_25.setText(QCoreApplication.translate("Dengy", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.label_26.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.label_info_4.setText("")
        self.pushButton_vnesti.setText(QCoreApplication.translate("Dengy", u"\u0412\u043d\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dengy", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dengy", u"\u0420\u0435\u0435\u0441\u0442\u0440", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dengy", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0444\u0430\u0439\u043b\u0430 \u0432\u0435\u0434\u043e\u043c\u043e\u0441\u0442\u0438", None))
        self.pushButton_open_ved_3.setText(QCoreApplication.translate("Dengy", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432\u0435\u0434\u043e\u043c\u043e\u0441\u0442\u044c", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("Dengy", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Dengy", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043a\u043d\u0438\u0433\u0438!!!", None))
        self.lineEdit_book_5.setText("")
        self.label_16.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u0441 \u2116 \u0441\u0447\u0435\u0442\u043e\u0432", None))
        self.label_17.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u0441 \u0441\u0443\u043c\u043c\u0430\u043c\u0438", None))
        self.label_18.setText(QCoreApplication.translate("Dengy", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.label_19.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.label_info_3.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Dengy", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0444\u0430\u0439\u043b\u0430 \u0440\u0435\u0435\u0441\u0442\u0440\u0430", None))
        self.pushButton_open_reestr1_3.setText(QCoreApplication.translate("Dengy", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0440\u0435\u0435\u0441\u0442\u0440", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("Dengy", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("Dengy", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043a\u043d\u0438\u0433\u0438!!!", None))
        self.lineEdit_book_6.setText("")
        self.label_34.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u0441 \u2116 \u0441\u0447\u0435\u0442\u043e\u0432", None))
        self.label_35.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u0441 \u0441\u0443\u043c\u043c\u0430\u043c\u0438", None))
        self.label_36.setText(QCoreApplication.translate("Dengy", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.label_37.setText(QCoreApplication.translate("Dengy", u"\u041a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.label_info_5.setText("")
        self.pushButton_vnesti_3.setText(QCoreApplication.translate("Dengy", u"\u0412\u043d\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButton_cancel_3.setText(QCoreApplication.translate("Dengy", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dengy", u"\u0412\u0435\u0434\u043e\u043c\u043e\u0441\u0442\u044c", None))
    # retranslateUi

