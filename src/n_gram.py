import io
import sys
import preprocess as pr
import randomselection as rd


train_file = sys.argv[1]
train_file2 = sys.argv[2]
ngram_file = sys.argv[3]
output_file = sys.argv[4]
infile = io.open(train_file,"r",encoding="cp1250")
infile2 = io.open(train_file2,"r",encoding="cp1250")
outfile = open(ngram_file, 'w')
sys.stdout = open(output_file, 'w')
text = infile.read()
text_test = infile2.read()
infile.close()
infile2.close()
word_list = pr.design_text(text)
test_words = pr.design_text(text_test)
words = pr.add_stop_symbol(word_list)


unigram = set(words)
unigram_iter = iter(unigram)
unigram = dict()
for word in words:
    if unigram.__contains__(word):
        unigram[word] += 1
    else:
        unigram[word] = 1


unigram = sorted(unigram.items(), key=lambda count: count[1])
outfile.write(str("Unigram Language Building\n"))
outfile.write(str(unigram))
outfile.write(str("\n**********************************************************************************************\n"))

start_word = words[len(words)//4]
start_word2 = test_words[len(test_words)//4]
# print (start_word)


def n_gram_generator(n):
    gram = dict()
    for i in range(len(words)-(n-1)):
        key = tuple(words[i:i+n])
        if gram.__contains__(key):
            gram[key] += 1
        else:
            gram[key] = 1
    gram = sorted(gram.items(), key=lambda count: count[1])
    return gram


# unigram = n_gram_generator(1)
bigram = n_gram_generator(2)
outfile.write(str("Bigram Language Building\n"))
outfile.write(str(bigram))
outfile.write(str("\n**********************************************************************************************\n"))
trigram = n_gram_generator(3)
outfile.write(str("Trigram Language Building\n"))
outfile.write(str(trigram))


def random_sentence(gram, word, n = 30):
    for i in range(n):
        print(word, " ", end="")
        options = [element for element in gram if element[0][0] == word]
        if not options:
            break

        word = rd.random_selection(options)[1]


for n in range(2, 4):
    ngram = n_gram_generator(n)
    print
    print("***********************************************%d-gram Essays*****************************************" % n,)
    print("\"", end="")
    random_sentence(ngram, start_word, len(ngram))
    print("\"")
    print("Done")
    print("***********************************************************************************************************")
    print("\"", end="")
    random_sentence(ngram, start_word2, len(ngram))
    print("\"")
    print("Done")