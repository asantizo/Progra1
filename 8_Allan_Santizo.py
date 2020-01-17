#!/usr/bin/env python
# coding: utf-8

# # Tarea día 8
# **Programación I**
# 
# $Allan$ $Santizo$

# In[1]:


#Importa modulo numpy
import numpy as np


# ## Ejercicio 1
# 
# Cree una matriz que contenga ceros. Rellene la mitad de ellos aleatoriamente con unos.

# In[2]:


#Elementos de la matriz y cantidad de elementos
filas=1000
columnas=1000
elementos=filas*columnas
mitad=int(round(elementos/2))

#Matriz de unos
unos=np.random.randint(1,2, elementos-mitad) 
#Matriz de ceros
ceros=np.random.choice(1,(mitad))
#Matriz de ceros y unos
conjunto=np.concatenate((unos,ceros))
#Matriz conjunto con unos en posiciones aleatorias
np.random.shuffle(conjunto)
#Matriz conjunto de la forma filas y columnas
conjunto.reshape(filas,columnas)


# ## Ejercicio 2
# Cree dos matrices de dimensiones $(5,2)$. La primera rellena de ceros y la siguiente de unos. 
# 1.	Convierta las matrices en vectores columna. 
# 2.	Apile ambos vectores a lo largo de una tercera dimensión. 
# 3.	Con las matrices originales, conviértalas en vectores fila y concaténelos verticalmente. 
# 

# In[3]:


#Matriz de unos y ceros
d= np.zeros([5,2])
e= np.ones([5,2])


# In[4]:


#Matriz de ceros en vector columna
r=d.reshape(10,1)
print(r)


# In[5]:


#Matriz de unos en vector de columna
s=e.reshape(10,1)
print(s)


# In[6]:


#Vector de unbos y ceros en tercera dimensión
t=np.concatenate((r,s))
c=t[:,None]
print(c)


# In[7]:


#Vector fila
m=d.reshape(1,10)
n=e.reshape(1,10)
#Concatenar verticalmente
g=np.vstack((m,n))
print(g)


# ## Ejercicio 3
# 
# Dada la función $f(x,y,z) = 2x +3y + z^2$
# 1.	Genere una matriz con números aleatorios, donde cada columna sea una variable. 
# 2.	Evalúe la matriz anterior en la función. El resultado debe ser una vector columna. 

# In[8]:


#Se define la función
def f(x,y,z):
    return 2*x + 3*y + z**2


# In[9]:


#Se genera matriz de aleatorios por columna
x=np.random.randint(1,10,(3,1))
y=np.random.randint(1,10,(3,1))
z=np.random.randint(1,10,(3,1))
m=np.hstack((x,y,z))
print(m)


# In[10]:


f(x,y,z)#evalua cada elemento


# ## Ejercicio 4
# 
# Suponga que dentro de un cuadrado de lado 50 cm, hay un cuadrado de 20cm. Ambos cuadrados comparten centro. Estime el área del cuadrado interno por método Monte Carlo. [Consulte Aquí]( http://mathonweb.com/entrtain/monte/t_monte.htm)

# In[11]:


#Elementos de la matriz y cantidad de elementos
filas=50
columnas=50
elementos=filas*columnas
mitad=int(round(elementos/2))
#Matriz de unos
unos=np.random.randint(1,2, elementos-mitad) 
#Matriz de ceros
ceros=np.random.choice(1,(mitad))
#Matriz de ceros y unos
conjunto=np.concatenate((unos,ceros))
#Matriz conjunto con unos en posiciones aleatorias
np.random.shuffle(conjunto)
#Matriz conjunto de la forma filas y columnas
conjunto.reshape(filas,columnas)
#Genera cuadrado
cuadrado=conjunto.reshape(filas,columnas)
#Crea cuadrado pequeño
mini=cuadrado[0:20,0:20].reshape(20,20)
#suma de unos de cada cuadrado
sumac=(sum(sum(cuadrado)))
sumam=(sum(sum(mini)))
#Calculo de areas
area=(filas*columnas)*(sumam/sumac)
print("El área del cuadrado interno es: ",area)


