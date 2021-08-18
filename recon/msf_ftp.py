from msf_handler import Msf



class FtpVersion(Msf):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.name = 'Get ftp version'
        self.tool = 'auxiliary/scanner/ftp/ftp_version'


FTP_EXPLOITS = [FtpVersion]