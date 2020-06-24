@ECHO OFF
ECHO Congratulations! Your batch file executed successfully.
ECHO Your test will running now...
REM behave --no-capture --junit TC1_02_login_branco.feature
REM behave -f allure_behave.formatter:AllureFormatter -o allure-results TC1_02_login_branco.feature
behave --junit TC1_02_login_branco.feature