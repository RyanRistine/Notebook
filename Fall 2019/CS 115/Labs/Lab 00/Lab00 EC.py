def main():
    movies=[]
    while True:
        movie = input('What is your favorite movie?')
        if movie in movies:
            print('You idiot, you already said that')
        else:
            movies.append(movie)
            print('Ugh, ', movie, ' is a terrible movie')
main()
