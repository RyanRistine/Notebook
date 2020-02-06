"""
Program: Project 2 Card Matching Game.
Author: Aaron Thistlethwaite
Description: There are 12 matches hidden within 25 card locations.
             Find all 12 matches to win so that only the extra card remains.
             You will reveal one card at a time.
             Once two cards are revealed they will stay revealed if they are the same.
             However, if they are different they will both become hidden again.
"""
from match_graphics import *
from graphics import *

def shuffle_cards():
    '''
    Generates a shuffled deck of cards. When done, cards[i][j] is the name
    of the card in row i and column j. It is a 5x5 grid comprised of 12
    card pairs and one extra card.
    '''

    shuffle(images) # (1) shuffle the images
    my_list = [] # Creates new list
    for i in range (12): # loop to create list
        my_list.append(images[i]) # (2) pick out 12 of the images (these are the ones that will be pairs)
        my_list.append(images[i]) # second set of images
    my_list.append(images[12]) # (3) pick out the 'extra image' and add it to list
    shuffle(my_list) # reshuffle the list

    # use the list of these 25 shuffled cards to build a 5x5 array of cards
    cards = []
    temp = 0
    for i in range(5): # create the array for the cards (25 spots)
        row = []
        for j in range(5):
            item = my_list[temp]
            temp += 1  # currently, array is the same card, over and over
            row.append(item) # add to row
        cards.append(row) # add to cards
    return cards


def show_card(win, card_name, i, j):
    '''
    Shows the card at row i and column j in the 5x5 grid in the window.
    '''

    #card location information

    top_left_x = i - (CARD_WIDTH / 2) # finds top left x value
    top_left_y = j - (CARD_HEIGHT / 2) # finds top left y value
    top_left_point = Point(top_left_x, top_left_y) # combining the previous 2 lines
    bottom_right_x = i + (CARD_WIDTH / 2) # calculates x for bottom right
    bottom_right_y = j + (CARD_HEIGHT / 2) # calculates y for bottom right
    bottom_right_point = Point(bottom_right_x, bottom_right_y) # combining the above two lines
    background = Rectangle(top_left_point, bottom_right_point) # creates rectangle
    background.setFill('light green') # each square is filled in by green
    background.setOutline('yellow') # creates the borders of the squares
    background.setWidth(5) # sets the width of the borders
    background.draw(win) # draws rectangles with the borders in the requested locations
    card = (Image(Point(i, j), card_name)) # tells where to draw/place the image
    card.draw(win) # draws the image
    return


def hide_card(win, i, j):
    '''
    Takes the window and cards and hides the card at row i and column j.
    '''

    # This code is extremely similar to the show card function

    top_left_x = i - (CARD_WIDTH / 2) # top left of specified location
    top_left_y = j - (CARD_HEIGHT / 2) # top left of specified location
    top_left_point = Point(top_left_x, top_left_y)  # combining the previous 2 lines
    bottom_right_x = i + (CARD_WIDTH / 2) # bottom right of specified location
    bottom_right_y = j + (CARD_HEIGHT / 2) # bottom right of specified location
    bottom_right_point = Point(bottom_right_x, bottom_right_y)  # combining the above two lines
    background = Rectangle(top_left_point, bottom_right_point) # creates the backround rectangle
    background.setFill('light green') # sets color of rectangle
    background.setOutline('yellow') # reprints the outline
    background.setWidth(5) # clarifies outline width
    background.draw(win) # draws in the window given
    return

def mark_card(win, i, j):
    '''
    Takes the window and cards and marks the card at row i and column j
    with a red X.
    '''

    # Creation of line top left to bottom right
    top_leftX = XMARGIN + (i * CARD_WIDTH) # finds the x value of top left
    top_leftY = YMARGIN + (j * CARD_HEIGHT) # finds the y value of top left
    top_left = Point(top_leftX, top_leftY) # sets the top left point
    bottom_rightX = XMARGIN + ((i+1) * CARD_WIDTH) # finds the x value of bottom right
    bottom_rightY = YMARGIN + ((j+1) * CARD_HEIGHT) # finds the y value of bottom right
    bottom_right = Point(bottom_rightX, bottom_rightY) # sets the bottom right point
    line1 = Line(top_left, bottom_right) # creates line between two points
    line1.setFill('red') # sets line color
    line1.setOutline('red') # outlines the line to add thickness
    line1.setWidth(3) # sets thickness of line
    line1.draw(win) # draws line

    # Creation of line top right to bottom left
    # repeats the above block of code for the second line
    top_rightX = XMARGIN + ((i+1) * CARD_WIDTH)
    top_rightY = YMARGIN + (j * CARD_HEIGHT)
    top_right = Point(top_rightX, top_rightY)
    bottom_leftX = XMARGIN + (i * CARD_WIDTH)
    bottom_leftY = YMARGIN + ((j+1) * CARD_HEIGHT)
    bottom_left = Point(bottom_leftX, bottom_leftY)
    line2 = Line(top_right, bottom_left)
    line2.setFill('red')
    line2.setOutline('red')
    line2.setWidth(3)
    line2.draw(win)

    return


