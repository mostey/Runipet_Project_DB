@echo off
chcp 65001 > nul
rem --------------------------------------------------
rem 1) 기존 가상환경 제거(선택적)
rem 2) 가상환경 생성 및 활성화
rem 3) pip 업그레이드 및 라이브러리 설치
rem --------------------------------------------------

set ROOT_DIR=%~dp0..

if exist "%ROOT_DIR%venv" (
    echo [!] 기존 가상환경(venv) 제거 중...
    rmdir /s /q "%ROOT_DIR%venv"
)

echo [1/3] 가상환경 생성 중...
python -m venv "%ROOT_DIR%venv"

echo [2/3] 가상환경 활성화 중...
call "%ROOT_DIR%venv\Scripts\activate.bat"

echo [3/3] pip 업그레이드 및 라이브러리 설치 중...
python -m pip install --upgrade pip
pip install -r "%~dp0requirements.txt"

echo 가상환경 및 의존성 설치 완료.
pause