from bin import ftpUtil

ftp=ftpUtil.myFtp('192.168.199.155',21)

ftp.Login('test','pass001!')

# bool=ftp.DownLoadFile(r'D:\python测试\组包\addlist\local.txt',r'test\remote.txt')
# print(bool)

# bool=ftp.UpLoadFile(r'D:\python测试\组包\addlist\local.txt',r'test\remote.txt')

# print(bool)

# ftp.UpLoadFileTree(r'D:\python测试\组包\addlist','test')

ftp.DownLoadFileTree(r'D:\python测试\组包\test1','test')

ftp.close()