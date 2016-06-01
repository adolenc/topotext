from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer


def BasicPrepreprocessor(text):
    """Basic preprocessor removes non alpha-numeric symbols
    and capitalization"""

    return Prepreprocessor(text, False, False, False)

def Prepreprocessor(text, remove_stopwords=True, stem=True, lemmatize=True):
    """
    Tokenize text.
    :return: Array of sentences. Each sentence is an array of words.
    """

    tokenizer = RegexpTokenizer(r'\w+')
    tokens = [[w.lower() for w in tokenizer.tokenize(sentence)] for sentence in sent_tokenize(text)]
    if remove_stopwords:
        from nltk.corpus import stopwords
        stops = set(stopwords.words('english'))
        tokens = [[w for w in sentence if w not in stops] for sentence in tokens]

    if stem:
        from nltk.stem.porter import PorterStemmer
        stemmer = PorterStemmer()
        tokens = [[stemmer.stem(w) for w in sentence] for sentence in tokens]

    if lemmatize:
        from nltk.stem.wordnet import WordNetLemmatizer
        lmtzr = WordNetLemmatizer()
        tokens = [[lmtzr.lemmatize(w) for w in sentence] for sentence in tokens]

    return [token for token in tokens if token]


if __name__ == '__main__':
    text = "This is a string with dot. dots... comma, commas,,, and more .. ? /.-'\;;'[-\n[;';'=-"
    print BasicPrepreprocessor(text)

    text = "This is a string with dot. dots... comma, commas,,, and more .. ? /.-'\;;'[-\n[;';'=- Testing testers tests test"
    print Prepreprocessor(text)


