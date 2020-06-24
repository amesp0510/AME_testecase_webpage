Feature: Test case Login Valido - Usuario fara uma tentativa de Sign In para
      acessar a conta em seguida deve preencher os campos de usuario
      cadastrado com email e senha e verifica se login foi bem sucedido

  Scenario: Verifica se ja possui conta criada no site atraves do e-mail e senha
    Given Acessa a pagina principal pelo navegador
    When Verifica se a pagina esta correta
    Then Clica sobre o botao Sign In
    Then Clica sobre o campo de email de conta cadastrada
    Then Digita seu e-mail "vinicius.mpinho@gmail.com" de acesso
    Then Cilca sobre o campo de senha
    Then Digita a senha no campo indicado "123mudar"
    Then Clica no Botao Sign IN
    Then Verifica se esta dentro a pagina da conta e verifica icone my account
    Then Clica no botao de logout para ver se estava logado
    And Fecha navegador e gera relatorio