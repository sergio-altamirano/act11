print("actividad 11 examen")
print("sergio damian altamirano mat:22308051281041")

class provedores1041:
    id_provedores=0
    cantidad=0
    direccion= "no"
    numero=0
    precio=0
    producto=" "
    nombre=" "

    #funciones dentro de la clase
    def mostrar_datos(self):
        print(f" id del provedor: {produc.id_provedores} \ncantidad: {produc.cantidad} \ndireccion: {produc.direccion} \nnumero: {produc.numero} \nprecio: {produc.precio} \nproducto: {produc.producto} \nnombre: {produc.nombre}")

#lista
    def lista_provedores(self):
        provedores=["1234", "300", "calle tornillo 260", "656 2140443", "4,500", "tortillas"]
        print(provedores)
        for x in provedores:
            print(x)
    print("------------------------------------------------------------------------------------")

#tupla
    def tupla_provedores(self):
        provedor=("1234", "300", "calle tornillo 260","6562140443", "4,500", "tortillas" )
        print(provedor)
        for x in provedor:
            print(x)
    print("------------------------------------------------------------------------------------")
#diccionario
    def diccionario_provedores(self):
            diccionario_elprovedor={
                "id: ": 1234,
                "cantidad: " : 300,
                "direccion" : "callle tornillo ",
                "numero" : "656 214 0443 ",
                "precio" : " 4,500",
                "producto" : "tortillas ",
                "nombre" : " loa nonos",
            }
            print(diccionario_elprovedor)
            for x,y in diccionario_elprovedor.items():
                print(x,y)
    def alta(self):
        print("\n el producto esta dado de alta correctamente")
    def baja(self):
        print("\n el producto esta dado de baja correctamente")
    print("------------------------------------------------------------------------------------")
#objetos
produc=provedores1041()
produc.id_provedores=1234
produc.cantidad=300
produc.direccion="calle tornillo 260"
produc.numero= 6562140443
produc.precio= 4,500
produc.producto="tortillas"
produc.nombre="sergio"
print("------------------------------------------------------------------------------------")
#llamado de funciones
produc.mostrar_datos()
produc.lista_provedores()
produc.tupla_provedores()
produc.diccionario_provedores()
produc.alta()
produc.baja()