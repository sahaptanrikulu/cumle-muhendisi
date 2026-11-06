@echo off
chcp 65001 >nul
title Cümle Mühendisi — Metin Denetim Aracı

echo ===============================================================================
echo                   C Ü M L E   M Ü H E N D İ S İ   v 2 . 0
echo          Türkçe Yapay Zeka ve Cümle Mimarisi Denetleyicisi
echo ===============================================================================
echo.

if "%~1"=="" goto no_file

echo [BILGI] Denetlenen Dosya: %~1
echo.
python scripts\detect_tr_ai.py "%~1"
goto finish

:no_file
echo [?] Bir metin dosyasini (.txt veya .md) bu pencerenin uzerine surukleyip birakin
echo     veya dosya yolunu yazip ENTER tusuna basin.
echo.
echo     (Not: Gorsel arayuz icin klasordeki "arayuz.html" dosyasina cift tiklayabilirsiniz.)
echo.
set /p filepath="Dosya yolu: "
if "%filepath%"=="" goto finish

echo.
python scripts\detect_tr_ai.py %filepath%

:finish
echo.
echo ===============================================================================
echo Islem tamamlandi. Pencereyi kapatmak icin herhangi bir tusa basin.
pause >nul
