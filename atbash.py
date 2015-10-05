#Escrito originalmente por Pedro Jesús González Vargas 
def contar(cad):
    abc = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    o=list(abc)
    o.reverse()
    b={}
    for i in range(len(abc)):
        b[str(abc[i])]=i
    for i in cad:
        print o[int(b[i])]
contar("KVWIL")
    
    
 

