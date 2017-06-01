def leerEntero(men):
    while True:
        try:
            valor = int(raw_input(men))
            break
        except ValueError:
            #raise ValueError("Digite un entero...")
            pass
    return valor

def leerFlotante(mens):
    while True:
        try:
            valor = float(raw_input(mens))
            break
        except ValueError:
            raise ValueError("Digite un flotante...")
            pass
    return valor

def leerChar(mens):
    while True:
        try:
            valor = raw_input(mens)
            valor = str(valor)
            valor = valor[0]
            valor.upper()
            break
        except ValueError:
            raise ValueError("Digite un char...")
            pass
    return valor[0]

def leerCadena(mens):
    while True:
        try:
            valor = input(mens)
            valor = str(valor)
            valor.upper()
            break
        except ValueError:
            raise ValueError("Digite un char...")
            pass
    return valor