def get_col(x):
    '''
    Takes the x-coordinate value and returns the column.
    If the x coordinate is outside the board, returns -1.
    '''

    x = int((x - XMARGIN) // (CARD_WIDTH)) # calculates the x coordinate 0-4
    if x > 4: # checks right side
        return -1
    if x < 0: # checks left side
        return -1
    return (x) # return x as an int for board coordinates and marking cards


def get_row(y):
    '''
    Takes the y-coordinate value and returns the row.
    If the y-coordinate is outside the board, returns -1.
    '''
    y = int((y - YMARGIN) // (CARD_HEIGHT)) # calculates the y coordinate 0-4
    if y > 4: # checks bottom edge
        return -1
    if y < 0: # checks top edge
        return -1
    return (y) # return y as an int for board coordinates


def main():
    '''
    This function operates in a series of simple steps.
    (1): Calls the create_board function and creates a board in the window.
    (2): Shuffles the list of cards and creates a separate list to track matches.
    (3): Draws the board itself with the cards hidden.
    (4): Starts a while loop for the user to input two clicks.
    (5): Receives the users click.
    (6): Calculates where the user clicked using the get_col and get_row functions.
    (7): Checks to see if the click is in a valid location, and proceeds accordingly.
    (8): If the click is valid the image is shown.
    (9): The code then proceeds to a nested while loop for the second click.
    (10): Assuming the second click also passes the check it will reveal both images.
    (11a): If the images do not match in the cards list they will flip and steps 5-10 will repeat.
    (11b): If the images match in the cards list they will remain flipped and add the locations to the matches list.
    (12): The match_pairs counter will increase by 1 and the user will be returned to step 5 to click on another image.
    (13): Returns user to step 5 to repeat steps 5-12 until the match_pairs counter reaches 12.
    (14): Once match_pairs counter reaches 12 call you_won function.
    '''

    # generate game window
    win = create_board()
    # shuffle the cards
    cards = shuffle_cards()
    matches = []
    # draws the 5x5 board with the cards on it
    for i in range(5):
        for j in range(5):
            hide_card(win, (i) * CARD_WIDTH + XMARGIN + CARD_WIDTH / 2, (j) * CARD_HEIGHT + YMARGIN + CARD_HEIGHT / 2)
    match_pairs = 0 # set win condition variable
    while match_pairs < 12: # Upon reaching 12 matching pairs you win.
        click = win.getMouse() # initiates the first click
        x = get_col(click.x) # find the x coordinate on the grid
        y = get_row(click.y) # find the y coordinate on the grid
        for items in matches: # Tests if the card selected is part of an existing match.
            if items == (x, y):
                y = -1
                x = -1
        if x == -1: # check if x value is invalid
            continue
        if y == -1: # check if y value is invalid
            continue
        x1 = int(x) # assign the x coordinate to a new variable for later use
        y1 = int(y) # assign the y coordinate to a new variable for later use
        #reveal card one
        show_card(win, cards[x1][y1], (x) * CARD_WIDTH + XMARGIN + CARD_WIDTH / 2, (y) * CARD_HEIGHT + YMARGIN + CARD_HEIGHT / 2)
        game_delay(1) # one second delay between selection of card one and card two.
        # second card selection below (a near repeat of part one)
        x2 = int(x1) # set new x variable to old x variable to access the while loop
        y2 = int(y1) # set new y variable to old while variable to access the loop
        while x2 == x1 and y1 == y2: # loop will continue until a unique 2nd click is selected
            click = (win.getMouse()) # click 2
            x = get_col(click.x) # find x value of click 2
            y = get_row(click.y) # find y value of click 2
            for items in matches: # Tests if the card selected is part of an existing match.
                if items == (x, y): # same check as click one
                    y = -1
                    x = -1
            if y == -1:
                continue
            if x == -1:
                continue
            if x1 == x and y1 == y: # tests if the first click is the same as the second click.
                continue
            x2 = int(x) # save 2nd x to new variable
            y2 = int(y) # save 2nd y to new variable
            # Reveal card 2
            show_card(win, cards[x2][y2], (x) * CARD_WIDTH + XMARGIN + CARD_WIDTH // 2, (y) * CARD_HEIGHT + YMARGIN + CARD_HEIGHT // 2)
            if cards[x1][y1]!=cards[x2][y2]: # if cards do not match
                game_delay(1) # gives the user 1 second to view both cards
                # Flips both cards over
                hide_card(win, (x1) * CARD_WIDTH + XMARGIN + CARD_WIDTH / 2, (y1) * CARD_HEIGHT + YMARGIN + CARD_HEIGHT / 2)
                hide_card(win, (x2) * CARD_WIDTH + XMARGIN + CARD_WIDTH / 2, (y2) * CARD_HEIGHT + YMARGIN + CARD_HEIGHT / 2)
        if cards[x1][y1] == cards[x2][y2]: # if the cards match
            i = x1 # setting variables for the mark_card function
            j = y1 # setting variables for the mark_card function
            mark_card(win, i, j) # send the info for the first image to be crossed out.
            i = x2 # setting variables for the mark_card function
            j = y2 # setting variables for the mark_card function
            mark_card(win, i, j) # sends info for second image to be crossed out.
            card1 = (x1, y1) # assign coordinates from first point
            card2 = (x2, y2) # assign coordinates from second point
            matches.append(card1) # add 1st coordinates to matches list
            matches.append(card2) # add 2nd coordinates to matches list
            match_pairs += 1 # add 1 to win counter
    you_won(win)

    win.getMouse()


main()
