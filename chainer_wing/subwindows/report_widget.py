from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from chainer_wing.subwindows.train_config import TrainParamServer


class ReportWidget(QtWidgets.QTabWidget):

    def __init__(self, *args, **kwargs):
        super(ReportWidget, self).__init__(*args, **kwargs)
        self.setStyleSheet('''ReportWidget{background: rgb(55,55,55)}
        ''')
        try:
            loss_image = TrainParamServer().get_result_dir() + "/loss.png"
        except KeyError:
            loss_image = "result/loss.png"

        self.loss_widget = GraphWidget(loss_image, parent=self)
        self.addTab(self.loss_widget, 'Loss')
        try:
            acc_image = TrainParamServer().get_result_dir() + "/accuracy.png"
        except KeyError:
            acc_image = "result/accuracy.png"
        self.acc_widget = GraphWidget(acc_image, parent=self)
        self.addTab(self.acc_widget, 'Accuracy')
        self.resize(200, 200)

    def update_report(self):
        self.removeTab(0)
        self.removeTab(0)
        try:
            loss_image = TrainParamServer().get_result_dir() + "/loss.png"
        except KeyError:
            loss_image = "result/loss.png"
        self.loss_widget = GraphWidget(loss_image, parent=self)
        self.addTab(self.loss_widget, 'Loss')
        try:
            acc_image = TrainParamServer().get_result_dir() + "/accuracy.png"
        except KeyError:
            acc_image = "result/accuracy.png"
        self.acc_widget = GraphWidget(acc_image, parent=self)
        self.addTab(self.acc_widget, 'Accuracy')


class GraphWidget(QtWidgets.QWidget):

    def __init__(self, image_file, *args, **kwargs):
        super(GraphWidget, self).__init__()
        self.setStyleSheet('''ReportWidget{background: rgb(55,55,55)}
        ''')
        self.pixmap = None
        self.image_file = image_file

    def paintEvent(self, event):
        if 'Class' not in TrainParamServer()['Task']:
            if 'accuracy' in self.image_file:
                return
        self.pixmap = QtGui.QPixmap(self.image_file)
        size = self.size()
        painter = QtGui.QPainter(self)
        point = QtCore.QPoint(0, 0)
        scaled_pix = self.pixmap.scaled(size, Qt.KeepAspectRatio,
                                        transformMode=Qt.SmoothTransformation)
        # start painting the label from left upper corner
        point.setX((size.width() - scaled_pix.width()) / 2)
        point.setY((size.height() - scaled_pix.height()) / 2)
        painter.drawPixmap(point, scaled_pix)
