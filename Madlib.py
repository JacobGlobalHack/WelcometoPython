print("Welcome to Madlibs")
print("You ll be asked for diferent nouns and verbs, try to keep them funny")

plural_noun = raw_input("Please provide a plural noun:")

noun1 = raw_input("Please provide a noun:")
noun2 = raw_input("Please provide a noun:")
song = raw_input("Please provide a song title:")
verb = raw_input("Please provide a verb:")

madlibs = ("""Learning to drive is a tricky process.  There are a few rules to follow. 
1. Keep two %s on the steering wheel at all times. 
2. Step on the %s to speed up and the %s to slow down."
3. Your parents will just LOVE it if you play %s on the radio. 
4. Make sure to honk your horn when you see %s on the street sign. 
""")
print(madlibs %(plural_noun,noun1,noun2,song,verb))