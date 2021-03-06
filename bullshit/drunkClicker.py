'''
READ THIS FIRST!
This script makes some initial assumptions,
1) You already have the Vaagur ancient and it is at MAX
	The timing of the buffs is based off of this.
	If not; you can still use this script with out the buffs by just using [-c X,Y]
2) You have all the available buffs from your adventures.
	Not necessary for it to work but I am just assuming.

3) You are using Windows - this is a must, no way around it.
	to use:
	- install python 3.x ( I used 3.4 )
	- install the win32api for python - http://sourceforge.net/projects/pywin32/files/pywin32/
	- from cmd, cd to the location of drunkCLicker.py
	- type python drunkClicker.py [-t x,y] to test where the mouse will move to on your screen.
		eg: [python drunkCLicker.py -t 1700,600]
		position this so that the mouse lands on top of the monster.
	- Once mouse position is confirmed -c x,y or -bc x,y can be used to start the clicking.
		eg: [python drunkClicker.py -c 1700,600] this will perform just mouse clicks.
		eg: [python drunkCLicker.py -bc 1700,600] This will perform mouse clicks with DR Ceremony.
4) This script may be CPU intensive to older systems. May cause lag.
	As a fail safe, moving the mouse will end this script.
5) If you experience system unresponsiveness,
	you can adjust the User Defined Variables below.

'''

from time import sleep
import win32api
import win32con
import win32com.client
import sys
import random
import threading
import pythoncom
import datetime
import getopt



#User Definable Variables
#For Timing - 1 = 1 sec : 0.1 = .1 Sec : 0.01 = SUPA FUCKING QUICK
pressSleep = 0.03 	#How long to wait in between pressing buffs
clkCount = 100		#How many times to click before moving the mouse
clkSleep = 0.03		#How long to pause in-between each click


'''
DO NOT EDIT BELOW THIS LINE
***************************************************************************************************
Or do edit, I don't really care . . .
'''
#Global Variables
mvPOS = 0
theShell = 0
lvlProgress = 4




def click (x,y):
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def getPOS ():
	xg, yg = win32api.GetCursorPos()
	return xg


def mvMouse (xm,ym):
	global mvPOS #only mvMouse may update this global, spot check! re-spot check!
	#re-position mouse within a 20 pixel area, this will avoid the "spam checker" in the game
	newPOSX = random.randint(xm -10, xm + 10)
	newPOSY = random.randint(ym -10, ym + 10)
	win32api.SetCursorPos((newPOSX,newPOSY))
	mvPOS= newPOSX #only mvMouse may update this global, spot check! re-spot check!
	return newPOSX, newPOSY


def mouseTest ( pos1, pos2 ):
		win32api.SetCursorPos((pos1, pos2))


def timesUP (mintoadd ) :
	newTime = []
	tNow = datetime.datetime.now()
	fTime = tNow + datetime.timedelta(minutes=mintoadd)
	x = str(fTime.time())
	x =  x.split('.')[0]					#	This
	newTime.extend(x.split(':'))				#	Shit
	if int(newTime[0]) >12 :				#	IS
		newTime[0] = str(int(newTime[0]) -12)		#	BANANAS
	return newTime[0]+':'+newTime[1]+':'+newTime[2]


def holdUp ( waitTime ) :
	global mvPOS

	while waitTime != 0 :
		if mvPOS == 0 :
			return 0
		waitTime = waitTime -0.5
		sleep(0.5)

def lvlProg ( ) :
	global theShell
	theShell.SendKeys( 'a', 0)

def fngrBlast ( ):
	global theShell
	global pressSleep


	sleep(pressSleep)
	theShell.SendKeys( '1', 0)
	sleep(pressSleep)
	theShell.SendKeys( '2', 0)
	sleep(pressSleep)
	theShell.SendKeys( '3', 0)
	sleep(pressSleep)
	theShell.SendKeys( '4', 0)
	sleep(pressSleep)
	theShell.SendKeys( '5', 0)
	sleep(pressSleep)
	theShell.SendKeys( '7', 0)

