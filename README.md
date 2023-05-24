# HyperionDev
Software Engineering NLP bootcamp tasks using spaCY

Implemented a script using spaCy to tokenize sentences, perform entity recognition, and provide explanations, analyzing garden path sentences and gaining insights into entities and
their associations.

semantic.py includes similarities between cat,monkey and banana using both simpler language model ‘en_core_web_sm’ and 'en_core_web_md'.

watch_next.py reads in the movies.txt ﬁle, where each separate line is a description of a different movie.
I created a function to return which movies a user would watch next if they have watched Planet Hulk with the description
“Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.”
The function takes in the description as a parameter and return the title of the most similar movie.
