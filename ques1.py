list=['hello','abc','great','hiyo']
sorted_list = sorted(list, key=lambda t: t[-2]) 
print(sorted_list)



for i in range(0,len(list)-2):
    for j in range(i+1,len(list)-2):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)