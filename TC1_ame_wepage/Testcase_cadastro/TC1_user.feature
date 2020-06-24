Feature: Test case Cadastro  - Usuario fara uma tentativa de Sign In para
    acessar a conta e em seguida digita seu email e pressiona
    botao para create account e espera uma mensagem de alerta para conta ja criada.


  Scenario: Verifica se ja possui conta criada no site atraves do e-mail
    Given Acessa a pagina principal pelo navegador
    When Verifica se a pagina esta correta
    Then Clica sobre o botao Sign In
    Then Clica sobre o campo de email
    Then Digita seu e-mail "vinicius.mpinho@gmail.com" de acesso
    Then Clica no botao Create an account
    Then Verifca se a mensagem de alerta de conta existente e gerado
    And Fecha navegador e gera relatorio
