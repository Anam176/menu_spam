import os
if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("run2").wa_sampingan().Menu()
   except Exception as e:
       exit(str(e))
