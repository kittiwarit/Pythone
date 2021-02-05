print('ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่ออกจากโปรเเกรม')
foodlist = []
n = 0
while(True) :
    n = n + 1
    print('อาหารโปรดลำดับที่',n,end= '')
    choose = input('คือ\t')
    foodlist.append(choose)
    if choose == 'exit' :
        break
print('รายการอาหารสุดโปรดของคุณ มีดังนี้',end= '')    
for x in range(1,n) :
    print(x,'',foodlist[x-1],end= '')