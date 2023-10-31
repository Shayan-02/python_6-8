from random import randint
from sys import platform
from os import system
from time import sleep

correctness = False
while not correctness:
    size = input("Enter room size: ")
    if size.isdigit():
        size = int(size)
        correctness = True
    else:
        print("Please enter a correct number.")
state = {
    "status": "Moving...",
    "clearCommand": "cls" if platform == "win32" else "clear",
    "reverse": False,
    "boxes": [],
    "canvas": "",
    "agentLocation": [],
}


def makeBoxes(boxesStatus: list = None) -> list:
    global size
    boxes = []
    for i in range(size):
        boxes.append([])
        for j in range(size):
            boxes[i].append(randint(0, 1))
    return boxes


def makeCanvas(boxes: list, agentLocation: list) -> str:
    global state
    canvas = ""
    for i in range(len(boxes)):
        canvas += "\n"
        for j in range(len(boxes[i])):
            canvas += (
                "● "
                if i == agentLocation[0] and j == agentLocation[1]
                else "x "
                if boxes[i][j] == 1
                else "  "
            )
    return canvas


def moveAgent(currentLocation: list = None) -> list:
    global state
    if currentLocation == []:
        newLocation = [0, 0]
    else:
        newLocation = [currentLocation[0], currentLocation[1]]
        if currentLocation[0] == (size - 1) and currentLocation[1] == (
            0 if size % 2 == 0 else (size - 1)
        ):
            state["status"] = "Finished."
        else:
            if currentLocation[1] == (size - 1) and state["reverse"] == False:
                newLocation[0] = currentLocation[0] + 1
                newLocation[1] = currentLocation[1]
                state["reverse"] = True
            elif currentLocation[1] == 0 and state["reverse"] == True:
                newLocation[0] = currentLocation[0] + 1
                newLocation[1] = currentLocation[1]
                state["reverse"] = False
            elif currentLocation[1] <= (size - 1) and state["reverse"] == True:
                newLocation[0] = currentLocation[0]
                newLocation[1] = currentLocation[1] - 1
            elif currentLocation[1] >= 0 and state["reverse"] == False:
                newLocation[0] = currentLocation[0]
                newLocation[1] = currentLocation[1] + 1
    return newLocation


def changeStatus(currentStatus: str, boxesStatus: list, agentLocation: list) -> str:
    if currentStatus != "Finished.":
        if currentStatus == "Moving...":
            newStatus = "Checking..."
        elif currentStatus == "Checking...":
            if boxesStatus[agentLocation[0]][agentLocation[1]] == 1:
                newStatus = "Cleaning..."
            else:
                newStatus = "Moving..."
        elif currentStatus == "Cleaning...":
            boxesStatus[agentLocation[0]][agentLocation[1]] = 0
            newStatus = "Moving..."
    else:
        newStatus = currentStatus
    return newStatus


def action() -> None:
    global state
    sleep(1)
    system(state["clearCommand"])
    state["agentLocation"] = (
        moveAgent(state["agentLocation"])
        if state["status"] == "Moving..."
        else state["agentLocation"]
    )
    state["boxes"] = makeBoxes() if state["boxes"] == [] else state["boxes"]
    canvas = makeCanvas(state["boxes"], state["agentLocation"])
    print(
        "Room size: " + str(size) + "x" + str(size),
        canvas,
        "Status: " + state["status"],
        sep="\n",
    )
    state["status"] = changeStatus(
        state["status"], state["boxes"], state["agentLocation"]
    )


def initialize() -> None:
    global state
    while state["status"] != "Finished.":
        action()


initialize()
