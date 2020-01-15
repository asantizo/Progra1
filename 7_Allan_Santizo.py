#!/usr/bin/env python
# coding: utf-8

# ## Clase `Dice`
# 
# Implementar una clase denominada `Dice`, que funcione como un conjunto de $n$ dados. La clase debe recibir como argumento el número de dados a tirar. Además, la clase debe implementar:
# 
# - Un método de `roll()` que simula la tirada de los $n$ dados y guarda internamente una lista con los valores resultantes. No devuelve nada.
#     
#     - Si no se ha llamado a `roll()`, la lista interna debe ser vacía.
# 
# - Un método `getLastRoll()` que devuelve la lista con los valores de la última tirada.
# 
# - Un método `getRollSum()` que devuelve la suma de los valores de la última tirada.
# 
#     - Si no se ha llamado a `roll()`, debe devolver cero.

# In[1]:


# Ayuda, utilizar la siguiente función del módulo random
import random
random.randint(1,6)


# In[2]:


class Dice:
    
    def __init__(self,n):
        self.n = n
        self.lanzamientos = []
        #pass
    
    
    def roll(self):
        self.lanzamientos=[]
        for i in range(self.n):
            cara=random.randint(1,6)
            self.lanzamientos.append(cara)
        return #OJO
        
        #pass
    
    def getLastRoll(self):
        return self.lanzamientos
    
        #pass
    
    def getRollSum(self):
        sum(self.lanzamientos)
        return sum(self.lanzamientos)
        
        #pass
    


# In[3]:


a = Dice(2)
a.getLastRoll()
# Devuelve lista vacía


# In[4]:


a.getRollSum()
# Devuelve 0


# In[5]:


a.roll()
a.getLastRoll()
# Devuelve lista con dos números


# In[6]:


a.getRollSum()
# Devuelve la suma de los números de la lista anterior


# ## Herencia de la clase `Rectangle`

# In[7]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return (2*self.length) + (2*self.width)
    
class Square(Rectangle):
    '''
        Redefinir el método constructor, sin redefinir las funciones de área
        y perímetro, para que un objeto de tipo Square con:
            .area() devuelva el área de un cuadrado de tamaño length y
            .perimeter() devuelva el perímetro del cuadrado
    '''
    def __init__(self, length):
        
        self.length=length
        self.width=self.length
        
                
class Cube(Square):
    '''
        Heredar de Square todos los métodos (incluido el constructor) y 
        agregar un método para obtener el volumen de un objeto de tipo Cube.
    '''
    
    def volume(self):
        volumen= self.area()*self.width
        return volumen
        


# Nota: instancie algunos objetos y muestre que sus métodos funcionan correctamente.

# In[8]:


a=Rectangle(2,4)
print(a)
a.area()


# ## Programando nuestro propio *Blockchain*
# 
# Crear una clase denominada `Block` que almacene un diccionario con transacciones. La clase `Block` debe implementar:
# 
# - Atributo de transacciones, representado con un diccionario `transactions`. Las llaves pueden ser alfanuméricas y los valores del diccionario representan los débitos ($-$) o créditos ($+$) relativas a una transacción.
# 
# - Atributos `previousBlock` y `nextBlock` que apuntan a objetos tipo `Block` para referir al anterior y siguiente "bloque" en la cadena.
#     - Estos deben ser `None` por defecto en el constructor.
#     - Se deben programar métodos *getter* y *setter* para acceder y modificar estos atributos.
#     
# - Un método `getBlockID()` para obtener el ID de un bloque específico utilizando **variables de clase**.
# 
# - Un método `getTransactions()` para obtener **una copia** del diccionario de transacciones.
# 
# - La asignación consiste en completar el método `getBalanceFromHere()`, que computa el balance de las cuentas desde el bloque actual hasta el final del *blockchain*.

# In[9]:


class Block(object):
    
    blockCount = 0
    
    # Inicializa el bloque con el diccionario de transacciones 
    def __init__(self, transactions={}, previousBlock=None, nextBlock=None):
        self.transactions = transactions
        self.previousBlock = None
        self.nextBlock = None
        self.blockID = Block.blockCount
        Block.blockCount += 1
        
    # Muestra el número de instancia y sus transacciones
    def __str__(self):
        return "Block %d: " % self.blockID + str(self.transactions)
        
    # Obtener el ID del bloque
    def getBlockID(self):
        return self.blockID
    def getTransactions(self):
        return self.transactions.copy()
    
    # Getters y setters para obtener bloque anterior y siguiente
    def setPreviousBlock(self, block):
        self.previousBlock = block
    def getPreviousBlock(self):
        return self.previousBlock
    def setNextBlock(self, block):
        self.nextBlock = block
        block.setPreviousBlock(self)
    def getNextBlock(self):
        return self.nextBlock
    
    ''' Completar para computar la función de 
        balance a partir de este bloque. Devuelve un 
        diccionario con las llaves y su balance acumulado
        a partir de este bloque (incluyendo las transacciones
        de este bloque).
    '''
    def getBalanceFromHere(self):  
        
        if self.blockID==0:#si es el bloque cero que traiga los saldos iniciales
            saldoinicial={'A':40,'B':0,'C':20}#Saldo inicial
            return saldoinicial 
        
        else: 
            
            almacena = {}
            inicial = self.getPreviousBlock().getBalanceFromHere()
            final = self.getPreviousBlock().getTransactions()
            for i in inicial:
                almacena[i]=inicial[i]
                
                if i in final:
                    almacena[i]=inicial[i]-final[i]
            return almacena


# In[10]:


dic2={"a":0,"b":10,"c":5}
dic1={"a":-10,"b":0,"c":10}
dic={"a":50,"b":-10,"c":5}


# In[11]:


for i in dic:
    print((dic[i]+dic1[i]+dic2[i]))


# In[12]:


# Creamos algunos bloques con transacciones
B0 = Block({'A': 50, 'B': -10, 'C': 5})
B1 = Block({'A':-10, 'C':+10})
B2 = Block({'B':+10, 'C':+5})
print(B0, B1, B2, sep='\n')


# In[13]:


# Configuramos la cadena de bloques
B0.setNextBlock(B1)
B1.setNextBlock(B2)


# In[14]:


print(B0.getNextBlock())
print(B1.getNextBlock())


# In[15]:


print(B1.getPreviousBlock())
print(B2.getPreviousBlock())


# In[16]:


print(B0.getPreviousBlock())
# Devuelve None


# In[17]:


print(B2.getNextBlock())
# Devuelve None


# In[18]:


B1.getBalanceFromHere()
# Debe devolver {'A': -10, 'C': 15, 'B': 10}


# In[19]:


B0.getBalanceFromHere()
# Debe devolver {'A': 40, 'B': 0, 'C': 20}

