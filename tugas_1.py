#Naufal Pramudya Ananda
#F1D02310085
#D

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class FormBiodataStyled(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10) 
        main_layout.setContentsMargins(15, 15, 15, 15) 

        font_label = QFont("Segoe UI", 10)
        style_input = """
            QLineEdit {
                border: 1px solid #7dc78d; /* Border Hijau sesuai target */
                border-radius: 5px;
                padding: 8px;
                background-color: #f6fff8; /* Sedikit kehijauan di latar belakang */
            }
            QLineEdit:focus {
                border: 2px solid #2ecc71; /* Lebih tebal saat diklik */
            }
        """

        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Masukkan Nama Lengkap")
        self.input_nama.setStyleSheet(style_input)
        
        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("Masukkan NIM")
        self.input_nim.setStyleSheet(style_input)
        
        self.input_kelas = QLineEdit()
        self.input_kelas.setPlaceholderText("Masukkan Kelas")
        self.input_kelas.setStyleSheet(style_input)

        self.combo_jk = QComboBox()
        self.combo_jk.addItems(["-- Pilih Jenis Kelamin --", "Laki-laki", "Perempuan"])
        self.combo_jk.setStyleSheet("""
            QComboBox {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 8px;
                color: #7f8c8d;
            }
        """)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(15)

        self.btn_tampilkan = QPushButton("Tampilkan")
        self.btn_tampilkan.setStyleSheet("""
            QPushButton {
                background-color: #3498db; 
                color: white; 
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 10pt;
            }
            QPushButton:hover {
                background-color: #2980b9; /* Lebih gelap saat kursor di atasnya */
            }
        """)

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6; 
                color: white; 
                border-radius: 5px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        
        btn_layout.addWidget(self.btn_tampilkan)
        btn_layout.addWidget(self.btn_reset)

        self.label_hasil = QLabel()
        self.reset_label_hasil_text() 
        self.label_hasil.setStyleSheet("""
            QLabel {
                background-color: #e8f5e9; /* Hijau muda latar belakang */
                border-left: 8px solid #2ecc71; /* Border hijau tebal di kiri */
                border-radius: 3px;
                padding: 15px; 
                color: #2c3e50;
                font-size: 9pt;
            }
        """)
        self.label_hasil.setWordWrap(True) 
        self.label_hasil.setAlignment(Qt.AlignmentFlag.AlignTop) 

        lbl_nama = QLabel("Nama Lengkap:")
        lbl_nama.setFont(font_label)
        main_layout.addWidget(lbl_nama)
        main_layout.addWidget(self.input_nama)
        main_layout.addSpacing(5)

        lbl_nim = QLabel("NIM:")
        lbl_nim.setFont(font_label)
        main_layout.addWidget(lbl_nim)
        main_layout.addWidget(self.input_nim)
        main_layout.addSpacing(5)

        lbl_kelas = QLabel("Kelas:")
        lbl_kelas.setFont(font_label)
        main_layout.addWidget(lbl_kelas)
        main_layout.addWidget(self.input_kelas)
        main_layout.addSpacing(5)

        lbl_jk = QLabel("Jenis Kelamin:")
        lbl_jk.setFont(font_label)
        main_layout.addWidget(lbl_jk)
        main_layout.addWidget(self.combo_jk)
        main_layout.addSpacing(15)

        main_layout.addLayout(btn_layout)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.label_hasil)

        self.setLayout(main_layout)
        self.setWindowTitle('Input Biodata Mahasiswa')
        self.btn_tampilkan.clicked.connect(self.proses_data)
        self.btn_reset.clicked.connect(self.reset_form)

    def reset_label_hasil_text(self):
        initial_text = f"<span style='color: #1e6b3b; font-weight: bold; font-size: 11pt;'>DATA BIODATA</span>"
        self.label_hasil.setText(initial_text)

    def proses_data(self):
        nama = self.input_nama.text()
        nim = self.input_nim.text()
        kelas = self.input_kelas.text()
        jk = self.combo_jk.currentText()

        # VALIDASI
        if not nama or not nim or not kelas or jk == "-- Pilih Jenis Kelamin --":
            QMessageBox.critical(self, "Validasi Gagal", "Semua field harus diisi!")
        else:
            teks_hasil = (
                f"<span style='color: #1e6b3b; font-weight: bold; font-size: 11pt;'>DATA BIODATA</span><br><br>"
                f"<span style='font-size: 10pt;'>Nama: {nama}<br>"
                f"NIM: {nim}<br>"
                f"Kelas: {kelas}<br>"
                f"Jenis Kelamin: {jk}</span>"
            )
            self.label_hasil.setText(teks_hasil)

    def reset_form(self):
        self.input_nama.clear()
        self.input_nim.clear()
        self.input_kelas.clear()
        self.combo_jk.setCurrentIndex(0)
        self.reset_label_hasil_text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormBiodataStyled()
    window.show()
    sys.exit(app.exec())