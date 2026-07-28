@echo off

echo Do Early Deck...
set "SRC=D:\StateOfSiege Normandy\MANUAL NEW CARD IMAGES\NEW STYLE CARDS\EARLY"
set "DEST=D:\StateOfSiege Normandy\VASSAL COMPONENTS\CARDS\NEW-EARLY"

::echo Do Mid Deck...
::set "SRC=D:\StateOfSiege Normandy\MANUAL NEW CARD IMAGES\NEW STYLE CARDS\MID"
::set "DEST=D:\StateOfSiege Normandy\VASSAL COMPONENTS\CARDS\NEW-MID"


::echo Do Late Deck...
::set "SRC=D:\StateOfSiege Normandy\MANUAL NEW CARD IMAGES\NEW STYLE CARDS\LATE"
::set "DEST=D:\StateOfSiege Normandy\VASSAL COMPONENTS\CARDS\NEW-LATE"

if not exist "%DEST%" mkdir "%DEST%"

for %%F in ("%SRC%\*.png") do (
    magick "%%F" -filter Lanczos -resize 400x600! "%DEST%\%%~nF.png"
    magick "%%F" -filter Lanczos -resize 1000x1500! "%DEST%\%%~nF-LARGE.png"
)

echo.
echo Finished!
pause