import sys
import mysql.connector
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QObject, Signal

version = 'beta 0.0.1'

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="sys"
)
cursor = conn.cursor()

def load_ui(path):
    loader = QUiLoader()
    ui_file = QFile(path)
    ui_file.open(QFile.ReadOnly)
    ui = loader.load(ui_file)
    ui_file.close()
    return ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("main.ui")
        self.setCentralWidget(self.ui)
        self.setCentralWidget(self.ui)
        width = 1100
        height = 450
        self.setFixedSize(width, height)
        self.ui.version.setText(f'версия {version}')
        cursor.execute("""
            SELECT u.Surname, u.Name, u.Patronymic
            FROM sys.Autorization a
            JOIN sys.Users u ON u.ID = a.UserID
            WHERE a.Login = %s
        """, (user,))
        user_SNP = cursor.fetchone()
        print(user_SNP)
        self.ui.label_user.setText(f'Пользователь: {user_SNP[0]} {user_SNP[1]} {user_SNP[2]}')




class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("login.ui")
        self.setCentralWidget(self.ui)
        self.ui.auth.clicked.connect(self.login)
        self.ui.pass_show.toggled.connect(self.toggle_password)
        self.ui.password.setEchoMode(QLineEdit.Password)
        self.setCentralWidget(self.ui)
        width = 500
        height = 250
        self.setFixedSize(width, height)

    def toggle_password(self, checked):
        if checked:
            self.ui.password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)

    def login(self):
        global user
        user = self.ui.login.text()
        password = self.ui.password.text()

        cursor.execute(
            "SELECT password FROM sys.Autorization WHERE login=%s",(user,)
        )
        result = cursor.fetchone()

        if not result or result[0] != password:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль.")
            return

        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
