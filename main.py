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


URL = "https://www.dustloop.com/w/GBVS/Gran"
page = requests.get(URL)

# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

results = soup.find(id="bodyContent")
# print(results.prettify())

allMoves = results.find_all("section", class_="section-collapsible", id="section-collapsible-2")
allMoveTitles = results.find_all("span", class_="mw-headline")
allMoveDescriptions = results.find_all("div", class_="attack-info-body")

listofmovenames = list()
normalList = list()
listofdescriptions = list()

# print(allMoveDescriptions)
# for moves in allMoveDescriptions:
#     moveFrameData = moves.find("p")
#     # print(moveFrameData.text)
def moveData(moveName):
    # newMove = Move(moveName, )
    for moves in allMoveDescriptions:
        moveDescription = moves.find("p")
        try:
            listofdescriptions.append(moveDescription.text)
        except:
            continue




    print(listofdescriptions)
moveData("c.M")
# Gets the Normals on the Site
# for NormalTitle in allMoveTitles:
#     if len(NormalTitle.text) <= 3 or NormalTitle.text == "Auto Combo":
#         normalList.append(NormalTitle.text)
#     #print(normalList)
#
# for moveDescriptions in allMoveDescriptions:
#     description = moveDescriptions.find("p")
#     print(description.text)
