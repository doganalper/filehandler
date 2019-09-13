import os
from shutil import move
from getpass import getuser

audio=['.aif','.cda','.mid','.midi','.mp3','.mpa','.wav']
compressed=['.7z','.pkg','.rar','.rpm','.z','.zip']
discandmedia=['.bin','.dmg','.iso','.vcd']
database=['.csv','.dat','.log','.mdb','.sav','.sql','.tar','.xml']
executables=['.apk','.bat','.bin','.cgi','.com','.exe','.jar','.wsf']
image=['.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.psd','.svg','.tiff']
internetrelated=['.asp','.aspx','.cgi','.pl','.html','.htm','.js','.css','.jsp','.php','.xhtml']
programming=['.c','.class','.py','.cs','.java','.vb']
video=['.avi','.flv','.mp4','.mpg','.mpeg','.swf','.vob','.wmv']
office=['.key','.pps','ppt','.pptx','.xlr','.xls','.xlsx','.doc','.docx','.pdf','.txt','.wpd','.odt'] 
ext_list=[audio,compressed,discandmedia,database,executables,image,internetrelated,programming,video,office]
ext_list_str=['audio','compressed','discandmedia','database','executables','image','internetrelated','programming','video','office']
count=0

#bilgisayarın kullanıcı adını aldık.
username=getuser()

#klasör içini tarayıp listeye attık.
liste=os.listdir(f'C:\\Users\\{username}\\Downloads')

while count<len(ext_list):
    
    for item in liste:
        try:
            if item.endswith('.torrent'): #listedeki itemlerin (.torrent) ile bitenleri seçtik
                if not os.path.exists(f'C:\\Users\\{username}\\Downloads\\Torrentler'): #Torrentler adlı klasör yoksa koşulu koyduk
                    os.makedirs(f'C:\\Users\\{username}\\Downloads\\Torrentler') #klasörü yaratır
                    print('Torrentler klasörü oluşturuldu.')
                    move(f'C:\\Users\\{username}\\Downloads\\{item}', f'C:\\Users\\{username}\\Downloads\\Torrentler') #klasik dosya taşıma
                else:
                    move(f'C:\\Users\\{username}\\Downloads\\{item}', f'C:\\Users\\{username}\\Downloads\\Torrentler')
            elif item.endswith(tuple(ext_list[count])): 
                if not os.path.exists(f'C:\\Users\\{username}\\Downloads\\{ext_list_str[count]}'): 
                    os.makedirs(f'C:\\Users\\{username}\\Downloads\\{ext_list_str[count]}')
                    print(f' {ext_list_str[count]} klasörü oluşturuldu.')
                    move(f'C:\\Users\\{username}\\Downloads\\{item}', f'C:\\Users\\{username}\\Downloads\\{ext_list_str[count]}')
                else:
                    move(f'C:\\Users\\{username}\\Downloads\\{item}', f'C:\\Users\\{username}\\Downloads\\{ext_list_str[count]}')
        except:
            pass
    count+=1
print('İşlem bitmiştir.')
os.system("pause")
