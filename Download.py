from bin import ftpUtil
import configparser
import datetime
import os
import shutil


#读取文件名、批次、任务
cf = configparser.ConfigParser(allow_no_value=True)
# cf.read(r"D:\python测试\组包\config.ini",encoding='utf-8')
cf.read(r"D:\Users\Desktop\版本\交易银行版本\config.txt",encoding='utf-8')

#文件下载
ip=cf.get('下载','IP')
port=int(cf.get('下载','PORT'))
user=cf.get('下载','user')
passwd=cf.get('下载','pass')
localPath=cf.get('下载','localPath')
remotePath=cf.get('下载','remotePath')


ftp=ftpUtil.myFtp(ip,port)#连接ftp
ftp.Login(user,passwd)
print('login success')
ftp.DownLoadFileTree(localPath,remotePath)
print('dwonload success')

ftp.close()

