import subprocess


class Msf:
    def __init__(self, RHOSTS, name=None, tool=None, PAYLOAD=None, LHOST=None, LPORT=None):
        self.name = name
        self.tool = tool
        self.PAYLOAD = PAYLOAD
        self.RHOSTS = RHOSTS
        self.LPORT = LPORT
        self.LHOST = LHOST
        self.command = self.generate_command()

    def generate_command(self):
        head = "msfconsole -q -x "
        body = f"use {self.tool};"
        if self.PAYLOAD:
            body += f'set payload {self.PAYLOAD};'
        if self.RHOSTS:
            body += f'set RHOSTS {self.RHOSTS};'
        if self.LHOST:
            body += f'set LHOST {self.LHOST};'
        if self.LPORT:
            body += f'set LPORT {self.LPORT};'

        return f"{head} \"{body} exploit;exit\""

    def exploit(self):
        subprocess.call(self.generate_command(),
        shell = True,

        )
