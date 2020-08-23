# Python regex expressions:  
```python
re.search(r"search text",parent text)  
```
> r stands for raw string format(recommended)  
> here "search text" can be anything intended to be looked inside the parent text. for example:  

```python
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
```

Character |	Description |	Example 
--------- | ----------- | ---------
[] |	A set of characters |	"[a-m]"
\ |	Signals a special sequence (can also be used to escape special characters) |	"\d"	
. |	Any character (except newline character) |	"he..o"	
^ |	Starts with |	"^hello"	
$ |	Ends with |	"world$"	
\* |	Zero or more occurrences |	"aix*"	
\+	| One or more occurrences |	"aix+"	
{} |	Exactly the specified number of occurrences |	"al{2}"	
\| |	Either or |	"falls|stays"	
() |	Capture and group
