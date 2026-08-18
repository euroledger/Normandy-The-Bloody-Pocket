$input = "FORTIFIED VILLAGES +1.png"
$output = "FORTIFIED VILLAGES +1 BLEED.png"

magick $input -set option:orig_w "%w" -set option:orig_h "%h" -bordercolor none -border 1x1 -alpha set -channel RGBA -separate +channel -write mpr:source +delete

magick $input -virtual-pixel edge -set option:extent_w "%[fx:w*1.3138889]" -set option:extent_h "%[fx:h*1.3138889]" -gravity center -background none -extent "%[fx:w*1.3138889]x%[fx:h*1.3138889]" $output