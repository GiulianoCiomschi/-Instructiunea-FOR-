n=eval(input("Dati numarul:"))
s1=0
s2=0
s3=0
p=1
s4=0
s5=0
s6=0
for i in range(1,n+1):
    s1+=i
print("suma1=",s1)
n=eval(input("Dati numarul:"))
for j in range(1,n+1):
    s2=s2+((j-1)*j)
print("suma2=",s2)
n=eval(input("Dati numarul:"))
for q in range(1,n+1):
    p=p*q
    s3=s3+p
print("suma3=",s3)
n=eval(input("Dati numarul:"))
for v in range(1,n+1):
    s4=s4+((v*10)+2)
print("suma4=",s4)
n=eval(input("Dati numarul:"))
for k in range(1,n+1):
    s5=s5+(k/(k+1))
print("suma5=",s5)
n=eval(input("Dati numarul:"))
for l in range(1,(n*2)+1):
    l=str(l)
    l=int("2"+l)
    s6=s6+l
print("suma6=",s6)
    