import spacy

nlp = spacy.load('en_core_web_sm')

garden_path_sentences:list= ["The old man the boat.", "The complex houses married and single soldiers and their families.", "The horse raced past the barn fell.", "The florist sent the flowers was pleased.", "Fat people eat accumulates."]

for garden_path_sentence in garden_path_sentences:
    doc = nlp(f"{garden_path_sentence}")
    #print([(w.text, w.pos_) for w in doc])
    print([(token, token.orth_, token.orth, token.tag_) for token in doc if not token.is_punct | token.is_space if token.is_stop == False ])
    
# The mistaken interpretation of the sentences is as expected. For instance, "old" - "JJ" when we understand it as "NNS" and "complex" - "JJ" instead of "NN"
# Likewise "houses" mistakenly "NNS" instead of "VBZ"


