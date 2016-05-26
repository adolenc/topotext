from nltk.tokenize import RegexpTokenizer


def BasicPrepreprocessor(text):
    '''Basic preprocessor removes non alpha-numeric symbols
    and capitalization'''

    return Prepreprocessor(text, False, False, False)

def Prepreprocessor(text, remove_stopwords=True, stem=True, lemmatize=True):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = [w.lower() for w in tokenizer.tokenize(text)]

    if remove_stopwords:
        from nltk.corpus import stopwords
        stops = set(stopwords.words('english'))
        tokens = [w for w in tokens if w not in stops]

    if stem:
        from nltk.stem.porter import PorterStemmer
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(w) for w in tokens]

    if lemmatize:
        from nltk.stem.wordnet import WordNetLemmatizer
        lmtzr = WordNetLemmatizer()
        tokens = [lmtzr.lemmatize(w) for w in tokens]

    return tokens


if __name__ == '__main__':
    text = "This is a string with dot. dots... comma, commas,,, and more .. ? /.-'\;;'[-\n[;';'=-"
    print BasicPrepreprocessor(text)

    text = "This is a string with dot. dots... comma, commas,,, and more .. ? /.-'\;;'[-\n[;';'=- Testing testers tests test"
    print Prepreprocessor(text)


