path="file pelanggan.riyo"
a1=open(path,"w")
a1.write("uji tes file pelanggan")
a1.close()

path="file pelanggan.riyo"
a1=open(path,"r")
a2=a1.read()
a1.close()
print(a2)

path="file pelanggan.riyo"
a1=open(path,"a")
a1.write("uji tes file pelanggan")
a1.close()