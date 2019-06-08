import os
import time

emptylogfile = []
Rinow = time.strftime('%d%m%Y%H%M%S') #in the format DMYHMS
with open("AuthenticationLog" + Rinow + ".txt", "w") as f:
    for i in emptylogfile:
        f.write(i)
x = "AuthenticationLog" + Rinow + ".txt"
os.system("powershell Get-EventLog -logname security -instanceid 4625,4624 -newest 10 >" + x)



