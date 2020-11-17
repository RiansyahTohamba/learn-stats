# import spacy
import spacy
from spacy import displacy

def read_article(file_name):
	file = open(file_name, "r")
	filedata = file.readlines()
	article = filedata[0].split(". ")
	sentences = []

	for sentence in article:
		print(sentence)

	sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
	sentences.pop() 

	return sentences

def generate_img(file_name):
	# Step 1 - Read text anc split it
	sentences = read_article(file_name)

	# load english language model
	nlp = spacy.load('en_core_web_sm',disable=['ner','textcat'])
	text = "The fear that Mr. Trump might take impulsive actions, however, often loomed in the background of discussions with the United States, they said.They saw the abrupt decision as a further sign that voices from the ground were lacking in the debate over the war and that with Mr. Mattis’s resignation, Afghanistan had lost one of the last influential voices in Washington who channeled the reality of the conflict into the White House’s deliberations."
	# create spacy
	doc = nlp(text)
	# for token in doc:
	#     print(token.text,'->',token.pos_)
	displacy.serve(doc, style='dep')       

sentences = read_article('papers/trumph.txt')
print('panjangnya = ',len(sentences))
print('kalimat 1 = ', sentences)
# generate_img('paper/trumph.txt')