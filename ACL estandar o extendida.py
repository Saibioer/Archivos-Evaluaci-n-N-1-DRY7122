def verifica_el_tipo_de_acl(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "Acl Estandar"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "ACL Extendida"
    else:
        return "El numero no corresponde a una lista de acceso"

def main():
    numero_acl = int(input("Introduce el numero de ACL que corresponde a IPV4: "))
    tipo_acl = verifica_el_tipo_de_acl(numero_acl)
    print("El numero de ACL IPV4", numero_acl, "corresponde a una", tipo_acl)

if __name__ == "__main__":
    main()
