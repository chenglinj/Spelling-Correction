Files GED.py and GED3.py are programs using Global Edit Distance of different parameters to confirm different hypotheses, these two programs have imported weighted-levenshetein 0.2.1, with which different {m, i, d, r} parameters can be used in calculation, andnumpy. Both packages are downloaded from https://pypi.org/

File GED2.py import the package python-Levenshtein 0.12.0 downloaded from https://pypi.org/ to calculate the Levenshtein Distance between misspelled word and each word in the dictionary to find the best match with the minimum distance.

File soundex.py import the package jellyfish 0.6.1 downloaded from https://pypi.org/ to transform each word in both misspelled list and dictionary list to the 4 character soundex format to find matched words.

File ngram_improved.py import the package ngram 3.3.2 downloaded from https://pypi.org/ to calculate the NGram Similarity between misspelled words and dictionary words with the parameter N=2, then find the best matches with the largest similarity.