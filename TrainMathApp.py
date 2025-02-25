import sys

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi
import random

class MathGUI1(QMainWindow):
    def __init__(self, startInfo):
        super().__init__()
        loadUi("GUI/screen1.ui",self)
        self.startInfo = startInfo
        self.start.clicked.connect(self.submit)

    def submit(self):
        try:
            num = self.lineNumber.text()
            if int(num) > 100:
                self.show_popup("Too many questions!")
                return

            self.startInfo[0] = self.comboBox.currentText()
            self.startInfo[1] = int(num)
            widget.setCurrentIndex(widget.currentIndex()+1)
        except:
            self.show_popup("You must enter number!")

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

    def showEvent(self, a0):
        super().__init__()
        self.lineNumber.setFocus()


class MathGUI2(QMainWindow):
    def __init__(self,startInfo,endInfo):
        super().__init__()
        loadUi("GUI/screen2.ui",self)

        self.clockContinue = True

        self.pushButton.clicked.connect(self.submit)
        self.pushButton_2.clicked.connect(self.support)

        self.reset.clicked.connect(self.moveToScreen1)
        self.stop.clicked.connect(self.control)

    def showEvent(self, a0):
        super().__init__()
        self.lineAnswer.setFocus()
        self.startInfo = startInfo
        self.endInfo = endInfo
        self.notify.setText("")

        self.count = 0
        self.streakRight = 0
        self.streakWrong = 0
        self.sp = 0
        self.error = 0

        self.eachNum.setText(f"{self.count + 1}")
        self.fullNum.setText(f"{startInfo[1]}")

        # Khởi tạo biến cho 2 số
        if startInfo[0] == "Easy":
            self.min = 1
            self.max = 19
        if startInfo[0] == "Normal":
            self.min = 10
            self.max = 49
        if startInfo[0] == "Hard":
            self.min = 100
            self.max = 1000

        self.clockContinue = True
        self.minute = 0
        self.second = 0
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.nextSecond)

        self.checkCreateCal()
        self.moveCalToGUI()

    def moveToScreen1(self):
        widget.setCurrentIndex(widget.currentIndex() -1)

    def nextSecond(self):
        if self.second == 59:
            self.second=0
            self.minute+=1
        else:
            self.second += 1
        self.lcdSecond.display(self.second)
        self.lcdMinute.display(self.minute)

    def control(self):
        if self.clockContinue:
            self.timer.stop()
            self.stop.setText("Continue")
        else:
            self.timer.start(1000)
            self.stop.setText("Stop")
        self.clockContinue = not self.clockContinue
        print("Stop clicked !")

    def createCal(self):
        self.a = random.randint(self.min, self.max)
        self.b = random.randint(self.min, self.max)
        self.operand = random.choice(["+","-"])
        question = str(self.a) + ' ' + self.operand + ' ' + str(self.b)
        self.answer = eval(question)

    def moveCalToGUI(self):
        self.firstNumber.setText(f"{self.a}")
        self.secondNumber.setText(f"{self.b}")
        self.operation.setText(f"{self.operand}")

    def checkCreateCal(self):
        self.createCal()
        if startInfo[0] == "Easy":
            while self.answer < 0 or self.answer > 100:
                self.createCal()
        else:
            while self.answer < 0:
                self.createCal()

    def submit(self):
        # Kiểm tra xem người dùng có nhập số không
        try:
            your_ans = int(self.lineAnswer.text())
        except:
            self.show_popup()
            return
        # Kiểm tra kết quả nhập
        if your_ans == self.answer: # Nếu làm đúng
            self.notify.setText("True")
            self.streakRight += 1
            self.streakWrong = 0
            if self.streakRight >= 10:
                self.label_2.setPixmap(QtGui.QPixmap("source/right-much.png"))
            else:
                self.label_2.setPixmap(QtGui.QPixmap("source/social-credit-right.jpg"))

            self.lineAnswer.setText("")

            # Số câu hỏi hoàn thành
            self.count += 1
            if self.count == startInfo[1]:
                self.notify.setText("Finish")
                self.endInfo[0] = self.startInfo[1]
                self.endInfo[1] = self.minute
                self.endInfo[2] = self.second
                self.endInfo[3] = self.sp
                self.endInfo[4] = self.error
                widget.setCurrentIndex(widget.currentIndex()+1)

            # Không để số âm và lớn hơn 10
            self.checkCreateCal()
            self.moveCalToGUI()
            self.eachNum.setText(f"{self.count + 1}")

        else: # Nếu làm sai
            self.notify.setText("False")
            self.error += 1
            self.streakWrong += 1
            self.streakRight = 0
            if self.streakWrong >= 2:
                self.label_2.setPixmap(QtGui.QPixmap("source/wrong.jpg"))
            else:
                self.label_2.setPixmap(QtGui.QPixmap("source/social-credit-wrong-less.jpg"))
            self.lineAnswer.setText("")

    def support(self):
        self.notify.setText(f"{self.answer}")
        self.sp += 1

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("You must enter number!")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

class MathGUI3(QMainWindow):
    def __init__(self, endInfo):
        super().__init__()
        loadUi("GUI/screen3.ui", self)
        self.pushButton_2.clicked.connect(self.moveToScreen1)

    def moveToScreen1(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

    def showEvent(self, a0):
        super().__init__()
        self.endInfo = endInfo
        self.labelNum.setText(str(self.endInfo[0]))
        self.labelTime.setText(f"{self.endInfo[1]}:{self.endInfo[2]}")
        self.labelSP.setText(str(self.endInfo[3]))
        self.labelError.setText(str(self.endInfo[4]))



if __name__ == "__main__":
    startInfo = ["Easy", 0] #Mode and number of questions
    endInfo = [0, 0, 0, 0, 0]
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()
    win1 = MathGUI1(startInfo)
    win2 = MathGUI2(startInfo,endInfo)
    win3 = MathGUI3(endInfo)

    widget.addWidget(win1)
    widget.addWidget(win2)
    widget.addWidget(win3)
    widget.setWindowTitle("Math Training")
    widget.show()
    sys.exit(app.exec())