import sys
import os.path
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import cv2
import numpy as np
import os,sys
import os.path
import cv2, glob
images=glob.glob(r'C:\Documents\python\template\cropped denomination_(FINAL)\*.jpg')



class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(450, 150, 1000, 450)
        self.setWindowTitle("Currency Recognition and Conversion")
        self.setWindowIcon(QtGui.QIcon('rupee.png'))
    
        
##        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
##        extractAction.setShortcut("Ctrl+Q")
##        extractAction.setStatusTip('Leave The App')
##        extractAction.triggered.connect(self.close_application)

        
		
        self.label1 = QtGui.QLabel(self)
        self.label1.move(350,100)
        self.label1.setFont(QtGui.QFont("Calibri",25, QtGui.QFont.Bold))
        self.label1.resize(500,70)

        self.label2 = QtGui.QLabel(self)
        self.label2.move(350,200)
        self.label2.setFont(QtGui.QFont("Calibri", 25, QtGui.QFont.Bold))
        self.label2.resize(500,70)

        self.label3 = QtGui.QLabel(self)
        self.label3.move(350,300)
        self.label3.setFont(QtGui.QFont("Calibri",25, QtGui.QFont.Bold))
        self.label3.resize(500,70)

        self.label4 = QtGui.QLabel(self)
        self.label4.move(100,300)
        self.label4.setFont(QtGui.QFont("Calibri",25, QtGui.QFont.Bold))
        self.label4.resize(350,70)
        self.label4.setText('Value(in Rupees):')

        self.label5 = QtGui.QLabel(self)
        self.label5.move(100,200)
        self.label5.setFont(QtGui.QFont("Calibri",25, QtGui.QFont.Bold))
        self.label5.resize(350,70)
        self.label5.setText('Denomination:')

        self.label6 = QtGui.QLabel(self)
        self.label6.move(100,100)
        self.label6.setFont(QtGui.QFont("Calibri",25, QtGui.QFont.Bold))
        self.label6.resize(350,70)
        self.label6.setText('Currency:')

        self.statusBar()

##        mainMenu = self.menuBar()
##        fileMenu = mainMenu.addMenu('&File')
##        fileMenu.addAction(extractAction)        
##        fileMenu.addAction(openFile)

        
        
        self.home()

    def home(self):
        
        
        
        extractAction = QtGui.QAction(QtGui.QIcon('currency.png'), 'Open File', self)
        extractAction.triggered.connect(self.file_open)
        extractAction.setShortcut("Ctrl+O")
        extractAction.setStatusTip('Open File')

        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        extractBattel = QtGui.QAction(QtGui.QIcon('switch.jpg'), 'Close', self)
        extractBattel.triggered.connect(self.close_application)
        extractBattel.setShortcut("Ctrl+q")
        extractBattel.setStatusTip('Close')

        
        self.toolBar = self.addToolBar("extractBattel")
        self.toolBar.addAction(extractBattel)

