import random
from prettytable import PrettyTable


detalleComprasTupla =([],[],[],[],[],[],[],[])

detalleCompras = list(detalleComprasTupla )

print(type(detalleCompras))


def menu():
  print("¿Que acción desea realizar?")
  print('*  1) Registrar pedidos')
  print('*  2) Mostrar pedidos')
  print('*  3) Eliminar pedido')
  print('*  4) Salir del sistema')
  return int(input("Ingrese la opción: "))


def registrarPedido():
  print("\n\t\t Ingresar los datos del cliente \n")
  nombre=input("Nombre: ")
  apellido=input("Apellido: ")
  telefono=input("Teléfono: ")
  print("\n\t\t Ingresar los datos de la policrush\n")
  nombrePolicrush=input("Nombre: ")
  lugarPolicrush=input("Dependencia: ")
  celularPolicrush=input("Teléfono: ")
  detalleCompras[0].append(nombre)
  detalleCompras[1].append(apellido)
  detalleCompras[2].append(telefono)
  detalleCompras[3].append(nombrePolicrush)
  detalleCompras[4].append(lugarPolicrush)
  detalleCompras[5].append(celularPolicrush)
  detalleCompras[6].append(random.randrange(1000, 9999))

  print("\n\t\t Selección del regalo \n")
  print("1) Opción 1: Poliflor + Polipeluche = $2.50")
  print("2) Opción 2: Poliflor + Policarta = $1.50")
  print("3) Opción 3: Poliflor + Polillavero = $2.00")
  print("4) Opción 4: Poliflor + Polivaso = $2.75")
  opcion= int(input("Ingrese la opción: "))
  if opcion==1:
    detalleCompras[7].append(2.50+(0.1*2.50))
  elif opcion==2:
    detalleCompras[7].append(1.50+(0.1*1.50))
  elif opcion==3:
    detalleCompras[7].append(2.00+(0.1*2.00))
  elif opcion==4:
    detalleCompras[7].append(2.75+(0.1*2.75))

  print("\n-------- Pedido registrado con éxito --------\n") 




def listarPedidos(i):
    print("\t\n\n Datos del cliente")
    print("\t\t\t * Nombre:", detalleCompras[0][i])
    print("\t\t\t * Apellido:", detalleCompras[1][i])
    print("\t\t\t * Teléfono:", detalleCompras[2][i])
    print("\t\t\n Datos de la entrega")
    print("\t\t\t * Nombre:", detalleCompras[3][i])
    print("\t\t\t * Dependencia:", detalleCompras[4][i])
    print("\t\t\t * Teléfono:", detalleCompras[5][i])
    print("\t\t\n Datos del pago")
    print("\t\t\t * Código del pedido:", detalleCompras[6][i])      
    print("\t\t\t * Pago final: $", detalleCompras[7][i])



def listarPedidosTabla(i):
  tabla = PrettyTable()

  tabla.field_names = ["Pedido", "Detalle"]
  tabla.align = "l"
  
  tabla.add_row(["Nombre del cliente", detalleCompras[0][i]])
  tabla.add_row(["Apellido del cliente", detalleCompras[1][i]])
  tabla.add_row(["Teléfono del cliente", detalleCompras[2][i]])

  tabla.add_row(["Nombre entrega", detalleCompras[3][i]])
  tabla.add_row(["Dependencia", detalleCompras[4][i]])
  tabla.add_row(["Teléfono entrega", detalleCompras[5][i]])

  tabla.add_row(["Código del pedido", detalleCompras[6][i]])
  tabla.add_row(["Pago final", f"$ {detalleCompras[7][i]}"])

  print(tabla)



def eliminarPedido():
  print("\n\n Ingrese el código del pedido que desea eliminar: \n\n")
  codigo= int(input("Código: "))
  if codigo in detalleCompras[6]:
    codigoFound = detalleCompras[6].index(codigo)
    print(codigoFound)
    for i in range(len(detalleCompras)):
      detalleCompras[i].pop(codigoFound)
    print("Pedido eliminado con éxito")
  else:
    print("\n\n El código ingresado no existe \n\n ")





def main():
  print("------------ MI POLICRUSH -------------")
  print("\n\t\t *** Bienvenido(a) ***\n")
  opcion= menu()
  while opcion !=4:
    if opcion==1:
      registrarPedido()
    elif opcion==2:
      if len(detalleCompras[0]) == 0:
        print("\n\n No existen pedidos registrados \n\n")
      else:
        for i in range(len(detalleCompras[0])):
          print(f"\n\n\n Detalle del pedido {i + 1}")
          listarPedidos(i)
          listarPedidosTabla(i)
    elif opcion==3:
      eliminarPedido()
      
    opcion= menu()

main()