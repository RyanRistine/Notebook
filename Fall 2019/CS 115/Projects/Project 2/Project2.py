"""
Program: Matching Game
Author: Stephen Case
Description: This project is a simple memory matching game with various images.
"""
from match_graphics import *


def shuffle_cards():
    # shuffle images array
    shuffle(images)

    # positions 0-11 will be our "paired" images
    pairedImages = images[:12]

    # position 12 will be our "extra" image
    extraImage = images[12]

    # duplicate each instance in pairedImages, creating pairs
    pairedImages *= 2

    # add extra image to the end
    pairedImages.append(extraImage)

    # shuffle the list again
    shuffle(pairedImages)

    # using list comprehension, populate the cards array
    cards = [pairedImages[i * 5:(i + 1) * 5] for i in range(5)]

    # ^^^^ explanation ^^^^
    # list comprehension works by taking an output expression and input sequence
    # in our case, we want a 2D array with each inner array being a length of 5.
    # our "output statement" is pairedImages[i * 5:(i + 1) * 5] --
    # which uses i to calculate which chunk of 5 it should take
    # for example, if i = 0, it would take pairedImages[0:5] aka the first 5 elements in out list
    # i = 1 would take paired images [5,10] which is the next five

    return cards


def show_card(win, card_name, i, j):
    if i >= 0 and i < 5 and j >= 0 and j < 5:

        # Draw a rectangle with a yellow border of line width 5
        # at the location associated with card (i,j)
        x = XMARGIN + (CARD_WIDTH * i)
        y = YMARGIN + (CARD_HEIGHT * j)

        x2 = x + CARD_WIDTH
        y2 = y + CARD_HEIGHT

        #draw the rectangle
        r = Rectangle(Point(x,y), Point(x2,y2))
        r.setFill("LightGreen")
        r.setOutline("Yellow")
        r.setWidth(5)
        r.draw(win)

        # shift the point since the picture is drawn from the center
        x += CARD_WIDTH/2
        y += CARD_HEIGHT/2

        # draw the image
        card = Image(Point(x,y), card_name)
        card.draw(win)

    return


def hide_card(win, i, j):
    '''
    Takes the window and cards and hides the card at row i and column j.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    '''

    x = XMARGIN + (CARD_WIDTH * i)
    y = YMARGIN + (CARD_HEIGHT * j)

    x2 = x + CARD_WIDTH
    y2 = y + CARD_HEIGHT

    # draw the rectangle
    r = Rectangle(Point(x, y), Point(x2, y2))
    r.setFill("LightGreen")
    r.setOutline("Yellow")
    r.setWidth(5)
    r.draw(win)

    return


def mark_card(win, i, j):
    '''
    Takes the window and cards and marks the card at row i and column j
    with a red X.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    '''

    # TODO (Final): finish this function as described
    return


def get_col(x):
    '''
    Takes the x-coordinate value and returns the column.
    If the x coordinate is outside the board, returns -1.

    TODO (Final): document the parameters and return value
    '''

    if x > XMARGIN and x < BOARD_WIDTH - XMARGIN:
        return int((x - XMARGIN) // CARD_WIDTH)
    else:
        return -1

def lolok(y):
    '''
    Takes the y-coordinate value and returns the row.
    If the y-coordinate is outside the board, returns -1.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    '''

    if y > YMARGIN and y < BOARD_HEIGHT -YMARGIN:
        return int((y - YMARGIN) // CARD_HEIGHT)
    else:
        return -1

def cardsMatch(cards, c1, c2):
    return cards[c1[0]][c1[1]] == cards[c2[0]][c2[1]]

def differentPositions(p1,p2):
    return p1[0] != p2[0] or p1[1] != p2[1]

def pickCard(win):
    click = win.getMouse()
    selection = (get_col(click.x), lolok(click.y))
    if (selection[0] >= 0 and selection[1] >= 0):
        return selection
    else:
        return pickCard(win)

def cardName(cards, x):
    return cards[x[0]][x[1]]



def main():
    '''
    TODO (Final): describe how your main function works.
    '''

    # generate game window
    win = create_board()

    # shuffle the cards
    cards = shuffle_cards()

    # draw the 5x5 board with the cards on it
    for i in range(5):
        for j in range(5):
            # For Checkpoint A, we place them face-up
            #show_card(win, cards[i][j], i, j)
            # For Checkpoint B, edit to place them face-down
            hide_card(win, i, j)

    # TODO (Checkpoint B): implement the below logic


    # until we win:
        # get a mouse click
        # figure out which card was clicked
        # if this is a 'first pick':
            # show the card
        # else, if this is a 'second pick':
            # show the card
            # wait 1 second
            # if we have a 'matched pair':
                # mark both pairs as matched (Final Code)
            # else:
                # hide both cards
    won = False
    prevSelection = (0,0)
    firstPick = True
    matches = []

    while not won:
        selection = pickCard(win)
        if not firstPick and selection == prevSelection:
            selection = pickCard(win)
        if firstPick:
            show_card(win, cardName(cards,selection), selection[0], selection[1])
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
