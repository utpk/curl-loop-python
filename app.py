import requests
import time

print("Startup...")
endpoints = ["https://login.microsoftonline.com","https://github.com","https://welltesting.free.beeceptor.com"]
i=0

while True:
  time.sleep(10) # pause for 10 seconds
  try:
    url = endpoints[i%3]
    print("curl ",url,"... ",end='', flush=True)
    r = requests.head(url, timeout=30, verify=Fause)
    r.raise_for_status()
  except Exception as e:
    print("FAILED",time.localtime())
  else:
    print("OK")
  finally:
    i+=1
