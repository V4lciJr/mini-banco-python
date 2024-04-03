

# Mini Sistema Bancário
Este mini sistema, visa simular situações de pequenas transações bancárias, como criar uma conta, depositar, sacar, listar contas cadastradas, listar clientes, pesquisar contas, imprimir extrato, transferir, entre outras. Todas as suas opções, estão listadas no menu abaixo, que é a primeira função a ser executada, assim que você inicia a aplicação:

~~~~
'''
         *************************************************
         ********************** ATM **********************
         ******************* New Bank ********************
         *************************************************
         ** O que você deseja fazer?         *************
         **                                  *************
         ** 1 - Criar conta                  *************
         ** 2 - Sacar                        *************
         ** 3 - Depositar                    *************
         ** 4 - Transferir                   *************
         ** 5 - Listar Contas                *************
         ** 6 - Listar Clientes              *************
         ** 7 - Pesquisar Conta por Número   *************
         ** 8 - Pesquisar Cliente por Número *************
         ** 9 - Imprimir Extrato             *************          
         ** 0 - Sair do Sistema              *************
         *************************************************
    '''
~~~~

## Desafio
Este projeto inicial foi desenvolvido no curso de **Programação em Python essencial da Geek University**, as funções que foram incrementadas fora do curso foram:
* Listar Clientes
* Pesquisar conta por Número
* Pesquisar Cliente por Número
* Algumas melhorias e validações

## Resumo do código
O código é composto por duas classes: Conta e Cliente, a classe Cliente possui as informações básicas de um possível cliente do banco, pois cada conta possui um cliente, digamos que, para esse início de versão, o nosso banco aceite apenas clientes pessoas físicas. Portando para criar uma Conta é necessário ter um cliente e os atributos necessários para a criação de um cliente são:
* Nome
* CPF
* Data de nascimento
* e-mail

No menu principal ao escolher a opção 1 criar conta, ele vai solicitar os dados do cliente para assim criar a conta, cada conta assim como o cliente, eles são criados com um número pre-determinado, o cliente possui um id_cliente que se inicia em 100 a partir do primeiro cadastro e o número da conta inicia em 1001, ambos vão sendo incrementados de 1 em 1, a cada nova conta e consequentemente a cada novo cliente. Nessa conta a cada criação, ela inicia com um limite de cheque especial de 200 e com o saldo zero, ou seja, caso já queira iniciar utilizando o cheque especial, este banco deixa, mas ficará com um saldo negativo de até o limite do cheque, que no caso são de R$ 200.00
Fora o módulo banco e as classes Conta e Cliente, o arquivo conta com um módulo helper, contendo algumas funções auxiliares de formatação, um módulo chamado menu, apenas para um melhor organização e um mais módulo de testes, para testarmos algumas implementações pontuais.
 

## Operações
Toda a lógica das operações estão praticamente implementadas na classe conta, mas todas as validações necessárias ao menos de início, são implementadas no módulo banco, fazer validações sem usar exceções deixa o código um pouco mais verboso e com muitas funções, futuramente essas validações serão implementadas utilizando o poder das exceções, essa parte ficará para aprimoramentos futuros. No módulo banco, ao iniciarmos o programa, imprimirá o menu de opções e a partir da escolha do usuário, as operações são chamadas e executadas, caso ele escolha alguma opção mas não exista contas cadastradas, o programa exibe a mensagem "ainda não existem contas cadastradas", para executar qualquer operação, faz-se necessário no mínimo termos um conta cadastrada.

### Criar conta
Essa opção solicitará os dados do cliente, como nome, cpf e etc, em seguida ela cria a conta do cliente no sistema. Essa é função que praticamente não tem validação, portanto, nome, cpf e email, como são strings, ele vai aceitar qualquer coisa que seja uma string, na data de nascimento, caso não esteja no padrão (dd/mm/aaaa) o programa dará um erro e parará a execução, esse tratamento será feito com exceções futuramente. Ao criar a conta ele exibe no painel conta criada com sucesso, contendo os dados principais da conta.

### Sacar
Com a conta cadastrada, podemos fazer qualquer operação e uma delas é o saque, como a conta é criada já com um limite de cheque especial de R$ 200,00, o usuário caso esteja no aperto pode sacar até esse valor, acima disso, a operação não permite. A função de saque ela valida se possui saldo e se o valor é maior que zero para poder efetuar a operaçao.

### Depositar
A operação de depósito primeiro valida se o valor é maior que zero e também assim como as outras, valida se a conta existe para poder efetuar a operação, em seguida pega o valor digitado e soma com o saldo da conta.

### Transferir
A operação faz todas as validações de saque e depósito, como também se as contas de origem e destino existem, por baixo dos panos e para simplificar, a função de transferir ela efetua um "saque" na conta de origem e faz um depósito na conta destino.

### Listar Contas
Operação básica e auxiliar, verifica se possui contas cadastradas, caso a resposta seja sim, ela varre a lista de contas e exibe o relatório na tela.

### Listar Clientes
Esta operação segue mesma lógica da função listar contas, a diferença é que ela percorre uma lista de clientes, que caso existam cadastrados, ele imprime o relatório na tela.

### Pesquisar Conta e Pesquisar cliente por número
Esas operações também possuem lógicas semelhantes. Primeiro elas validam se possuem contas ou clientes cadastrados, caso sim, validam se possuem contas ou clientes com número que foi solicitado, caso sim imprime-se os dados na tela, caso não, uma mensagem informado que não foram encontradas contas ou clientes com aquele número, é exibida.

### Imprimir Extrato
Essa operação deve listar todos os depósitos, saques e transferências realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, deve exibir a mensagem: **Não foram realizadas movimentações**
Os valores devem ser exibidos utilizando R$ xxx.xx.

**Ex:** 1750,20 = R$ 1750,20


! Este projeto visa melhorar e praticar o aprendizado nos estudo em python e talvez ajude alguém que precisa implementar uma lógica parecido ou algum projeto semelhante na universade ou nos estudos. Lembrando que nem todas as validações estão funcionando perfeitamente, essas melhorias serão aplicadas com o tempo.