# ## Ejercicio 5
# 
# ### *Tarea*
# 
# 1. De las siguientes secciones, escoger 73 funciones de NumPy y mostrar su utilización en un ejemplo.
# 
#     - [Array creation routines](https://numpy.org/devdocs/reference/routines.array-creation.html)
# 
#     - [Array manipulation routines](https://numpy.org/devdocs/reference/routines.array-manipulation.html)
# 
#     - [Binary operations](https://numpy.org/devdocs/reference/routines.bitwise.html)
# 
#     - [String operations](https://numpy.org/devdocs/reference/routines.char.html)

# ## 1. numpy.linspace
# Return evenly spaced numbers over a specified interval.

# In[12]:


a=np.linspace(10, 20, 5)
print(a)


# ## 2. numpy.arange
# Return evenly spaced values within a given interval.

# In[13]:


np.arange(5,30,5)


# ## 3. numpy.diag
# Extract a diagonal or construct a diagonal array.

# In[14]:


matriz=np.arange(1,26).reshape((5,5))
print(matriz)
np.diag(matriz)


# ## 4. numpy.diagflat
# Create a two-dimensional array with the flattened input as a diagonal.

# In[15]:


np.diagflat([[1,2], [3,4],[3,10]])


# ## 5. numpy.tri
# An array with ones at and below the given diagonal and zeros elsewhere.

# In[16]:


np.tri(4, 4, 0, dtype=float)


# ## 6. numpy.asmatrix
# Interpret the input as a matrix.
# 

# In[17]:


a = np.array([[1, 2], [3, 4]])
b = np.asmatrix(a)
a[0,0] = 10
b


# ## 7. numpy.bmat
# Build a matrix object from a string, nested sequence, or array.

# In[18]:


a = np.mat('1 1; 1 1')
b = np.mat('2 2; 2 2')
c = np.mat('3 3; 3 3')
d = np.mat('4 4; 5 5')


# In[19]:


np.bmat([[a,b],[c,d]])


# ## 8. numpy.array
# Create an array.

# In[20]:


hh=np.array([[100,99,98.0],[97,96,0]],dtype=int)
hh


# ## 9. numpy.asarray
# Convert the input to an array.

# In[21]:


a = [1,2,5,6,7,8,9,11]
np.asarray(a)


# ## 10. numpy.copy
# Return an array copy of the given object.

# In[22]:


x = np.array([100, 95, 98])
y=np.copy(x)


# ## 11. numpy.full
# Return a new array of given shape and type, filled with fill_value.

# In[23]:


np.full((5,5),(1))


# ## 12. numpy.full_like
# Return a full array with the same shape and type as a given array.

# In[24]:


x= np.arange(10,dtype=int)
np.full_like(x,10)


# ## 13. numpy.identity
# Return the identity array.

# In[25]:


np.identity(5)


# ## 14. numpy.eye
# Return a 2-D array with ones on the diagonal and zeros elsewhere.

# In[26]:


np.eye(3,k=-1,dtype=int)


# ## 15. numpy.ones
# Return a new array of given shape and type, filled with ones.

# In[27]:


a=(3,2)
np.ones(a)


# ## 16. numpy.zeros
# Return a new array of given shape and type, filled with zeros.

# In[28]:


np.zeros((100),dtype=int)


# ## 17. numpy.copyto
# Copies values from one array to another, broadcasting as necessary.

# In[29]:


a= np.array((10,11,12)) 
b=[20,30,40]
np.copyto(a,b)
a


# ## 18. numpy.shape
# Return the shape of an array.

# In[30]:


np.shape(np.eye(3,k=-1,dtype=type))


# ## 19. numpy.reshape
# Gives a new shape to an array without changing its data.

# In[31]:


a = np.array([[100,100,100,2],[1050,80,150,2]])
np.reshape(a,8)


# In[32]:


b= np.arange(50).reshape(1,50)
b


# ## 20. numpy.ndarray.flat
# attribute

