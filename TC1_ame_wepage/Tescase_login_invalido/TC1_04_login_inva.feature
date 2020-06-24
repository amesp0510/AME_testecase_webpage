Feature: Test case Login em Invalido- Usuario fara uma tentativa de Sign In para
      acessar a conta em seguida deve preencher os campos de usuario
      cadastrado com email e senha e verifica se login falhou

  Scenario: Verifica se ja possui conta criada no site atraves do e-mail e senha
    Given Acessa a pagina principal pelo navegador
    When Verifica se a pagina esta correta
    Then Clica sobre o botao Sign In
    Then Clica sobre o campo de email de conta cadastrada
    Then Digita seu e-mail "meunomeehojuara@cabra" de acesso
    Then Cilca sobre o campo de senha
    Then Digita a senha no campo indicado "11333444"
    Then Clica no Botao Sign IN
    Then Verifica se mensagem de erro foi exibida
    And Fecha navegador e gera relatorio
