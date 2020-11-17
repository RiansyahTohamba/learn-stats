
# How can it be both? 
\b = backspace atau boundary?

halaman 44
Well, actually, \b is a backspace in some situations, 
but in others, 
it matches a word boundary. 

How can it be both? 
The next section tells us.

hal 46
And what about this \b business? 
This is a regex thing: in Perl regular expressions, \b normally matches a word boundary, but within a character class, it matches a backspace. 

A word boundary would make no sense as part of a class, so Perl is free to let it mean something else. 

# flavor regex in many language
The warnings in the first chapter about how a character class’s “sub language” is different from the main regex language certainly apply to Perl (and every other regex flavor as well).

## table 3-3
table 3-3 menunjukkan beberapa fitur dengan berbagai flavor 
bahasa regexnya yang berbeda.

kolomnya sebagai berikut
Feature | Modern grep | Modern egrep|   GNU Sun’s Java  Emacs Tcl Perl .NET packa ge

# Word boundar ies: \b, \B, \<, \>, ...
hal 133
Like line anchors, word-boundary anchors match a location in the string. There are two distinct approaches. One provides separate metasequences for start- and endof-wor d boundaries (often \< and \>), while the other provides ones catch-all
wor d boundary metasequence (often \b). Either generally provides a not-wor dboundary metasequence as well (often \B).


.*\bin\b(?!\b.+ing)

\b in \b ()

# untuk sublime 
## diawal \bchar 
example :  \bs 
tools akan menangkap 'huruf solo s' atau 'huruf s diawal'

## diakhir char\b
example :  s\b 
tools akan menangkap 'huruf solo s' atau 'huruf s diakhir'

## within scope
\bchar\b
example :  \bs\b 
tools akan menangkap 'huruf solo s'

\bassert\b
tools akan menangkap kata 'assert' saja

## contoh kata
assert = s ditenga
sinai = s diawal
books = s diakhir

## referensi 
Friedl
