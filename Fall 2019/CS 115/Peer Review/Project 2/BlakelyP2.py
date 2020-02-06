"""
Author: Preston Blakely
Class: CS115
Program: Project02
Description: This program creates a matching game in which the user must match pictures
together until all the pictures are uncovered.
"""
from match_graphics import *

e_list = []


def shuffle_cards():
    '''
    Generates a shuffled deck of cards. When done, cards[i][j] is the name
    of the card in row i and column j. It is a 5x5 grid comprised of 12
    card pairs and one extra card.
    '''
    # The idea of how we shuffle is the following:
    # (1) shuffle the images
    # (2) pick out 12 of the images (these are the ones that will be pairs)
    # (3) pick out the 'extra image' (this is the one that will have no pair)
    # (4) create a list with 2 of each pair and the extra image
    # (5) shuffle that list

    images_12 = images
    shuffle(images_12)
    images_12 = images[0:12]
    last_image = images[12]
    images_12.extend(images_12)
    images_12.append(last_image)
    shuffle(images_12)
    mouse = 0

    # use the list of these 25 shuffled cards to build a 5x5 array of cards
    cards = []
    for i in range(5):
        row = []
        for j in range(5):
            item = images_12[mouse]  # currently, array is the same card, over and over
            mouse += 1
            row.append(item)
        cards.append(row)
    return cards


def show_card(win, card_name, i, j):
    '''
    Shows the card at row i and column j in the 5x5 grid in the window.
    '''

    # Draw a rectangle with a yellow border of line width 5
    #  at the location associated with card (i,j)
    #  Ex: card (0,0) has upper-right corner (XMARGIN, YMARGIN) and
    #   lower-right corner (XMARGIN+CARD_WIDTH, YMARGIN+CARD_HEIGHT)
    # hide_card(win, i ,j)
    # Draw the image for card_name at the center of the rectangle.
    spot = Point(XMARGIN + (i * CARD_WIDTH), YMARGIN + (j * CARD_HEIGHT))
    deck = Image(Point(spot.x + CARD_HEIGHT / 2, spot.y + CARD_HEIGHT / 2), card_name)
    deck.draw(win)

    return


def hide_card(win, i, j):
    '''
    Takes the window and cards and hides the card at row i and column j.
    '''

    x = Point(XMARGIN + (j * CARD_WIDTH), YMARGIN + (i * CARD_HEIGHT))
    y = Point(XMARGIN + ((j + 1) * CARD_WIDTH), YMARGIN + (i + 1) * CARD_HEIGHT)
    rectangle_1 = Rectangle(x, y)
    rectangle_1.setFill('LightGreen')
    rectangle_1.setOutline('Yellow')
    rectangle_1.setWidth(5)
    rectangle_1.draw(win)

    return


def mark_card(win, i, j):
    '''
    Takes the window and cards and marks the card at row i and column j
    with a red X.
    '''

    mark1 = Point((j * CARD_WIDTH) + XMARGIN + 125, (i * CARD_HEIGHT) + YMARGIN)
    mark2 = Point((j * CARD_WIDTH) + XMARGIN, (i * CARD_HEIGHT) + YMARGIN + 125)
    mark3 = Point((j * CARD_WIDTH) + XMARGIN, (i * CARD_HEIGHT) + YMARGIN)
    mark4 = Point((j * CARD_WIDTH) + XMARGIN + 125, (i * CARD_HEIGHT) + YMARGIN + 125)
    xdraw1 = Line(mark1, mark2)
    xdraw1.setWidth(5)
    xdraw1.draw(win)
    xdraw1.setOutline('red')
    xdraw2 = Line(mark3, mark4)
    xdraw2.setWidth(5)
    xdraw2.draw(win)
    xdraw2.setOutline('red')

    return


def get_col(x):
    '''
    Takes the x-coordinate value and returns the column.
    If the x coordinate is outside the board, returns -1.
    '''

    if 0 < x < 25 or 650 < x < 675:
        return -1
    else:
        col = ((x - XMARGIN) // CARD_HEIGHT)
        return col


def get_row(y):
    '''
    Takes the y-coordinate value and returns the row.
    If the y-coordinate is outside the board, returns -1.
    '''

    if 0 < y < 25 or 650 < y < 675:
        return -1
    else:
        row = ((y - YMARGIN) // CARD_HEIGHT)
        return row


def main():
    '''
    iterates through loops and calls necessary functions to carry out
    the entire program
    '''

    # generate game window
    win = create_board()

    # shuffle the cards
    cards = shuffle_cards()

    # draw the 5x5 board with the cards on it
    for i in range(5):
        for j in range(5):
            # For Checkpoint A, we place them face-up
            hide_card(win, j, i)
            # For Checkpoint B, edit to place them face-down

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

    mouse = 0
    oc = 0
    pb = -10
    bp = -10
    ext = 0
    while ext == 0:
        c_point = win.getMouse()
        x_c_point = c_point.getX()
        y_c_point = c_point.getY()
        cj = int(get_col(x_c_point))
        ri = int(get_row(y_c_point))
        if cj == -1 or ri == -1 or (pb == cj and bp == ri) or e_list.__contains__(cards[cj][ri]):
            continue
        if mouse == 0:
            show_card(win, cards[cj][ri], cj, ri)
            oc = cards[cj][ri]
            pb = cj
            bp = ri
            mouse = 1
        else:
            show_card(win, cards[cj][ri], cj, ri)
            game_delay(1)
            if pb == cj and bp == ri:
                continue
            if cards[cj][ri] == oc:
                mark_card(win, ri, cj)
                mark_card(win, bp, pb)
                e_list.append(cards[cj][ri])
            else:
                hide_card(win, ri, cj)
                hide_card(win, bp, pb)
            mouse = 0
            if len(e_list) == 12:
                you_won(win)
                # if we got here, then we won
                # so, call the you_won function.
    win.getMouse()


main()