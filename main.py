import psycopg2 as psycopg2
import os
import getpass
from datetime import datetime

#Define o tamanho que ira abrir o prompt
os.system('mode 210,25')
#Define a cor da letra como verde no prompt
os.system("color a")
#Pega o nome do usuario do desktop
usuario = getpass.getuser()
#pega a data que o programa esta sendo executado
data = datetime.now().strftime('%Y-%m-%d')

print(data,'\n')
print('Ola ',usuario, ' Vamos começar')

try:
    
    #A Função Con é a principal onde existem as sub funções, foi criada para que o programa possa ser reiniciado de qualquer outra função.
    def con():
        #As informações serão utilizadas no where do select -------------------------------------------------
        loja = input("\nQual o numero da Loja? - Como exemplo loja: 12\n\n")
        os.system('cls')
        pdv = input("\nQual o numero do PDV? - Como exemplo PDV: 003 \n\n")
        os.system('cls')
        movimento = input("\nQual o Movimento da Quebra? - Usando o padrão ANO-MES-DIA\n\n")
        os.system('cls')
        print('\n\nBuscando informações .......\n\n')
        ------------------------------------------------------------------------------------------------------
        #Conexão com banco postgresql
        conexao = psycopg2.connect(host='', database='', user='', password='')
        cursor = conexao.cursor()

        cursor = conexao.cursor()
        ------------------------------------------------------------------------------------------------------
        #A Função menu é chama após trazer as informações das quebras-----------------------------------------
        def menu():

            opcao = int(input('\nDeseja consultar outra quebra ?\n1 - Sim\n2 - Não \n'))
            if opcao == 1:
                os.system('cls')
                con()
            elif opcao == 2:
                quit()
            elif opcao == "'":
                print('opcao invalida\n')
                menu()
            else:
                 print('opcao invalida\n')
                 menu()
        --------------------------------------------------------------------------------------------------------
        def sistema():

            def contador():

                comando = f"SELECT COUNT(p.cod_usuario) FROM T_PDV p JOIN usuario u ON p.cod_usuario = u.id AND p.valorVendido > '0' WHERE datafiscal = '{movimento}' and p.nestab = '{loja}' and p.npdv = '{pdv}'"

                cursor.execute(comando)

                resultado = cursor.fetchall()  # ler o banco de dados

                return resultado

            quantidade = int(contador()[0][0])
            limite = 0

            if quantidade == 0:
                    os.system('cls')
                    print('\n\nNão existem registros o PDV informado\nValidade os dados\n\n')
                    menu()
            else:
                os.system('cls')
                print("\tOperadora\t\tPagamento em Dinheiro\t\t    Sagria Dinheiro\t\t Diferença Dinheiro\t\tPagamento com Cartões\t\t   Sangria Cartões\t   Diferença Cartões")
                print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

                while limite < quantidade:

                        def operadores():
                                    comando = f"SELECT RPAD(u.nome, 26, ' '),p.cod_usuario ID_Operadora FROM T_PDV p JOIN usuario u ON p.cod_usuario = u.id AND p.valorVendido > '0' WHERE datafiscal = '{movimento}' and p.nestab = '{loja}' and p.npdv = '{pdv}'"

                                    cursor.execute(comando)

                                    resultado = cursor.fetchall()  # ler o banco de dados

                                    return resultado



                        def pagamentodinheiro():

                                    comando = f"SELECT SUM(round (valor,2))  FROM T_VendaPagto vp JOIN T_Venda v ON vp.cod_venda = v.cod_venda JOIN T_PDV pdv ON pdv.ID = v.IDPDV and pdv.nestab = v.nestab and pdv.npdv = v.npdv and pdv.datafiscal = v.datafiscal JOIN usuario u ON pdv.cod_usuario = u.id WHERE vp.idtipopagto IN ('1','0') AND vp.subtipotrans = 'E' AND v.vendaEncerrada = 'S' AND  vp.datafiscal = '{movimento}' AND cod_usuario = '{operadores()[limite][1]}' and vp.nestab  = '{loja}' and vp.npdv = '{pdv}';"

                                    cursor.execute(comando)

                                    resultado = cursor.fetchall()  # ler o banco de dados

                                    return resultado

                        def sangriadinheiro():

                                    comando = f"SELECT  SUM(round (valor,2))  FROM T_VendaPagto vp JOIN T_Venda v ON vp.cod_venda = v.cod_venda JOIN T_PDV pdv ON pdv.ID = v.IDPDV and pdv.nestab = v.nestab and pdv.npdv = v.npdv and pdv.datafiscal = v.datafiscal JOIN usuario u ON pdv.cod_usuario = u.id WHERE vp.idtipopagto IN ('1') AND vp.subtipotrans = 'S' AND v.vendaEncerrada = 'S' and vp.datafiscal = '{movimento}' AND cod_usuario = '{operadores()[limite][1]}' and vp.nestab  = '{loja}' and vp.npdv = '{pdv}';"

                                    cursor.execute(comando)

                                    resultado = cursor.fetchall()  # ler o banco de dados

                                    return resultado

                        def pagamentocartao():

                                    comando = f"SELECT SUM(round (valor,2))  FROM T_VendaPagto vp JOIN T_Venda v ON vp.cod_venda = v.cod_venda JOIN T_PDV pdv ON pdv.ID = v.IDPDV and pdv.nestab = v.nestab and pdv.npdv = v.npdv and pdv.datafiscal = v.datafiscal JOIN usuario u ON pdv.cod_usuario = u.id WHERE vp.idtipopagto IN ('4','5','7','10','13','21') AND vp.subtipotrans = 'E' AND v.vendaEncerrada = 'S'AND  vp.datafiscal = '{movimento}' AND cod_usuario = '{operadores()[limite][1]}' and vp.nestab  = '{loja}' and vp.npdv = '{pdv}';"

                                    cursor.execute(comando)

                                    resultado = cursor.fetchall()  # ler o banco de dados

                                    return resultado


                        def sangriacartao():

                            comando = f"SELECT  SUM(round (valor,2))  FROM T_VendaPagto vp JOIN T_Venda v ON vp.cod_venda = v.cod_venda JOIN T_PDV pdv ON pdv.ID = v.IDPDV and pdv.nestab = v.nestab and pdv.npdv = v.npdv and pdv.datafiscal = v.datafiscal JOIN usuario u ON pdv.cod_usuario = u.id WHERE vp.idtipopagto IN ('4','5','7','10','13','21') AND vp.subtipotrans = 'S' AND v.vendaEncerrada = 'S' and vp.datafiscal = '{movimento}' AND cod_usuario = '{operadores()[limite][1]}' and vp.nestab  = '{loja}' and vp.npdv = '{pdv}';"

                            cursor.execute(comando)

                            resultado = cursor.fetchall()  # ler o banco de dados

                            return resultado

                        operador = operadores()[limite][0]
                        pdinheiro = pagamentodinheiro()[0][0]
                        sdinheiro = sangriadinheiro()[0][0]
                        ddinheiro = pdinheiro -- sdinheiro
                        pcartao = pagamentocartao()[0][0]
                        scartao = sangriacartao()[0][0]
                        dcartao = pcartao--scartao

                        print(f"|{operador}|\t\t{str(pdinheiro).ljust(17)}|\t\t{str(sdinheiro).ljust(17)}|\t\t{str(round(ddinheiro,2)).ljust(17)}|\t\t{str(pcartao).ljust(17)}|\t\t{str(scartao).ljust(17)}|\t{round(dcartao,2)}\t\t|")

                        limite += 1

                        menu()
        sistema()
    con()

except:
    print('\nOcorreu um erro ao tentar buscar informações solicitadas')
