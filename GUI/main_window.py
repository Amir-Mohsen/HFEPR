import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit,
    QGroupBox, QGridLayout
)
from PySide6.QtCore import Qt
import pyqtgraph as pg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HFEPR Control System")
        self.resize(1200, 800)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        # ===== LEFT PANEL (Controls) =====
        control_panel = QVBoxLayout()

        control_panel.addWidget(self.create_temperature_box())
        control_panel.addWidget(self.create_piezo_box())
        control_panel.addWidget(self.create_scan_box())

        control_panel.addStretch()

        # ===== RIGHT PANEL (Plot) =====
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setTitle("Lock-in Signal")
        self.plot_widget.setLabel("left", "Signal (V)")
        self.plot_widget.setLabel("bottom", "Field (T)")

        main_layout.addLayout(control_panel, 1)
        main_layout.addWidget(self.plot_widget, 2)

    def create_temperature_box(self):
        box = QGroupBox("Temperature Control")
        layout = QGridLayout()

        self.temp_label = QLabel("Magnet Temp: -- K")
        self.vti_label = QLabel("VTI Temp: -- K")

        layout.addWidget(self.temp_label, 0, 0, 1, 2)
        layout.addWidget(self.vti_label, 1, 0, 1, 2)

        box.setLayout(layout)
        return box

    def create_piezo_box(self):
        box = QGroupBox("Piezo Control (Z)")
        layout = QGridLayout()

        self.step_input = QLineEdit("10")

        move_up_btn = QPushButton("Move +")
        move_down_btn = QPushButton("Move -")

        layout.addWidget(QLabel("Steps:"), 0, 0)
        layout.addWidget(self.step_input, 0, 1)
        layout.addWidget(move_up_btn, 1, 0)
        layout.addWidget(move_down_btn, 1, 1)

        box.setLayout(layout)
        return box

    def create_scan_box(self):
        box = QGroupBox("EPR Scan")
        layout = QGridLayout()

        self.start_field = QLineEdit("0.0")
        self.end_field = QLineEdit("1.0")
        self.points_input = QLineEdit("100")

        start_btn = QPushButton("Start Scan")
        stop_btn = QPushButton("Stop Scan")

        layout.addWidget(QLabel("Start Field (T)"), 0, 0)
        layout.addWidget(self.start_field, 0, 1)
        layout.addWidget(QLabel("End Field (T)"), 1, 0)
        layout.addWidget(self.end_field, 1, 1)
        layout.addWidget(QLabel("Points"), 2, 0)
        layout.addWidget(self.points_input, 2, 1)

        layout.addWidget(start_btn, 3, 0)
        layout.addWidget(stop_btn, 3, 1)

        box.setLayout(layout)
        return box


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())