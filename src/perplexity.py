import collections
import sys
import io
import preprocess as pr

train_in = sys.argv[1]
f = io.open(train_in, "r", encoding="cp1250")
text = f.read()
f.close()
word_list = pr.design_text(text)
words = pr.add_stop_symbol(word_list)


def n_gram_generator(n, words):
    ngram = collections.defaultdict(lambda: 0.01)
    for i in range(len(words)-(n-1)):
        key = tuple(words[i:i+n])
        if ngram.__contains__(key):
            ngram[key] += 1
        else:
            ngram[key] = 1
    for word1 in ngram:
        ngram[word1] = ngram[word1]/float(sum(ngram.values()))
    return ngram


def computing_perplexity(n, sentence, model):
    sentence = sentence.split()
    sentence = n_gram_generator(n, sentence)

    perplexity = 1
    N = 0
    for word in sentence:
        N += 1
        perplexity = perplexity * (1/model[word])
    perplexity = pow(perplexity, 1/float(N))
    return perplexity





hamiltonsentences = "the ommon council confederate republic commercial character of america the government jealous circumspection, restricted the authority of the state legislatures"
maddisonsentences = "legislative departments executive departments and judiciary departments tyrannical laws to execute constitutional limits dissolution of the union arrives"


bigram = n_gram_generator(2, words)
trigram = n_gram_generator(3, words)
p1 = (computing_perplexity(2, hamiltonsentences, bigram))
p2 = (computing_perplexity(2, maddisonsentences, bigram))
p3 = (computing_perplexity(3, hamiltonsentences, trigram))
p4 = (computing_perplexity(3, maddisonsentences, trigram))

if p1 > p2:
    print("for bigram")
    print(p1)
    print(p2)
    print("Author:Hamilton")
else:

    print("for bigram")
    print(p1)
    print(p2)
    print("Author:Maddison")

if p3 > p4:
    print("**********************************************************************************")
    print("for trigram")
    print(p3)
    print(p4)
    print("Author:Hamilton")
else:
    print("**********************************************************************************")
    print("for trigram")
    print(p3)
    print(p4)
    print("Author:Maddison")