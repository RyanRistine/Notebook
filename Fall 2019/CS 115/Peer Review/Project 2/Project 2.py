"""
Program: CS 115 Project 2 Matching Game
Author: Grant Reynolds
Description: TODO
"""
from match_graphics import *


def shuffle_cards():
    '''
    Generates a shuffled deck of cards. When done, cards[i][j] is the name
    of the card in row i and column j. It is a 5x5 grid comprised of 12
    card pairs and one extra card.

    TODO (Final): document the parameters and return value
    '''
    # TODO (Checkpoint A): implement the below logic
    #

    shuffle(images)
    list_cards = []
    for j in range(12):
        list_cards.append(images[j])
        list_cards.append(images[j])
    list_cards.append(images[12])
    shuffle(list_cards)

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
    Shows the card at row i and column j in the 5x5 grid in the window.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    '''

    if i >= 0 and i < 5 and j >= 0 and j < 5:


        x = XMARGIN + (CARD_WIDTH * i)
        y = YMARGIN + (CARD_HEIGHT * j)

        x2 = x + CARD_WIDTH
        y2 = y + CARD_HEIGHT
        margin = 5
        # create rectangle
        r = Rectangle(Point(x, y), Point(x2, y2))
        r.setFill("LightGreen")
        r.setOutline("Yellow")
        r.setWidth(margin)
        r.draw(win)

        x = x + CARD_WIDTH / 2
        y = y + CARD_HEIGHT / 2

        # draw the image
        card = Image(Point(x, y), card_name)
        card.draw(win)

    return


def hide_card(win, i, j):
    x_Val = XMARGIN + (CARD_WIDTH * i)
    y_Val = YMARGIN + (CARD_HEIGHT * j)

    x_Val_2 = x_Val + CARD_WIDTH
    y_Val_2 = y_Val + CARD_HEIGHT

    '''
    Takes the window and cards and hides the card at row i and column j.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    '''
    # draw the rectangle
    rect = Rectangle(Point(x_Val, y_Val), Point(x_Val_2, y_Val_2))
    rect.setFill("LightGreen")
    rect.setOutline("Yellow")
    rect.setWidth(5)
    rect.draw(win)

    return


def mark_card(win, i, j):

    return


def get_row(y):

    if y > YMARGIN and y < BOARD_HEIGHT - YMARGIN:
        return int((y - YMARGIN) // CARD_HEIGHT)
    else:
        return -1


def get_col(x):

    if x > XMARGIN and x < BOARD_WIDTH - XMARGIN:
        return int((x - XMARGIN) // CARD_WIDTH)
    else:
        return -1


def cardsMatch(cards, c1, c2):
    return cards[c1[0]][c1[1]] == cards[c2[0]][c2[1]]


def differentPositions(p1, p2):
    return p1[0] != p2[0] or p1[1] != p2[1]


def cardName(cards, x):
    return cards[x[0]][x[1]]


def pickCard(win):
    click = win.getMouse()
    selection = (get_col(click.x), get_row(click.y))
    if (selection[0] >= 0 and selection[1] >= 0):
        return selection
    else:
        return pickCard(win)


def main():

    # generate game window
    win = create_board()

    # shuffle the cards
    cards = shuffle_cards()

    for i in range(5):
        for j in range(5):
            hide_card(win, i, j)

    won = False
    prevSelection = (0, 0)
    firstPick = True
    matches = []

    while not won:
        selection = pickCard(win)
        if not firstPick and selection == prevSelection:
            selection = pickCard(win)
        if firstPick:
            show_card(win, cardName(cards, selection), selection[0], selection[1])
        else:
            show_card(win, cardName(cards, selection), selection[0], selection[1])
            game_delay(1)

            currentCard = cardName(cards, selection)
            prevCard = cardName(cards, prevSelection)

            if differentPositions(selection, prevSelection) and cardsMatch(cards, selection, prevSelection):
                print('Incorrect')
                if not currentCard in matches:
                    matches.append(currentCard)
                    print('MATCH!!')
                    print('Matched pairs: ', matches)
            else:
                # hide both (if statements prevent matches pairs from hiding)
                if not currentCard in matches:
                    hide_card(win, selection[0], selection[1])
                if not prevCard in matches:
                    hide_card(win, prevSelection[0], prevSelection[1])

        firstPick = not firstPick
        prevSelection = selection

        # once you have 12 matches, you won!
        if len(matches) == 12:
            won = True
            you_won(win)


main()
