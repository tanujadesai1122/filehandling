File=open("mast.txt","r")
data=File.read()
print("data is:",data)
File.close()

#write code open a file named mydate.txt in read mode
File=open("mydate.txt","r")
data=File.read()
print("data is:",data)
File.close()

#practice que=2
File=open("certificate.txt","r")
dataOfile=File.read()
dataOfile=dataOfile.lower()
if  "live" in dataOfile:
    print("the live is present")
else:
    print("no")
File.close()

