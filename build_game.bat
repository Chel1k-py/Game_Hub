@echo off
REM === Сборка игры BeatShooter ===

REM Переход в папку с проектом
cd /d "%~dp0"

REM Удаляем старые сборки
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del main.spec 2>nul

REM Собираем exe
pyinstaller --onefile --noconsole main.py

REM Копируем ресурсы
xcopy img dist\img /E /I /Y
copy stats.json dist\ /Y

echo.
echo === Сборка завершена! ===
echo Файл: dist\main.exe
pause