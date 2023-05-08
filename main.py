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
    def __init__(self, MoveName, FrameData, Description, Image):
        self.MoveName = MoveName
        self.FrameData = FrameData
        self.Description = Description
        self.Image = Image


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
listofFrameData = list()

for moves in allMoveDescriptions:

    try:
        moveDamage = moves.find("tbody", class_="field_Damage")
        print(moveDamage.text)
    except:
        continue

# def moveData(moveName):
#
#     for moves in allMoveDescriptions:
#         moveDescription = moves.find("p")
#         try:
#             listofDescriptions.append(moveDescription.text)
#         except:
#             continue
#     description = ""
#     match moveName:
#         case "c.L":
#            description = listofDescriptions(1)
#         case _:
#            description = listofDescriptions(2)
# newMove = Move(moveName, ,description )


# moveData("c.M")


# Gets the Normals on the Site
# for NormalTitle in allMoveTitles:
#     if len(NormalTitle.text) <= 3 or NormalTitle.text == "Auto Combo":
#         normalList.append(NormalTitle.text)
#     #print(normalList)
#
# for moveDescriptions in allMoveDescriptions:
#     description = moveDescriptions.find("p")
#     print(description.text)
