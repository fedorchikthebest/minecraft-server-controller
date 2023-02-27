from PyQt5 import QtCore
from time import sleep


class ServerThread(QtCore.QThread):
    serverSignal = QtCore.pyqtSignal(str)
    serverFinish = QtCore.pyqtSignal()

    def __init__(self, server):
        super(ServerThread, self).__init__(None)
        self.server = server

    def run(self, *args, **kwargs):
        while True:
            sleep(0.1)
            i = self.server.get_lasted_string()
            if i:
                self.serverSignal.emit(i)
            if not self.server.is_running():
                self.server.exit()
                break
        self.serverFinish.emit()