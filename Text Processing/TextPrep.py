import spacy
import re


class TextPrep:
    """
    Class for either tokenizing or lemmatizing a corpus of documents

    key_words is a list of words you're interested in locating in the text

    key_synonyms is meant to be a dictionary of synonyms and their associated
    key tokens. Use with the replace_synonyms method so that all synonyms
    can be replaced by a single token from the key_words list.

    twitter_preprocess does basic cleaning for twitter text

    replace_keyword is used to replace synonyms with a single keyword

    tag_tokens will tag keywords found within a text with the appropriate label

    spacy_tokenizer and spacy_lemmatizer remove digits, punctuation, stopwords, and returns
    either the token or lemma
    """
    def __init__(self, model = 'en', stopwords = None, key_words = None, key_synonyms = None):
        self.model = model
        self.stopwords = stopwords
        self.key_words = key_words
        self.key_synonyms = key_synonyms

    def twitter_preprocess(self, text):
        """
        This functions does some preliminary cleaning for twitter text. It will:
        1. Remove all web addresses from text
        2. Remove punctuation, digits, and emoji
        3. Remove excess white space
        4. Convert to lower case
        """
        # remove websites
        text = re.sub('https:\S*', '', text)
        # remove all punctuation and digits
        text = re.sub('[^\w\s_]|_|\d','',text)
        # remove excess white space between words
        text = re.sub('\s+', ' ', text)
        # remove leading and trailing white space
        text = text.strip()
        # convert to lower case
        text = text.lower()
        return text

    def replace_synonyms(self, keyword, text):
        """
        Called by the tag_keywords method.

        Uses the key_synonyms dictionary to locate synonyms and
        replace them with their associated key word. Will not work
        if the key word is not found in the key_synonyms dictionary
        """
        # subset key words dictionary to only those with the selected key word
        dictionary = {key:value for key, value in self.key_synonyms.items() if value == keyword}
        # Create a regular expression  from the dictionary keys
        regex = re.compile("(%s)" % "|".join(map(re.escape, dictionary.keys())))
        # For each match, look-up corresponding value in dictionary
        return regex.sub(lambda mo: dictionary[mo.string[mo.start():mo.end()]], text)

    def tag_keywords(self, keyword, text, tag):
        """
        Finds all instances of a user defined token within a specific corpus and tags it to
        a specific group. Pass a list of text documents, and a list of associated tags for those documents
        such as two columns from a data frame.
        """
        # replace synonyms of the key words with the key word
        text = self.replace_synonyms(keyword, text)
        # isolate the key word with space so it can be treated as an individual token
        text = re.sub(keyword, ' ' + keyword + ' ', text)
        # Add the group label
        text = re.sub(keyword, keyword + "_" + tag, text)
        # eliminate excess whitespace created
        text = re.sub('\s+', ' ', text).strip()
        return text

    def spacy_tokenizer(self, text):
        """
        Tokenizes, returns lower case, removes stop words and punctuation,
        """
        nlp = spacy.load(self.model, disabled = ['tagger', 'parser', 'ner', 'textcat'])
        # tokenize
        text = self.nlp(text)
        # take the token unless it is a stopword
        text = [token.text.lower().strip() for token in text if not token.is_stop]
        return text

    def spacy_lemmatizer(self, text):
        """
        Tokenizes, lemmatizes, returns lower case, removes stop words and punctuation
        """
        # reload spacy with pat of speech tagger
        nlp = spacy.load(self.model, disable = ['parser', 'ner', 'textcat'])
        # tokenize
        text = nlp(text)
        # take the lemma unless it is a stopword
        text = [token.lemma_.lower().strip() for token in text if not token.is_stop]
        return text

    def multi_lemmatizer(self, text_list, threads):
        """
        Lemmatizer with multiprocessing. Pass a list of text documents and
        define the number of desired threads
        """
        # reload spacy with pat of speech tagger
        nlp = spacy.load(self.model, disable = ['parser', 'ner', 'textcat'])

        text_lemmas = []
        for text in nlp.pipe(text_list, n_threads = threads):
            tokens = [token.lemma_.lower().strip() for token in text if not token.is_stop) > 1]
            text_lemmas.append(tokens)
        return text_lemmas
