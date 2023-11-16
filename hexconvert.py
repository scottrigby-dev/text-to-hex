import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class HexConverterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hex Converter')
        self.setGeometry(100, 100, 400, 150)

        # Widgets
        self.input_label = QLabel('Enter English Word:', self)
        self.input_lineedit = QLineEdit(self)

        self.output_label = QLabel('Hexadecimal:', self)
        self.output_lineedit = QLineEdit(self)
        self.output_lineedit.setReadOnly(True)

        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert_to_hex)

        # Layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.input_label)
        v_layout.addWidget(self.input_lineedit)
        v_layout.addWidget(self.output_label)
        v_layout.addWidget(self.output_lineedit)
        v_layout.addWidget(self.convert_button)

        self.setLayout(v_layout)

    def convert_to_hex(self):
        text = self.input_lineedit.text()
        hex_result = self.text_to_hex(text)
        self.output_lineedit.setText(hex_result)

    def text_to_hex(self, text):
        hex_result = '-'.join(format(ord(char), '02X') for char in text)
        return hex_result

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HexConverterApp()
    window.show()
    sys.exit(app.exec_())
