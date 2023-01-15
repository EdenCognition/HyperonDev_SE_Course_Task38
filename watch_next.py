############################## Compulsory Task 2 ###############################

#################################### START #####################################

# Declares look up model in to variable
movie_summary = """Will he save their world or destory it? When the Hulk
becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle
and launch him into space to a planet where Hulk can libe in peace.
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery
and trained as a gladiator."""

def get_movies():
    """Reads movies from text file
    
        Declares empty dictionary, opens file, reads file,
        stores file content in to list, iterates over the elements
        in list, adds elements in to dictionary, returns dictionary
    
    Keyword arguments: None
    """
    # Declares empty
    # dictionary
    movie_catalog = {}
    # Opens file 
    with open('movies.txt', 'r', encoding='UTF-8') as movies_file:
        # reads and stores content in to list
        movies_list = movies_file.readlines()
        # Iterates over elements in list
        for movies in movies_list:
            # Adds keys & values in to
            # dictionary
            key, value = movies.split(":")
            movie_catalog[key] = value
    return movie_catalog

def get_next_movie(movie_summary):
    """Determins a similar movie
    
        Loads advanced language model, declares empty lists, creates
        NLP object, calls 'get_movies' function, iterates over the values
        dictionary, compares tokens, determines similarity,  

    Keyword arguments: 
        movie_summary --dict, - dictionary:
                                    keys: Film name
                                    values: Film description
    
    """
    from spacy import load
    # loads a larger pipline with vectors
    nlp = load('en_core_web_md')
    # Declares empty lists
    prediction_list = []
    prediction_results = []
    # Creates NLP object and stores in variable
    current_movie = nlp(movie_summary)
    # Calls function and stores results in to variable
    movie_catalogue = get_movies()
    # iterates over the dictionary values
    for movie in movie_catalogue:
            # Determines similarity and stores it in to variable
            next_movie = nlp(movie_catalogue[movie]).similarity(current_movie)
            # Appends variables in to lists
            prediction_results.append(next_movie)
            prediction_list.append([movie, next_movie])
    # Determines the highest similarity
    next_movie = (max(prediction_results))
    # Iterates over elements in the list
    for movie in prediction_list:
        # Checks the value matches the value in the list
        if movie[1] == next_movie:
            # Displays the value
            print(f"\nWatch next: {movie[0]}\n")

get_next_movie(movie_summary)

#################################### END #######################################
