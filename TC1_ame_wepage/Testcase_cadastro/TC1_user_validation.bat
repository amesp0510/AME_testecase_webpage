@ECHO OFF
ECHO Congratulations! Your batch file executed successfully.
ECHO Your test will running now...
REM behave --no-capture --junit TC1_user.feature
REM behave -f allure_behave.formatter:AllureFormatter -o allure-results TC1_user.feature
behave --no-capture --junit TC1_user.feature
