import spacy

# * To add features to output message

GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


nlp = spacy.load("en_core_web_lg")  # Given that the description of the films is very detailed,
                                    # I opted for the large version of en_core_web

# Reading the movies.txt file
with open("movies.txt", "r") as f:
    movies = f.read().splitlines()


# Based on the experience running the semantic.py program with the small version of en_core_web, I've learn to compute
# the word vectors for each movie description capturing their semantic meaning and context, that is, words with similar
# meanings and contexts are located close to each other with a high-dimensional vector in a continuous vector space.
# I've used list comprehension to each movie description in the movies list to find the word vector for that description.
movie_vectors = [nlp(movie) for movie in movies]


def get_similar_movie(description):
    '''
    Function to get the most similar movie
    :param description: Variable define in the main body, in this example, the description of "Planet Hulk"
    :return: The description of the most similar movie in the movie list, that is the one with the highest score
    '''
    # Apply the spaCy language model (nlp) to the parameter description
    description_vector = nlp(description)
    # Comparing the similarity between the two word vectors that correspond to the parameter descripition and the
    # descirption of each movie in the movie list, and appending the similarity score to the list similarities.
    similarities = []
    for movie_vector in movie_vectors:
        similarity = description_vector.similarity(movie_vector)
        similarities.append(similarity)
    # Get the index of the most similar movie, that is, the one that scored the highest similarity
    most_similar_index = similarities.index(max(similarities))
    return movies[most_similar_index]

# Calling the function after assigning 'Planet Hulk' description to variable that becomes parameter
description = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
                 the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk
                 can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''
similar_movie = get_similar_movie(description)
split_description = similar_movie[9:].split(", ")
print(f"\nIf you enjoy watching {BOLD}{UNDERLINE}{GREEN}Planet Hulk{WHITE}, you might also liked {BOLD}{UNDERLINE}{RED}{similar_movie[:7]}{WHITE}:\n")
for line in split_description:
    print(f"\033[3m{line},\033[0m")
