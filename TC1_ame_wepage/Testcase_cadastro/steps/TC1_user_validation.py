from behave import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Import os foi usado para gerar print na tela, uma vez que nunca usei BDD.
import os

@given('Acessa a pagina principal pelo navegador')
def openweb(context):
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
def pageurlcheck(context):
    # verifica se esta dentro da pagina correta de teste
    check_page = context.driver.current_url
    assert "http://automationpractice.com/index.php" in check_page
    time.sleep(1)


@then('Clica sobre o botao Sign In')
def botaosign(context):
    context.driver.find_element_by_xpath("//a[@class='login']").click()
    time.sleep(1)


@then('Clica sobre o campo de email')
def emailcheck(context):
    context.driver.find_element_by_xpath("//body[@id='authentication']").click()
    time.sleep(2)


@then('Digita seu e-mail "{email}" de acesso')
def emailtext(context, email):
    context.driver.find_element_by_xpath("//input[@id='email_create']").send_keys(email)
    time.sleep(4)


@then('Clica no botao Create an account')
def botaocreated(context):
    context.driver.find_element_by_xpath("//form[@id='create-account_form']//span[1]").click()
    time.sleep(3)


@then('Verifca se a mensagem de alerta de conta existente e gerado')
def messagecheck(context):
    time.sleep(5)
    # This is a message that can print in the console --but need to use  {behave --no-capture TC1_user.feature} in
    # the command line print(context.driver.find_element_by_xpath("//li[contains(text(),'An account using this email
    # address has already be')]").text)
    message_account_created = context.driver.find_element_by_xpath("//div[@id='create_account_error']").text
    assert "An account" in message_account_created


@then('Fecha navegador e gera relatorio')
def closebrowser(context):
    time.sleep(2)
    context.driver.close()
