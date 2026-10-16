print("Hello, \nWorld!")
print("Tere tulemast\t!")
print("Õpin",1,".kursusel") #sep=" " vaikimisi on tühik


#paremetrid sep ja end
print() #see on tühi rida
print("Õpin",1,".kursusel",sep="***") #sep="" tähendab,et tühikut ei ole
print("2026", "10", "01", sep="-")
print("Sama ", end="") #end="" tähendab, et reavahetust ei ole end="\n"
print("rida")


#muutujad
nimi = "Python" #str ehk sõne
print("Tere,", nimi)
kursus=1
print("Õpin",kursus,".kursusel")

# input() funktsioon
nimi = input("Siseta oma nimi: ") #programm küsib ja ootab kasutaja sisestust või vastust
print("Tere,", nimi)
kursus= int(input("Sisesta kursuse number: ")) #teisendab sõne arvuks
print("Õpin",kursus,".kursusel")
print("jargmisel aastal õpin ",kursus+1,".kursusel") #kursus +1 tähendab, et kursuse number suureneb 1 võrra
print(kursus,"+",kursus,"=",kursus + kursus)

print("liitmine")
a =float( input("Esimene arv: "))
b =float( input("Teine arv: "))
print(a,"+",b,"=",a + b)

print("lahutamine")
a =float( input("Esimene arv: "))
b =float( input("Teine arv: "))
print(a,"-",b,"=",a - b)

print("jagamisjääk")
a =float( input("Esimene arv: "))
b =float( input("Teine arv: "))
print(a,"%",b,"=",a % b)

print("jagamise täisarvuline osa")
a =float( input("Esimene arv: "))
b =float( input("Teine arv: "))
print(a,"//",b,"=",a // b)

print("jagamine")
a =float( input("Esimene arv: "))
b =float( input("Teine arv: "))
print(a,"/",b,"=",a / b)
print("Ümardatud arv:", round(a / b,2))

print("korrutamine")
a =float( input("Esimene arv: "))
b =float( input("Teine arv: "))
print(a,"*",b,"=",a * b)

print("astendamine")
a =float( input("Esimene arv: "))
b =float( input("Teine arv: "))
print(a,"**",b,"=",a ** b)

nimi = "Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")

a=float(input("esimine arv: "))
tehe=input("Tehe: ")
b=float(input("Teine arv: "))
print(f"{a} {tehe} {b} = {eval(f'{a} {tehe} {b}')}")
