# chapter 1 origin of regex
Although there is evidence of earlier work, the first published computational use of regular expressions I have actually been able to find is Ken Thompson’s 1968
article Regular Expression Search Algorithm § in which he describes a regularexpr ession compiler that produced IBM 7094 object code. 
This led to his work on qed, an editor that formed the basis for the Unix editor ed.

# 4: The Mechanics of Expression Processing
## Match Basics
Befor e looking at the differ ences among these engine types, let’s first look at their
similarities. 

Certain aspects of the drive train are the same (or for all practical purposes appear to be the same), so these examples can cover all engine types.
## About the Examples
This chapter is primarily concerned with a generic, full-function regex engine, so
some tools won’t support exactly everything presented. In my examples, the dipstick might be to the left of the oil filter, while under your hood it might be behind
the distributor cap. Your goal is to understand the concepts so that you can drive
and maintain your favorite regex package (and ones you find interest in later).