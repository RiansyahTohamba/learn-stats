import nltk
# sent singkatan dari sentences

def ie_preprocess(document):
#     1. segmenter [1],
    sentences = nltk.sent_tokenize(document)
# 2. word tokenizer [2]
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
# 3. part-of-speech tagger [3]:
    sentences = [nltk.pos_tag(sent) for sent in sentences]    
    return sentences
    
# sisa tahap 4 dan 5

def ekspor():
	alvesSentences = ie_preprocess(open('papers/alves2010.txt').read())
	with open("alves2010.txt", "w") as output:
	    output.write(str(alvesSentences))

def eksporTree():
	sent = nltk.corpus.treebank.tagged_sents()[22]
	# gimana cara bacanya? wkwkw
	with open("tree.txt", "w") as output:
		output.write(str(nltk.ne_chunk(sent)))

def ideComparative():
	# ide comparative? 
	# bagus nih,buat membandingkan a > b atau a < b
	# 1. search tuple dengan value JJR OR RBR
	# 2. 
	pass

# teknik filter yang baik?


# alvesSentences = ie_preprocess(open('papers/alves2010.txt').read())
# print(alvesSentences[1])
eksporTree()