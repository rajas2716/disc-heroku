from datetime import datetime, timedelta
import time
import requests
while 1:
    payload = {
    'content' : "!work"
    }

    header = {
    'authorization' : 'MzY3MjY5MTc4NzA2NjI0NTEy.YZi7NQ.q0IhwFmygmfj4UHdtEVrxmMDXrk'
    }

    r = requests.post("https://discord.com/api/v9/channels/892453734301433936/messages", data = payload, headers = header) 

    dt = datetime.now() + timedelta(hours=1)
    dt = dt.replace(minute=10)

    while datetime.now() < dt:
        time.sleep(1)