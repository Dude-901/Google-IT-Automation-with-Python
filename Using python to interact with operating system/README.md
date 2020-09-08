# Python regex expressions:  
```python
re.search(r"search text",parent text)
re.findall(r"search text",parent text) 
re.split(r"[.?!]", "first. Second! Is it third?") # use ([.?!]) to include the symbols also
re.sub(r""
```

r stands for raw string format(recommended)  
here "search text" can be anything intended to be looked inside the parent text. for example:  


```python
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
```

here . is known as wildcard expression which can be replaced by any character  
and * takes as many characters as possible [look example](https://github.com/Dude-901/Google-IT-Automation-with-Python/blob/master/Using%20python%20to%20interact%20with%20operating%20system/repetition%20qualifiers.py)  
>`[aaaab]` is same as `[ab]`  
> `^[0-999999]$` is equivalent to: `^[0-9]$`  

### Metacharacters   
Character |	Description |	Example 
--------- | ----------- | ---------
[] |	A set of characters |	"[a-m]" or "[a,A]"
\ |	Signals a special sequence (can also be used to escape special characters) |	"\d"	
. |	Any character (except newline character) |	"he..o"	
^ |	Starts with |	"^hello"	
$ |	Ends with |	"world$"	
? |	optional |	"[ ]?"	
\* |	Zero or more occurrences |	"aix*"	
\+	| One or more occurrences |	"aix+"	
{} |	Exactly the specified number of occurrences |	"al{2}"	
\| |	Or |	"AM\|am"	
() |	Capture and group
 
### Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character |	Description |	Example 
--------- | ----------- | ---------
\A |	Returns a match if the specified characters are at the beginning of the string	| "\AThe"	
\b	| Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")	| r"\bain" r"ain\b"	
\B	| Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")	| r"\Bain" r"ain\B"	
\d	| Returns a match where the string contains digits (numbers from 0-9) |	"\d"	 
\D	| Returns a match where the string DOES NOT contain digits |	"\D"	 
\s	| Returns a match where the string contains a white space character	| "\s"	 
\S	| Returns a match where the string DOES NOT contain a white space character |	"\S"	 
\w	| Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) |	"\w"	 
\W	| Returns a match where the string DOES NOT contain any word characters	| "\W"	 
\Z	| Returns a match if the specified characters are at the end of the string	| "Spain\Z"  
