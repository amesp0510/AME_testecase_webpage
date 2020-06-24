@ECHO OFF
ECHO Congratulations! Your batch file executed successfully.
ECHO Your test will running now...
REM behave --no-capture --junit TC1_04_login_inva
REM behave -f allure_behave.formatter:AllureFormatter -o allure-results TC1_04_login_inva
behave --junit TC1_04_login_inva.feature