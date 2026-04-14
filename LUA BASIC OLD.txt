-- GUID Configuration WOOF 88888
zoneGUID      = "58c86e"
midDeckGUID   = "7434f2"
lateDeckGUID  = "eb14ea"

card1GUID     = "d547bc"
card2GUID     = "5ac114"
card20GUID    = "975d05"
card37GUID    = "eb305b"

dummyGUID     = "d8c9e0"

drawCount = 0
shuffleUsed = false

function onSave()
    return JSON.encode({
        drawCount = drawCount,
        shuffleUsed = shuffleUsed
    })
end

function onLoad(saved_data)
    if saved_data ~= "" then
        local data = JSON.decode(saved_data)
        drawCount = data.drawCount or 0
        shuffleUsed = data.shuffleUsed or false
    else
        shuffleUsed = false
    end

    math.randomseed(os.time())
    self.setColorTint({1,1,1,0})
    self.setLock(true)
    createButtons()
end

function createButtons()
    self.clearButtons()

    -- Draw button
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

    -- Shuffle button (only before first use)
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

function getDeckFromZone()
    local zone = getObjectFromGUID(zoneGUID)
    if not zone then return nil end
    for _, obj in ipairs(zone.getObjects()) do
        if obj.tag == "Deck" or obj.tag == "Card" then return obj end
    end
    return nil
end

function findCardByGUID(deck, guid)
    for i, obj in ipairs(deck.getObjects()) do
        if obj.guid == guid then return i - 1 end
    end
    return nil
end

-- =========================
-- MOVE DUMMY TO BOTTOM
-- =========================

function moveDummyToBottom(retries)
    retries = retries or 0

    local deck = getDeckFromZone()
    if not deck or deck.tag ~= "Deck" then return end

    local objects = deck.getObjects()
    if not objects then return end

    for i, obj in ipairs(objects) do
        local guid = obj.guid or obj.GUID

        if guid == dummyGUID then
            if i == #objects then return end

            deck.takeObject({
                index = i - 1,
                position = {0, -50, 0},
                smooth = false,
                callback_function = function(card)
                    Wait.frames(function()
                        local d = getDeckFromZone()
                        if d and d.tag == "Deck" then
                            d.putObject(card)
                        end
                    end, 1)
                end
            })
            return
        end
    end

    if retries < 5 then
        Wait.time(function()
            moveDummyToBottom(retries + 1)
        end, 0.5)
    end
end

-- =========================
-- REMOVE DUMMY
-- =========================

function removeDummyFromDeck(retries)
    retries = retries or 0

    local deck = getDeckFromZone()
    if not deck or deck.tag ~= "Deck" then return end

    local objects = deck.getObjects()
    if not objects then return end

    for i, obj in ipairs(objects) do
        local guid = obj.guid or obj.GUID

        if guid == dummyGUID then
            deck.takeObject({
                index = i - 1,
                position = {0, -50, 0},
                smooth = false,
                callback_function = function(card)
                    if card then card.destruct() end
                end
            })
            return
        end
    end

    if retries < 5 then
        Wait.time(function()
            removeDummyFromDeck(retries + 1)
        end, 0.5)
    end
end

-- =========================
-- MERGE FUNCTION
-- =========================

function mergeAdditionalDeck(newDeckGUID, newName, broadcastMsg)
    local newDeck = getObjectFromGUID(newDeckGUID)
    local zone = getObjectFromGUID(zoneGUID)
    
    if newDeck and zone then
        broadcastToAll("Merging " .. newName .. "...", {0, 1, 1})
        newDeck.setPositionSmooth(zone.getPosition() + Vector(0, 4, 0))
        
        Wait.time(function()
            local deck = getDeckFromZone()
            if deck and deck.tag == "Deck" then
                deck.setName(newName)
                
                deck.shuffle()
                Wait.time(function() deck.shuffle() end, 0.2)
                Wait.time(function() deck.shuffle() end, 0.4)

                if newDeckGUID == lateDeckGUID then
                    -- Reset draw count for new phase
                    drawCount = 0

                    Wait.time(function()
                        removeDummyFromDeck()
                    end, 1.5)
                else
                    Wait.time(function()
                        moveDummyToBottom()
                    end, 1.5)
                end

                broadcastToAll(broadcastMsg, {0, 1, 0})
            end
        end, 2.5)
    end
end

-- =========================
-- DRAW FUNCTION
-- =========================

function drawCard(_, _, alt_click)
    if alt_click then return end
    local deck = getDeckFromZone()
    if not deck then
        broadcastToAll("No cards found!", {1,0,0})
        return
    end

    local targetPos = self.getPosition() + Vector(10, 2, 0)
    drawCount = drawCount + 1

    if deck.tag == "Deck" then
        local targetGUID = nil
        if drawCount == 1 then targetGUID = card1GUID
        elseif drawCount == 2 then targetGUID = card2GUID end

        if targetGUID then
            local idx = findCardByGUID(deck, targetGUID)
            if idx ~= nil and idx >= 0 then
                deck.takeObject({
                    index = idx,
                    position = targetPos,
                    rotation = {0,180,0},
                    smooth = true
                })
                return
            end
        end
        
        local deckObjs = deck.getObjects()
        local topCardGUID = deckObjs[1].guid 
        
        deck.takeObject({position=targetPos, rotation={0,180,0}, smooth=true})
        
        if topCardGUID == card20GUID then
            Wait.time(function() mergeAdditionalDeck(midDeckGUID, "Early-Mid Deck", "Mid Deck cards merged and shuffled") end, 1.5)
        elseif topCardGUID == card37GUID then
            Wait.time(function() mergeAdditionalDeck(lateDeckGUID, "Full Campaign Deck", "Late Deck cards merged and shuffled") end, 1.5)
        end
    else
        if deck.guid == card20GUID then 
            Wait.time(function() mergeAdditionalDeck(midDeckGUID, "Early-Mid Deck", "Mid Deck merged") end, 1.5) 
        elseif deck.guid == card37GUID then
            Wait.time(function() mergeAdditionalDeck(lateDeckGUID, "Full Campaign Deck", "Late Deck merged") end, 1.5)
        end
        deck.setPositionSmooth(targetPos + Vector(0,2,0), false, true)
        deck.setRotation({0,180,0})
    end
end

-- =========================
-- SHUFFLE FUNCTION
-- =========================

function shuffleDeck()
    local deck = getDeckFromZone()
    if deck and deck.tag == "Deck" then
        deck.shuffle()
        drawCount = 0
        broadcastToAll("Deck Shuffled and Seeds Reset.", {1,1,0})

        shuffleUsed = true
        createButtons()

        Wait.time(function()
            moveDummyToBottom()
        end, 1.5)
    end
end