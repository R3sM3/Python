# Cambiar el valor de 2 variables sin usar una variable temporal

# Metodo mas usado en Python 

a=5
b=10

print ("El valor inicial de a es: ", a)
print ("El valor inicial de b es: ", b)

a,b=b,a

print ("El valor final de a es: ", a)
print ("El valor final de b es: ", b)

# Otra forma mediante Sumas

a=5
b=10

print ("El valor inicial de a es: ", a)
print ("El valor inicial de b es: ", b)

a = a + b
b = a - b
a = a - b

print ("El valor final de a es: ", a)
print ("El valor final de b es: ", b)


