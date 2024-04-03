

# Mini Sistema Banc�rio
Este mini sistema, visa simular situa��es de pequenas transa��es banc�rias, como criar uma conta, depositar, sacar, listar contas cadastradas, listar clientes, pesquisar contas, imprimir extrato, transferir, entre outras. Todas as suas op��es, est�o listadas no menu abaixo, que � a primeira fun��o a ser executada, assim que voc� inicia a aplica��o:

~~~~
'''
         *************************************************
         ********************** ATM **********************
         ******************* New Bank ********************
         *************************************************
         ** O que voc� deseja fazer?         *************
         **                                  *************
         ** 1 - Criar conta                  *************
         ** 2 - Sacar                        *************
         ** 3 - Depositar                    *************
         ** 4 - Transferir                   *************
         ** 5 - Listar Contas                *************
         ** 6 - Listar Clientes              *************
         ** 7 - Pesquisar Conta por N�mero   *************
         ** 8 - Pesquisar Cliente por N�mero *************
         ** 9 - Imprimir Extrato             *************          
         ** 0 - Sair do Sistema              *************
         *************************************************
    '''
~~~~

## Desafio
Este projeto inicial foi desenvolvido no curso de **Programa��o em Python essencial da Geek University**, as fun��es que foram incrementadas fora do curso foram:
* Listar Clientes
* Pesquisar conta por N�mero
* Pesquisar Cliente por N�mero
* Algumas melhorias e valida��es

## Resumo do c�digo
O c�digo � composto por duas classes: Conta e Cliente, a classe Cliente possui as informa��es b�sicas de um poss�vel cliente do banco, pois cada conta possui um cliente, digamos que, para esse in�cio de vers�o, o nosso banco aceite apenas clientes pessoas f�sicas. Portando para criar uma Conta � necess�rio ter um cliente e os atributos necess�rios para a cria��o de um cliente s�o:
* Nome
* CPF
* Data de nascimento
* e-mail

No menu principal ao escolher a op��o 1 criar conta, ele vai solicitar os dados do cliente para assim criar a conta, cada conta assim como o cliente, eles s�o criados com um n�mero pre-determinado, o cliente possui um id_cliente que se inicia em 100 a partir do primeiro cadastro e o n�mero da conta inicia em 1001, ambos v�o sendo incrementados de 1 em 1, a cada nova conta e consequentemente a cada novo cliente. Nessa conta a cada cria��o, ela inicia com um limite de cheque especial de 200 e com o saldo zero, ou seja, caso j� queira iniciar utilizando o cheque especial, este banco deixa, mas ficar� com um saldo negativo de at� o limite do cheque, que no caso s�o de R$ 200.00
Fora o m�dulo banco e as classes Conta e Cliente, o arquivo conta com um m�dulo helper, contendo algumas fun��es auxiliares de formata��o, um m�dulo chamado menu, apenas para um melhor organiza��o e um mais m�dulo de testes, para testarmos algumas implementa��es pontuais.
 

## Opera��es
Toda a l�gica das opera��es est�o praticamente implementadas na classe conta, mas todas as valida��es necess�rias ao menos de in�cio, s�o implementadas no m�dulo banco, fazer valida��es sem usar exce��es deixa o c�digo um pouco mais verboso e com muitas fun��es, futuramente essas valida��es ser�o implementadas utilizando o poder das exce��es, essa parte ficar� para aprimoramentos futuros. No m�dulo banco, ao iniciarmos o programa, imprimir� o menu de op��es e a partir da escolha do usu�rio, as opera��es s�o chamadas e executadas, caso ele escolha alguma op��o mas n�o exista contas cadastradas, o programa exibe a mensagem "ainda n�o existem contas cadastradas", para executar qualquer opera��o, faz-se necess�rio no m�nimo termos um conta cadastrada.

### Criar conta
Essa op��o solicitar� os dados do cliente, como nome, cpf e etc, em seguida ela cria a conta do cliente no sistema. Essa � fun��o que praticamente n�o tem valida��o, portanto, nome, cpf e email, como s�o strings, ele vai aceitar qualquer coisa que seja uma string, na data de nascimento, caso n�o esteja no padr�o (dd/mm/aaaa) o programa dar� um erro e parar� a execu��o, esse tratamento ser� feito com exce��es futuramente. Ao criar a conta ele exibe no painel conta criada com sucesso, contendo os dados principais da conta.

### Sacar
Com a conta cadastrada, podemos fazer qualquer opera��o e uma delas � o saque, como a conta � criada j� com um limite de cheque especial de R$ 200,00, o usu�rio caso esteja no aperto pode sacar at� esse valor, acima disso, a opera��o n�o permite. A fun��o de saque ela valida se possui saldo e se o valor � maior que zero para poder efetuar a opera�ao.

### Depositar
A opera��o de dep�sito primeiro valida se o valor � maior que zero e tamb�m assim como as outras, valida se a conta existe para poder efetuar a opera��o, em seguida pega o valor digitado e soma com o saldo da conta.

### Transferir
A opera��o faz todas as valida��es de saque e dep�sito, como tamb�m se as contas de origem e destino existem, por baixo dos panos e para simplificar, a fun��o de transferir ela efetua um "saque" na conta de origem e faz um dep�sito na conta destino.

### Listar Contas
Opera��o b�sica e auxiliar, verifica se possui contas cadastradas, caso a resposta seja sim, ela varre a lista de contas e exibe o relat�rio na tela.

### Listar Clientes
Esta opera��o segue mesma l�gica da fun��o listar contas, a diferen�a � que ela percorre uma lista de clientes, que caso existam cadastrados, ele imprime o relat�rio na tela.

### Pesquisar cliente Conta e Pesquisar cliente por n�mero
Esas opera��es tamb�m possuem l�gicas semelhantes. Primeiro elas validam se possuem contas ou clientes cadastrados, caso sim, validam se possuem contas ou clientes com n�mero que foi solicitado, caso sim imprime-se os dados na tela, caso n�o, uma mensagem informado que n�o foram encontradas contas ou clientes com aquele n�mero, � exibida.

### Imprimir Extrato
Essa opera��o deve listar todos os dep�sitos, saques e transfer�ncias realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, deve exibir a mensagem: **N�o foram realizadas movimenta��es**
Os valores devem ser exibidos utilizando R$ xxx.xx.

**Ex:** 1750,20 = R$ 1750,20


! Este projeto visa melhorar e praticar o aprendizado nos estudo em python e talvez ajude algu�m que precisa implementar uma l�gica parecido ou algum projeto semelhante na universade ou nos estudos. Lembrando que nem todas as valida��es est�o funcionando perfeitamente, essas melhorias ser�o aplicadas com o tempo.
