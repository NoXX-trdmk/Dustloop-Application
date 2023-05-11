import requests
from bs4 import BeautifulSoup
from enum import Enum


class MoveType(Enum):
    NormalMoves = 'Normal Moves'
    Unique = 'Unique Action'
    Uni = 'Universal Mechanics'
    SM = 'Special Moves'
    SA = 'Skybound Arts'


class Move:
    def __init__(self, FrameData, Description):
        self.FrameData = list(FrameData)
        self.Description = Description


class FrameData:
    def __init__(self, Name, Damage, Guard, Startup, Active, Recovery, OnBlock, OnHit, Invuln):
        self.Name = Name
        self.Damage = Damage
        self.Guard = Guard
        self.Startup = Startup
        self.Active = Active
        self.Recovery = Recovery
        self.OnBlock = OnBlock
        self.OnHit = OnHit
        self.Invuln = Invuln


URL = "https://www.dustloop.com/w/GBVS/Gran"
page = requests.get(URL)

# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

results = soup.find(id="bodyContent")
# print(results.prettify())

allMoves = results.find_all("section", class_="section-collapsible", id="section-collapsible-2")
allMoveTitles = results.find_all("span", class_="mw-headline")
allMoveDescriptions = results.find_all(class_="attack-info")
allMoveVersions = results.find_all(class_="field_Version")
allMoveDamage = results.find_all(class_="field_Damage")
allMoveGuard = results.find_all(class_="field_Guard")
allMoveStartup = results.find_all(class_="field_Startup")
allMoveActive = results.find_all(class_="field_Active")
allMoveRecovery = results.find_all(class_="field_Recovery")
allMoveOnBlock = results.find_all(class_="field_On-Block")
allMoveOnHit = results.find_all(class_="field_On-Hit")
allMoveInvul = results.find_all(class_="field_Invuln")

listofMovenames = list()
normalList = list()
listofDescriptions = list()
listofFrameDataDamage = list()
listofFrameDataGuard = list()
listofFrameDataStartup = list()
listofFrameDataActive = list()
listofFrameDataRecovery = list()
listofFrameDataOnblock = list()
listofFrameDataOnhit = list()
listofFrameDataInvul = list()
listofMoveVersion = list()

listofFrameData = list()

#