# In[33]:


a = np.arange(1,26).reshape(5,5)
print(a)
print(a.flat[-1])


# ## 21. numpy.moveaxis
# Move axes of an array to new positions.

# In[34]:


x=np.zeros((15,20,25))
np.moveaxis(x,0,-1).shape


# ## 22. numpy.rollaxis
# Roll the specified axis backwards, until it lies in a given position.

# In[35]:


a = np.ones((3,1,3,3))
a
np.rollaxis(a,1,1).shape


# ## 23. numpy.swapaxes
# Interchange two axes of an array.

# In[36]:


a = np.array([[9,8,7]])
np.swapaxes(a,0,1)


# ## 24. numpy.ndarray.T
# attribute

# In[37]:


a = np.array([[10,11],[12,14]])
print(x)
a.T


# ## 25. numpy.transpose
# Reverse or permute the axes of an array; returns the modified array.

# In[38]:


a = np.arange(1,10).reshape((3,3))
print(a)
np.transpose(a)


# ## 26. numpy.expand_dims
# Expand the shape of an array.

# In[39]:


a = np.array([1, 2])
a.shape
b = np.expand_dims(x, axis=0)
print(a.ndim)
print(b.ndim)


# ## 27. numpy.squeeze
# Remove single-dimensional entries from the shape of an array.
# 
# 

# In[40]:


a= np.array([[[100],[99],[98]]])
np.squeeze(a)


# ## 28. numpy.asfarray
# Return an array converted to a float type.
# 
# 

# In[41]:


a=np.asfarray([2, 3])
a


# ## 29. numpy.asarray_chkfinite
# Convert a list into an array. 
# If all elements are finite asarray_chkfinite is identical to asarray.

# In[42]:


a = [90,80,70]
np.asarray_chkfinite(a,dtype=float)


# ## 30. numpy.asscalar
# Convert an array of size 1 to its scalar equivalent.

# In[43]:


np.asscalar(np.array([10000000]))


# ## 31. numpy.concatenate
# Join a sequence of arrays along an existing axis.

# In[44]:


a = np.array([[25,50],[75,100]])
b = np.array([[125,150],[175,200]])
np.concatenate((a,b.T), axis=1)


# ## 32. numpy.stack
# Join a sequence of arrays along a new axis.

# In[45]:


a = np.array([125, 682, 743])
b = np.array([620, 543, 463])
np.stack((a, b))


# ## 33. numpy.hstack
# Stack arrays in sequence horizontally (column wise).

# In[46]:


a = np.array([125, 682, 743])
b = np.array([620, 543, 463])
np.hstack((a, b))


# ## 34. numpy.vstack
# Stack arrays in sequence vertically (row wise).

# In[47]:


a = np.array([125, 682, 743])
b = np.array([620, 543, 463])
np.vstack((a, b))


# ## 35. numpy.block
# Assemble an nd-array from nested lists of blocks.

# In[48]:


a=np.arange((5))
b=np.arange(5,11)
np.block([a,b])


# ## 36. numpy.split
# Split an array into multiple sub-arrays as views into ary.

# In[49]:


a = np.arange(50)
b= np.split(a, 10)
b


# ## 37. numpy.array_split
# Split an array into multiple sub-arrays.

# In[50]:


a = np.arange(50)
np.array_split(a,8)


# ## 38. numpy.dsplit
# Split array into multiple sub-arrays along the 3rd axis (depth).

# In[51]:


s=np.arange(24).reshape(3, 2, 4)
print(s)
r=np.dsplit(s,4)
print(r)


# ## 39. numpy.hsplit
# Split an array into multiple sub-arrays horizontally (column-wise).

# In[52]:


k=np.arange(9).reshape(3,3)
j=np.hsplit(k,3)
j


# ## 40. numpy.vsplit
# plit an array into multiple sub-arrays vertically (row-wise).

# In[53]:


k=np.arange(25).reshape(5,5)
j=np.vsplit(k,5)
j


# # 41. numpy.tile
# Construct an array by repeating A the number of times given by reps.

