##Быстрая сортировка
def qsort(lst):
    if len(lst)<=0 :
        return lst
    else:
        l=[]
        r=[]
        e_nums = []
        mid=len(lst)//2
        for i in lst:
            if i>lst[mid]:
                l.append(i)
            elif i<lst[mid]:
                r.append(i)
            else:
                e_nums.append(i)
        return  qsort(r)+e_nums+qsort(l)

##Перестановки в отсортированном массиве

import itertools ## Простой способ с itertools
val = [1,2,3]
perm_set = itertools.permutations(val)
for i in perm_set:
    print(i)

    
def string_permutations(s, i, n):
    if i==n:
        print(s)
    else:
        for j in range(i,n):
            s[i], s[j] = s[j], s[i]
            string_permutations(s, i+1, n) 
