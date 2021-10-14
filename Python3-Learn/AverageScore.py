if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    mylist=student_marks.get(query_name)
    result=sum(mylist)/len(mylist)
    print(format(result,'.1f'))