from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QRadioButton, QButtonGroup
from PyQt5.QtGui import QPixmap, QIcon
from test import tests 

class TestApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.current_test = 0
        self.tests = tests
        self.correct_answers = 0  

        self.label = QLabel(self)
        pixmap = QPixmap("minimalist.jpg")
        self.label.setPixmap(pixmap)
        self.label.setGeometry(0, 0, self.width(), self.height())
        self.label.setScaledContents(True)


        self.UIqism()
    
    def UIqism(self):
        self.layout = QVBoxLayout()
        
        self.question_label = QLabel(self)
        self.question_label.setStyleSheet("font-size: 20px")
        self.layout.addWidget(self.question_label)

        self.option_buttons = QButtonGroup(self)
        self.radio_buttons = []

        for i in range(3):
            button = QRadioButton(self)
            button.setStyleSheet("font-size: 18px")
            self.option_buttons.addButton(button)
            self.radio_buttons.append(button)
            self.layout.addWidget(button)
        
        self.keyingiKnopka = QPushButton("Keyingi", self)
        self.keyingiKnopka.setStyleSheet("""
                                QPushButton{
                                         font-size: 20px; 
                                         font-weight: bold;
                                         background-color: #facb84;
                                         }
                                        """)
        self.keyingiKnopka.clicked.connect(self.keyingiSavol)
        self.layout.addWidget(self.keyingiKnopka)

        self.setLayout(self.layout)
        self.showTest(self.current_test)
    
    def showTest(self, index):
        test = self.tests[index]
        self.question_label.setText(test["question"])
        for i, option in enumerate(test["options"]):
            self.radio_buttons[i].setText(option)
            self.radio_buttons[i].setChecked(False)  
    
    def keyingiSavol(self):
        selected_button = self.option_buttons.checkedButton()  
        selected_answer = selected_button.text() if selected_button else None
        
        
        if selected_answer == self.tests[self.current_test]['answer']:
            self.correct_answers += 1  

        if self.current_test < len(self.tests) - 1:
            self.current_test += 1
            self.showTest(self.current_test)
        else:
            self.question_label.setText(f"Test tugadi! Siz {self.correct_answers} ta to'g'ri javob berdingiz.")
            self.question_label.move((self.width() - self.question_label.width()) // 2, 100)

            for button in self.radio_buttons:
                button.setText("")
                button.setEnabled(False)
                
            self.keyingiKnopka.setEnabled(False)  

app = QApplication([])
window = TestApp()
window.setFixedSize(400, 300) 
window.setWindowIcon(QIcon("test.png"))
window.setWindowTitle("Test App")
window.show()
app.exec_()
