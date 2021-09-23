def score_name(name):
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
score = 0
for char in name:
  score += letters.index(char) + 1
return score

f = open("p022_names.txt", "r")
for names in f:
  names = names.replace('"', '')
  names = names.split(",")
  names.sort()
    
total = 0
for name in names:
  score = score_name(name)
  position = names.index(name) + 1
  score = score * position
  total += score
print(total)
