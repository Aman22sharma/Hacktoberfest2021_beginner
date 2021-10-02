# AUTHOR: Neethu Joji George
# Python3 Concept: quicksort
# GITHUB: https://github.com/srikar999

def partition(lst,start,end):
    pivot=lst[start]
    pivot_index=start
    while start<end:
        while start<len(lst) and lst[start]<pivot:start+=1
        while lst[end]>pivot:end-=1
        if start<end:
            lst[start],lst[end]=lst[end],lst[start]
    lst[end],lst[pivot_index]=lst[pivot_index],lst[end]
    return end
def quick(lst,start,end):
    if start<end:
        p=partition(lst,end,start)
        quick(lst,start,p-1)
        quick(lst,p+1,end)
l=[0,5,0,8,0,3]
quick(l,0,len(l)-1)
print(l)