def getFrameData(moveName):
    match moveName.lower():
        case "c.l":
            name = moveName[0:len(moveName)-1] + moveName[len(moveName)-1:len(moveName)].upper()
            damage = allMoveDamage[1]
            guard = allMoveGuard[1]
            startup = allMoveStartup[1]
            active = allMoveActive[1]
            recovery = allMoveRecovery[1]
            onblock = allMoveOnBlock[1]
            onhit = allMoveOnHit[1]
            invul = allMoveInvul[1]

        case "c.m":
            name = moveName[0:len(moveName)-1] + moveName[len(moveName)-1:len(moveName)].upper()
            damage = allMoveDamage[3]
            guard = allMoveGuard[3]
            startup = allMoveStartup[3]
            active = allMoveActive[3]
            recovery = allMoveRecovery[3]
            onblock = allMoveOnBlock[3]
            onhit = allMoveOnHit[3]
            invul = allMoveInvul[3]
        case "c.h":
            name = moveName[0:len(moveName)-1] + moveName[len(moveName)-1:len(moveName)].upper()
            damage = allMoveDamage[5]
            guard = allMoveGuard[5]
            startup = allMoveStartup[5]
            active = allMoveActive[5]
            recovery = allMoveRecovery[5]
            onblock = allMoveOnBlock[5]
            onhit = allMoveOnHit[5]
            invul = allMoveInvul[5]
        case "auto-combo":
            name = "c.XX"
            damage = allMoveDamage[7]
            guard = allMoveGuard[7]
            startup = allMoveStartup[7]
            active = allMoveActive[7]
            recovery = allMoveRecovery[7]
            onblock = allMoveOnBlock[7]
            onhit = allMoveOnHit[7]
            invul = allMoveInvul[7]

            name2 = "c.XXX"
            damage2 = allMoveDamage[8]
            guard2 = allMoveGuard[8]
            startup2 = allMoveStartup[8]
            active2 = allMoveActive[8]
            recovery2 = allMoveRecovery[8]
            onblock2 = allMoveOnBlock[8]
            onhit2 = allMoveOnHit[8]
            invul2 = allMoveInvul[8]
        case "f.l":
            name = moveName[0:len(moveName)-1] + moveName[len(moveName)-1:len(moveName)].upper()
            damage = allMoveDamage[10]
            guard = allMoveGuard[10]
            startup = allMoveStartup[10]
            active = allMoveActive[10]
            recovery = allMoveRecovery[10]
            onblock = allMoveOnBlock[10]
            onhit = allMoveOnHit[10]
            invul = allMoveInvul[10]
        case "f.m":
            name = moveName[0:len(moveName)-1] + moveName[len(moveName)-1:len(moveName)].upper()
            damage = allMoveDamage[12]
            guard = allMoveGuard[12]
            startup = allMoveStartup[12]
            active = allMoveActive[12]
            recovery = allMoveRecovery[12]
            onblock = allMoveOnBlock[12]
            onhit = allMoveOnHit[12]
            invul = allMoveInvul[12]
        case "f.h":
            name = moveName[0:len(moveName)-1] + moveName[len(moveName)-1:len(moveName)].upper()
            damage = allMoveDamage[14]
            guard = allMoveGuard[14]
            startup = allMoveStartup[14]
            active = allMoveActive[14]
            recovery = allMoveRecovery[14]
            onblock = allMoveOnBlock[14]
            onhit = allMoveOnHit[14]
            invul = allMoveInvul[14]
        case "f.h":
            name = moveName[0:len(moveName)-1] + moveName[len(moveName)-1:len(moveName)].upper()
            damage = allMoveDamage[14]
            guard = allMoveGuard[14]
            startup = allMoveStartup[14]
            active = allMoveActive[14]
            recovery = allMoveRecovery[14]
            onblock = allMoveOnBlock[14]
            onhit = allMoveOnHit[14]
            invul = allMoveInvul[14]
        case "2l":
            name = moveName[0:len(moveName) - 1] + moveName[len(moveName) - 1:len(moveName)].upper()
            damage = allMoveDamage[16]
            guard = allMoveGuard[16]
            startup = allMoveStartup[16]
            active = allMoveActive[16]
            recovery = allMoveRecovery[16]
            onblock = allMoveOnBlock[16]
            onhit = allMoveOnHit[16]
            invul = allMoveInvul[16]
        case "2m":
            name = moveName[0:len(moveName) - 1] + moveName[len(moveName) - 1:len(moveName)].upper()
            damage = allMoveDamage[18]
            guard = allMoveGuard[18]
            startup = allMoveStartup[18]
            active = allMoveActive[18]
            recovery = allMoveRecovery[18]
            onblock = allMoveOnBlock[18]
            onhit = allMoveOnHit[18]
            invul = allMoveInvul[18]
        case "2h":
            name = moveName[0:len(moveName) - 1] + moveName[len(moveName) - 1:len(moveName)].upper()
            damage = allMoveDamage[20]
            guard = allMoveGuard[20]
            startup = allMoveStartup[20]
            active = allMoveActive[20]
            recovery = allMoveRecovery[20]
            onblock = allMoveOnBlock[20]
            onhit = allMoveOnHit[20]
            invul = allMoveInvul[20]
        case "2h":
            name = moveName[0:len(moveName) - 1] + moveName[len(moveName) - 1:len(moveName)].upper()
            damage = allMoveDamage[22]
            guard = allMoveGuard[22]
            startup = allMoveStartup[22]
            active = allMoveActive[22]
            recovery = allMoveRecovery[22]
            onblock = allMoveOnBlock[22]
            onhit = allMoveOnHit[22]
            invul = allMoveInvul[22]
        case"2u":
            name = moveName[0:len(moveName) - 1] + moveName[len(moveName) - 1:len(moveName)].upper()
            damage = allMoveDamage[22]
            guard = allMoveGuard[22]
            startup = allMoveStartup[22]
            active = allMoveActive[22]
            recovery = allMoveRecovery[22]
            onblock = allMoveOnBlock[22]
            onhit = allMoveOnHit[22]
            invul = allMoveInvul[22]
        case"j.u":
            name = moveName[0:len(moveName) - 1] + moveName[len(moveName) - 1:len(moveName)].upper()
            damage = allMoveDamage[24]
            guard = allMoveGuard[24]
            startup = allMoveStartup[24]
            active = allMoveActive[24]
            recovery = allMoveRecovery[24]
            onblock = allMoveOnBlock[24]
            onhit = allMoveOnHit[24]
            invul = allMoveInvul[24]

        case"5u":
            name = moveName[0:len(moveName) - 1] + moveName[len(moveName) - 1:len(moveName)].upper()
            damage = allMoveDamage[25]
            guard = allMoveGuard[25]
            startup = allMoveStartup[25]
            active = allMoveActive[25]
            recovery = allMoveRecovery[25]
            onblock = allMoveOnBlock[25]
            onhit = allMoveOnHit[25]
            invul = allMoveInvul[25]

            name2 = moveName[0:len(moveName) - 1] + moveName[len(moveName) - 1:len(moveName)].upper()
            damage2 = allMoveDamage[26]
            guard2 = allMoveGuard[26]
            startup2 = allMoveStartup[26]
            active2 = allMoveActive[26]
            recovery2 = allMoveRecovery[26]
            onblock2 = allMoveOnBlock[26]
            onhit2 = allMoveOnHit[26]
            invul2 = allMoveInvul[26]
        case"reginleiv":
            name = moveName
            damage = allMoveDamage[28]
            guard = allMoveGuard[28]
            startup = allMoveStartup[28]
            active = allMoveActive[28]
            recovery = allMoveRecovery[28]
            onblock = allMoveOnBlock[28]
            onhit = allMoveOnHit[28]
            invul = allMoveInvul[28]

            name2 = moveName
            damage2 = allMoveDamage[29]
            guard2 = allMoveGuard[29]
            startup2 = allMoveStartup[29]
            active2 = allMoveActive[29]
            recovery2 = allMoveRecovery[29]
            onblock2 = allMoveOnBlock[29]
            onhit2 = allMoveOnHit[29]
            invul2 = allMoveInvul[29]

            name3 = moveName
            damage3 = allMoveDamage[30]
            guard3 = allMoveGuard[30]
            startup3 = allMoveStartup[30]
            active3 = allMoveActive[30]
            recovery3 = allMoveRecovery[30]
            onblock3 = allMoveOnBlock[30]
            onhit3 = allMoveOnHit[30]
            invul3 = allMoveInvul[30]
        case _:
            print("")



    match moveName.lower():
        case "5u":
            frameData = FrameData(name, damage, guard, startup, active, recovery, onblock, onhit, invul)
            frameData2 = FrameData(name2, damage2, guard2, startup2, active2, recovery2, onblock2, onhit2, invul2)
            frameDataList = list()
            frameDataList.append(frameData)
            frameDataList.append(frameData2)
            return frameDataList
        case "auto-combo":
            frameData = FrameData(name, damage, guard, startup, active, recovery, onblock, onhit, invul)
            frameData2 = FrameData(name2, damage2, guard2, startup2, active2, recovery2, onblock2, onhit2, invul2)
            frameDataList = list()
            frameDataList.append(frameData)
            frameDataList.append(frameData2)
            return frameDataList
        case "reginleiv":
            frameData = FrameData(name, damage, guard, startup, active, recovery, onblock, onhit, invul)
            frameData2 = FrameData(name2, damage2, guard2, startup2, active2, recovery2, onblock2, onhit2, invul2)
            frameData3 = FrameData(name3,damage3, guard3, startup3, active3, recovery3, onblock3, onhit3, invul3)
            frameDataList = list()
            frameDataList.append(frameData)
            frameDataList.append(frameData2)
            frameDataList.append(frameData3)
            return frameDataList
        case _:
            try:
                frameData = FrameData(name, damage, guard, startup, active, recovery, onblock, onhit, invul)
            except Exception as e:
                raise Exception("wrong input")
            frameDataList = list()
            frameDataList.append(frameData)
            return frameDataList


