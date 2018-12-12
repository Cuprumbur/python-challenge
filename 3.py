with open("data 3.txt",mode = 'r',encoding="utf-8") as text_file:
    text=text_file.read()

import re
pattern = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
matches = re.findall(pattern, text)
for i in matches:
    print(i, end='')
                    
