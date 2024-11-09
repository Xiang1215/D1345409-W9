#3n+1問題(Collatz猜想)(以函式完成)

def collatz():
    time=0
    while True:
        n=int(input('請輸入一個正整數: '))
        print(round(n),end=' -> ') 
        if n==1:
            print()
            exit()
        while n!=1:
            if n/2==1 or 3*n+1==1:
                print('1')
                time+=1
                break
            elif n % 2 ==0:
                n/=2 
                time+=1 
                print(round(n),end=' -> ') 
            else :
                n=3*n+1
                time+=1 
                print(round(n),end=' -> ')    
            
        return time

print('總共步數: ', collatz())