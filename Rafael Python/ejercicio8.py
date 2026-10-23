nombre = input("Cual es tu nombre")
edad = int(input("Tu edad"))
prom1 = float(input("nota 1:"))
prom2 = float(input("nota 2:"))
prom3 = float(input("nota 3:"))
nota = prom1+prom2+prom3
total = nota/3
if total >= 71:
    print("hola" + nombre + "de" + edad + "años tiene una nota de " + total+ "estas aprobado")
else:
    print("hola" + nombre + "de" + edad + "años tiene una nota de " + total+ "estas reprobado")
