input_file="C:/Users/Somesh/Desktop/Somesh_Details.csv"
output="C:/Users/Somesh/Desktop/Somesh_Details.txt"
ifh=open(input_file,'r')
ofh=open(output,'w')
res=ifh.readlines()
print(res)
for i in res:
    print(i)
