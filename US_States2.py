import ssl
import csv
import requests
import pandas as pd
import re


csvFile = open("usa.states.txt","r")
csvText = csv.reader(csvFile)

newFile = open("usa_states_alphabetical.txt","w")
states_alphabetical_csv = csv.writer(newFile, lineterminator = '\n')
statesAlphabetical = csv.writer(newFile, lineterminator = '\n')
header = "State","Number of letters"

states = []
with open("usa.states.txt") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        states.append(line[0])
    alphabetical = sorted(states, key = str.lower)
    reverseAlphabetical = sorted(states, key = str.lower,reverse = True)
    print(alphabetical)
    print(reverseAlphabetical)

for word in alphabetical:
    length = len(word)
    states_alphabetical_csv.writerow([word,length])

newFile2 = open("usa_states_reverse_alphabetical.txt","w")
states_reverse_alphabetical_csv = csv.writer(newFile2, lineterminator = '\n')

for word in reverseAlphabetical:
    length = len(word)
    states_reverse_alphabetical_csv.writerow([word,length])

newFile3 = open("usa_states_double_lettered.txt","w")
states_double_lettered = csv.writer(newFile3, lineterminator = '\n')
for word in alphabetical:
    count = 0
    char = 1
    for char in range(len(word)):
        if word[char] == word[char-1]:
            states_double_lettered.writerow([word])

newFile4 = open("usa_states_less_than_10.txt","w")
states_less_than_10 = csv.writer(newFile4, lineterminator = '\n')
for word in alphabetical:
    count = 0
    char = 1
    if len(word) < 10:
        states_less_than_10.writerow([word])