import time
import webbrowser

valid = 1
counter = 1
check = 1

while (check == 1):
   if (20 == int((time.strftime("%d", time.localtime())))):# Program performs only if date matches 20(or any date given)

       while (counter == 1):
           
           T = int((time.strftime("%H",time.localtime()))) # Reads the current hour time from computer
           ff_path = webbrowser.get("c:/Program Files (x86)/Mozilla Firefox/firefox.exe %s").open("https://www.youtube.com/watch?v=uHNxEVY9v98")
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
    
   
            
    
        

       
            
    
