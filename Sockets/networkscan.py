
import os

NET = "192.168.1"

for i in range(10): # 0 - 255 --> host 
    ip = NET + "." + str(i)
    obj = os.popen(f"ping {ip}")
    output = obj.read()
    if not "unreach" in output:
        print(f"{ip} is active")