def darkRit () :
	global theShell
	global pressSleep

	theShell.SendKeys( '8', 0)
	sleep(pressSleep)
	theShell.SendKeys( '6', 0)
	sleep(pressSleep)
	theShell.SendKeys( '9', 0)



def darkRitload () :
	global theShell
	global pressSleep

	theShell.SendKeys( '8', 0)
	sleep(pressSleep)
	theShell.SendKeys( '9', 0)


def buffStart () :
	'''
	THE DR CEREMONY
	Finger Blast Buffs (1,2,3,4,5,7)
	Dark Ritual combo (8,6,9)
	Wait 15 minutes
	Energize Reload (8,9)
	Use Finger Blast Buffs (1,2,3,4,5,7) every 2.5 min - 6 times (total = 15min)
	Repeat step 1.
	'''
	global mvPOS

	curProg = lvlProgress
	fbCD = 150 #2.5 min for lowest CD
	drCD = 900 #15 min for DR Ceremony
	while mvPOS != 0 :
		if curProg == 0:
			lvlProg()
			curProg = lvlProgress
		else :
			curProg = curProg -1
		fngrBlast ()
		darkRit ()
		print ('DR START : Dark Ritual Ceremony has started, will complete at ' + timesUP(15) )
		if holdUp (drCD) == 0: #A return of 0 means the mouse has moved in MAIN__
			return
		darkRitload ()
		print ('DR DONE : Dark Ritual Ceremony is complete, next ceremony at ' + timesUP(15) )
		#Repeat the none DR buffs 6 times, 2.5 min each *6 = 15min
		for r in range(6) :
			fngrBlast ()
			if holdUp (fbCD ) == 0 :
				return

def main ( cords, buffs  )	:
	global mvPOS
	global clkSleep
	global clkCount
	global theShell


	xy = cords.split (',')
	POS1 = int(xy[0])
	POS2 = int(xy[1])
	curPOS1, curPOS2 = mvMouse( POS1, POS2 )
	#mvPOS to sync with latest mvMouse
	mvPOS = curPOS1
	click(curPOS1, curPOS2) #Click it once to gain focus

	if buffs == 1 :
		pythoncom.CoInitialize()
		theShell = win32com.client.Dispatch("WScript.shell")
		theShell.AppActivate( 'I <3 Scotch' )
		tDR = threading.Thread(name='buffStart', target=buffStart)
		tDR.start()



	'''
	This is the 'MAIN__' Script Loop, it will continue until the mouse moves.
	'''
	#while the mouse is where the app set it, continue, otherwise stop.
	clkCountTick = clkCount
	print ('Clicking like fucking crazzy!' )
	while mvPOS != 0 :
		click(curPOS1, curPOS2)
		if getPOS() != curPOS1 :
			print ( 'Mouse moved! Expeted: ' + str(getPOS()) + ' Actuall: ' + str(curPOS1) )
			mvPOS = 0 #This tells the Buffing thread and MAIN__ loop to stop.
		clkCountTick = clkCountTick -1
		sleep(clkSleep) #not using holdUp since we are already past the getPOS, will never be true
		if clkCountTick == 0: #After we click X times, move the mouse a bit.
			curPOS1, curPOS2 = mvMouse( POS1, POS2 )
			clkCountTick = clkCount


#BEGIN
doBuffs = 0

opts, args = getopt.getopt(sys.argv[1:], 'p:c:t:b') #create an array for variables
for o,a in opts :	#o is the flag argument, a is for the following variable
	if o ==  '-t' :
   	#This will simply move the mouse to the x,y
		xy = a.split(',')
		mouseTest( int(xy[0]), int(xy[1]) )
	if o == '-b':
		doBuffs = 1
	if o == '-c' :
		main(a, doBuffs)
