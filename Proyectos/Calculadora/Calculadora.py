import numpy as ny
import math as matematica

while 1:

    primer_numero = float(input('Indica el valor del primer numero: '))

    segundo_numero = float(input('Indica el valor del segundo numero: '))

    print('Selecciona la operacion que deseas realizar: ')

    print('1. Sumar')

    print('2. Restar')

    print('3. Multiplicar')

    print('4. Dividir')

    print('5. Potencia')

    print('6. Logaritmo')

    opcion_para_operar = int(input('Cual eliges: '))

    if opcion_para_operar==1:

        resultado = primer_numero + segundo_numero
        print(resultado)

    elif opcion_para_operar==2:
        
        resultado = primer_numero - segundo_numero
        print(resultado)

    elif opcion_para_operar==3:
        
        resuldato = primer_numero * segundo_numero
        print(resultado)

    elif opcion_para_operar==4 and segundo_numero!=0:

        resultado = primer_numero / segundo_numero
        print(resultado)

    elif opcion_para_operar==5:
        
        resultado = primer_numero**segundo_numero
        print(resultado)

    elif opcion_para_operar==6 and primer_numero>0:

        resultado = matematica.log10(primer_numero)
        print(resultado)
        
    else:

        print('Opcion desconocida Elija otra')





