cuentas = ["juan", "andres", "maria"]
contras = ["Juanm3005", "andres234", "valentina25"]
saldo = [700000, 400000, 300000]

while True:
    print("Ingrese su cuenta: ")
    usuario = input()
    print("Ingrese la contraseña: ")
    contra = input()
    
    continuar = False  # Inicializar continuar como False
    for i in range(len(cuentas)):  # Cambiar a len(cuentas)
        if usuario == cuentas[i] and contra == contras[i]:
            continuar = True
            break  # Salir del bucle si se encuentra la cuenta

    if continuar:
        while True:
            opcion = int(input("""Menu:
    1. Transferir dinero
    2. Consultar saldo
    3. Depositar
    4. Retirar
    5. Cerrar sesion
    """))
            match opcion:
                case 1:
                    while True:
                        usuario2 = input("Ingrese el nombre de la segunda cuenta: ")
                        if usuario2 in cuentas:
                            saldo_transferir = int(input("Ingrese el saldo a transferir: "))
                            if saldo[cuentas.index(usuario)] >= saldo_transferir:
                                saldo[cuentas.index(usuario)] -= saldo_transferir
                                saldo[cuentas.index(usuario2)] += saldo_transferir
                                print(f"Transferencia exitosa. Nuevo saldo: {saldo[cuentas.index(usuario)]}")
                            else:
                                print("Saldo insuficiente para la transferencia.")
                            break  # Salir del bucle después de la transferencia
                        else:
                            print("Error en la cuenta, verifique el nombre.")
                
                case 2:
                    print("El saldo que hay en su cuenta es de: ")
                    print(saldo[cuentas.index(usuario)])
                
                case 3:
                        deposito = int(input("ingrese la cantidad de dinero que desea depositar "))
                        saldo[cuentas.index(usuario)] += deposito
                        print(f"Su nuevo saldo es: {saldo[cuentas.index(usuario)]}")
                
                case 4:
                    while True:
                        retiro = int(input("ingrese la cantidad de dinero que desea retirar "))
                        if retiro <= saldo[cuentas.index(usuario)]:
                            saldo[cuentas.index(usuario)] -= retiro
                            print(f"su nuevo saldo es: {saldo[cuentas.index(usuario)]}")
                            break
                        else:
                            print("la cantidad de retiro fue erronea no tiene suficiente dinero")
                    pass
                case 5:
                      # Preguntar si desea cerrar sesión
                    print("¿Desea cerrar sesión? 1. (sí) 2. (no)")
                    cerrar = input("")
                    if cerrar == "1":  # Comparar con la cadena "1"
                        break  # Salir del bucle del menú
                    pass

            
          
    else:
        print("Contraseña o nombre equivocado. Intente de nuevo.")