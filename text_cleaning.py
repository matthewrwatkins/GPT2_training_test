#Loop to keep only generated text and add it as a new column in the dataframe
my_generations=[]

for i in range(len(generated_lyrics)):
  a = test_set['Lyric'][i].split()[-30:] #Get the matching string we want (30 words)
  b = ' '.join(a)
  c = ' '.join(generated_lyrics[i]) #Get all that comes after the matching string
  my_generations.append(c.split(b)[-1])

test_set['Generated_lyrics'] = my_generations


#Finish the sentences when there is a point, remove after that
final=[]

for i in range(len(test_set)):
  to_remove = test_set['Generated_lyrics'][i].split('.')[-1]
  final.append(test_set['Generated_lyrics'][i].replace(to_remove,''))

test_set['Generated_lyrics'] = final
view raw
