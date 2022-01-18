import pyshorteners

url= 'https://github.com/GlenanCastilho'

s = pyshorteners.Shortener()

shortUrl = s.tinyurl.short(url)

print(f"URL Encurtada: {shortUrl}")