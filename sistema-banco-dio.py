menu = '''
   [d] Depositar
   [s] Sacar
   [e] Extrato
   [q] Sair
 
'''

saldo = 0
LIMITE = 500
extrato_depositos = []
extrato_saques = []
limite_saque =  0

while True:
    opcao = input(menu)

    if opcao == "d":
     #logica depositar
     valor_depositado = int(input("Informe o valor do deposito: "))
     saldo += valor_depositado
     print("Depósito realizado com sucesso!!")
     print(f"Saldo disponivel: {saldo}")

     if(valor_depositado < 0):
        print("Não é possivel depositar um valor negativo, por favor informe um valor positivo")
     extrato_depositos.append(valor_depositado) 


    elif opcao == "s":
             #logica de sacar
           valor_saque = float(input("Informe o valor que deseja sacar: "))
           if(valor_saque > LIMITE): 
                print("Não é permitido o saque no valor maior que 500 reais")
           elif(valor_saque > saldo or saldo == 0):
                print("Não é possivel realizar um saque, saldo insuficiente")
           elif(valor_saque <= 0):
                print("Não é possivel sacar um valor negativo ou zero na conta") 
           elif saldo >= valor_saque:
                 saldo -= valor_saque
                 limite_saque += 1
                 if limite_saque > 3:
                   print("O limite de saque por dia é de 3, tente novamente mais tarde")
                 else:
                   print("Saque realizado com sucesso!!")
                   print(f"Valor retirado: {valor_saque}")
                   print(f"Saldo disponivel: {saldo}")  
                   extrato_saques.append(valor_saque)
                
     
    elif opcao == "e":
    #logica de extrato
     if not len(extrato_depositos): 
       print("Não há depósitos registrados na conta") 

     else:
       print('''########## +DEPÓSITOS+ ##########''')     
     for deposito in extrato_depositos: 
          print(f'''R${float(deposito):.2f}''') 
    
          print("##################################")

     if not len(extrato_saques):
         print("Não há saques registrados na conta")   
     else:
       print()
       print()
       print('''########## -SAQUES- ###############''')  
     for saque in extrato_saques:
           print(f'''R${float(saque):.2f}''') 
    
           print("##################################")
     print(f"$ Saldo Atual $ : R${saldo:.2f}")

                           
    elif opcao == "q":
     break
    
    else:
       print("Operação inválida, por favor selecione novamente a opção desejada")
