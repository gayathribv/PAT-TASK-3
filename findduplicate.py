"""
Python program to find duplicates in three lists of numbers
list1 = [1,2,3,4,5,6]
list2=[4,5,6,7,8,9]
list3=[1,2,7,8,10,11]

LOGIC:
compare list1 and list2 by traversing through the list; store the duplicates
list12_dup
compare list1 and list3 by traversing through the list; store the duplicates
in list13_dup
compare list2 and list3 by traversing through the list; store the duplicate
list23_dup
print uniq of all three lists list12_dup, list13_dup, list23_dup
"""

list1 =[1,2,3,4,5,6]
list2=[4,5,6,7,8,9]
list3=[1,2,7,8,10,11]
list12_dup=[]
list13_dup=[]
list23_dup=[]
all_list=[]
j=0

for i in list1:
    for j in range(0,len(list2)-1):
        if i == list2[j]:
            list12_dup.append(list2[j])

for i in list2:
    for j in range(0,len(list3)-1):
        if i == list3[j]:
            list23_dup.append(list3[j])


for i in list1:
    for j in range(0,len(list3)-1):
        if i == list3[j]:
            list13_dup.append(list3[j])


all_list=list12_dup + list23_dup + list13_dup
all_list.sort()
print(all_list)