##        Game = QtGui.QAction(QtGui.QIcon('guitar.jpg'), 'TP', self)
##        Game .triggered.connect(self.message_application)
##        Game .setStatusTip('OOPs')
##
##        
##        self.toolBar = self.addToolBar("Game ")
##        self.toolBar.addAction(Game )

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(100, 400, 550, 20)

        
        self.show()


    def message_application(self):
        self.completed=0
        self.progress.setValue(self.completed)

        choice = QtGui.QMessageBox.information(self,'Oops!',"No match found")
        
        
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Close',"Do you want to Exit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
           
            sys.exit()
        else:
            pass

    def download(self):
        
        self.completed = 0

        while self.completed < 75:
            self.completed = (d/75)*100

        
            self.progress.setValue(self.completed)
            return

      
    def file_open(self):

        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')
        global d
        global a
        d=1
        
        self.label1.setText('')
        self.label2.setText('')
        self.label3.setText('')

        for image in images:
            img_rgb = cv2.imread(name)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

            template = cv2.imread(image,0)
            w, h = template.shape[::-1]

        ##    print (img_gray.shape)
            r = 500.0 / img_gray.shape[1]
            dim = (500, int(img_gray.shape[0] * r))

            resized1 = cv2.resize(img_rgb, dim, interpolation = cv2.INTER_AREA)    
            resized2 = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA)


            retval,binary = cv2.threshold(resized2, 110, 255, cv2.THRESH_BINARY)

            res = cv2.matchTemplate(binary,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.6
            loc = np.where( res >= threshold)
            a,b=loc[::-1]

            for pt in zip(*loc[::-1]):
                cv2.rectangle(resized1,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)

##            print (a,b)
            
            d=d+1
            global c

            self.download()
            basename=os.path.basename(image)
               
            c=os.path.splitext(basename)[0]

            print (c)
            c=int(c)

            if (c==9):
                self.message_application()
                
                
            if  a != ():
                cv2.imshow('detected',resized1)
##                cv2.imshow('resized2',resized2)
                
                self.completed=100
                self.progress.setValue(self.completed)
               
                
            
##                print ('c=',c)
                    
                if (c==1 or c==2):
                    
                    self.label1.setText('Indian Rupee')
                    self.label1.show()

                    self.label2.setText('10 Rupees')
                    self.label2.show()

                    self.label3.setText('10 ')
                    self.label3.show()

                elif (c==3 or c==4):
    ##                    print('Currency: Indian Rupee')
    ##                    print('Denomination:20 Rupees')
    ##                    print('Value= 20 Rupees')

                    self.label1.setText('Indian Rupee')
                    self.label1.show()

                    self.label2.setText('20 Rupees')
                    self.label2.show()

                    self.label3.setText('20 ')
                    self.label3.show()
                    
                elif  (c==5 or c==6):
    ##                    print('Currency: Indian Rupee')
    ##                    print('Denomination:50 Rupees (old)')
    ##                    Value= 50 Rupees

                    self.label1.setText('Indian Rupee')
                    self.label1.show()

                    self.label2.setText('50 Rupees (old)')
                    self.label2.show()

                    self.label3.setText('50 ')
                    self.label3.show()

                elif  (c==7 or c==8):
    ##                    print('Currency: Indian Rupee')
    ##                    print('Denomination:50 Rupees (new)')
    ##                    Value= 50 Rupees

                    self.label1.setText('Indian Rupee')
                    self.label1.show()

                    self.label2.setText('50 Rupees (new)')
                    self.label2.show()

                    self.label3.setText('50 ')
                    self.label3.show()
                   
                elif  (c==9 or c==10):
    ##                    print('Currency: Indian Rupee')
    ##                    print('Denomination:100 Rupees ')
    ##                    Value= 100 Rupees

                    self.label1.setText('Indian Rupee')
                    self.label1.show()

                    self.label2.setText('100 Rupees')
                    self.label2.show()

                    self.label3.setText('100 ')
                    self.label3.show()
                    
                elif  (c==11 or c==12):
    ##                    print('Currency: Indian Rupee')
    ##                    print('Denomination:200 Rupees ')
    ##                    Value= 200 Rupees

                    self.label1.setText('Indian Rupee')
                    self.label1.show()

                    self.label2.setText('200 Rupees ')
                    self.label2.show()

                    self.label3.setText('200 ')
                    self.label3.show()

                elif  (c==13 or c==14):
    ##                    print('Currency: Indian Rupee')
    ##                    print('Denomination:500 Rupees ')
    ##                    Value= 500 Rupees

                    self.label1.setText('Indian Rupee')
                    self.label1.show()

                    self.label2.setText('500 Rupees ')
                    self.label2.show()

                    self.label3.setText('500 ')
                    self.label3.show()

                elif  (c==15 or c==16):
    ##                    print('Currency: Indian Rupee')
    ##                    print('Denomination:2000 Rupees ')
    ##                    Value= 2000 Rupees

                    self.label1.setText('Indian Rupee')
                    self.label1.show()

                    self.label2.setText('2000 Rupees ')
                    self.label2.show()

                    self.label3.setText('2000 ')
                    self.label3.show()

                elif  (c==17 or c==18):
    ##                    print('Currency: US Dollar ')
    ##                    print('Denomination:1 Dollar ')
                    Value= 1*64 

                    self.label1.setText('US Dollar ')
                    self.label1.show()

                    self.label2.setText('1 Dollar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==19 or c==20):
    ##                    print('Currency: US Dollar ')
    ##                    print('Denomination:5 Dollars ')
    ##                    Value= 5*64 Rupees

                    self.label1.setText('US Dollar ')
                    self.label1.show()

                    self.label2.setText('5 Dollars ')
                    self.label2.show()

                    self.label3.setNum(5*64)
                    self.label3.show()

                elif  (c==21 or c==22):
##                    print('Currency: US Dollar ')
##                    print('Denomination:10 Dollars ')
##                    Value= 10*64 

                    self.label1.setText('US Dollar ')
                    self.label1.show()

                    self.label2.setText('10 Dollars ')
                    self.label2.show()

                    self.label3.setNum(10*64 )
                    self.label3.show()

                   

                elif  (c==23 or c==24):
##                    print('Currency: US Dollar ')
##                    print('Denomination:20 Dollars ')
                    Value= 20*64

                    self.label1.setText('US Dollar ')
                    self.label1.show()

                    self.label2.setText('20 Dollars')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==25 or c==26):
##                    print('Currency: euro ')
##                    print('Denomination:10 euro ')
                    Value= 10*80 

                    self.label1.setText('Euro')
                    self.label1.show()

                    self.label2.setText('10 Euro')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==27 or c==28):
