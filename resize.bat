@echo off

::echo Do Early Deck...
::set "SRC=D:\StateOfSiege Normandy\MANUAL NEW CARD IMAGES\NEW STYLE CARDS\EARLY"
::set "DEST=D:\StateOfSiege Normandy\MANUAL NEW CARD IMAGES\PRINTER-READY DECK"

::echo Do Mid Deck...
::set "SRC=D:\StateOfSiege Normandy\MANUAL NEW CARD IMAGES\NEW STYLE CARDS\MID"
::set "DEST=D:\StateOfSiege Normandy\MANUAL NEW CARD IMAGES\PRINTER-READY DECK"


echo Do Late Deck...
set "SRC=D:\StateOfSiege Normandy\MANUAL NEW CARD IMAGES\NEW STYLE CARDS\LATE"
set "DEST=D:\StateOfSiege Normandy\MANUAL NEW CARD IMAGES\PRINTER-READY DECK"

if not exist "%DEST%" mkdir "%DEST%"

for %%F in ("%SRC%\*.png") do (
    magick "%%F" -filter Lanczos -resize 1125x1575! "%DEST%\%%~nF.png"
)

echo.
echo Finished!
pause