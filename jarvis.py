from speach import speak # for speaking use speak("enter text to speak")

from wish_me import wishMe # for wishing use wishMe()

from security import security # for login into the jarvis

import query_listener  # the commands said by person (constant)







speak(" please login into your account")
print(" default username and password root ")
security()
speak("login succesfull")
print("login succesfull,,,,")

wishMe()










# functions for operational settings


def add():
      a= query
      lst=[]
      for i in a.split():
            if i.isdigit():
                  lst+=[int(i)]
      d=sum(lst)
      print(d)
def sub():
      a= query
      lst=[]
      for i in a.split():
            if i.isdigit():
                  lst+=[int(i)]
      if len(lst)==2:
            print(lst[1]-lst[0])
      else:
            print("subtraction requires only two operands")
      
def mul():
      s=1
      a= query
      lst=[]
      for i in a.split():
            if i.isdigit():
                  lst+=[int(i)]
      for i in lst:
            s*=i
      print(s)
def div():
      a= query
      lst=[]
      for i in a.split():
            if i.isdigit():
                  lst+=[int(i)]
      if len(lst)==2:
            if lst[1]!=0:
                  print(lst[0]/lst[1])
            else:
                  print("divide by zero!")
      else:
            print("division requires only two operands")









#main program starts here
while True:            
    query_listener.takecommand()
    query = query_listener.query
    if "how are you" in query:
          speak("fine sir,")
    elif "division" in query or "divide" in query:
          div()
    elif "multiply" in query:
          mul()
    elif "add" in query:
          add()
    elif "subtract" in query or "subtraction" in query or "substract" in query:
          sub()
            

    



    
    

