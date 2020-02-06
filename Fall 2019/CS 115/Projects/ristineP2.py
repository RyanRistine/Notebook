"""
Program: CS 115 Project 2 Matching Game
Author: Ryan Ristine
Description: Simple matching game in which the user makes two selections on a
             game board, if the two selections are a match the cards remain
             face up. Once the user makes 12 matches the user has won.
"""
from match_graphics import *

def shuffle_cards():
    '''
    Creates shuffled list of cards and returns it
    '''
    shuffle(images)
    list_cards = []
    for j in range(12):
        list_cards.append(images[j])
        list_cards.append(images[j])
    list_cards.append(images[12])
    shuffle(list_cards)
    # shuffles for a second time so that the single card isn't always at the end
    cards = []
    placeholder = 0
    for i in range(5):
        row = []
        for j in range(5):
            item = list_cards[placeholder]
            placeholder = placeholder + 1
            row.append(item)
        cards.append(row)
    return cards

def show_card(win, card_name, i, j):
    '''
    Draws the card in the window at point i,j
    '''
    if i >= 0 and j >= 0 and i < 5 and j < 5:
        xInit = XMARGIN + (CARD_WIDTH * i)
        yInit = YMARGIN + (CARD_HEIGHT * j)
        xSec = xInit + CARD_WIDTH
        ySec = yInit + CARD_HEIGHT

        rect = Rectangle(Point(xInit,yInit), Point(xSec,ySec))
        rect.setFill("LightGreen")
        rect.setOutline("Yellow")
        rect.setWidth(5)
        rect.draw(win)

        xInit += CARD_WIDTH/2
        yInit += CARD_HEIGHT/2
        cardImg = Image(Point(xInit,yInit), card_name)
        cardImg.draw(win)
    return

def hide_card(win, i, j):
    '''
    Hides the card in the window that is located
    at the provided row (i) and column (j)
    '''
    xInit = XMARGIN + (CARD_WIDTH * i)
    yInit = YMARGIN + (CARD_HEIGHT * j)

    ySec = yInit + CARD_HEIGHT
    xSec = xInit + CARD_WIDTH

    rect = Rectangle(Point(xInit, yInit), Point(xSec, ySec))
    rect.setFill("LightGreen")
    rect.setOutline("Yellow")
    rect.setWidth(5)
    rect.draw(win)
    return

def mark_card(win, i, j):
    '''
    To be completely honest I ran out of time to implement this
    '''
    return

def get_row(y):
    '''
    Returns row at given y-coordinate.
    A y-coordinate outside the board will return -1.

    '''
    if y > YMARGIN and y < BOARD_HEIGHT - YMARGIN:
        return int((y - YMARGIN) // CARD_HEIGHT)
    else:
        return -1

def get_col(x):
    '''
    returns column at given x coordinate.
    if x coordinate is outside the board returns -1

    '''
    if x > XMARGIN and x < BOARD_WIDTH - XMARGIN:
        return int((x - XMARGIN) // CARD_WIDTH)
    else:
        return -1

def cardsMatch(cards, c1, c2):
    '''
    Returns Boolean that is dependent on if the cards match
    '''
    return cards[c1[0]][c1[1]] == cards[c2[0]][c2[1]]
        # compares first selection to second selection, if they are a match
        # returns True if not returns False

def differentPositions(p1,p2):
    '''
    returns whether or not the selection and the previous selection are
    at different positions
    '''
    return p1[0] != p2[0] or p1[1] != p2[1]

def cardName(cards, x):
    '''
    returns the name of the card at the provided point x
    '''
    return cards[x[0]][x[1]]

def pickCard(win):
    '''
    Gets the user click and returns which card
    the click corresponds to
    '''
    choice = win.getMouse()
    choiceLoc = (get_col(choice.x), get_row(choice.y))
    if (choiceLoc[0] >= 0 and choiceLoc[1] >= 0):
        return choiceLoc
    else:
        return pickCard(win)


def main():
    '''
    Creates the gameboard, shuffles the cards then
    hides them. Intializes variables, then interates
    while the user makes selections, checks the selections
    to see if they're matches, if they are the pair gets
    appended to the matchList list, once there are 12 matches the loop
    stops iterating and the user has won.
    '''

    win = create_board()
    cards = shuffle_cards()

    for i in range(5):
        for j in range(5):
            hide_card(win, i, j)
    won = False
    lastPick = (0,0)
    firstPick = True
    matchList = []

    while not won:
        # iterates infintely until won is True, which changes when the len of the
        # list of matches reaches 12
        selected = pickCard(win)
        if not firstPick and selected == lastPick:
            selected = pickCard(win)
        if firstPick:
            show_card(win, cardName(cards,selected), selected[0], selected[1])
        else:
            show_card(win, cardName(cards, selected), selected[0], selected[1])
            game_delay(1)

            chosenCard = cardName(cards, selected)
            lastCard = cardName(cards, lastPick)

            if differentPositions(selected, lastPick) and cardsMatch(cards, selected, lastPick):
                print('Incorrect')
                if not chosenCard in matchList:
                    matchList.append(chosenCard)
                    print('MATCH!!')
                    print('Matched pairs: ', matchList)
            else:
                if not chosenCard in matchList:
                    hide_card(win, selected[0], selected[1])
                if not lastCard in matchList:
                    hide_card(win, lastPick[0], lastPick[1])

        firstPick = not firstPick
        lastPick = selected

        if len(matchList) == 12:
            won = True
            you_won(win)
main()
