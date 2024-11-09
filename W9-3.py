#成績輸入並儲存(以函式完成)

def input_grades():
    grades=[]
    while True:
        n=int(input('請輸入成績 (輸入負數以結束): '))
        if n<=-1:
            break
        elif n >=101:
            print('成績應是0-100之間的整數')    
        else:
            grades.append(n)
            
    return grades

print('輸入的成績: ',input_grades())