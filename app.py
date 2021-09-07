import requests
import time
import urllib3

urllib3.disable_warnings()

print("Startup...")
endpoints = ["https://login.microsoftonline.com", "https://github.com"]
i = 0
fail_count = 0

while True:
    time.sleep(10)
    try:
        url = endpoints[i % len(endpoints)]
        print("curl", url, "... ", end="", flush=True)
        r = requests.head(url, timeout=30, verify=False)
        r.raise_for_status()
    except Exception as e:
        fail_count += 1
        print(r.elapsed, "FAILED", fail_count, time.ctime())
    else:
        print(r.elapsed, "OK")
    finally:
        i += 1
