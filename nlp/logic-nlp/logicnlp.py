import nltk
from nltk.parse import malt
from nltk.tag import RegexpTagger
tagger = RegexpTagger(
	[('^(chases|runs)$', 'VB'),
	('^(a)$', 'ex_quant'),
	('^(every)$', 'univ_quant'),
	('^(dog|boy)$', 'NN'),
	('^(He)$', 'PRP')]
)
# With MALT_PARSER and MALT_MODEL environment set.\n,
mp = malt.MaltParser('maltparser-1.9.2', 'engmalt.linear-1.7.mco') # doctest: +SKIP\n,
mp.parse_one('I shot an elephant in my pajamas .'.split()).tree() # doctest: +SKIP\n,

# mp = nltk.MaltParser(tagger=tagger)

# rc = nltk.DrtGlueReadingCommand(depparser=mp)


# dt = nltk.DiscourseTester(['Every dog chases a boy', 'He runs'], rc)
# dt.readings()

