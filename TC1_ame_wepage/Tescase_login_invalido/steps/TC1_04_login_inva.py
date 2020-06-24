from behave import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Import os foi usado para gerar print na tela, uma vez que nunca usei BDD.
import os


@given('Acessa a pagina principal pelo navegador')
def webpageone(context):
    # here you can add your path for Chromedriver in case you have your path
    # context.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    # My Chromedriver located in Environment windows by default.
    chrome_options = Options()
    # para teste com navegador aberto, comente a linha abaixo
    chrome_options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.get("http://automationpractice.com/index.php")
    time.sleep(2)
    print(".......................................................")


@when('Verifica se a pagina esta correta')
def webapgecheck(context):
    # verifica se esta dentro da pagina correta de teste
    check_page = context.driver.current_url
    assert "http://automationpractice.com/index.php" in check_page
    time.sleep(1)


@then('Clica sobre o botao Sign In')
def botaosign(context):
    context.driver.find_element_by_xpath("//a[@class='login']").click()
    time.sleep(1)


@then('Clica sobre o campo de email de conta cadastrada')
def emailconta(context):
    context.driver.find_element_by_xpath("//input[@id='email']").click()
    time.sleep(1)


@then('Digita seu e-mail "{email}" de acesso')
def emailtex(context, email):
    context.driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
    time.sleep(4)


@then('Cilca sobre o campo de senha')
def senhafield(context):
    context.driver.find_element_by_xpath("//input[@id='passwd']").click()
    time.sleep(1)


@then('Digita a senha no campo indicado "{password}"')
def digitaconta(context, password):
    context.driver.find_element_by_xpath("//input[@id='passwd']").send_keys(password)
    time.sleep(1)


@then('Clica no Botao Sign IN')
def botao_signin_green(context):
    context.driver.find_element_by_xpath("//p[@class='submit']//span[1]").click()
    time.sleep(1)


@then('Verifica se mensagem de erro foi exibida')
def mensagemembranco(context):
    message_email_blank = context.driver.find_element_by_xpath("//li[contains(text(),'Invalid email address.')]").text
    assert "Invalid email" in message_email_blank


@then('Fecha navegador e gera relatorio')
def closebrowser(context):
    time.sleep(2)
    context.driver.close()
