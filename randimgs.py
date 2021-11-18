filename="D:\\常用软件\\阿里云盘\\webp随机图\\randimgs.txt"
randimgs=open(filename,"a")
for numbers in range(1,169):
    randimgs.write("https://cdn.jsdelivr.net/gh/TonaSmith/picture/img/"+str(numbers)+".webp\n")
randimgs.close()
