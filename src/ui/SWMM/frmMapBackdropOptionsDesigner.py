# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui\src\ui\SWMM\frmMapBackdropOptions.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmMapBackdropOptions(object):
    def setupUi(self, frmMapBackdropOptions):
        frmMapBackdropOptions.setObjectName(_fromUtf8("frmMapBackdropOptions"))
        frmMapBackdropOptions.resize(553, 467)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmMapBackdropOptions.setFont(font)
        frmMapBackdropOptions.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralWidget = QtGui.QWidget(frmMapBackdropOptions)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.cmdOK = QtGui.QPushButton(self.centralWidget)
        self.cmdOK.setGeometry(QtCore.QRect(190, 430, 75, 23))
        self.cmdOK.setObjectName(_fromUtf8("cmdOK"))
        self.cmdCancel = QtGui.QPushButton(self.centralWidget)
        self.cmdCancel.setGeometry(QtCore.QRect(290, 430, 75, 23))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.gbxMap = QtGui.QGroupBox(self.centralWidget)
        self.gbxMap.setGeometry(QtCore.QRect(20, 20, 511, 141))
        self.gbxMap.setObjectName(_fromUtf8("gbxMap"))
        self.gbxLLMap = QtGui.QGroupBox(self.gbxMap)
        self.gbxLLMap.setGeometry(QtCore.QRect(20, 30, 231, 91))
        self.gbxLLMap.setObjectName(_fromUtf8("gbxLLMap"))
        self.lblLLX = QtGui.QLabel(self.gbxLLMap)
        self.lblLLX.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.lblLLX.setObjectName(_fromUtf8("lblLLX"))
        self.lblLLY = QtGui.QLabel(self.gbxLLMap)
        self.lblLLY.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.lblLLY.setObjectName(_fromUtf8("lblLLY"))
        self.txtLLXMap = QtGui.QLineEdit(self.gbxLLMap)
        self.txtLLXMap.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.txtLLXMap.setObjectName(_fromUtf8("txtLLXMap"))
        self.txtLLYMap = QtGui.QLineEdit(self.gbxLLMap)
        self.txtLLYMap.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.txtLLYMap.setObjectName(_fromUtf8("txtLLYMap"))
        self.gbxURMap = QtGui.QGroupBox(self.gbxMap)
        self.gbxURMap.setGeometry(QtCore.QRect(260, 30, 231, 91))
        self.gbxURMap.setObjectName(_fromUtf8("gbxURMap"))
        self.lblURX = QtGui.QLabel(self.gbxURMap)
        self.lblURX.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.lblURX.setObjectName(_fromUtf8("lblURX"))
        self.txtURYMap = QtGui.QLineEdit(self.gbxURMap)
        self.txtURYMap.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.txtURYMap.setObjectName(_fromUtf8("txtURYMap"))
        self.txtURXMap = QtGui.QLineEdit(self.gbxURMap)
        self.txtURXMap.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.txtURXMap.setObjectName(_fromUtf8("txtURXMap"))
        self.lblURY = QtGui.QLabel(self.gbxURMap)
        self.lblURY.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.lblURY.setObjectName(_fromUtf8("lblURY"))
        self.lblBackdrop = QtGui.QLabel(self.centralWidget)
        self.lblBackdrop.setGeometry(QtCore.QRect(20, 240, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblBackdrop.setFont(font)
        self.lblBackdrop.setObjectName(_fromUtf8("lblBackdrop"))
        self.txtBackdropFile = QtGui.QLineEdit(self.centralWidget)
        self.txtBackdropFile.setGeometry(QtCore.QRect(150, 240, 381, 20))
        self.txtBackdropFile.setObjectName(_fromUtf8("txtBackdropFile"))
        self.gbxMapUnits = QtGui.QGroupBox(self.centralWidget)
        self.gbxMapUnits.setGeometry(QtCore.QRect(20, 170, 511, 61))
        self.gbxMapUnits.setObjectName(_fromUtf8("gbxMapUnits"))
        self.rbnFeet = QtGui.QRadioButton(self.gbxMapUnits)
        self.rbnFeet.setGeometry(QtCore.QRect(40, 30, 82, 17))
        self.rbnFeet.setObjectName(_fromUtf8("rbnFeet"))
        self.rbnMeters = QtGui.QRadioButton(self.gbxMapUnits)
        self.rbnMeters.setGeometry(QtCore.QRect(140, 30, 82, 17))
        self.rbnMeters.setObjectName(_fromUtf8("rbnMeters"))
        self.rbnDegrees = QtGui.QRadioButton(self.gbxMapUnits)
        self.rbnDegrees.setGeometry(QtCore.QRect(250, 30, 82, 17))
        self.rbnDegrees.setObjectName(_fromUtf8("rbnDegrees"))
        self.rbnNone = QtGui.QRadioButton(self.gbxMapUnits)
        self.rbnNone.setGeometry(QtCore.QRect(370, 30, 82, 17))
        self.rbnNone.setObjectName(_fromUtf8("rbnNone"))
        self.gbxBackdrop = QtGui.QGroupBox(self.centralWidget)
        self.gbxBackdrop.setGeometry(QtCore.QRect(20, 270, 511, 141))
        self.gbxBackdrop.setObjectName(_fromUtf8("gbxBackdrop"))
        self.gbxLLBack = QtGui.QGroupBox(self.gbxBackdrop)
        self.gbxLLBack.setGeometry(QtCore.QRect(20, 30, 231, 91))
        self.gbxLLBack.setObjectName(_fromUtf8("gbxLLBack"))
        self.lblLLXBack = QtGui.QLabel(self.gbxLLBack)
        self.lblLLXBack.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.lblLLXBack.setObjectName(_fromUtf8("lblLLXBack"))
        self.lblLLYBack = QtGui.QLabel(self.gbxLLBack)
        self.lblLLYBack.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.lblLLYBack.setObjectName(_fromUtf8("lblLLYBack"))
        self.txtLLXBack = QtGui.QLineEdit(self.gbxLLBack)
        self.txtLLXBack.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.txtLLXBack.setObjectName(_fromUtf8("txtLLXBack"))
        self.txtLLYBack = QtGui.QLineEdit(self.gbxLLBack)
        self.txtLLYBack.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.txtLLYBack.setObjectName(_fromUtf8("txtLLYBack"))
        self.gbxURBack = QtGui.QGroupBox(self.gbxBackdrop)
        self.gbxURBack.setGeometry(QtCore.QRect(260, 30, 231, 91))
        self.gbxURBack.setObjectName(_fromUtf8("gbxURBack"))
        self.lblURXBack = QtGui.QLabel(self.gbxURBack)
        self.lblURXBack.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.lblURXBack.setObjectName(_fromUtf8("lblURXBack"))
        self.txtURYBack = QtGui.QLineEdit(self.gbxURBack)
        self.txtURYBack.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.txtURYBack.setObjectName(_fromUtf8("txtURYBack"))
        self.txtURXBack = QtGui.QLineEdit(self.gbxURBack)
        self.txtURXBack.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.txtURXBack.setObjectName(_fromUtf8("txtURBack"))
        self.lblURYBack = QtGui.QLabel(self.gbxURBack)
        self.lblURYBack.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.lblURYBack.setObjectName(_fromUtf8("lblURYBack"))
        frmMapBackdropOptions.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmMapBackdropOptions)
        QtCore.QMetaObject.connectSlotsByName(frmMapBackdropOptions)

    def retranslateUi(self, frmMapBackdropOptions):
        frmMapBackdropOptions.setWindowTitle(_translate("frmMapBackdropOptions", "SWMM Map/Backdrop Options", None))
        self.cmdOK.setText(_translate("frmMapBackdropOptions", "OK", None))
        self.cmdCancel.setText(_translate("frmMapBackdropOptions", "Cancel", None))
        self.gbxMap.setTitle(_translate("frmMapBackdropOptions", "Map Dimensions", None))
        self.gbxLLMap.setTitle(_translate("frmMapBackdropOptions", "Lower Left", None))
        self.lblLLX.setText(_translate("frmMapBackdropOptions", "X-Coordinate", None))
        self.lblLLY.setText(_translate("frmMapBackdropOptions", "Y-Coordinate", None))
        self.gbxURMap.setTitle(_translate("frmMapBackdropOptions", "Upper Right", None))
        self.lblURX.setText(_translate("frmMapBackdropOptions", "X-Coordinate", None))
        self.lblURY.setText(_translate("frmMapBackdropOptions", "Y-Coordinate", None))
        self.lblBackdrop.setText(_translate("frmMapBackdropOptions", "Backdrop File Name", None))
        self.gbxMapUnits.setTitle(_translate("frmMapBackdropOptions", "Map Units", None))
        self.rbnFeet.setText(_translate("frmMapBackdropOptions", "Feet", None))
        self.rbnMeters.setText(_translate("frmMapBackdropOptions", "Meters", None))
        self.rbnDegrees.setText(_translate("frmMapBackdropOptions", "Degrees", None))
        self.rbnNone.setText(_translate("frmMapBackdropOptions", "None", None))
        self.gbxBackdrop.setTitle(_translate("frmMapBackdropOptions", "Backdrop Dimensions", None))
        self.gbxLLBack.setTitle(_translate("frmMapBackdropOptions", "Lower Left", None))
        self.lblLLXBack.setText(_translate("frmMapBackdropOptions", "X-Coordinate", None))
        self.lblLLYBack.setText(_translate("frmMapBackdropOptions", "Y-Coordinate", None))
        self.gbxURBack.setTitle(_translate("frmMapBackdropOptions", "Upper Right", None))
        self.lblURXBack.setText(_translate("frmMapBackdropOptions", "X-Coordinate", None))
        self.lblURYBack.setText(_translate("frmMapBackdropOptions", "Y-Coordinate", None))

