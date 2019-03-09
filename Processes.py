import os, time

GoodProcesses = []
NewProcesses = []
i = 0

while i != 60:
    os.system("ps -A > tempps.txt")
    i = i + 1
with open("tempps.txt","r") as DataIn:
    for line in DataIn:
        GoodProcesses.append(str(line))
DataIn.close()
#os.remove("tempps.txt")
while True:
    try:
        os.system("clear")
        os.system("ps -A > tempps.txt")
        with open("tempps.txt","r") as DataIn:
            for line in DataIn:
                if line not in GoodProcesses and " ps\n" not in line and " sh\n" not in line:
                    NewProcesses.append(str(line))
                else:
                    pass
        DataIn.close
        print("NEW PROCESSES:")
        NewProcesses = list(dict.fromkeys(NewProcesses))
        for process in NewProcesses:
            print(str(process).strip("\n"))
            #os.system("ps aux | grep "+str(process.split(" ")[1]))
        time.sleep(1)
    except KeyboardInterrupt:
        exit()
