#影片推薦(以函式完成)
def the_movie():
    n = int(input("輸入影片總數: "))
    movies_data = []
    for i in range(n):
        movie = input("輸入影片數據: ")
        data = movie.split()
        name = data[0]
        p = int(data[1])
        t = int(data[2])
        l = int(data[3])
        r = int(data[4])
        f=p*t*l*r
        movies_data.append((-f,name))
        
    movies_data.sort()
    
    for f,name in movies_data:
        print(name)
the_movie()
