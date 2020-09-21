#coding:utf-8
from ctypes import *
import os
import sys
import ftplib

class myFtp:
    ftp = ftplib.FTP()
    bIsDir = False
    path = ""
    def __init__(self, host, port='21'):
        # self.ftp.set_debuglevel(2) #打开调试级别2，显示详细信息 
        #self.ftp.set_pasv(0)      #0主动模式 1 #被动模式
        self.ftp.connect( host, port )
            
    def Login(self, user, passwd):
        self.ftp.login( user, passwd )
        print (self.ftp.welcome)

    def DownLoadFile(self, LocalFile, RemoteFile):
        file_handler = open( LocalFile, 'wb' )
        self.ftp.retrbinary('RETR ' + RemoteFile, file_handler.write)
        file_handler.close()
        return True
    
    def UpLoadFile(self, LocalFile, RemoteFile):
        if os.path.isfile( LocalFile ) == False:
            return False
        file_handler = open(LocalFile, "rb")
        self.ftp.storbinary('STOR '+ RemoteFile, file_handler, 4096)
        file_handler.close()
        return True

    def UpLoadFileTree(self, LocalDir, RemoteDir):
        if not os.path.exists(LocalDir):
            return False
        print ("LocalDir:", LocalDir)
        LocalNames = os.listdir(LocalDir)
        print ("list:", LocalNames)
        print (RemoteDir)
        self.ftp.cwd( RemoteDir )
        print('remoteDir is:',self.ftp.pwd())
        for Local in LocalNames:
            print(Local)
            src = os.path.join( LocalDir, Local)
            if src.find(".") == -1:
                self.ftp.mkd(Local)  
                self.UpLoadFileTree( src, Local )
            else:
                self.UpLoadFile( src, Local )
                
        self.ftp.cwd( ".." )
        return
    
    def DownLoadFileTree(self, LocalDir, RemoteDir):
        print ("remoteDir:", RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
            # print('creat localDir')
        self.ftp.cwd( RemoteDir )
        RemoteNames = self.ftp.nlst()  
        print ("RemoteNames", RemoteNames)
        # print (self.ftp.nlst("/del1"))
        for file in RemoteNames:
            Local = os.path.join( LocalDir, file )
            if file.find(".") == -1:
                self.DownLoadFileTree(Local, file)             
            else:
                self.DownLoadFile( Local, file )
        self.ftp.cwd( ".." )
        return
    
    
    def close(self):
        self.ftp.quit()

if __name__ == "__main__":
    ftp = myFtp('192.168.199.155',21)
    ftp.Login('test','pass001!')

    ftp.DownLoadFileTree(r'D:\python测试\组包\test1','test')#ok
    ftp.UpLoadFileTree(r'D:\python测试\组包\test1','test' )
    ftp.close()
    print ("ok!")