# In[54]:


g=np.array([1,2,3,4,5,6,7,8,9,10])
np.tile(g,3)


# ## 42. numpy.repeat
# Repeat elements of an array.

# In[55]:


np.repeat(1,100).reshape(10,10)


# ## 43. numpy.delete
# Return a new array with sub-arrays along an axis deleted. For a one dimensional array, this returns those entries not returned by arr[obj].

# In[56]:


a=(np.arange(12)+1).reshape(4,3)
np.delete(a,0,1)


# ## 44. numpy.insert
# Insert values along the given axis before the given indices.

# In[57]:


d=(np.arange(12)+1).reshape(4,3)
np.insert(a,0,[0,2,9])


# ## 45.  numpy.append
# Append values to the end of an array.

# In[58]:


a=np.arange(10)
b=np.arange(10)
np.append(a,b)


# ## 46. numpy.resize
# Return a new array with the specified shape.

# In[59]:


a=np.array([[1,1],[1,1]])
np.resize(a,(10,10))


# ## 47. numpy.trim_zeros
# Trim the leading and/or trailing zeros from a 1-D array or sequence.

# In[60]:


a = np.array((0,5,0,0,0,1,0,0,5,0))
np.trim_zeros(a)


# ## 48. numpy.unique
# Find the unique elements of an array.

# In[61]:


a=np.array([1,2,3,4,5,1,2,3,4,5,6,7,8])
a
np.unique(a)


# ## 49. numpy.flip
# Reverse the order of elements in an array along the given axis.

# In[62]:


a=np.array([1,2,3,4,5,1,2,3,4,5,6,7,8])
np.flip(a)


# ## 50. numpy.fliplr
# Flip array in the left/right direction.

# In[63]:


a=np.arange(1,10).reshape(3,3)
print(a)
np.fliplr(a)


# ## 51. numpy.flipud
# Flip array in the up/down direction.

# In[64]:


a=np.arange(1,10).reshape(3,3)
print(a)
np.flipud(a)


# ## 52. numpy.reshape
# Gives a new shape to an array without changing its data.

# In[65]:


a=np.array([1,2,3,4,5,6])
np.reshape(a,(3,-1))


# ## 53. numpy.roll
# Roll array elements along a given axis.

# In[66]:


a= np.arange(10)
np.roll(a,5)


# ## 54. numpy.rot90
# Rotate an array by 90 degrees in the plane specified by axes.

# In[67]:


a=np.array([1,2,3,4,5,6]).reshape(2,3)
a
np.rot90(a)


# ## 55. numpy.char.add
# Return element-wise string concatenation for two arrays of str or unicode.

# In[68]:


a=np.char.add("Hola ","mundo")
print(a)


# ## 56. numpy.char.multiply
# Return (a * i), that is string multiple concatenation, element-wise.

# In[69]:


np.char.multiply("BANGUAT ",3)


# ## 57. numpy.char.capitalize
# Return a copy of a with only the first character of each element capitalized.

# In[70]:


a=np.array(["a","b","c"])
np.char.capitalize(a)


# ## 58. numpy.char.center
# Return a copy of a with its elements centered in a string of length width.

# In[71]:


a=np.array(["BANGUAT"])
np.char.center(a,20,fillchar="_")


# ## 59. numpy.char.encode
# Calls str.encode element-wise.

# In[72]:


a=np.array(["BANGUAT"])
b=np.char.encode(a,"cp500")
b


# ## 60. numpy.char.decode
# Calls str.decode element-wise.

# In[73]:


np.char.decode(b,"cp500")


# ## 61. numpy.char.join
# Return a string which is the concatenation of the strings in the sequence seq.

# In[74]:


A=np.char.join('-','ALLAN')
print(A)


# ## 62. numpy.char.ljust
# Return an array with the elements of a left-justified in a string of length width.

# In[75]:


a=np.char.ljust('Allan',30,fillchar='!')
a


# ## 63 . numpy.char.lower
# Return an array with the elements converted to lowercase.

