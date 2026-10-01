print("ELIJA COMO SE VA A ENVIAR SU PAQUETE")
print("1.recogo en oficina")
print("2.Envio a domicillo")
eliga_opcion = input("1 o 2: ")

print("A DONDE SE VA A ENVIAR SU PAQUETE")
print("1.LIMA","2.TRUJILLO", "3.CHICLAYO")
eliga_destino = input("1 o 2 o 3: ") 
costo_base = 0

print("COSTO DEL PAQUETE")
if eliga_destino == "1":
    costo_base=20
    print("el costo a lima es S/20 (incluye un 1kg)")
elif eliga_destino== "2":
    costo_base=15
    print("el costo a trujillo es S/15 (incluye un 1kg)")
elif eliga_destino == "3":
    costo_base=10
    print("el costo a chiclayo es S/10 (incluye un 1kg)")
else:
    print("opcion de destino invalida ")

if costo_base>0:
    print("ingrese el peso del paquete")
    kilos=int(input("cuantos kilos pesa: "))
    if kilos>1:
        kilos_extras= kilos-1
        cobro_adicioanal = kilos_extras*4
    else:
        cobro_adicioanal=0
    costo_total = costo_base + cobro_adicioanal
    print("cobro adicional por peso es S/",cobro_adicioanal)
    print("el costo total a pagar es S/",costo_total)
    print("procedemos a enviar su paquete")
print("ingrese el contenido del paquete")
declaraciondelcontenido = input(":")
print("TICKET" )
print()