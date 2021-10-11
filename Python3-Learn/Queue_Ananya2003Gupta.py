// AUTHOR: Ananya
// Python3 Concept: Queue
// GITHUB: https://github.com/Ananya2003Gupta

lim=100
s=[]
def enqueue(s):
    global lim
    n=int(input("Enter the value:"))
    l=len(s)
    if l==lim:
        print("Overflow")
    else:
        s.append(n)
        print("Number added in queue")

def dequeue(s):
    if len(s)==0:
        print("Underflow")
    else:
        a=s.pop(0)
        print("Deleted {} from queue".format(a))

def queuelim():
    global lim
    lim=int(input("Enter the queue limit"))
    print("Limit set as",lim)

def view(s):
    for i in range(len(s)):
        print(s[i])

def frontandrear(s):
    if len(s)==0:
        print("Queue is empty")
    else:
        print("Front element is",s[0])
        print("Rear element is",s[len(s)-1])

def main():
    c=1
    while c!=0:
        print("""Menu
1.Add elements in queue
2.Delete elements from queue
3.Set queue limit(By default queue limit is 100)
4.View queue
5.View Front and Rear elements of queue
6.Exit""")
        a=int(input("Enter your choice:"))
        if a==1:
            enqueue(s)
        elif a==2:
            dequeue(s)
        elif a==3:
            queuelim()
        elif a==4:
            view(s)
        elif a==5:
            frontandrear(s)
        elif a==6:
            c=0
        else:
            print("Invalid Input")
main()
