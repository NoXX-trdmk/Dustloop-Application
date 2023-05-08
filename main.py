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
    def __init__(self, MoveName, FrameData, Description):
        self.MoveName = MoveName
        self.FrameData = FrameData
        self.Description = Description


class FrameData:
    def __init__(self, Damage, Guard, Startup, Active, Recovery, OnBlock, OnHit, Invuln):
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


# Gets the individual frame data for each attribute of the FrameData Class Type
def getFrameData(moveName):
    for moves in allMoveDescriptions:
        try:
            # moveVersion = moves.find_previous(class_="field_Version")
            moveDamage = moves.find_previous(class_="field_Damage")
            moveGuard = moves.find_previous(class_="field_Guard")
            moveStartup = moves.find_previous(class_="field_Startup")
            moveActive = moves.find_previous(class_="field_Active")
            moveRecovery = moves.find_previous(class_="field_Recovery")
            moveOnblock = moves.find_previous(class_="field_On-Block")
            moveOnhit = moves.find_previous(class_="field_On-Hit")
            moveInvul = moves.find_previous(class_="field_Invuln")

            listofFrameDataDamage.append(moveDamage)
            listofFrameDataGuard.append(moveGuard)
            listofFrameDataStartup.append(moveStartup)
            listofFrameDataActive.append(moveActive)
            listofFrameDataRecovery.append(moveRecovery)
            listofFrameDataOnblock.append(moveOnblock)
            listofFrameDataOnhit.append(moveOnhit)
            listofFrameDataInvul.append(moveInvul)


        except:
            continue
    match moveName:
        case "c.L":
            damage = listofFrameDataDamage[1]
            guard = listofFrameDataGuard[1]
            startup = listofFrameDataStartup[1]
            active = listofFrameDataActive[1]
            recovery = listofFrameDataRecovery[1]
            onblock = listofFrameDataOnblock[1]
            onhit = listofFrameDataOnhit[1]
            invul = listofFrameDataInvul[1]

        case _:
            damage = listofFrameDataDamage[2]
            guard = listofFrameDataGuard[2]
            startup = listofFrameDataStartup[2]
            active = listofFrameDataActive[2]
            recovery = listofFrameDataRecovery[2]
            onblock = listofFrameDataOnblock[2]
            onhit = listofFrameDataOnhit[2]
            invul = listofFrameDataInvul[2]

    frameData = FrameData(damage, guard, startup, active, recovery, onblock, onhit, invul)
    return frameData


def moveData(moveName):
    for moves in allMoveDescriptions:
        moveDescription = moves.find("p")
        try:
            listofDescriptions.append(moveDescription.text)
        except:
            continue
    # calls the getFrameData Function

    moveFrameData = getFrameData(moveName)
    match moveName:
        case "c.L":
            description = listofDescriptions[0]
        case _:
            description = listofDescriptions[1]
    newMove = Move(moveName, moveFrameData, description)

    print(newMove.MoveName,
          "\n",
          newMove.FrameData.Damage.text,
          newMove.FrameData.Guard.text,
          newMove.FrameData.Startup.text,
          newMove.FrameData.Active.text,
          newMove.FrameData.Recovery.text,
          newMove.FrameData.OnBlock.text,
          newMove.FrameData.OnHit.text,
          newMove.FrameData.Invuln.text, "\n",
          newMove.Description)


moveData(input())
# moveData("c.L")


# Gets the Normals on the Site
# for NormalTitle in allMoveTitles:
#     if len(NormalTitle.text) <= 3 or NormalTitle.text == "Auto Combo":
#         normalList.append(NormalTitle.text)
#     #print(normalList)
#
# for moveDescriptions in allMoveDescriptions:
#     description = moveDescriptions.find("p")
#     print(description.text)
