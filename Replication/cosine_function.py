from gensim.models import Word2Vec

def cosine_sim(parser, keyword, text, labels, relative = False, threads = 1, window = 10, skipgram = 1):
    """
    module for get the cosine similarity or relative cosine similarity 
    between one word and its counterpart when used in a different data sets.
    
    parser uses the TextPrep class to prep the data
    
    key words is the word you want to compare between the data sets
    
    Text is a list of text documents to analyze
    
    labels is a list of labels that identify which group a document belongs to
    
    Set relative to True if you want relative cosine similarity
    
    Set the window size of the word2vec model with the window variable
    
    set skipgram to 0 to use CBOW architecture instead
    
    """
    
    # define tagged keywords.
    keyword_r = keyword + '_r'
    keyword_d = keyword + '_d'
    
    # isolate and tag key words
    tweets = []
    for i in range(len(text)):
        try:
            tweets.append(parser.tag_keywords(keyword, text[i], labels[i]))
        except Exception as e:
            print(e)
            print('failed at '+ keyword + str(i))
            
    # lemmatize
    tweets = parser.multi_lemmatizer(tweets, threads = threads)

    # drop single letters
    for i in range(len(tweets)):
        tweets[i] = [word for word in tweets[i] if len(word) > 1]

    # train and save word2vec
    model = Word2Vec(tweets, window = window, sg = skipgram)
    
    # return cosine similarity between the words
    if relative == True:
        return model.wv.relative_cosine_similarity(keyword_r, keyword_d, topn=10)
    else:
        return model.wv.similarity(keyword_r, keyword_d)