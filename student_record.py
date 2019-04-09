for i in range(int(input())):
    n = int(input())
    l = list(input().split(' '))
    c = 0
    max = 0
    for j in range(n):
        arr = l[c:c+4]
        name = arr[0]
        marks = list(map(int,arr[1:]))
        avg = int(sum(marks)/3)
        c = c + 4
        if(max == 0):
            max = avg
            naam = name 
        elif(max<avg):
            max = avg
            naam = name
        elif (max==avg):
            naam += " "+name
    print(naam + " " + str(max))
        