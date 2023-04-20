import threading

from PyQt6.QtCore import pyqtSignal
from PySide6.QtCore import QThread




class SearchThread(QThread):
    finished = pyqtSignal()

    def __init__(self,parent=None):
        super(SearchThread, self).__init__(parent)

    def run(self):
        # 在这里执行您的搜索任务
        print("Search started")
        # 搜索任务完成后，发出finished信号
        self.finished.emit()

