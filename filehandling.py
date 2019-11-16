import os
from shutil import move
from getpass import getuser
from platform import uname
from PyQt5.QtWidgets import *
import sys

class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.buton = QPushButton('Click Me!')
        self.buton.show()
        self.buton.clicked.connect(self.filehandle)
        self.butonexit = QPushButton('Click Me For Exit!')
        self.butonexit.hide()
        self.butonexit.clicked.connect(self.eventExit)

        self.textArea = QPlainTextEdit(self)
        self.textArea.move(200,200)
        self.textArea.setReadOnly(True)
        self.textArea.hide()

        v_box = QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.butonexit)
        v_box.addWidget(self.textArea)

        self.setLayout(v_box)

    def eventExit(self):
        self.destroy()

    def filehandle(self):
        self.textArea.show()
        audio=['.aif','.cda','.mid','.midi','.mp3','.mpa','.wav']
        compressed=['.7z','.pkg','.rar','.rpm','.z','.zip']
        discandmedia=['.bin','.dmg','.iso','.vcd']
        database=['.csv','.dat','.log','.mdb','.sav','.sql','.tar','.xml','.db']
        executables=['.apk','.bat','.bin','.cgi','.com','.exe','.jar','.wsf']
        image=['.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.psd','.svg','.tiff']
        internetrelated=['.asp','.aspx','.cgi','.pl','.html','.htm','.js','.css','.jsp','.php','.xhtml']
        programming=['.c','.class','.py','.cs','.java','.vb']
        video=['.avi','.flv','.mp4','.mpg','.mpeg','.swf','.vob','.wmv']
        office=['.key','.pps','ppt','.pptx','.xlr','.xls','.xlsx','.doc','.docx','.pdf','.txt','.wpd','.odt'] 
        ext_list=[audio,compressed,discandmedia,database,executables,image,internetrelated,programming,video,office]
        ext_list_str=['Audio','Compressed','Discandmedia','Database','Executables','Image','Internet related','Programming','Video','Office']
        count=0

        #getting name of the user
        username=getuser()

        platformName = uname()
        if platformName[0] == 'Windows':
            #scanning the downloads folder
            liste=os.listdir(f'C:\\Users\\{username}\\Downloads')

            #main loop
            while count<len(ext_list):
                for item in liste:
                    try:
                        if item.endswith('.torrent'): 
                            if not os.path.exists(f'C:\\Users\\{username}\\Downloads\\Torrentler'):
                                os.makedirs(f'C:\\Users\\{username}\\Downloads\\Torrents') 
                                self.textArea.insertPlainText('Torrents has been created. \n')
                                move(f'C:\\Users\\{username}\\Downloads\\{item}', f'C:\\Users\\{username}\\Downloads\\Torrentler')
                            else:
                                move(f'C:\\Users\\{username}\\Downloads\\{item}', f'C:\\Users\\{username}\\Downloads\\Torrentler')
                        elif item.endswith(tuple(ext_list[count])): 
                            if not os.path.exists(f'C:\\Users\\{username}\\Downloads\\{ext_list_str[count]}'): 
                                os.makedirs(f'C:\\Users\\{username}\\Downloads\\{ext_list_str[count]}')
                                self.textArea.insertPlainText(f' {ext_list_str[count]} has been created. \n')
                                move(f'C:\\Users\\{username}\\Downloads\\{item}', f'C:\\Users\\{username}\\Downloads\\{ext_list_str[count]}')
                            else:
                                move(f'C:\\Users\\{username}\\Downloads\\{item}', f'C:\\Users\\{username}\\Downloads\\{ext_list_str[count]}')
                    except:
                        pass
                count+=1
        else:
            self.textArea.insertPlainText("This program can't run right now because operating system is not Windows :((")
        self.textArea.insertPlainText('It\'s Done!')
        self.butonexit.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())
