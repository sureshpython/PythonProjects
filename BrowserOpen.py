
import time
import webbrowser
import subprocess
import threading


def open():
   subprocess.call(["c:/Program Files (x86)/Mozilla Firefox/firefox.exe"])


def main():
   
   valid = 1
   counter = 1
   check = 1
   ourprogram = threading.Thread(target = open)
   ourprogram.start()

   while check == 1:
      
      
      if (1 == int((time.strftime("%d", time.localtime())))):# Program performs only if date matches 20(or any date given)

          while (counter == 1):
              
              T = int((time.strftime("%H",time.localtime()))) # Reads the current hour time from computer
              ff_path = webbrowser.open("https://www.youtube.com/watch?v=uHNxEVY9v98")
              N = T     # Passes the current hour number to N variable
              valid = 1
              
              while (T != 24) and (valid == 1) : 
                  if (N == int((time.strftime("%H",time.localtime())))):# Comparing to check if computer hour time changes
                      
                      T = int((time.strftime("%H",time.localtime())))
                      valid = 1
                     
               
                  else:
                       valid = 0 
                       counter = 1
                       T = int((time.strftime("%H",time.localtime())))
      

      else:
         pass
             
if (__name__ == "__main__"):
   main()


   
