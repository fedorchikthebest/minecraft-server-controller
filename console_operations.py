from subprocess import Popen, PIPE, STDOUT
from rcon.source import Client
import server_info


class ConsoleOperations:
    def __init__(self, file_name, xmx=1024, xms=1024):
        self.p = Popen(['java', f'-Xmx{xmx}M', f'-Xms{xms}M', '-jar',
                        f'{file_name}', 'nogui'],
                       stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        self.response = ''

    def get_lasted_string(self):
        uns = self.p.stdout.readline().rstrip()
        try:
            return uns.decode()
        except UnicodeDecodeError:
            return '?' * len(uns)

    def input(self, string):
        if self.p.poll() is None:
            with Client('127.0.0.1', server_info.port,
                        passwd=server_info.password) as client:
                self.response = client.run(str(string) + '\n')
            return self.response

    def is_running(self):
        return self.p.poll() is None

    def exit(self):
        if self.p.poll() is None:
            with Client('127.0.0.1', server_info.port,
                        passwd=server_info.password) as client:
                self.response = client.run('/stop')