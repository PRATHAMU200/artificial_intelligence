#Binary Files Complete
import pickle as p
import pywhatkit as kit
import datetime
def send(to,content):
    hour = int(datetime.datetime.now().hour)
    minu = int(datetime.datetime.now().minute)
    kit.sendwhatmsg(to,content,hour,minu+1)
def Write():
    f=open("STU.dat","ab")
    d={}
    while True:
        nm=input("enter name")
        num=input("enter number")
        d['nm']=nm
        d['num']=num
        p.dump(d,f)
        x=input("continue???")
        if x=='N' or x=='n':
            break
    f.close()
con="i love pythob"
    
def Search(l,con):
    try:
        f=open("STU.dat","rb")
        d={}
        fn=False
        try:
            while True:
                d=p.load(f)
                if d["nm"]==l:
                    send(d["num"],con)
                    fn=True
        except EOFError:
            f.close()
            if fn==False:
                print("Record Not Found")
    except FileNotFoundError:
        print("File Doesnot exists")
Write()

def group(a):
    l=a.split()
    lst=[]
    for i in range(3,len(l)):
        lst.append(l[i])
        top=len(lst)-1
    for i in range(top,-1,-1):
        Search(lst[i],con)
a=input("enter")
group(a)
