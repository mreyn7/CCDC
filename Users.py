import os, time
from threading import Thread
################################################################################
################################################################################
def Integrity():
    while True:
        try:
            #Check MD5 of files and directories to make sure nothing is changed
            CurrentPasswd = os.system("md5sum /etc/passwd")
            CurrentShadow = os.system("md5sum /etc/shadow")
            """
            CurrentBin = os.system("md5deep -r /bin")
            CurrentEtc = os.system("md5deep -r /etc")
            """
            #Clears the terminal screen and prints a header
            os.system("clear");print("What\t\tStatus\n")
            #Compares the current and good MD5 to check for discrepencies
            if str(CurrentPasswd) != str(GoodPasswd):
                print("etc/passwd\tConflict")
            elif str(CurrentShadow) != str(GoodShadow):
                print("etc/shadow\tConflict")
            else:
                print("etc/passwd\tGood")
                print("etc/shadow\tGood")
            #Display users logged on
            print("\n\nUsers logged on:");os.system("w")
            #Pauses so that it runs every 1 second
            time.sleep(1)
        except KeyboardInterrupt:
            exit()
################################################################################
def Main():
    try:
        if __name__ == '__main__':
            Integrity()
    except KeyboardInterrupt:
        os.system("sudo pkill python")
        exit()
################################################################################
#Disables login of the root account
os.system("sudo passwd -l root")
#Installs md5deep
os.system("sudo apt-get install md5deep -y")
#Creates good MD5s of the /etc/passwd and /etc/shadow files
#Stores original copy into text files to be used as a compare if needed
GoodPasswd = os.system("md5sum /etc/passwd");os.system("cat /etc/passwd > ~/xj5fa2.txt")
GoodShadow = os.system("md5sum /etc/shadow");os.system("cat /etc/shadow > ~/a4mkh2.txt")
"""
GoodBin = os.system("md5deep -r /bin")
GoodEtc = os.system("md5deep -r /etc")
"""
Main()
