'''
Create a URL Shortner in Python
'''

import pyshorteners as sh

link = 'https://github.com/KoushikNavuluri/URL-SHORTENER'

s = sh.Shortener()
x = (s.tinyurl.short(link))

print(x)

# One-liner
#print(pyshorteners.Shortener().tinyurl.short('https://github.com/KoushikNavuluri/URL-SHORTENER'))
