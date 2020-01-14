#!/usr/bin/env python
# coding: utf-8

# # Tarea #6
# **Programacion I**
# 
# $Allan$ $Santizo$

# ## Ejercicio 1
# 
# Ejecute el siguiente programa y explique su procedimiento y el porqué del resultado. 

# In[ ]:


def Recusion(f):
    f(f)
    
Recusion(Recusion)


# *La función recursión se llama recurre a ella misma y repite el proceso idefinidamente, no existe un caso base.
# El caso base debe reducir el problema en varias tareas, se debe obtener uno suficientemente pequeño.*
# 

# ## Ejercicio 2
# 
# Vea el siguiente vídeo: <https://www.youtube.com/watch?v=qxRW5pDT2o4>  
# 
# Complete el código siguiente para encontrar el máximo común divisor dado dos números enteros. 
# 
# Las condiciones básicas, son:

# Para dos números $a$ y $b$, tal que $b\leq a$:
# * $mcd(a,0) = a$
# * Si $b\vert a$ (divida enteramente), entonces $mcd(a,b)=b$
# * En otro caso, $mcd(a,b) = mcd(b,a \,mod \, b)$
# 
# 

# In[12]:


#Función que define algoritmo de Euclides
def mcd(a,b):
    '''Donde a >= b'''
    if (a or b) ==0: #Caso base
        return b
    elif (a % b)==0: #Caso
        return b        
    else:
        return mcd(b,a%b) 
    
print("MCD: ",mcd(225,300))


# ## Ejercicio 3
# 
# Implemente un algoritmo recursivo para obtener la parte entera de la división entre dos números enteros. (Pista: Asocie con la resta).

# In[16]:


#Logaritmo recursivo parte entera de la división

def divEntera(a,b):
    
    if (a-b) ==0: #Caso base 
        return 1
    elif (a-b)<b: #resta menor a b
        return 1        
    else:
        return 1+DivEntera(a-b,b)  #Resto de casos

print("Parte entera de la divisón: ",divEntera(2,10))   


# # Ejercicio 4
# 
# En el ejemplo de clase (Coordinate), modifique el método constructor para que verifique que los argumentos $x$ y $y$ sean flotantes.  

# In[19]:


class coordenada(object):
    #Atributos(datos,funciones)
    
    #Método constructor
    
    def __init__(self,x,y):
        assert type(x) == float and type(y) == float, "Debe ingresar numeros con decimales"
        #¿Cómo queremos inicializar el objeto?
        self.x = x
        self.y = y
        
verif = coordenada(-1,1.0)
print(verif)


# # Ejercicio 5
# 
# 1. Cree una clase llamada ``Persona``, que asigne una cadena a la propiedad ``nombre`` y un número entero a la propiedad ``edad``. Al imprimir el objeto, debe concatenar tanto el nombre con la edad. 
# 2. A la clase anterior, añada un método para sumar dos objetos de tipo ``Persona``. El resultado debe ser ambos nombres concatenados y la suma de ambas edades.
# 3. Modifique la clase para que el objeto tenga otra propiedad llamada ``altura``. Cuando se solicite la longitud del objeto, muestre la altura. También debe modificar el método de impresión para que muestre la altura. ¿Qué pasa con el método de suma?
# 
# 

# In[29]:


#Se define la clase persona con los argumentos nombre,edad, altura

class persona(object):
    
    def __init__(self,nombre,edad,altura):#define los argumentos de la clase
        self.nombre= str(nombre)
        self.edad=int(edad)
        self.altura=int(altura)
    
    def __str__(self):#devuelve la cadena
        return "Nombres: " +self.nombre+ "Edad :" + str(self.edad) + " Altura : " + str(self.altura)
    
    def __add__(self,other):#considera el resto de casos
        sumaNombre= self.nombre + other.nombre
        sumaEdad=self.edad+other.edad
        sumaAltura=self.altura+other.altura
        return persona(sumaNombre,sumaEdad,sumaAltura)
    
    def __len__(self):#considera el tamaño de la altura
        return self.altura
    
salida= persona("Allan ",29,2)
salida2=persona("Elmer ",29,2)
salida3=persona("Mariela ",29,2)
salida4=persona("Erwin ",32,1)
suma3=salida+salida2+salida3+salida4
print(suma3)


# # Canasta

# In[31]:


#Define la clase canasta para hacer comparaciones

class canasta(object):
    def __init__(self,cerveza,ocio,cevichongo):#se definen los argumentos
        self.cerveza = cerveza
        self.ocio = ocio
        self.cevichongo = cevichongo
        
    def __eq__(self,other):#función para comparar si son iguales las canastas
        canasta3=(self.cerveza**0.3)*(self.ocio**0.6)*(self.cevichongo**0.1)
        canasta4=(other.cerveza**0.3)*(other.ocio**0.6)*(other.cevichongo**0.1)
        return canasta3==canasta4
        
    def __lt__(self,other):#función que compara si es mayor o menor
        canasta1=(self.cerveza**0.3)*(self.ocio**0.6)*(self.cevichongo**0.1)
        canasta2=(other.cerveza**0.3)*(other.ocio**0.6)*(other.cevichongo**0.1)
        return canasta1<canasta2
    

salida=canasta(1,5,10)
salida1=canasta(1,5,10)
salida==salida1


# # Codificador

# In[76]:


#Crea clase que contiene funciones para encriptar y desincriptar

class enigma(object):
    
    #función que define el texto
    def __init__(self,texto):
        self.texto=str(texto)
        
    #Función para cada elemento de la cadena hace la conversión y se añade a la cadena de texto    
    def codificar(self):
        codigoEnigma=""
        for i in range(len(self.texto)):
            codigoEnigma += chr(ord(self.texto[i])+3)
        return codigoEnigma
        
    #Función para cada elemento de la cadena hace la desconversión y se añade a la cadena de texto    
    def decodificar(self):
        codigoDeco=""
        for i in range(len(self.texto)):
            codigoDnigma += chr(ord(self.texto[i])-3)
        return codigoDeco


# In[79]:


posicionEnemigo = enigma('abc')
posicionEnemigo.codificar()

