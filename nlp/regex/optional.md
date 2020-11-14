contoh : threshold, thresholds
---
Let’s look at matching color or colour. 


Since they are the same except that one has a 'u' and the other doesn’t, we can use 'colou?r' to match either. 



The metacharacter ? (question mark) means optional. 

It is placed after the character that is
allowed to appear at that point in the expression, but whose existence isn’t actually requir ed to still be considered a successful match.
Unlike other metacharacters we have seen so far, the question mark attaches only
to the immediately-preceding item. Thus, colou?r is interpreted as 
“c then o then l then o then u? then r. ”
The u? part is always successful: sometimes it matches a u in the text, while other
times it doesn’t. The whole point of the ?-optional part is that it’s successful either
way. This isn’t to say that any regular expression that contains ? is always successful. For example, against ‘semicolon’, both colo and u? ar e successful (matching
colo and nothing, respectively). However, the final r fails, and that’s what disallows semicolon, in the end, from being matched by colou?r.