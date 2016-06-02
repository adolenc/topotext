from utils import map_flatten, avg, map_map
from collections import Counter
from operator import le, ge

""" Helper functions """

def get_ratio(array, fn):
    """
    Returns the ratio of elements that satisfy fn(e).
    :param array: array of elements.
    :param fn: condition
    """
    cntr = Counter(array)

    selected = [(key, val) for key,val in cntr.items() if fn(key)]
    if not selected:
        return 0
    (_, counts) = zip(*selected)
    (_, all_counts) = zip(*cntr.items())

    return sum(counts)/float(sum(all_counts))


def min_max_avg(array):
    """
    Returns min,max and avg elements of array..
    """
    return min(array), max(array), avg(array)


def ratio_length_of_words_text(word_lens, n=3, op=le):
    return get_ratio(word_lens, lambda x: op(x, n))


def ratio_most_common(words, n):
    cntr = Counter(words)
    (_, counts) = zip(*cntr.most_common(n))
    (_, all_counts) = zip(*cntr.items())
    return sum(counts)/float(sum(all_counts))


""" Simple features functions """

def word_lengths_funcs(texts):
    """
    Returns the ratio of (average word length)/(longest word length),
    """
    word_stats = map(min_max_avg, map_map(len, map_flatten(texts)))
    avg_max = map(lambda x:x[2]/float(x[1]), word_stats)
    return avg_max


def sentence_lengths_funcs(texts):
    """
    Returns: - the ratio of (average sentence length)/(longest sentence length)
             - the ratio of (shortest sentence length)/(longest sentence length)
    """
    sent_stats = map(min_max_avg, map_map(len, texts))
    avg_max = map(lambda x:x[2]/float(x[1]), sent_stats)
    min_max = map(lambda x:x[0]/float(x[1]), sent_stats)
    return map(list,zip(avg_max, min_max))


def ratio_most_n_common_words(texts, n=3):
    """
    Returns the ratio of the total number of "n" most common words among all the words.
    """
    return map(lambda x: ratio_most_common(x, n), map_flatten(texts))


def ratio_length_of_words_texts(texts, n=3, op=le):
    """
    Returns the ratio of the number of words of op(length(word), n) among all words.
    """
    word_lens = map_map(len, map_flatten(texts))
    return map(lambda x: ratio_length_of_words_text(x, n, op), word_lens)



if __name__ == '__main__':
    test = [
            [["one", "two", "three", "five"],["sad","panda","is","sad"]],
            [["second", "sentence", "is", "a", "lie"],["first","sentence", "is", "true"]]
            ]

    print word_lengths_funcs(test)
    print sentence_lengths_funcs(test)
    print ratio_most_n_common_words(test)
    print ratio_length_of_words_texts(test, 3, le)
    print ratio_length_of_words_texts(test, 8, ge)