##                    print('Currency: pound ')
##                    print('Denomination:5 pound ')
                    Value= 5*90 

                    self.label1.setText('Pound')
                    self.label1.show()

                    self.label2.setText('5 Pound ')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==29 or c==30):
##                    print('Currency: pound ')
##                    print('Denomination:20 pound ')
                    Value= 20*90 

                    self.label1.setText('Pound')
                    self.label1.show()

                    self.label2.setText('20 Pound ')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==31 or c==32):
##                    print('Currency: rupiah ')
##                    print('Denomination:2000 rupiah ')
                    Value= 2000 

                    self.label1.setText('Rupiah ')
                    self.label1.show()

                    self.label2.setText('2000 Rupiah')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==33 or c==34):
##                    print('Currency: rupiah ')
##                    print('Denomination:5000 rupiah ')
                    Value= 5000 

                    self.label1.setText('Rupiah')
                    self.label1.show()

                    self.label2.setText('5000 Rupiah')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()


                elif  (c==35 or c==36):
##                    print('Currency: Aus dollar ')
##                    print('Denomination:5 Aus dollar')
                    Value= 5*51 

                    self.label1.setText('Australian dollar')
                    self.label1.show()

                    self.label2.setText('5 Australian dollar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()


                elif  (c==37 or c==38):
##                    print('Currency: Australian dollar')
##                    print('Denomination:5 Australian dollar')
                    Value= 10*51 

                    self.label1.setText('Australian dollar')
                    self.label1.show()

                    self.label2.setText('5 Australian dollar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==39 or c==40):
##                    print('Currency: Australian dollar ')
##                    print('Denomination:5 Australian dollar')
                    Value= 20*51

                    self.label1.setText('Australian dollar')
                    self.label1.show()

                    self.label2.setText('5 Australian dollar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()


                elif  (c==41 or c==42):
##                    print('Currency: Australian dollar ')
##                    print('Denomination:5 Australian dollar')
                    Value= 50*51 

                    self.label1.setText('Australian dollar ')
                    self.label1.show()

                    self.label2.setText('50 Australian dollar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==43 or c==44):
##                    print('Currency: Dirham ')
##                    print('Denomination:5 Dirham')
                    Value= 5*17 

                    self.label1.setText('Dirham ')
                    self.label1.show()

                    self.label2.setText('5 Dirham')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==45 or c==46):
##                    print('Currency: dirham ')
##                    print('Denomination:10 dirham')
                    Value= 10*17 

                    self.label1.setText('Dirham ')
                    self.label1.show()

                    self.label2.setText('10 Dirham')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==47 or c==48):
##                    print('Currency: dirham ')
##                    print('Denomination:20 dirham')
                    Value= 20*17 

                    self.label1.setText('Dirham')
                    self.label1.show()

                    self.label2.setText('20 Dirham')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==49 or c==50):
##                    print('Currency: dirham ')
##                    print('Denomination:50 dirham')
                    Value= 50*17 

                    self.label1.setText('Dirham ')
                    self.label1.show()

                    self.label2.setText('50 Dirham')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==51 or c==52):
##                    print('Currency: dirham ')
##                    print('Denomination:100 dirham')
                    Value= 100*17 

                    self.label1.setText('Dirham')
                    self.label1.show()

                    self.label2.setText('100 Dirham')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==53 or c==54):
