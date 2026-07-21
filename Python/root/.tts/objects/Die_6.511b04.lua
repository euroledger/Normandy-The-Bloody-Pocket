whiteDie = getObjectFromGUID("511b04")
greenDie = getObjectFromGUID("7d7f52")

function onScriptingButtonDown(index, playerColor)
    if index == 1 then
        whiteDie.randomize()
    elseif index == 2 then
        greenDie.randomize()
    end
end