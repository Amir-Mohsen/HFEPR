import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QPushButton, QTextEdit,
    QGroupBox, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import pyqtgraph as pg


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HFEPR Monitoring Dashboard")
        self.resize(1600, 900)

        self.dark_mode = True

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        # LEFT SIDE (Graph + Parameters)
        left_layout = QVBoxLayout()

        self.graph = pg.PlotWidget()
        self.graph.setTitle("Temperature Monitor")
        self.graph.setLabel("left", "Temperature (K)")
        self.graph.setLabel("bottom", "Time (s)")
        self.graph.showGrid(x=True, y=True)
        left_layout.addWidget(self.graph, 3)

        left_layout.addWidget(self.create_parameters_group(), 1)

        # RIGHT SIDE (Logs + Instruments)
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.create_logs_group(), 2)
        right_layout.addWidget(self.create_instruments_group(), 1)

        main_layout.addLayout(left_layout, 3)
        main_layout.addLayout(right_layout, 1)

        self.apply_dark_theme()

    # ==========================
    # PARAMETERS PANEL
    # ==========================
    def create_parameters_group(self):
        box = QGroupBox("Parameters")
        layout = QGridLayout()

        labels = [
            "Magnet Field", "Magnet Temp", "VTI Temp",
            "Lock-in Amplitude", "Piezo Position", "Microwave Power"
        ]

        for i, text in enumerate(labels):
            name = QLabel(text)
            value = QLabel("--")
            value.setFrameStyle(QFrame.Panel | QFrame.Sunken)
            value.setAlignment(Qt.AlignCenter)

            layout.addWidget(name, i // 2, (i % 2) * 2)
            layout.addWidget(value, i // 2, (i % 2) * 2 + 1)

        box.setLayout(layout)
        return box

    # ==========================
    # LOGS PANEL
    # ==========================
    def create_logs_group(self):
        box = QGroupBox("Logs")
        layout = QVBoxLayout()

        self.logs = QTextEdit()
        self.logs.setReadOnly(True)

        layout.addWidget(self.logs)
        box.setLayout(layout)
        return box

    # ==========================
    # INSTRUMENT PANEL
    # ==========================
    def create_instruments_group(self):
        box = QGroupBox("Instrument Control")
        layout = QVBoxLayout()

        self.connect_btn = QPushButton("Connect Instruments")
        self.disconnect_btn = QPushButton("Disconnect")

        self.theme_btn = QPushButton("Switch to Light Mode")

        layout.addWidget(self.connect_btn)
        layout.addWidget(self.disconnect_btn)
        layout.addWidget(self.theme_btn)

        box.setLayout(layout)

        # Button styling
        self.style_buttons()

        self.theme_btn.clicked.connect(self.toggle_theme)

        return box

    # ==========================
    # BUTTON STYLING
    # ==========================
    def style_buttons(self):
        button_style = """
        QPushButton {
            border-radius: 8px;
            padding: 8px;
            font-weight: bold;
            background-color: #3a7afe;
            color: white;
        }
        QPushButton:hover {
            background-color: #5c94ff;
        }
        QPushButton:pressed {
            background-color: #2a5bd7;
        }
        """

        danger_style = """
        QPushButton {
            border-radius: 8px;
            padding: 8px;
            font-weight: bold;
            background-color: #c0392b;
            color: white;
        }
        QPushButton:hover {
            background-color: #e74c3c;
        }
        """

        self.connect_btn.setStyleSheet(button_style)
        self.disconnect_btn.setStyleSheet(danger_style)
        self.theme_btn.setStyleSheet(button_style)

    # ==========================
    # THEME TOGGLE
    # ==========================
    def toggle_theme(self):
        if self.dark_mode:
            self.apply_light_theme()
            self.theme_btn.setText("Switch to Dark Mode")
        else:
            self.apply_dark_theme()
            self.theme_btn.setText("Switch to Light Mode")

        self.dark_mode = not self.dark_mode

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #1e1e1e; }
            QLabel { color: white; }
            QGroupBox { 
                color: white;
                border: 1px solid #444;
                margin-top: 10px;
                font-weight: bold;
            }
        """)

        pg.setConfigOption('background', '#1e1e1e')
        pg.setConfigOption('foreground', 'w')

    def apply_light_theme(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #f2f2f2; }
            QLabel { color: black; }
            QGroupBox { 
                color: black;
                border: 1px solid #bbb;
                margin-top: 10px;
                font-weight: bold;
            }
        """)

        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())