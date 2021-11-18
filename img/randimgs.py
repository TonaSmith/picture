filename="D:\\常用软件\\阿里云盘\\webp\\randimgs.txt"
randimgs=open(filename,"n")
for numbers in range(1,169):
    randimgs.write("https://cdn.jsdelivr.net/gh/TonaSmith/picture/img/"+str(numbers)+".webp\n")
randimgs.close()
