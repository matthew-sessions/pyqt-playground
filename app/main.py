
import sys
import time
from PySide6.QtWidgets import QMainWindow
from ui.ui_core_interface import Ui_MainWindow
from video_controller.local_camera_thread import LocalCameraThread

import cv2
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QImage,  QPixmap



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
      





        # Create a label for the display camera
        self.label = self.ui.videoLable
        # self.label.setFixedSize(640, 480)

        # Thread in charge of updating the image
        self.th = LocalCameraThread(self)
        self.th.finished.connect(self.close)
        self.th.updateFrame.connect(self.setImage)

        # self.ui.menuToggle.clicked.connect(self.mod_menu)
        self.ui.toggleButton.clicked.connect(self.mod_menu)
        self.menu_state_open = False


        self.start()

    # @Slot
    def mod_menu(self):
        print(dir(self.ui.menuToggle))
        if self.menu_state_open:
            self.ui.menuContainer.setMaximumSize(QSize(45, 16777215))
            self.menu_state_open = False
            self.ui.missionButton.setText("")
        else:
            self.ui.menuContainer.setMaximumSize(QSize(200, 16777215))
            self.ui.missionButton.setText("Data Mission")
            self.menu_state_open = True


    @Slot()
    def set_model(self, text):
        self.th.set_file(text)

    @Slot()
    def kill_thread(self):
        print("Finishing...")
        self.button2.setEnabled(False)
        self.button1.setEnabled(True)
        self.th.cap.release()
        cv2.destroyAllWindows()
        self.status = False
        self.th.terminate()
        # Give time for the thread to finish
        time.sleep(1)

    @Slot()
    def start(self):
        print("Starting...")

        self.th.start()

    @Slot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))




