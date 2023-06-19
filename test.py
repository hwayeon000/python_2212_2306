print("py check")


# N = int(input())
# N_list = list(map(int, input().split(" ")))

# h, m = map(int, input().split())
# time = int(input())
# if time>60:
#     h+=time//60
#     m+=time%60
# else:
#     m+=time
# if m>=60:
#     h+=m//60
#     m%=60
# if h>=24:
#     h%=24
# print(h, m)

# a,b,c=sorted(map(int,input().split()))
# print([c,b+10,b*10+100][[a,b,c].count(b)-1]*100)


# i=0
# for a,_,c,_ in[*open(0)][1:]:i+=1;print(f'Case #{i}:',a,'+',c,'=',int(a)+int(c))

# n=int(input())
# for i in range(1,n+1):
#     print(' '*(n-i), end="")
#     print('*'*i)

import sys
list=[]
res=[]
index=[1 for i in range(1,6)]
for i in range(3):
    m=int(sys.stdin.readline())
    list.append(m)
list.sort()
t_dict = dict(zip(list, index))
print(t_dict)