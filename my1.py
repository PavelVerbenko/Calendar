from PyQt5 import uic# я загрузил код который выводит визуализацию приложения с PyQt5 designer
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("treker.ui")#Написал название своего кода

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
# Загрузил все библиотеки которые нужны были для работы