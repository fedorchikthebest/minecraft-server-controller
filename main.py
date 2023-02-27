import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, \
    QFileDialog, QCompleter, QDialog
from main_gui import Ui_MainWindow
from console_operations import ConsoleOperations
from PyQt5.QtCore import Qt
from console_thread import ServerThread
from init_gui import Ui_InitWindow
import webbrowser
import server_info
import shutil
import os
import sqlite3
from properties_gui import Ui_PropertiesWindow


class PropertiesWindow(QMainWindow, Ui_PropertiesWindow):
    def __init__(self, *args):
        super().__init__()
        self.setWindowTitle('Настройка server.properties')
        self.setupUi(self)
        with open('shab.txt') as f:
            with open('server.properties', encoding="ISO-8859-1") as d:
                e = d.read().split('\n')
                if e[0][0] == '#':
                    del e[0]
                if e[0][0] == '#':
                    del e[0]
                for i in zip(f.read().split('\n'), e):
                    if i[0] != 'enable_rcon':
                        uns = str(i[1].split('=')[-1])
                        if uns != '':
                            eval(f"self.{i[0]}.setText('{uns}')")
                        else:
                            eval(f"self.{i[0]}.clear()")
                    if i[0] == 'server_ip' and self.server_ip.text() == '256':
                        self.server_ip.clear()
        self.save.clicked.connect(self.save_properties)
        self.server = args[0]

    def save_properties(self):
        uns = []
        con = sqlite3.connect('../../Рабочий стол/config.sqlite3')
        cur = con.cursor()
        server_port = cur.execute(f"""SELECT znach FROM settings
                                    WHERE name = 'server_port'
                                    """).fetchone()[0]
        rcon_port = server_info.port
        con = sqlite3.connect('../../Рабочий стол/config.sqlite3')
        cur = con.cursor()
        with open('shab.txt') as f:
            with open('properties.txt') as d:
                for i in zip(f.read().split('\n'), d.read().split('\n')):
                    if i[0] != 'enable_rcon':
                        pr = eval(f'self.{i[0]}.text()')
                        if i[0] == 'rcon_password':
                            if pr != '':
                                if pr.encode().decode('ISO-8859-1') \
                                        == pr.encode().decode('UTF-8'):
                                    cur.execute(f"""UPDATE settings
                                                    SET znach = '{pr}'
                                                    WHERE name = 'password'""")
                                    server_info.password = pr
                                else:
                                    dialog = QMessageBox(self)
                                    dialog.setWindowTitle("Информация")
                                    dialog.setText("Некорректный пароль"
                                                   "(Пароль должен состоять из"
                                                   "латинских букв и цифр)")
                                    dialog.show()
                                    return
                            else:
                                cur.execute(f"""UPDATE settings
                                                SET znach = '1'
                                                WHERE name = 'password'""")
                                server_info.password = '1'
                                pr = '1'
                        if i[0] == 'rcon_port':
                            if pr != '':
                                rcon_port = pr
                        if i[0] == 'server_port':
                            if pr != '':
                                server_port = pr
                        if i[0] == 'server_ip' and pr == 256:
                            pr = ''
                        uns.append(f'{i[1]}={pr}')
                    elif i[0] == 'enable_rcon':
                        uns.append('enable-rcon=true')
        if str(server_port) != str(rcon_port):
            try:
                if 1 <= int(server_port) <= 65534 and \
                        1 <= int(rcon_port) <= 65534:
                    with open('server.properties', 'w') as e:
                        e.write('\n'.join(uns))
                    cur.execute(f"""UPDATE settings
                                            SET znach = {int(rcon_port)}
                                            WHERE name = 'port'""")
                    server_info.port = int(rcon_port)
            except ValueError:
                dialog = QMessageBox(self)
                dialog.setWindowTitle("Информация")
                dialog.setText("Некорректное значение порта\n"
                               "порты должны быть целыми числами от 1 до 65534"
                               "и не должны быть равны")
                dialog.exec()
                return
        else:
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Информация")
            dialog.setText("Некорректное значение порта\n"
                           "порты должны быть целыми числами"
                           "и не должны быть равны")
            dialog.exec()
            return
        con.commit()
        con.close()
        if self.server is not None:
            self.server.input('reload')
        self.close()


