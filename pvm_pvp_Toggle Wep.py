# Toggle alternate wep by MatsaMilla
# 

leftHand = Player.GetItemOnLayer('LeftHand')
rightHand = Player.GetItemOnLayer('RightHand')

if Misc.CheckSharedValue(Player.Name + 'wep'):
    tempwep = Items.FindBySerial(Misc.ReadSharedValue(Player.Name + 'wep'))
    if tempwep:
        wep = tempwep.Serial
    else:
        Player.HeadMessage(66,'Target New Wep')
        wep = Target.PromptTarget()
        Misc.SetSharedValue(Player.Name + 'wep', wep)
        Player.HeadMessage(66, 'Wep Set')
else:
    Player.HeadMessage(66,'Target Wep')
    wep = Target.PromptTarget()
    Misc.SetSharedValue(Player.Name + 'wep', wep)
    Player.HeadMessage(66, 'Wep Set')
    

if rightHand:
    if rightHand.Serial == wep:
        Items.Move(wep,Player.Backpack.Serial,0)
        
if leftHand:
    if leftHand.Serial == wep:
        Items.Move(wep,Player.Backpack.Serial,0)
    else:
        Items.Move(leftHand.Serial,Player.Backpack.Serial,0)
        Misc.Pause(600)
        Player.EquipItem(wep)
else:
    Player.EquipItem(wep)