##                    print('Currency:Singapore dollar ')
##                    print('Denomination:5 singapore dollar')
                    Value= 5*49 

                    self.label1.setText('Singapore Dollar')
                    self.label1.show()

                    self.label2.setText('5 Singapore Dollar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==55 or c==56):
##                    print('Currency: singapore dollar ')
##                    print('Denomination:10 singapore dollar')
                    Value= 10*49 

                    self.label1.setText('Singapore Dollar')
                    self.label1.show()

                    self.label2.setText('10 Singapore Dollar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==57 or c==58):
##                    print('Currency: singapore dollar')
##                    print('Denomination:20 singapore dollar')
                    Value= 2*49 

                    self.label1.setText('Singapore Dollar')
                    self.label1.show()

                    self.label2.setText('2 Singapore Dollar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==59 or c==60):
##                    print('Currency: riyal ')
##                    print('Denomination:1 riyal')
                    Value= 1*17 

                    self.label1.setText('Riyal')
                    self.label1.show()

                    self.label2.setText('1 Riyal')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()


                elif  (c==61 or c==62):
##                    print('Currency: Hk dollar ')
##                    print('Denomination:10 Hk dollar')
                    Value= 10*8 

                    self.label1.setText('Hk Dollar ')
                    self.label1.show()

                    self.label2.setText('10 Hk Dollar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==63 or c==64):
##                    print('Currency: rufiyaa')
##                    print('Denomination:5 rufiyaa')
                    Value= 5*4 

                    self.label1.setText('Rufiyaa')
                    self.label1.show()

                    self.label2.setText('5 Rufiyaa')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==65 or c==66):
##                    print('Currency: rufiyaa')
##                    print('Denomination:10 rufiyaa')
                    Value= 10*4 

                    self.label1.setText('Rufiyaa')
                    self.label1.show()

                    self.label2.setText('10 Rufiyaa')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==67 or c==68):
##                    print('Currency: lira')
##                    print('Denomination:5 lira')
                    Value= 5*17 

                    self.label1.setText('Lira')
                    self.label1.show()

                    self.label2.setText('5 Lira')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==69 or c==70):
##                    print('Currency: dinar')
##                    print('Denomination: 10 dinar')
                    Value= 10*215 

                    self.label1.setText('Dinar')
                    self.label1.show()

                    self.label2.setText('10 Dinar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==71 or c==72):
##                    print('Currency: Nepalese rupee')
##                    print('Denomination: 10 Nepalese rupee')
                    Value= 10*0.63 

                    self.label1.setText('Nepalese rupee')
                    self.label1.show()

                    self.label2.setText('10 Nepalese rupee')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==73 or c==74):
##                    print('Currency: Nepalese rupee')
##                    print('Denomination: 20 Nepalese rupee')
                    Value= 20*0.63 

                    self.label1.setText('Nepalese rupee')
                    self.label1.show()

                    self.label2.setText('20 Nepalese rupee')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==75 or c==76):
##                    print('Currency: Nepalese rupee')
##                    print('Denomination: 50 Nepalese rupee')
                    Value= 50*0.63 

                    self.label1.setText('Nepalese rupee')
                    self.label1.show()

                    self.label2.setText('50 Nepalese rupee')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==77 or c==78):
##                    print('Currency: yuan')
##                    print('Denomination: 10 yuan')
                    Value= 100*64 

                    self.label1.setText('US Dollar')
                    self.label1.show()

                    self.label2.setText('100 Dollar')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==79 or c==80):
##                    print('Currency: yuan')
##                    print('Denomination: 10 yuan')
                    Value= 20*2

                    self.label1.setText('Baht')
                    self.label1.show()

                    self.label2.setText('20 Baht')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                
                elif  (c==81 or c==82):
##                    print('Currency: yuan')
##                    print('Denomination: 10 yuan')
                    Value= 100*2

                    self.label1.setText('Baht')
                    self.label1.show()

                    self.label2.setText('100 Baht')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()

                elif  (c==83 or c==84):
##                    print('Currency: yuan')
##                    print('Denomination: 10 yuan')
                    Value= 500*2

                    self.label1.setText('Baht')
                    self.label1.show()

                    self.label2.setText('500 Baht')
                    self.label2.show()

                    self.label3.setNum(Value)
                    self.label3.show()


                   
                break
           
            
            cv2.destroyAllWindows()


    

    
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
