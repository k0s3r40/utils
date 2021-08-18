# main.py
import sys


class Port:
    def __init__(self, data):
        self.port_number = int(data.split('/')[0])
        self.port_type = data.split(' ')[-1]
    

class PortChecker:
    def __init__(self, ip):
        self.ip = ip
        self.ports = []
        with open(f'/tmp/scan.{ip}.log') as f:
            self.ports = [Port(line.replace('\n', '')) for line in f.readlines() if 'open' in line]

    def scan(self):
        for port in self.ports:
            print(f"Scanning {port.port_number, port.port_type}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('ip of the target is required ')
    port_checker = PortChecker(sys.argv[1])
    port_checker.scan()
