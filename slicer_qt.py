"""
Created on Fri Mar 11 2022

@author: Iain Emslie
Technical Assistant (Plant Imaging)
Canadian Light Source
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QGroupBox, QLabel, QCheckBox, QFileDialog, QMessageBox,\
                            QApplication, QGridLayout, QRadioButton

from slicer import run_slicer


class SlicerGUI(QWidget):
    def __init__(self, *args, **kwargs):
        super(SlicerGUI, self).__init__(*args, **kwargs)
        self.infile_path = ""
        self.outdir_path = ""

        self.setWindowTitle('XRF-Slicer')

        self.input_button = QPushButton("Select input file (.xls, xlsx, .ods): ")
        self.input_button.clicked.connect(self.input_button_pressed)
        self.input_entry = QLineEdit("...Enter the path to the input file")
        self.input_entry.textChanged.connect(self.set_input_entry)

        self.output_button = QPushButton("Select output directory: ")
        self.output_button.clicked.connect(self.output_button_pressed)
        self.output_entry = QLineEdit("...Enter the path to the output directory")
        self.output_entry.textChanged.connect(self.set_output_entry)

        self.help_button = QPushButton("Help")
        self.help_button.clicked.connect(self.help_button_pressed)

        self.slice_button = QPushButton("Run Slicer")
        self.slice_button.clicked.connect(self.slice_button_pressed)

        self.setMinimumSize(700, 100)
        self.set_layout()
        self.show()

    def set_layout(self):
        layout = QGridLayout()

        layout.addWidget(self.input_button, 0, 0)
        layout.addWidget(self.input_entry, 0, 1)

        layout.addWidget(self.output_button, 1, 0)
        layout.addWidget(self.output_entry, 1, 1)

        layout.addWidget(self.help_button, 2, 0)
        layout.addWidget(self.slice_button, 2, 1)

        self.setLayout(layout)

    def input_button_pressed(self):
        dir_explore = QFileDialog(self)
        self.infile_path = dir_explore.getOpenFileName()[0]
        self.input_entry.setText(self.infile_path)

    def output_button_pressed(self):
        dir_explore = QFileDialog(self)
        self.outdir_path = dir_explore.getExistingDirectory()
        self.output_entry.setText(self.outdir_path)

    def set_input_entry(self):
        self.infile_path = self.input_entry.text()

    def set_output_entry(self):
        self.outdir_path = self.output_entry.text()

    def slice_button_pressed(self):
        run_slicer(self.infile_path, self.outdir_path)

    def help_button_pressed(self):
        h_string = "XRF-Slicer turns excel x-ray fluorescence data into .tiff images." \
                   " The output is saved to /sli directory within the specified output directory.\n\n"
        h_string += "Input file: Input path to .xlsx, .xls or .ods file\n\n"
        h_string += "Output directory: Output path to store /sli directory containing .tiff images"
        QMessageBox.information(self, "Help", h_string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SlicerGUI()
    sys.exit(app.exec_())
