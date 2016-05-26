from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


def BasicPrepreprocessor(text):
    '''Basic preprocessor removes non alpha-numeric symbols
    and capitalization'''

    return Preprocessor(text, False, False)

def Prepreprocessor(text, remove_stopwords=True, lemmatize=True):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = [w.lower() for w in tokenizer.tokenize(text)]

    if remove_stopwords:
        stops = set(stopwords.words('english'))
        tokens = [w for w in tokens if w not in stops]

    if stem:
        from nltk.stem.porter import *
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(w) for w in tokens]

    if lemmatize:
        from nltk.stem.wordnet import WordNetLemmatizer
        lmtzr = WordNetLemmatizer()
        tokens = [lmtzr.lemmatize(w) for w in tokens]

    return tokens


if __name__ == '__main__':
    text = "This is a string with dot. dots... comma, commas,,, and more .. ? /.-'\;;'[-\n[;';'=-"
    print BasicPreprocessor(text)

    text = "This is a string with dot. dots... comma, commas,,, and more .. ? /.-'\;;'[-\n[;';'=- Testing testers tests test"
    print Preprocessor(text)


