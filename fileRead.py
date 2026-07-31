#with keyword
'''File=open("report.txt","r")
data= File.read()
File.close()

with open("report.txt","r") as f:
    data=f.read()
    print(data)'''

#read line by line
with open("new.txt","r") as f:
    '''line1=f.readline()
    line2=f.readline()
    print(line1)
    print(line2)'''
    readlineMethod=f.readlines()
    print(readlineMethod)

#print how many lines are present in the file
print("lenth of:",len(readlineMethod))