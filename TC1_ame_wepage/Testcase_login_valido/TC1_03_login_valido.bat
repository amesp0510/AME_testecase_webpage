@ECHO OFF
ECHO Congratulations! Your batch file executed successfully.
ECHO Your test will running now...
REM behave --no-capture --junit TC1_03_login_valido.feature
REM behave -f allure_behave.formatter:AllureFormatter -o allure-results TC1_03_login_valido.feature
behave --junit TC1_03_login_valido.feature