@echo off
echo =========================================
echo Travel Memories サーバーを起動しています...
echo =========================================

cd "C:\Users\kaika\OneDrive - kaiyodai.ac.jp\Programming\japan_trip_project"

echo 仮想環境をオンにしています...
call venv\Scripts\activate

echo ブラウザを開きます...
start http://127.0.0.1:8000/

echo サーバーを起動します！（※この黒い画面はアプリを使っている間は閉じないでください）
python manage.py runserver

pause