import os
s =input("do you want to shutdown [yes/no]")
def shutdown(s):
    if s=="y":
     print("shutting down")
     os.system("/s /t 1")
    else:
     print("not shutting down")