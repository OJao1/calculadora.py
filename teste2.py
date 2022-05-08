def Menu():
    print("=-==-==-==-==-= Menu de Opções =-==-==-==-==-=")

    print('''
        [1] Criar uma lista: 
        [2] Calculadora Básica: 
        [3] Conversor
        [4] Em desenvolvimento
        ''')

    Op = int(input("Escolha uma opção: "))

    if Op == 1:
        Lista = []
        Itens = int(input("Quantidade de itens na lista: "))
        for i in range(Itens):
            x = input("Item: ")
            Lista.append(x)
        print(Lista)

    teste = input("Deseja continuar? Sim/Não ")
    if teste == "Sim" or teste == "sim":
        return(Menu())

    elif teste == "Não" or teste == "não":
        exit("Saindo do programa...")

    elif Op == 2:
        # int transforma string em número inteiro
        num1 = int(input("Digite um número: "))
        operador = input(
            "Digite o operador (+(soma),-(subtração),/(divisão),*(multiplicação),**(elevado), */(Raiz Quadrada), /*(Raiz Cúbica): ")

    # */ Raiz Quadrada
        if operador == "*/":
            print("A raiz quadrada de {} é {}".format(num1, (num1 ** 0.5)))
    # */ Raiz Cúbica
        if operador == "/*":
            print("A raiz cúbica de {} é {}".format(num1, (num1 ** 1/3)))
    # + soma
        if operador == "+":
            num2 = int(input("Digite outro número: "))
            print("A soma entre {} e {} é {}".format(num1, num2, (num1 + num2)))
    # - subtração
        if operador == "-":
            num2 = int(input("Digite outro número: "))
            print("A subtração entre {} e {} é {}".format(num1, num2, (num1 - num2)))
    # / divisão
        if operador == "/":
            num2 = int(input("Digite outro número: "))
            print("A divisão entre {} e {} é {}".format(num1, num2, (num1 / num2)))
    # * multiplicação
        if operador == "*":
            num2 = int(input("Digite outro número: "))
            print("A multiplicação entre {} e {} é {}".format(num1, num2, (num1 * num2)))
    # ** Elevado
        if operador == "**":
            num2 = int(input("Digite outro número: "))
            print("O número {} elevado a {} é {}".format(num1, num2, (num1 ** num2)))

    teste = input("Deseja continuar? Sim/Não ")
    if teste == "Sim" or teste == "sim":
        return(Menu())

    elif teste == "Não" or teste == "não":
        exit("Saindo do programa...")

    elif Op == 3:

        print(''' 
                [1] Distância
                [2] Peso
                ''')

        converter = input("O que deseja conveter? ")
        
        if converter == 'Distância':
            print('''
                [1] Quilômetro (km)
                [2] Hectômetro (hm)
                [3] Decâmetro (dam)
                [4] Metro (m)
                [5] Decímetro (dm)
                [6] Centímetro (cm)
                [7] Milímetro (mm)
                ''')
            
            op1 = input('Unidade a ser convertida: ')
            op2 = input('Unidade para conversão: ')

    # =-=-=-=-=-=-=-=-=-= KM =-=-=-=-=-=-=-=-=-=-=-=-

    # KM p/ HM

            if op1 == 'km' and op2 == 'hm':
                q = float(input('Valor: '))
                m = print("{} km em hectômetros é {} hm".format(q, (q * 10)))

    # KM p/ DAM 
            
            elif op1 == 'km' and op2 == 'dam':
                q = float(input('Valor: '))
                m = print("{} km em decâmetros é {} dm".format(q, (q * 100)))

    # KM p/ M
            
            elif op1 == 'km' and op2 == 'm':
                q = float(input('Valor: '))
                m = print("{} km em metros é {} m".format(q, (q * 1000)))

    # KM p/ DM

            elif op1 == 'km' and op2 == 'dm':
                q = float(input('Valor: '))
                m = print("{} km em decímetros é {} dm".format(q, (q * 10000)))

    # KM p/ CM

            elif op1 == 'km' and op2 == 'cm':
                q = float(input('Valor: '))
                m = print("{} km em centímetros é {} cm".format(q, (q * 100000)))

    # KM p/ MM

            elif op1 == 'km' and op2 == 'mm':
                q = float(input('Valor: '))
                m = print("{} km em milímetros é {} mm".format(q, (q * 1000000)))

    # =-=-=-=-=-=-=-=-=-= HM =-=-=-=-=-=-=-=-=-=-=-=-

    # HM p/ KM

            elif op1 == 'hm' and op2 == 'km':
                q = float(input('Valor hm: '))
                m = print("{} hm em quilômetros é {} km".format(q, (q / 10)))

    # HM p/ DAM

            elif op1 == 'hm' and op2 == 'dam':
                q = int(input('Valor hm: '))
                m = print("{} hm em decâmetros é {} dam".format(q, (q * 10)))

    # HM p/ M

            elif op1 == 'hm' and op2 == 'm':
                q = int(input('Valor hm: '))
                m = print("{} hm em metros é {} m".format(q, (q * 100)))

    # HM p/ DM

            elif op1 == 'hm' and op2 == 'dm':
                q = int(input('Valor hm: '))
                m = print("{} hm em decímetros é {} dm".format(q, (q * 1000)))

    # HM p/ CM

            elif op1 == 'hm' and op2 == 'cm':
                q = int(input('Valor hm: '))
                m = print("{} hm em centímetros é {} cm".format(q, (q * 10000)))

    # HM p/ MM

            elif op1 == 'hm' and op2 == 'mm':
                q = int(input('Valor hm: '))
                m = print("{} hm em quilômetros é {} mm".format(q, (q * 1000000)))

    # =-=-=-=-=-=-=-=-=-= DAM =-=-=-=-=-=-=-=-=-=-=-=-

    # DAM p/

            elif op1 == 'dam' and op2 == 'km':
                q = int(input('Valor dam: '))
                m = print("{} dam em quilômetros é {} km".format(q, (q / 100)))

    # DAM p/ HM
            elif op1 == 'dam' and op2 == 'hm':
                q = int(input('Valor dam: '))
                m = print('{} dam em hectômetros é {} hm'.format(q, (q / 10)))

    # DAM p/ M

            elif op1 == 'dam' and op2 == 'm':
                q = int(input('Valor dam: '))
                m = print('{} dam em metros é {} m'.format(q, (q * 10)))

    # DAM p/ DM

            elif op1 == 'dam' and op2 == 'dm':
                q = int(input('Valor dam: '))
                m = print("{} dam em decímetros é {} dm".format(q, (q * 100)))
            
    # DAM p/ CM

            elif op1 == 'dam' and op2 == 'cm':
                q = int(input('Valor dam: '))
                m = print('{} dam em centímetros é {} cm'.format(q, (q * 1000)))

    # DAM p/ MM

            elif op1 == 'dam' and op2 == 'mm':
                q = int(input('Valor dam: '))
                m = print('{} dam em milímetros é {}'.format(q, (q * 10000)))

    # =-=-=-=-=-=-=-=-=-= M =-=-=-=-=-=-=-=-=-=-=-=-

    # M p/ KM 

            elif op1 == 'm' and op2 == 'km':
                q = float(input('Valor m: '))
                m = print('{} m em quilômetros são {} km'.format(q, (q / 1000)))

    # M p/ HM

            elif op1 == 'm' and op2 == 'hm':
                q = float(input('Valor m: '))
                m = print('{} m em hectômetros são {} hm'.format(q, (q / 100)))

    # M p/ DAM

            elif op1 == 'm' and op2 == 'dam':
                q = float(input('Valor m: '))
                m = print('{} m em decâmetros são {} dam'.format(q, (q / 10)))

    # M p/ DM 

            elif op1 == 'm' and op2 == 'dm':
                q = float(input('Valor em metros: '))
                m = print('{} m em decímetros é {} dm'.format(q, (q * 10)))


    # M p/ CM 

            elif op1 == 'm' and op2 == 'cm':
                q = float(input('Valor em metros: '))
                m = print('{} m em centímetros é {} cm'.format(q, (q * 100)))

    # M p/ MM

            elif op1 == 'm' and op2 == 'mm':
                q = float(input('Valor em metros: '))
                m = print('{} m em milímetros é {} mm'.format(q, (q * 1000)))

    # =-=-=-=-=-=-=-=-=-= DM =-=-=-=-=-=-=-=-=-=-=-=-

    # DM p/ KM

            elif op1 == 'dm' and op2 == 'km':
                q = float(input('Valor em decímetros: '))
                m = print('{} dm em quilômetros são {} km'.format(q, (q / 10000)))

    # DM p/ HM

            elif op1 == 'dm' and op2 == 'hm':
                q = float(input('Valor em decímetros: '))
                m = print('{} dm em decímetros são {} hm'.format(q, (q / 1000)))

    # DM p/ DAM

            elif op1 == 'hm' and op2 == 'dam':
                q = float(input('Valor em decímetros: '))
                m = print('{} dm em decâmetros são {} dam'.format(q, (q / 100)))

    # DM p/ M

            elif op1 == 'dm' and op2 == 'm':
                q = float(input('Valor em decímetros: '))
                m = print('{} dm em metros são {} m'.format(q, (q / 10)))

    # DM p/ CM

            elif op1 == 'dm' and op2 == 'cm':
                q = float(input('Valor em decímetros: '))
                m = print('{} dm em centímetros são {} cm'.format(q, (q * 10)))

    # DM p/ MM

            elif op1 == 'dm' and op2 == 'mm':
                q = float(input('Valor em centímetros: '))
                m = print('´{} dm em milímetros são {} mm'.format(q, (q * 100)))

    # =-=-=-=-=-=-=-=-=-= CM =-=-=-=-=-=-=-=-=-=-=-=-

    # CM p/ KM

            elif op1 == 'cm' and op2 == 'km':
                q = float(input('Valor em centímetros: '))
                m = print('{} cm em quilômetros são {} km'.format(q, (q / 100000)))

    # CM p/ HM

            elif op1 == 'cm' and op2 == 'hm':
                q = float(input('Valor em centímetros: '))
                m = print('{} cm em hectômetros são {} hm'.format(q, (q / 10000)))

    # CM p/ DAM

            elif op1 == 'cm' and op2 == 'dam':
                q = float(input('Valor em centímetros: '))
                m = print('{} cm em decâmetros são {} dam'.format(q, (q / 1000)))

    # CM p/ M

            elif op1 == 'cm' and op2 == 'm':
                q = float(input('Valor em centímetros: '))
                m = print('{} cm em metros são {} m'.format(q, (q / 100)))

    # CM p/ DM

            elif op1 == 'cm' and op2 == 'dm':
                q = float(input('Valor em centímetros: '))
                m = print('{} cm em decímetros são {} dm'.format(q, (q / 10)))

    # CM p/ MM

            elif op1 == 'cm' and op2 == 'mm':
                q = float(input('Valor em centímetros: '))
                m = print('{} cm em milímetros são {} mm'.format(q, (q * 10)))

    # =-=-=-=-=-=-=-=-=-= MM =-=-=-=-=-=-=-=-=-=-=-=-

    # MM p/ KM

            elif op1 == 'mm' and op2 == 'km':
                q = float(input('Valor em milímetros: '))
                m = print('{} mm em quilômetros são {} km'.format(q, (q / 1000000)))

    # MM p/ HM

            elif op1 == 'mm' and op2 == 'hm':
                q = float(input('Valor em milímetros: '))
                m = print('{} mm em hectômetros são {} hm'.format(q, (q / 100000)))

    # MM p/ DAM

            elif op1 == 'mm' and op2 == 'dam':
                q = float(input('Valor em milímetros: '))
                m = print('{} mm em decâmetros são {} dam'.format(q, (q / 10000)))

    # MM p/ M

            elif op1 == 'mm' and op2 == 'm':
                q = float(input('Valor em milímetros: '))
                m = print('{} mm em metros são {} m'.format(q, (q / 1000)))

    # MM p/ DM

            elif op1 == 'mm' and op2 == 'dm':
                q = float(input('Valor em milímetros: '))
                m = print('{} mm em decímetros são {} dm'.format(q, (q / 100)))

    # MM p/ CM

            elif op1 == 'mm' and op2 == 'cm':
                q = float(input('Valor em milímetros: '))
                m = print('{} mm em centímetros são {} cm'.format(q, (q / 10)))
            

        if converter == 'Peso':
            print('''
                [1] Quilograma (kg)
                [2] Hectograma (hg)
                [3] Decagrama (dag)
                [4] Grama (g)
                [5] Decigrama (dg)
                [6] Centigrama (cg)
                [7] Miligrama (mg)
                ''')

            opcao_1 = input('Unidade a ser convertida: ')
            opcao_2 = input('Unidade para conversão: ')

            if opcao_1 == 'kg' and opcao_2 == 'hg':
                q = float(input('Valor em quilogramas: '))
                m = print('{} kg em hectogramas são {} hg'.format(q, (q * 10)))

            elif opcao_1 == 'kg' and opcao_2 == 'dag':
                q = float(input('Valor em quilogramas: '))
                m = print('{} kg em decagramas são {} dag'.format(q, (q * 100)))

            elif opcao_1 == 'kg' and opcao_2 == 'g':
                q = float(input('Valor em quilogramas: '))
                m = print('{} kg em gramas são {} g'.format(q, (q * 1000)))
                

            elif opcao_1 == 'kg' and opcao_2 == 'dg':
                q = float(input('Valor em quilogramas: '))
                m = print('{} kg em decigramas são {} dg'.format(q, (q * 10000)))
                

            elif opcao_1 == 'kg' and opcao_2 == 'cg':
                q = float(input('Valor em quilogramas: '))
                m = print('{} kg em centigramas são {} cg'.format(q, (q * 100000)))
                
            
            elif opcao_1 == 'kg' and opcao_2 == 'mg':
                q = float(input('Valor em quilogramas: '))
                m = print('{} kg em miligramas são {} mg'.format(q, (q * 1000000)))
                
    # --------------------------------------------------------------------------------------------------------------------            

            if opcao_1 == 'hg' and opcao_2 == 'kg':
                q = float(input('Valor em hectogramas: '))
                m = print('{} hg em quilogramas são {} kg'.format(q, (q / 10)))
                

            elif opcao_1 == 'hg' and opcao_2 == 'dag':
                q = float(input('Valor em hectogramas: '))
                m = print('{} hg em decagramas são {} dag'.format(q, (q * 10)))
                

            elif opcao_1 == 'hg' and opcao_2 == 'g':
                q = float(input('Valor em hectogramas: '))
                m = print('{} hg em gramas são {} g'.format(q, (q * 100)))
                

            elif opcao_1 == 'hg' and opcao_2 == 'dg':
                q = float(input('Valor em hectogramas: '))
                m = print('{} hg em decigramas são {} dg'.format(q, (q * 1000)))
                

            elif opcao_1 == 'hg' and opcao_2 == 'cg':
                q = float(input('Valor em hectogramas: '))
                m = print('{} hg em centigramas são {} cg'.format(q, (q * 10000)))
                

            elif opcao_1 == 'hg' and opcao_2 == 'mg':
                q = float(input('Valor em hectogramas: '))
                m = print('{} hg em hectogramas são {} mg'.format(q, (q * 100000)))
                

    # --------------------------------------------------------------------------------------------------------------------    

            if opcao_1 == 'dag' and opcao_2 == 'kg':
                q = float(input('Valor em decagrama: '))
                m = print('{} dag em quilogramas são {} kg'.format(q, (q / 100)))
                

            if opcao_1 == 'dag' and opcao_2 == 'hg':
                q = float(input('Valor em decagrama: '))
                m = print('{} dag em hectogramas são {} hg'.format(q, (q / 10)))
                

            if opcao_1 == 'dag' and opcao_2 == 'g':
                q = float(input('Valor em decagrama: '))
                m = print('{} dag em gramas são {} g'.format(q, (q * 10)))
                

            if opcao_1 == 'dag' and opcao_2 == 'dg':
                q = float(input('Valor em decagrama: '))
                m = print('{} dag em decigramas são {} dg'.format(q, (q * 100)))
                

            if opcao_1 == 'dag' and opcao_2 == 'cg':
                q = float(input('Valor em decagrama: '))
                m = print('{} dag em centigramas são {} cg'.format(q, (q * 1000)))
                

            if opcao_1 == 'dag' and opcao_2 == 'mg':
                q = float(input('Valor em decagrama: '))
                m = print('{} dag em miligramas são {} mg'.format(q, (q * 10000)))
                

    # -------------------------------------------------------------------------------------------------------------------- 

            if opcao_1 == 'g' and opcao_2 == 'kg':
                q = float(input('Valor em gramas: '))
                m = print('{} g em quilogramas são {} kg'.format(q, (q / 1000)))
                
            if opcao_1 == 'g' and opcao_2 == 'hg':
                q = float(input('Valor em gramas: '))
                m = print('{} g em hectogramas são {} hg'.format(q, (q / 100)))
                
            if opcao_1 == 'g' and opcao_2 == 'dag':
                q = float(input('Valor em gramas: '))
                m = print('{} g em decagramas são {} dag'.format(q, (q / 10)))
                            
            if opcao_1 == 'g' and opcao_2 == 'dg':
                q = float(input('Valor em gramas: '))
                m = print('{} g em decigramas são {} dg'.format(q, (q * 10)))
                    
            if opcao_1 == 'g' and opcao_2 == 'cg':
                q = float(input('Valor em gramas: '))
                m = print('{} g em centigramas são {} cg'.format(q, (q * 100)))
                
            if opcao_1 == 'g' and opcao_2 == 'mg':
                q = float(input('Valor em gramas: '))
                m = print('{} g em miligramas são {} mg'.format(q, (q * 1000)))     

    # -------------------------------------------------------------------------------------------------------------------- 

            if opcao_1 == 'dg' and opcao_2 == 'kg':
                q = float(input('Valor em decigramas: '))
                m = print('{} dg em quilogramas são {} kg'.format(q, (q / 1000)))
                
            if opcao_1 == 'dg' and opcao_2 == 'hg':
                q = float(input('Valor em decigramas: '))
                m = print('{} dg em hectogramas são {} hg'.format(q, (q / 100)))
                
            if opcao_1 == 'dg' and opcao_2 == 'dag':
                q = float(input('Valor em decigramas: '))
                m = print('{} dg em decigramas são {} dag'.format(q, (q / 10)))
                
            if opcao_1 == 'dg' and opcao_2 == 'g':
                q = float(input('Valor em decigramas: '))
                m = print('{} dg em gramas são {} g'.format(q, (q * 10)))
                
            if opcao_1 == 'dg' and opcao_2 == 'cg':
                q = float(input('Valor em decigramas: '))
                m = print('{} dg em centigramas são {} cg'.format(q, (q * 100)))
                        
            if opcao_1 == 'dg' and opcao_2 == 'mg':
                q = float(input('Valor em decigramas: '))
                m = print('{} dg em miligramas são {} mg'.format(q, (q * 1000)))
                
    # -------------------------------------------------------------------------------------------------------------------- 

            if opcao_1 == 'cg' and opcao_2 == 'kg':
                q = float(input('Valor em centigramas: '))
                m = print('{} cg em quilogramas são {} kg'.format(q, (q / 100000)))
                
            if opcao_1 == 'cg' and opcao_2 == 'hg':
                q = float(input('Valor em centigramas: '))
                m = print('{} cg em hectogramas são {} hg'.format(q, (q / 10000)))
                
            if opcao_1 == 'cg' and opcao_2 == 'dag':
                q = float(input('Valor em centigramas: '))
                m = print('{} cg em decagramas são {} dag'.format(q, (q / 1000)))
                
            if opcao_1 == 'cg' and opcao_2 == 'g':
                q = float(input('Valor em centigramas: '))
                m = print('{} cg em gramas são {} g'.format(q, (q / 100)))
                
            if opcao_1 == 'cg' and opcao_2 == 'dg':
                q = float(input('Valor em centigramas: '))
                m = print('{} cg em decigramas são {} dg'.format(q, (q / 10)))
                
            if opcao_1 == 'cg' and opcao_2 == 'mg':
                q = float(input('Valor em centigramas: '))
                m = print('{} cg em miligramas são {} mg'.format(q, (q * 10)))
                
    # -------------------------------------------------------------------------------------------------------------------- 

            if opcao_1 == 'mg' and opcao_2 == 'kg':
                q = float(input('Valor em miligramas: '))
                m = print('{} mg em quilogramas são {} kg'.format(q, (q / 1000000)))
                
            if opcao_1 == 'mg' and opcao_2 == 'hg':
                q = float(input('Valor em miligramas: '))
                m = print('{} mg em hectogramas são {} hg'.format(q, (q / 100000)))
                
            if opcao_1 == 'mg' and opcao_2 == 'dag':
                q = float(input('Valor em miligramas: '))
                m = print('{} mg em decagramas são {} dag'.format(q, (q / 10000)))
                
            if opcao_1 == 'mg' and opcao_2 == 'g':
                q = float(input('Valor em miligramas: '))
                m = print('{} mg em gramas são {} g'.format(q, (q / 1000)))
                            
            if opcao_1 == 'mg' and opcao_2 == 'dg':
                q = float(input('Valor em miligramas: '))
                m = print('{} mg em decigramas são {} dg'.format(q, (q / 100)))
                
            if opcao_1 == 'mg' and opcao_2 == 'cg':
                q = float(input('Valor em miligramas: '))
                m = print('{} mg em centigramas são {} cg'.format(q, (q / 10)))

            teste = input("Deseja continuar? Sim/Não ")
            if teste == "Sim" or teste == "sim":
                return(Menu())

            elif teste == "Não" or teste == "não":
                exit("Saindo do programa...")

            else:
                print("Erro: Ação Inválida!")

        else:
            print("Erro: Ação Inválida!")
            
    

    
            
