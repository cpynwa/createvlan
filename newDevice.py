import sys
from PyQt5.QtWidgets import *

class Device:


    def device_form(self, count):
        self.mbox = QHBoxLayout()
        self.mbox.addWidget(QLabel(f'Device{count}:'))

        cb = QCheckBox('Fortigate')
        self.mbox.addWidget(cb)

        host_name = QLineEdit()
        self.mbox.addWidget(host_name)

        user_name = QLineEdit()
        self.mbox.addWidget(user_name)

        user_pass = QLineEdit()
        self.mbox.addWidget(user_pass)

        interfaces = QLineEdit()
        self.mbox.addWidget(interfaces)