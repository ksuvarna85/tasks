def func1(i,j):

    lst=[]
    lst_nos=[]
    flag=0

    for x in range(i,j):
        lst_nos.append(x)
        z=bin(x).replace('0b',"")
        lst.append(z)

    #print(lst,lst_nos)

    #print(len(lst[0]))
    lst_ans=[]

    for x in lst:
        for y in range(0,len(x)-1):
            if x[y]=='1' and x[y+1]=='1':
                flag=1
                break
            else:
                flag=0
        if flag==1:
            lst_ans.append(True)
        else:
            lst_ans.append(False)
    #print(lst_ans)
    dict_ans={}
    for key in lst_nos:
        for value in lst_ans:
            dict_ans[key]=value
            lst_ans.pop(0)
            break
    return (dict_ans)
while(True):
    try:
        i=int(input("enter lower limit"))
        j=int(input(("enter the upper limit")))
        break
    except:
        print("PLEASE ENTER A NUMBER")

ans=func1(i,j)
print(ans)
