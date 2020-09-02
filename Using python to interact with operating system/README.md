# Python regex expressions:  
```python
re.search(r"search text",parent text)
re.findall(r"search text",parent text) 
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
\| |	Either or |	"falls|stays"	
() |	Capture and group