class InitWindow(QMainWindow, Ui_InitWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Предварительная настройка')
        self.setupUi(self)
        self.elua.clicked.connect(self.open_elua)
        self.next.setDisabled(True)
        self.elua_check.clicked.connect(self.check_eula)
        self.next.clicked.connect(self.to_main_window)
        self.pushButton.clicked.connect(self.open_file)
        self.file_selected = False
        self.eula_accept = False

    def check_eula(self):
        self.eula_accept = self.elua_check.isChecked()
        if self.eula_accept and self.file_selected:
            self.next.setEnabled(True)
        else:
            self.next.setEnabled(False)

    def open_file(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл сервера', '',
            'Файл сервера (*.jar)')[0]
        if fname != '':
            try:
                shutil.copy(fname, 'server.jar')
            except shutil.SameFileError:
                dialog = QMessageBox(self)
                dialog.setWindowTitle("Информация")
                dialog.setText("Этот файл уже принадлежит серверу")
                dialog.exec()
        self.file_selected = bool(fname)
        if self.eula_accept and self.file_selected:
            self.next.setEnabled(True)
        else:
            self.next.setEnabled(False)

    def open_elua(self):
        webbrowser.open('https://www.minecraft.net/en-us/eula')

    def to_main_window(self):
        self.main_window = MainWindow()
        uns = []
        server_port = 25565
        rcon_port = 25575
        con = sqlite3.connect('../../Рабочий стол/config.sqlite3')
        cur = con.cursor()
        with open('shab.txt') as f:
            with open('properties.txt') as d:
                for i in zip(f.read().split('\n'), d.read().split('\n')):
                    if i[0] != 'enable_rcon':
                        pr = eval(f'self.{i[0]}.text()')
                        if i[0] == 'rcon_password':
                            if pr != '':
                                if pr.encode().decode('ISO-8859-1') \
                                        == pr.encode().decode('UTF-8'):
                                    cur.execute(f"""UPDATE settings
                                                    SET znach = '{pr}'
                                                    WHERE name = 'password'""")
                                    server_info.password = pr
                                else:
                                    dialog = QMessageBox(self)
                                    dialog.setWindowTitle("Информация")
                                    dialog.setText("Некорректный пароль"
                                                   "(Пароль должен состоять из"
                                                   "латинских букв и цифр)")
                                    dialog.show()
                                    return
                            else:
                                cur.execute(f"""UPDATE settings
                                                SET znach = '1'
                                                WHERE name = 'password'""")
                                server_info.password = '1'
                                pr = '1'
                        if i[0] == 'rcon_port':
                            if pr != '':
                                rcon_port = pr
                        if i[0] == 'enable_rcon':
                            pr = 'true'
                        if i[0] == 'server_port':
                            if pr != '':
                                server_port = pr
                        uns.append(f'{i[1]}={pr}')
                    else:
                        uns.append('enable-rcon=true')
        if str(server_port) != str(rcon_port):
            try:
                if 1 <= int(server_port) <= 65534 and \
                        1 <= int(rcon_port) <= 65534:
                    with open('server.properties', 'w') as e:
                        e.write('\n'.join(uns))
                    cur.execute(f"""UPDATE settings
                                    SET znach = {int(rcon_port)}
                                    WHERE name = 'port'""")
                    cur.execute(f"""UPDATE settings
                                        SET znach = {int(server_port)}
                                        WHERE name = 'server_port'""")
                    server_info.port = int(rcon_port)
            except ValueError:
                dialog = QMessageBox(self)
                dialog.setWindowTitle("Информация")
                dialog.setText("Некорректное значение порта\n"
                               "порты должны быть целыми числами от 1 до 65534"
                               "и не должны быть равны")
                dialog.exec()
                return
        else:
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Информация")
            dialog.setText("Некорректное значение порта\n"
                           "порты должны быть целыми числами"
                           "и не должны быть равны")
            dialog.exec()
            return
        con.commit()
        con.close()
        with open('eula.txt', 'w') as f:
            f.write('eula=true')
        self.main_window.show()
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Главная')
        self.commands = ['advancement', 'attribute', 'bossbar', 'clear',
                         'clone', 'data', 'datapack', 'debug',
                         'defaultgamemode', 'difficulty', 'effect', 'enchant',
                         'execute', 'experience', 'fill', 'forceload',
                         'function', 'gamemode', 'gamerule', 'give', 'help',
                         'kill', 'list', 'kill', 'locate', 'locatebiome',
                         'loot', 'me', 'msg', 'particle', 'playsound',
                         'publish', 'recipe', 'reload', 'replaceitem', 'say',
                         'schedule', 'scoreboard', 'seed', 'setblock',
                         'setworldspawn', 'spawnpoint', 'spectate',
                         'spreadplayers', 'stopsound', 'summon', 'tag', 'team',
                         'teammsg', 'teleport', 'tell', 'tellraw', 'time',
                         'title', 'tm', 'tp', 'trigger', 'w', 'weather',
                         'worldborder', 'xp']
        self.ban_unsvers = [
            '[RCON Listener #1/INFO]: Rcon connection from: /127.0.0.1']
        self.start.clicked.connect(self.run)
        self.stop.clicked.connect(self.server_stop)
        self.console.setReadOnly(True)
        self.input.setReadOnly(True)
        self.stop.setDisabled(True)
        self.accept.clicked.connect(self.save)
        self.xmx = 1024
        self.xms = 1024
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab),
                                  "главная")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab),
                                  "настройки")
        con = sqlite3.connect('../../Рабочий стол/config.sqlite3')
        cur = con.cursor()
        self.pop_up_window = cur.execute(f"""SELECT znach FROM SETTINGS
                                                WHERE name = 'messagewindow'
                                                """).fetchone()[0] == 'true'
        self.hints_server = cur.execute(f"""SELECT znach FROM SETTINGS
                                                WHERE name = 'hints'
                                                """).fetchone()[0] == 'true'
        self.question_window.setChecked(self.pop_up_window)
        self.hints_box.setChecked(self.hints_server)
        self.chendge_settings()
        self.question_window.clicked.connect(self.set_puw)
        con.close()
        self.completer = QCompleter(self.commands, self.input)
        self.input.setCompleter(self.completer)
        self.hints_box.clicked.connect(self.change_hints)
        self.server_properties_settings.clicked.connect(
            self.change_server_settings
        )
        self.server = None
        self.change_core.clicked.connect(self.change_server_core)

    def change_server_settings(self):
        self.properties = PropertiesWindow(self.server)
        self.properties.show()

    def change_server_core(self):
        if self.server is not None and self.server.is_running():
            message = QMessageBox(self)
            message.setWindowTitle('Информация')
            message.setText("Выключите сервер перед сменой ядра")
            message.exec()
            return
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл сервера', '',
            'Файл сервера (*.jar)')[0]
        if fname != '':
            try:
                shutil.copy(fname, 'server.jar')
            except shutil.SameFileError:
                dialog = QMessageBox(self)
                dialog.setWindowTitle("Информация")
                dialog.setText("Этот файл уже принадлежит серверу")
                dialog.exec()

    def set_puw(self):
        self.pop_up_window = self.question_window.isChecked()
        con = sqlite3.connect('../../Рабочий стол/config.sqlite3')
        cur = con.cursor()
        cur.execute(f"""UPDATE settings
                        SET znach = {str(self.pop_up_window).lower()}
                        WHERE name = 'messagewindow'""")
        con.commit()
        con.close()

    def change_hints(self):
        if self.hints_box.isChecked():
            self.completer = QCompleter(self.commands, self.input)
            self.input.setCompleter(self.completer)
        else:
            self.completer = QCompleter([], self.input)
            self.input.setCompleter(self.completer)
        con = sqlite3.connect('../../Рабочий стол/config.sqlite3')
        cur = con.cursor()
        cur.execute(f"""UPDATE settings
                        SET znach = {str(self.hints_box.isChecked()).lower()}
                        WHERE name = 'hints'""")
        con.commit()
        con.close()

    def save(self):
        try:
            self.xmx = int(self.Xmx.text())
            self.xms = int(self.Xms.text())
        except ValueError:
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Информация")
            dialog.setText("Некорректное значение")
            dialog.exec()

    def run(self):
        self.server = ConsoleOperations('server.jar', xmx=self.xmx,
                                        xms=self.xms)
        self.thread = ServerThread(self.server)
        self.thread.serverSignal.connect(self.on_serverSignal)
        self.thread.serverFinish.connect(self.serverFinished)
        self.thread.start()
        self.start.setDisabled(True)

    def server_stop(self):
        self.server.exit()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            txt = self.input.text()
            if txt != '':
                self.console.append(f'Вы: {txt}')
                line = self.server.input(txt)
                self.console.append(line)
                self.input.clear()

    def on_serverSignal(self, value):
        if 'RCON running' in value:
            self.input.setReadOnly(False)
            self.stop.setDisabled(False)
        if ' '.join(value.split()[1:]) not in self.ban_unsvers:
            self.console.append(value)

    def serverFinished(self):
        self.start.setDisabled(False)
        self.input.setReadOnly(True)
        self.stop.setDisabled(True)
        self.start.setDisabled(False)
        if self.pop_up_window:
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Информация")
            dialog.setText("Сервер остановлен!")
            dialog.exec()

    def chendge_settings(self):
        con = sqlite3.connect('../../Рабочий стол/config.sqlite3')
        cur = con.cursor()
        uns = cur.execute("""SELECT znach FROM settings
            WHERE name = 'hints'""")
        self.hints_server = uns.fetchone()[0] == 'true'
        uns = cur.execute("""SELECT znach FROM settings
                    WHERE name = 'messagewindow'""")
        self.hints_server = uns.fetchone()[0] == 'true'

    def closeEvent(self, event):
        try:
            self.server.exit()
        except AttributeError:
            pass
        event.accept()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    txt = ''
    if 'eula.txt' in os.listdir():
        with open('eula.txt') as f:
            txt = f.read().split('\n')
    if 'server.properties' in os.listdir() and \
            'eula.txt' in os.listdir() and \
            'server.jar' in os.listdir() and \
            'eula=true' in txt:
        ex = MainWindow()
        ex.show()
    else:
        ex = InitWindow()
        ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