# In[76]:


a=np.array("ALLAN")
a
np.char.lower(a)


# ## 64. numpy.char.lstrip
# For each element in a, return a copy with the leading characters removed.

# In[77]:


a=np.array("ahSantizo")
a
np.char.lstrip(a,"ah")


# ## 65. numpy.char.partition
# Partition each element in a around sep.

# In[78]:


a="QUIERO TOMAR CERVEZA"
np.char.partition(a,"TOMAR")


# ## 66. numpy.char.replace
# For each element in a, return a copy of the string with all occurrences of substring old replaced by new.

# In[79]:


np.char.replace ('QUIERO TOMAR CERVEZA', 'TOMAR', 'MUCHA')


# ## 66. numpy.char.split
# For each element in a, return a list of the words in the string, using sep as the delimiter string.

# In[80]:


A=np.char.split ('HOLA K AZE')
print(A)


# ## 67. numpy.char.splitlines
# or each element in a, return a list of the lines in the element, breaking at line boundaries.

# In[81]:


a=np.char.splitlines('QUIERO\nUNA CERVEZA!')
print(a)


# ## 68. numpy.char.swapcase
# Return element-wise a copy of the string with uppercase characters converted to lowercase and vice versa.

# In[82]:


a="quiero tomar cerveza"
np.char.swapcase(a)


# ## 69. numpy.char.title
# Return element-wise title cased version of string or unicode.

# In[83]:


a="quiero tomar cerveza"
np.char.title(a)


# ## 70. numpy.char.upper
# Return an array with the elements converted to uppercase.

# In[84]:


a="quiero tomar cerveza"
np.char.upper(a)


# ## 71. numpy.char.zfill
# Return the numeric string left-filled with zeros

# In[85]:


a = np.char.zfill('Allan',20)
a


# ## 72. numpy.char.equal
# Return (x1 == x2) element-wise.

# In[86]:


a="quiero tomar cerveza"
b="quiero mucha cerveza"
np.char.equal(a,b)


# ## 73. numpy.char.count
# Returns an array with the number of non-overlapping occurrences of substring sub in the range [start, end].

# In[87]:


a="QUIERO TOMAR CERVEZA"
np.char.count(a,"E")


# 2. Crear un ejemplo de cómo guardar y cargar arreglos de un archivo binario `.npy` y `.npz`:
# 
#     - [NumPy binary files (NPY, NPZ)](https://numpy.org/devdocs/reference/routines.io.html#numpy-binary-files-npy-npz)
#     

# In[88]:


#Guarda archivo
a=np.array([1,2,3,4])
np.save('prueba',a)

#Carga el archivo
b=np.load('prueba.npy')
b


# 
# 3. Crear un ejemplo de cómo guardar y cargar arreglos de un archivo de texto `.txt`:
# 
#     - [NumPy Text files](https://numpy.org/devdocs/reference/routines.io.html#text-files)    

# In[89]:


#Se crea información a cargar
a=np.arange(0,10).reshape(2,5)
#Guarda archivo de texto
np.savetxt('prueba.txt',a, delimiter=",")
#Carga archivo de texto
np.loadtxt('prueba.txt',delimiter=",")


# 4. Crear una función llamada `estimacionMCO` que lea un archivo CSV con 7 columnas, que corresponden a las variables $(x_{1i}, \ldots, x_{6i})$ y $y_i$. 
#     - La función debe computar matricialmente los parámetros del modelo de regresión lineal: $y = X\beta$. 
#     - Estos parámetros deben ser devueltos como un arreglo de NumPy. 
# 
#     - Utilice la función de lectura de archivos de NumPy.

# In[90]:


def estimacionMCO():
    base=str(input("documento "))+".csv"
    data=np.genfromtxt(base,delimiter=',',skip_header=1)  
    b=data[: , :6]
    y=data[:,6:7]
    matrizb=(b.T)@b
    matrizy=((b.T)@y)
    salida=((np.linalg.inv(matrizb))@ matrizy)
    return salida


# In[91]:


estimacionMCO()

