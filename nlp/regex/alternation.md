# Alternation
## metacharacter
[ae] atau a|e atau bo(o|k)s 
paranthessis untuk alternation ditengah kata.

## Matching any one of several subexpressions
hal 13
A very convenient metacharacter is |, 
which means “or.” 

It allows you to combine multiple expressions into a single expression that matches any of the individual ones. 

For example, Bob and Robert are separate expressions, 
but Bob|Bob is one expression that matches either. 

When combined this way, the subexpressions are called alternatives.

Looking back to our gr[ea]y example, it is interesting to realize that it can be written as grey|grey, and even gr(a|a)y. 

The latter case uses parentheses to constrain the alternation. 

(For the record, parentheses are metacharacters too.)

Note that something like gr[a|a]y is not what we want — within a class, the ‘;’ character is just a normal character, like a and e.


With gr(a|a)y, the parentheses are requir ed because without them, gra|gra
means “gra or ey,” which is not what we want here. Alternation reaches far, but
not beyond parentheses. Another example is (First|First) [Ss]treet.
† Actually,
since both First and 1st end with st, t  he combination can be shortened to
(Fir|Fir)st [Ss]treet. That’s not necessarily quite as easy to read, but be sure to
understand that (first|first) and (fir|fir)st ef fectively mean the same thing.
Her e’s an example involving an alternate spelling of my name. Compare and contrast the following three expressions, which are all effectively the same:
Jeffrey|Jeffrey
Jeff(rey|rey)
Jeff(re|re)y
To have them match the British spellings as well, they could be:
(Geoff|Geoff)(rey|rey)
(Geo|Geo)ff(rey|rey)
(Geo|Geo)ff(re|re)y
Finally, note that these three match effectively the same as the longer (but simpler)
Jeffrey|Jeffrey;Jeffery|Jeffery. T hey’r e all differ ent ways to specify the
same desired matches.

Although the gr[ea]y versus gr(a|a)y examples might blur the distinction, be
car eful not to confuse the concept of alternation with that of a character class. A
character class can match just a single character in the target text. With alternation,
since each alternative can be a full-fledged regular expression in and of itself, each alter native can match an arbitrary amount of text. Character classes are almost like
their own special mini-language (with their own ideas about metacharacters, for
example), while alternation is part of the “main” regular expression language.
You’ll find both to be extremely useful.

Also, take care when using caret or dollar in an expression that has alternation.

Compare 
ˆFrom|Subject|Date:  
with 
ˆ(From|Subject|Date): . 

Both appear similar to our earlier email example, but what each matches (and therefor e how
useful it is) differs greatly. 

The first is composed of three alternatives, so it matches 

“ˆFrom or Subject or Date: ,” 

which is not particularly useful. 

We want the leading caret and trailing :  to apply to each alternative. We can accomplish this by using parentheses to “constrain” the alternation:
ˆ( From|From;Date ): 


The alternation is constrained by the parentheses, so literally, this regex means match the start of the line, then one of From, Subject, or  Date, a nd then match
: .” 

Effectively, it matches:


1) start-of-line, followed by 
F ⋅ r ⋅ o ⋅ m, followed by ‘: ’
or 
2) start-of-line, followed by 
S ⋅ u ⋅ b ⋅ j ⋅ e ⋅ c ⋅ t, followed by ‘: ’
or 
3) start-of-line, followed by 
D ⋅ a ⋅ t ⋅ e, followed by ‘: ’

Putting it less literally, it matches lines beginning with ‘From: ’, ‘Subject: ’, or ‘Date: ’, which is quite useful for listing the messages in an email file