$input = "Fortified Villages +1.png"
$output = "Fortified Villages +1 BLEED.png"
magick "$input" -virtual-pixel edge -set option:extent_w "%[fx:w*1.3138889]" -set option:extent_h "%[fx:h*1.3138889]" -gravity center -background none -extent "%[fx:w*1.3138889]x%[fx:h*1.3138889]" "$output"