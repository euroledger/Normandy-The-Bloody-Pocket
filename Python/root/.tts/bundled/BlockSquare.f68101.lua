-- =========================
-- DEBUG
-- =========================
DEBUG = true

function dbg(msg)
    if DEBUG then
        print("[DEBUG] " .. msg)
    end
end

-- =========================
-- GUIDS
-- =========================
mainDeckGUID = "15501e"
midDeckGUID  = "39a856"
lateDeckGUID = "46e30b"

card1GUID  = "fbe6b6"
card2GUID  = "18a65f"
card20GUID = "8778ed"
card37GUID = "ad0b65"
dummy1GUID = "321021"
dummy2GUID = "e1ab05"

-- =========================
-- LOAD / SAVE
-- =========================
function onSave()
    return JSON.encode({
        drawCount = drawCount,
        shuffleUsed = shuffleUsed,
        lastCardGUID = lastCardGUID
    })
end

function onLoad(saved_data)
    if saved_data ~= "" then
        local data = JSON.decode(saved_data)
        drawCount = data.drawCount or 0
        shuffleUsed = data.shuffleUsed or false
        lastCardGUID = data.lastCardGUID
    end

    self.setLock(true)
    createButtons()

    Wait.frames(moveDummiesToBottom, 60)
end

-- =========================
-- BUTTONS
-- =========================
function createButtons()
    self.clearButtons()

    self.createButton({
        label="Draw",
        click_function="drawCard",
        function_owner=self,
        position={0,0.6,0},
        rotation={0,180,0},
        width=1200,
        height=500,
        font_size=250
    })

    if not shuffleUsed then
        self.createButton({
            label="Shuffle",
            click_function="shuffleDeck",
            function_owner=self,
            position={0,0.6,-1},
            rotation={0,180,0},
            width=1200,
            height=500,
            font_size=250
        })
    end
end

-- =========================
-- GET DECK
-- =========================
function getDeck()
    local obj = getObjectFromGUID(mainDeckGUID)
    if obj then return obj end

    if lastCardGUID then
        return getObjectFromGUID(lastCardGUID)
    end

    return nil
end

-- =========================
-- MOVE DUMMIES
-- =========================
function moveDummiesToBottom()
    local deck = getDeck()
    if not deck or deck.tag ~= "Deck" then return end

    local pos = deck.getPosition() + Vector(0,-5,0)

    local function moveDummy(guid, callback)
        deck.takeObject({
            guid = guid,
            position = pos,
            smooth = false,
            callback_function = function(card)
                if card then
                    Wait.frames(function()
                        local d = getDeck()
                        if d and d.tag == "Deck" then
                            d.putObject(card)
                        end
                        if callback then callback() end
                    end, 1)
                else
                    if callback then callback() end
                end
            end
        })
    end

    moveDummy(dummy1GUID, function()
        moveDummy(dummy2GUID)
    end)
end

-- =========================
-- REMOVE DUMMIES
-- =========================
function removeDummies()
    local deck = getDeck()
    if not deck or deck.tag ~= "Deck" then return end

    local pos = deck.getPosition() + Vector(0,-5,0)

    local function removeDummy(guid, callback)
        deck.takeObject({
            guid = guid,
            position = pos,
            smooth = false,
            callback_function = function(card)
                if card then card.destruct() end
                if callback then callback() end
            end
        })
    end

    removeDummy(dummy1GUID, function()
        removeDummy(dummy2GUID)
    end)
end

-- =========================
-- DRAW
-- =========================
function drawCard(_,_,alt_click)
    if alt_click then return end

    local deck = getDeck()
    if not deck then return end

    local pos = self.getPosition() + Vector(10,2,0)
    drawCount = drawCount + 1

    if deck.tag == "Deck" then

        local objects = deck.getObjects()
        local deckSize = #objects

        local twoCardGUIDs = nil

        if deckSize == 2 then
            twoCardGUIDs = {}
            for _, obj in ipairs(objects) do
                table.insert(twoCardGUIDs, obj.guid)
            end
        end

        local targetGUID = nil
        if drawCount == 1 then targetGUID = card1GUID end
        if drawCount == 2 then targetGUID = card2GUID end

        if targetGUID then
            deck.takeObject({
                guid = targetGUID,
                position = pos,
                rotation = {0,180,0}
            })
            return
        end

        deck.takeObject({
            position = pos,
            rotation = {0,180,0},

            callback_function = function(card)
                if not card then return end

                local drawnGUID = card.getGUID()

                if twoCardGUIDs then
                    for _, g in ipairs(twoCardGUIDs) do
                        if g ~= drawnGUID then
                            lastCardGUID = g
                            break
                        end
                    end
                else
                    lastCardGUID = drawnGUID
                end

                if drawnGUID == card20GUID then
                    Wait.time(function()
                        mergeDeck(midDeckGUID, "Mid Deck merged")
                    end, 1)
                end

                if drawnGUID == card37GUID then
                    Wait.time(function()
                        mergeDeck(lateDeckGUID, "Late Deck merged")
                    end, 1)
                end
            end
        })

    elseif deck.tag == "Card" then
        dbg("FINAL CARD → simulated draw physics")

        -- lift slightly to engage physics
        deck.setPosition(deck.getPosition() + Vector(0,2,0))

        Wait.frames(function()
            deck.setPositionSmooth(pos)
            deck.setRotationSmooth({0,180,0})
        end, 1)
    end
end

-- =========================
-- MERGE
-- =========================
function mergeDeck(newDeckGUID, msg)
    local base = getDeck()
    local newDeck = getObjectFromGUID(newDeckGUID)

    if not base or not newDeck then return end

    local originalPos = base.getPosition()

    base.setPositionSmooth(originalPos)
    newDeck.setPositionSmooth(originalPos + Vector(0,3,0))

    Wait.time(function()

        if base.tag == "Card" then
            newDeck.putObject(base)
        else
            base.putObject(newDeck)
        end

        Wait.time(function()

            local finalDeck = getDeck()
            if not finalDeck then return end

            finalDeck.setPosition(originalPos)

            Wait.time(function()
                finalDeck.shuffle()

                Wait.time(function()
                    finalDeck.shuffle()

                    Wait.time(function()
                        moveDummiesToBottom()

                        if newDeckGUID == lateDeckGUID then
                            Wait.time(removeDummies, 1)
                        end
                    end, 0.5)

                end, 0.3)
            end, 0.5)

            broadcastToAll(msg, {0,1,0})

        end, 1)

    end, 1)
end

-- =========================
-- SHUFFLE
-- =========================
function shuffleDeck()
    local deck = getDeck()

    if deck and deck.tag == "Deck" then
        deck.shuffle()
        drawCount = 0
        lastCardGUID = nil

        shuffleUsed = true
        createButtons()

        Wait.time(moveDummiesToBottom, 1)
    end
end