def calcular_imposto(salario):
    
    
    if salario<2259.2:
        
        imposto=0
        print(f"o valor do imposto é:R${imposto}")
        
    elif 2826.65>salario>2259.21:
        
        
        imposto=salario*0.075-169.44 
        print(f"o valor do imposto é:R${imposto}")
        
    elif 3751.05>salario>2826.66:
        
        
        imposto=salario*0.15-381.44
        print(f"o valor do imposto é:R${imposto}")
        
    elif 4664.68>salario>3751.06:
        
        
        imposto=salario*0.225-662.77
        print(f"o valor do imposto é:R${imposto}")
        
     
    elif salario>4664.68:
        
         
        imposto=salario*0.275-896
    
        print(f"o valor do imposto é:R${imposto}")


salario1=float(input("o valor do salário é:"))

imposto1=calcular_imposto(salario1)







 
        
        
