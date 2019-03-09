import os, time


while True:
    try:
        os.system("clear")
        #Change ports monitored here
        os.system("netstat -tupn | grep -E \":(22|445|23|53|25|587|465|110|21|443|80) .*\"")
        time.sleep(1)
    except KeyboardInterrupt:
        False
        exit()
