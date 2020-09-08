import re
def multi_vowel_words(text):
  pattern = r"\b\w*[aeiou]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']
