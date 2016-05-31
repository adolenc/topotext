import collections
import numpy as np
from sklearn.preprocessing import Normalizer

#This is an un-efficient implementation of an tf-idf matrix contruction

#iterates trough all lists in input list and get the vocabulary
def get_words(input_list, n=False):
    cnt = collections.Counter() #instantiate a counter
    #Count the words in the entire corpus - all the documents
    for l in input_list: #For each list representing a text                
        for word in l: #For each word in text
            cnt[word] += 1
    words = [] #Get the n words that appear most frequently in a text (corpus) as a list of strings
    if n: d2 = cnt.most_common(n)
    else: d2 = cnt.most_common() #take all words
    for key, value in d2: words.append(key)
    return words

#Iterate over lists(texts) in the input list and present each text with a n-dimensional vector according to provided list words
#If the k-th vector has a value i on j-th place it means the word words[j] appears i times in this k-th text
def get_M(input_list, words):
    n = len(words)
    M = []
    for l in input_list: #Count the words in a list
        vector = np.zeros(n) #a vector representation of the text file                     
        for word in l:
            if word in words: #if word appears in words list 
                vector[words.index(word)] += 1 #add 1 to appropriate dimension
        M.append(vector) #add the vector to the M matrix
    M = np.array(M)
    return M

#takes an M matrix generated by get_M and returns a tf_idf matrix (basic variant)
def get_tf_idf_M(M, norm_samps=False):
    N = len(M)
    tf_M = np.copy(M) #just the frequency of the word in a text
    idf_v = []
    for i in range(M.shape[1]): #get the number of texts that contain a word words[i]
        idf_v.append(np.count_nonzero(tf_M[:,i])) #count the non zero values in columns of matrix M
    idf_v = np.array(idf_v)
    idf_v = np.log(float(N)/idf_v)
    tf_idf_M = tf_M*idf_v
    if norm_samps:
        normalizer = Normalizer()
        tf_idf_M = normalizer.fit_transform(tf_idf_M)
    return tf_idf_M

if __name__ == '__main__':
    inp_lst = [["tole", "je", "testni", "input", "file"],
               ["notri", "se", "nekaj", "besed", "ponovi"],
               ["tko", "kot", "na", "primer", "besede"],
               ["tole", "se", "nekaj", "in", "besed"]]
    wrds = get_words(inp_lst, 5)
    M = get_M(inp_lst, wrds)
    tf_idf = get_tf_idf_M(M)
    print wrds
    print M
    print tf_idf
