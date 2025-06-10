@echo off
call .venv\Scripts\activate
echo %VIRTUAL_ENV%
echo starting server...
timeout /t 2 >nul

flask --app app run --debug

call .venv\Scripts\deactivate