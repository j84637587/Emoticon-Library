from PyQt6 import QtWidgets, QtCore, QtGui
from view import Ui_MainWindow
import json
import pyperclip as pc
from notifypy import Notify

emojis = []

def copyEmoji(text: str):
    pc.copy(text)
    notification = Notify()
    notification.title = "顏文字"
    notification.message = f"複製 {text} 至剪貼簿"
    notification.application_name = "顏文字庫"
    notification.send()

def createEmojiBtn(objName: str, text: str):
    _translate = QtCore.QCoreApplication.translate
    btn = QtWidgets.QPushButton(ui.scrollAreaWidgetContents)
    btn.setObjectName(objName)
    btn.setText(_translate("MainWindow", text))
    btn.setMinimumSize(QtCore.QSize(100, 70))
    btn.setMaximumSize(QtCore.QSize(100, 70))
    btn.setStyleSheet("border-radius: 10px;border: none;background-color: #82929A;")
    btn.clicked.connect(lambda: copyEmoji(text)) 
    return btn


def loadEmojis():
    file = open("emojis.json", "r", encoding="utf-8")
    return json.load(file)


def initGui(ui):
    emojis = loadEmojis()

    for idx, emoji in enumerate(emojis):
        if idx % 5 == 0:
            for j in range(5):
                ui.si = QtWidgets.QSpacerItem(
                    0,
                    20,
                    QtWidgets.QSizePolicy.Policy.Minimum,
                    QtWidgets.QSizePolicy.Policy.Fixed,
                )
                ui.emojiGridLayout.addItem(ui.si, int(int(idx / 5) * 2), 1 + j, 1, 1)
        ui.pushButton = createEmojiBtn(f"pushButton_{idx}", emoji['text'])
        ui.emojiGridLayout.addWidget(ui.pushButton, int(int(idx / 5) * 2 + 1), int(idx % 5 + 1), 1, 1)
        print(emoji['text'], idx, int(int(idx / 5) * 2 + 1), int((idx % 5) + 1))

    # for i in range(20):
    #     for j in range(5):
    #         if i % 2 == 0:
    #             ui.pushButton = createEmojiBtn(f"pushButton_{i}_{j}", f"pushButton_{i}_{j}")
    #             ui.emojiGridLayout.addWidget(ui.pushButton, 6 + i, 1 + j, 1, 1)
    #         else: # spacer
    #             ui.si = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
    #             ui.emojiGridLayout.addItem(ui.si, 6 + i, 1 + j, 1, 1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    initGui(ui)
    ui.statusbar.showMessage("MIT License Copyright (c) 2022 SpicyRat")
    MainWindow.show()
    sys.exit(app.exec())
