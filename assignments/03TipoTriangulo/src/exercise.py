def main():
 #escribe tu código abajo de esta línea
 pass

 lado1 = int(input("Ingresa la medida del lado 1: "))
 lado2 = int(input("Ingresa la medida del lado 2: "))
 lado3 = int(input("Ingresa la medida del lado 3: "))

 if lado1 + lado2 < lado3 :
  print("NO ES TRIANGULO")
 elif lado1 + lado3 < lado2 :
  print("NO ES TRIANGULO")
 elif lado2 + lado3 < lado1 :
  print("NO ES TRIANGULO")
 elif lado1 == lado2 and lado2 == lado3:
  print("ES UN TRIANGULO EQUILATERO")
 elif (lado1 != lado2 and lado1 == lado3) or (lado1 != lado3 and lado1 == lado2) or (lado2 == lado3 and lado1 != lado3):
  print("ES UN TRIANGULO ISOSCELES")
 elif lado1 != lado2 and lado1 != lado3:
  print("ES UN TRIANGULO ESCALENO")
 



if __name__=='__main__':
      main()

  


