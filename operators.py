#import query_listener
#query_listener.takecommand()
#Q=query_listener.query

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



