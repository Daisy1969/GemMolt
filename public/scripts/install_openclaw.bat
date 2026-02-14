@echo off
echo Checking for Node.js...
node -v >nul 2>&1
if %errorlevel% neq 0 (
    echo Node.js is not installed. Please install Node.js from https://nodejs.org/
    start https://nodejs.org/
    pause
    exit /b 1
)
echo Installing OpenClaw...
call npm install -g openclaw
if %errorlevel% neq 0 (
    echo Failed to install OpenClaw. Please try running as Administrator.
    pause
    exit /b 1
)
echo Starting OpenClaw Onboarding Wizard...
openclaw onboard
pause
