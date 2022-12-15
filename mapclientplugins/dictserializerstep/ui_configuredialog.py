# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditIdentifier)

        self.checkBoxDefaultLocation = QCheckBox(self.configGroupBox)
        self.checkBoxDefaultLocation.setObjectName(u"checkBoxDefaultLocation")
        self.checkBoxDefaultLocation.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.checkBoxDefaultLocation)

        self.label0_2 = QLabel(self.configGroupBox)
        self.label0_2.setObjectName(u"label0_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label0_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditOutputLocation = QLineEdit(self.configGroupBox)
        self.lineEditOutputLocation.setObjectName(u"lineEditOutputLocation")

        self.horizontalLayout.addWidget(self.lineEditOutputLocation)

        self.pushButtonOutputLocation = QPushButton(self.configGroupBox)
        self.pushButtonOutputLocation.setObjectName(u"pushButtonOutputLocation")

        self.horizontalLayout.addWidget(self.pushButtonOutputLocation)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)


        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Dict Serializer", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.checkBoxDefaultLocation.setText(QCoreApplication.translate("ConfigureDialog", u"Use output default location", None))
        self.label0_2.setText(QCoreApplication.translate("ConfigureDialog", u"Output File:  ", None))
        self.pushButtonOutputLocation.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
    # retranslateUi

