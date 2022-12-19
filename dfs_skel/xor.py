skeletorstring= "skeletor"
array=[8,9,10,11,12,13,14,15,]
a=""
for i in skeletorstring:
    a= a+(i ^ array[index])
    index= index +1
    
print(a)