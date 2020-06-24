from behave import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Import os foi usado para gerar print na tela, uma vez que nunca usei BDD.
import os


@given('Acessa a pagina principal pelo navegador')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Acessa a pagina principal pelo navegador')


@when(Verifica se a pagina esta correta')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Verifica se a pagina esta correta')


@then('Clica sobre o botao Sign In')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Clica sobre o botao Sign In')


@then('Clica sobre o campo de email de conta cadastrada')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Clica sobre o campo de email de conta cadastrada')


@then('Digita seu e-mail "vinicius.mpinho@gmail.com" de acesso')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Digita seu e-mail "vinicius.mpinho@gmail.com" de acesso')


@then('Cilca sobre o campo de senha')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Cilca sobre o campo de senha')


@then('Digita a senha no campo indicado "123mudar"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Digita a senha no campo indicado "123mudar"')


@then('Verifica se esta dentro a pagina da conta e verifica icone my account')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verifica se esta dentro a pagina da conta e verifica icone my account')


@then('Clica no botao de logout para ver se estava logado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Clica no botao de logout para ver se estava logado')


@then('Fecha navegador e gera relatorio')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Fecha navegador e gera relatorio')