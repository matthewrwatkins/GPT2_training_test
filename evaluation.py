#Using BLEU score to compare the real sentences with the generated ones
import statistics
from nltk.translate.bleu_score import sentence_bleu

scores=[]

for i in range(len(test_set)):
  reference = test_set['True_end_lyrics'][i]
  candidate = test_set['Generated_lyrics'][i]
  scores.append(sentence_bleu(reference, candidate))

statistics.mean(scores)
