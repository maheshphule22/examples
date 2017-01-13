'''
This file is used to check the ftp setup
( connecting and uploading file to ftp server)
change vatiables in this file before use (according to ftp setup) 
'''
ftp_server_ip = '127.0.0.1'
ftp_server_user_name = 'anonymous'
ftp_server_password = 'anonymous'
ftp_upload_dir_name = 'myftp'
destination_file_name = 'test.txt'
file_name = 'check_ftp.py'

from ftplib import FTP

ftp = FTP(ftp_server_ip)
ftp.set_debuglevel(1)
ftp.login(ftp_server_user_name,ftp_server_password)
ftp.pwd()
print ftp.nlst()
ftp.cwd(ftp_upload_dir_name)
ftp.storbinary('STOR '+destination_file_name, open(fileName, 'rb'))
ftp.quit()
