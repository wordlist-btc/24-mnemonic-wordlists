import requests, random, os

url = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"

r = requests.get(url)
words = [word for word in r.text.split("\n") if word]

os.system('rm -rf wordlists && mkdir wordlists')

for j in range(1,10000):
 random.shuffle(words)
 with open('wordlists/'+str(j)+'.txt', 'a') as the_file:
  index = {word: i for i, word in enumerate(words)}
  for key in sorted(index.iterkeys()):
   the_file.write(str(index[key]) + '\t' + key + '\n')
