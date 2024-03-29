from __future__ import absolute_import, division, print_function

from sinling.sinhala.tokenizer import SinhalaTweetTokenizer

#encoding. word encodig
import codecs

#save to disk
import pickle

f_1 = codecs.open("Preprocessed/test_1.txt", encoding='utf-8', errors='ignore')
f_2 = codecs.open("Preprocessed/test_2.txt", encoding='utf-8', errors='ignore')
f_3 = codecs.open("Preprocessed/test_3.txt", encoding='utf-8', errors='ignore')
f_4 = codecs.open("Preprocessed/test_4.txt", encoding='utf-8', errors='ignore')
f_5 = codecs.open("Preprocessed/test_5.txt", encoding='utf-8', errors='ignore')
f_6 = codecs.open("Preprocessed/test_6.txt", encoding='utf-8', errors='ignore')

tokenizer = SinhalaTweetTokenizer()

sentences = []
for line in f_1:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))
print("Finished File 1")

for line in f_2:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))
print("Finished File 2")

for line in f_3:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))
print("Finished File 3")

for line in f_4:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))
print("Finished File 4")

for line in f_5:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))
print("Finished File 5")

for line in f_6:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 6")

