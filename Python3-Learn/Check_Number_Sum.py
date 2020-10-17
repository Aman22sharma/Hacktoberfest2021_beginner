def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    if s == target: 
        print ("sum(%s)=%s" % (partial, target))
    if s >= target:
        return
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 


if _name_ == "_main_":
    subset_sum([3,9,8,4,5,7,10],100)
                #numbers       #sum
#This Code Will Tell which numbers combination add upto the sum stated.
