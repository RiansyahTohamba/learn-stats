nlp-sem
# overview
This package contains classes for representing semantic structure in formulas of first-order logic and for evaluating such formulas in set-theoretic models.

>>> from nltk.sem import logic
>>> logic._counter._value = 0

The package has two main components:

logic provides support for analyzing expressions of First Order Logic (FOL).

evaluate allows users to recursively determine truth in a model for formulas of FOL.

A model consists of a domain of discourse and a valuation function, which assigns values to non-logical constants. 

We assume that entities in the domain are represented as strings such as 'b1', 'g1', etc. 

A Valuation is initialized with a list of (symbol, value) pairs, where values are entities, sets of entities or sets of tuples of entities. 

The domain of discourse can be inferred from the valuation, and model is then created with domain and valuation as parameters.

>>> from nltk.sem import Valuation, Model
>>> v = [('adam', 'b1'), ('betty', 'g1'), ('fido', 'd1'),
... ('girl', set(['g1', 'g2'])), ('boy', set(['b1', 'b2'])),
... ('dog', set(['d1'])),
... ('love', set([('b1', 'g1'), ('b2', 'g2'), ('g1', 'b1'), ('g2', 'b1')]))]
>>> val = Valuation(v)
>>> dom = val.domain
>>> m = Model(dom, val)

# extract_rels
Signature:
nltk.sem.extract_rels(
    ['subjclass', 'objclass', 'doc', "corpus='ace'", 'pattern=None', 'window=10'],
)
Docstring:
Filter the output of ``semi_rel2reldict`` according to specified NE classes and a filler pattern.

The parameters ``subjclass`` and ``objclass`` can be used to restrict the
Named Entities to particular types (any of 'LOCATION', 'ORGANIZATION',
'PERSON', 'DURATION', 'DATE', 'CARDINAL', 'PERCENT', 'MONEY', 'MEASURE').

:param subjclass: the class of the subject Named Entity.
:type subjclass: str
:param objclass: the class of the object Named Entity.
:type objclass: str
:param doc: input document
:type doc: ieer document or a list of chunk trees
:param corpus: name of the corpus to take as input; possible values are
    'ieer' and 'conll2002'
:type corpus: str
:param pattern: a regular expression for filtering the fillers of
    retrieved triples.
:type pattern: SRE_Pattern
:param window: filters out fillers which exceed this threshold
:type window: int
:return: see ``mk_reldicts``
:rtype: list(defaultdict)
File:      ~/anaconda3/lib/python3.7/site-packages/nltk/sem/relextract.py
Type:      function