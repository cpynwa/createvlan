import sys
from PyQt5.QtWidgets import *
from newDevice import Device
from PyQt5.QtGui import *

# class ConfigFinder(QWidget):
class createDeivceUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('sslvpn설정 생성')

        ### START ###
        h1box = QHBoxLayout()
        # Number of Device
        h1box.addWidget(QLabel('장비 수량:'))

        self.number_of_Device = QSpinBox()
        h1box.addWidget(self.number_of_Device)

        createButton = QPushButton('장비생성')
        h1box.addWidget(createButton)
        createButton.clicked.connect(self.createButtonClicked)



        # VLAN ID
        h2box = QHBoxLayout()
        h2box.addWidget(QLabel('VLAN:'))

        self.vlan_id = QSpinBox()
        h2box.addWidget(self.vlan_id)

        executeButton = QPushButton('설정시작')
        h2box.addWidget(executeButton)



        # Column
        h3box = QHBoxLayout()
        h3box.addWidget(QLabel('장비명'))
        h3box.addWidget(QLabel('Host Name'))
        h3box.addWidget(QLabel('User Name'))
        h3box.addWidget(QLabel('Password'))
        h3box.addWidget(QLabel('Interface'))



        # # Deivce 1
        # m1box = QHBoxLayout()
        # m1box.addWidget(QLabel('Device1:'))
        #
        # cb = QCheckBox('Fortigate', self)
        # m1box.addWidget(cb)
        #
        # host_name = QLineEdit()
        # m1box.addWidget(host_name)
        #
        # user_name = QLineEdit()
        # m1box.addWidget(user_name)
        #
        # user_pass = QLineEdit()
        # m1box.addWidget(user_pass)
        #
        # interfaces = QLineEdit()
        # m1box.addWidget(interfaces)
        #
        #
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(h1box)
        self.vbox.addLayout(h2box)
        self.vbox.addLayout(h3box)
        # vbox.addLayout(m1box)
        self.setLayout(self.vbox)

        # Device 3
        # count = self.createButtonClicked()
        # print(count)
        #
        # device = []
        # for i in range(count):
        #     form = Device()
        #     device.append(form)
        #     device[i].device_form(i)
        #     vbox.addLayout(form.mbox)

        # form = Device(count)
        # device3 = form.device_form()
        # vbox.addLayout(form.mbox)

        ### END ###

    # 버튼 메소드
    device = []
    def createButtonClicked(self):
        device_count = self.number_of_Device.value()
        device = []
        for i in range(device_count):
            form = Device()
            device.append(form)
            device[i].device_form(i)
            self.vbox.addLayout(form.mbox)
        #print(type(device_count))
        return device_count

    def showModal(self):
        return super().exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = createDeivceUI()
    ex.show()
    sys.exit(app.exec_())