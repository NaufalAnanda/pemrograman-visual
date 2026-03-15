#Naufal Pramudya Ananda
#F1D02310085
#D

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class KonverterSuhu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(12)
        main_layout.setContentsMargins(20, 20, 20, 20)

        self.label_judul = QLabel("KONVERTER SUHU CELSIUS")
        self.label_judul.setStyleSheet("font-weight: bold; color: #2c3e50; font-size: 14pt;")
        self.label_judul.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_celsius = QLineEdit()
        self.input_celsius.setPlaceholderText("Masukkan nilai Celsius (angka)...")
        self.input_celsius.setStyleSheet("""
            QLineEdit {
                border: 2px solid #3498db;
                border-radius: 6px;
                padding: 10px;
                font-size: 11pt;
                background-color: #f8f9fa;
            }
            QLineEdit:focus {
                border: 2px solid #2ecc71;
            }
        """)

        btn_layout = QHBoxLayout()
        
        self.btn_f = QPushButton("KE FAHRENHEIT")
        self.btn_f.setStyleSheet("""
            QPushButton { background-color: #2980b9; color: white; padding: 12px; font-weight: bold; border-radius: 5px; }
            QPushButton:hover { background-color: #3498db; }
        """)

        self.btn_k = QPushButton("KE KELVIN")
        self.btn_k.setStyleSheet("""
            QPushButton { background-color: #2980b9; color: white; padding: 12px; font-weight: bold; border-radius: 5px; }
            QPushButton:hover { background-color: #3498db; }
        """)

        self.btn_r = QPushButton("KE REAMUR")
        self.btn_r.setStyleSheet("""
            QPushButton { background-color: #2980b9; color: white; padding: 12px; font-weight: bold; border-radius: 5px; }
            QPushButton:hover { background-color: #3498db; }
        """)

        btn_layout.addWidget(self.btn_f)
        btn_layout.addWidget(self.btn_k)
        btn_layout.addWidget(self.btn_r)

        self.label_hasil = QLabel("HASIL KONVERSI")
        self.label_hasil.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_hasil.setStyleSheet("""
            QLabel {
                background-color: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                padding: 20px;
                color: #2c3e50;
                font-size: 12pt;
                font-weight: bold;
            }
        """)

        self.btn_reset = QPushButton("Reset Input")
        self.btn_reset.setStyleSheet("background-color: #95a5a6; color: white; border-radius: 5px; padding: 5px;")

        main_layout.addWidget(self.label_judul)
        main_layout.addSpacing(10)
        main_layout.addWidget(QLabel("Input Suhu (Celsius):"))
        main_layout.addWidget(self.input_celsius)
        main_layout.addLayout(btn_layout)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.label_hasil)
        main_layout.addWidget(self.btn_reset)

        self.setLayout(main_layout)
        self.setWindowTitle('Aplikasi Konverter Suhu - PySide6')
        self.setFixedWidth(450)

        self.btn_f.clicked.connect(lambda: self.hitung("F"))
        self.btn_k.clicked.connect(lambda: self.hitung("K"))
        self.btn_r.clicked.connect(lambda: self.hitung("R"))
        self.btn_reset.clicked.connect(self.reset_app)

    def hitung(self, tipe):
        try:
            val = float(self.input_celsius.text())
            
            if tipe == "F":
                res = (val * 9/5) + 32
                unit = "Fahrenheit"
                color = "#2980b9"
            elif tipe == "K":
                res = val + 273.15
                unit = "Kelvin"
                color = "#2980b9"
            else: 
                res = val * 4/5
                unit = "Reamur"
                color = "#2980b9"

            self.label_hasil.setText(f"HASIL KONVERSI:<br><span style='color: {color}; font-size: 18pt;'>{res:.2f} °{unit}</span>")
            
        except ValueError:
            QMessageBox.warning(self, "Input Salah", "Mohon masukkan angka yang valid!")

    def reset_app(self):
        self.input_celsius.clear()
        self.label_hasil.setText("HASIL KONVERSI")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KonverterSuhu()
    window.show()
    sys.exit(app.exec())