# getFrameData("auto-combo")
def moveData(moveName):
    for moves in allMoveDescriptions:
        moveDescription = moves.find("p")
        try:
            listofDescriptions.append(moveDescription.text)
        except:
            continue
    # calls the getFrameData Function

    moveFrameData = getFrameData(moveName)
    match moveName.lower():
        case "c.l":
            description = listofDescriptions[0]
        case "c.m":
            description = listofDescriptions[1]
        case "c.h":
            description = listofDescriptions[2]
        case "auto-combo":
            description = listofDescriptions[3]
        case "f.l":
            description = listofDescriptions[4]
        case "f.m":
            description = listofDescriptions[5]
        case "f.h":
            description = listofDescriptions[6]
        case "2l":
            description = listofDescriptions[7]
        case "2m":
            description = listofDescriptions[8]
        case "2h":
            description = listofDescriptions[9]
        case "2u":
            description = listofDescriptions[10]
        case "j.l":
            description = listofDescriptions[11]
        case "j.m":
            description = listofDescriptions[12]
        case "j.h":
            description = listofDescriptions[13]
        case "j.u":
            description = listofDescriptions[14]
        case "5u":
            description = listofDescriptions[15]
        case "throw":
            description = listofDescriptions[16]
        case "air-throw":
            description = listofDescriptions[17]
        case "oh":
            description = listofDescriptions[18]
        case "throw":
            description = listofDescriptions[19]
        case "reginleiv":
            description = listofDescriptions[20]



    newMove = Move(moveFrameData, description)
    for frameData in moveFrameData:
        print(frameData.Name + "\n",
              frameData.Damage.text,
              frameData.Guard.text,
              frameData.Startup.text,
              frameData.Active.text,
              frameData.Recovery.text,
              frameData.OnBlock.text,
              frameData.OnHit.text,
              frameData.Invuln.text + "\n")
    print(newMove.Description)


moveData(input("Give an input "))


# Gets the Normals on the Site
# for NormalTitle in allMoveTitles:
#     if len(NormalTitle.text) <= 3 or NormalTitle.text == "Auto Combo":
#         normalList.append(NormalTitle.text)
#     #print(normalList)
#
# for moveDescriptions in allMoveDescriptions:
#     description = moveDescriptions.find("p")
#     print(description.text)
