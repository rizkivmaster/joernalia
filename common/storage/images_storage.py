from ftplib import FTP

public_address = 'http://braderhut.netne.net'

ftp = FTP('braderhut.netne.net')


def start():
    ftp.login(user='a1634887', passwd='qwerty7890')
    ftp.cwd('public_html/images')


def stop():
    ftp.quit()


def save_and_get_url(imagename, file):
    ftp.storlines('STOR ' + str(imagename), file)
    return '/'.join(public_address,imagename)