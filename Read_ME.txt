Vinicius Miranda de Pinho

2020 - Junho  - Versao 0001


Para executar os testes nesta pasta eu recomendo:


Windows 10


Pycharm PyCharm 2020.1.2 (Community Edition)
Build #PC-201.7846.77, built on June 1, 2020
Runtime version: 11.0.7+10-b765.53 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Windows 10 10.0
GC: ParNew, ConcurrentMarkSweep
Memory: 1981M
Cores: 8


Python 3.8
pip 20.1.1


behave - 1.2.6.
Selenium 3.141.0



Allure Report ---

Baixe a versao 2.13.1 zip
Instalar em C:
Colocar o bin folder como path (envorimental windows)
https://github.com/allure-framework/allure2/releases

Para rodar o servidor, abra um cmd e execute o commado 

allure serve "path da pasta do report aonde rodou o teste aonde rodou o teste."
https://docs.qameta.io/allure/

https://pypi.org/project/allure-behave/





1 - Passo - Voce precisa do chromedrive compativel com seu navegador

2 - Passo - Pycharm ou terminal do Windows voce pode executar a batch nesta pasta nome : TC1_user_validation

3 - Passo - os commandos dentro da Bath sao --no-capture (imprimir no terminal) --junit(gerar um relatorio XML, confesso que nao gostei nada deste report, mas ele contem tudo que precisa entao mantive)


Nota: Devido a minha internet ruim eu coloquei varios atrasos (time.sleep) entre as linhas, caso nao queira esperar tanto pode remover ou diminuir desde que saiba que isso afeta a establidade do teste.

Eu fiz os teste no Windows e acredito que a unica diferenca para o Linux sera o destino das pastas, caso queira rodar Linux me avise ou por favor veja a estrutura das pastas.


Nota2 - Para executar no Chrome tem uma mensagem chata que aparece no inicio do teste (linha de comando), o problema e do Google e ficaram de resolver na proxima versao.


Note3 para o Teste case 1 TC1 se quiser testar com navegador, precisa comentar a linha 16, caso fique aberto o jenkins reprova de forma aleatoria.


Nota4 - Todos os reports que tentei usar no BDD me deram problema, ele nao cancela toda a saida do console e no caso do allure alem de ser complicado olhar o relatorio ele cancela os steps.
Para usar o alluere entre no arquivo TC1_user_validation e remove o comentario do allure que o report sera gerado.



