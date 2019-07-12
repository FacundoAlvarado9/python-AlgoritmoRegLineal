from numpy import *

#Calculo del error de los intentos
def calculo_de_error(b, m, puntos):
    errorTotal = 0
    for i in range(1, len(puntos)):
        x = puntos[i, 0]
        y = puntos[i, 1]
        #Error total = error total + la diferencia entre el punto y el aproximado
        errorTotal += (y - (m * x + b)) ** 2
    return errorTotal / float(len(puntos))

#Devuelve valores de b y m 
def paso_gradiente(b_actual, m_actual, puntos, learning_rate):
    gradiente_b = 0
    gradiente_m = 0
    N = float(len(puntos))
    for i in range (1, len(puntos)):
        x = puntos[i, 0]
        y = puntos[i, 1]
        gradiente_b += -(2/N) * (y - ((m_actual * x) + b_actual))
        gradiente_m += -(2/N) * x * (y - ((m_actual * x) + b_actual))
    nuevo_b = b_actual - (learning_rate * gradiente_b)
    nuevo_m = m_actual - (learning_rate * gradiente_m)
    return [nuevo_b, nuevo_m]

#Maneja las iteraciones
def iterador_gradiente(b_inicial, m_inicial, puntos, learning_rate, iteraciones):
    b = b_inicial
    m = m_inicial
    for i in range (num_iteraciones):
        b, m = paso_gradiente(b, m, array(puntos), velocidad_apren)
    return [b,m]


puntos = genfromtxt("data.csv", delimiter=",")
velocidad_apren = 0.0001
b_inicial = 0
m_inicial = 0 
num_iteraciones = 1000
print("Empezando descenso de gradiente con b = {0}, m = {1},  y un error igual a  {2}".format(b_inicial, m_inicial, calculo_de_error(b_inicial, m_inicial, puntos)))
print("Calculando... *beep boop bap bip*")
[b, m] = iterador_gradiente(b_inicial, m_inicial, puntos, velocidad_apren, num_iteraciones)
print("Después de {0} iteraciones, se llegó al resultado: b = {1}, m = {2}, error = {3}".format(num_iteraciones, b, m, calculo_de_error(b,m,puntos)))
