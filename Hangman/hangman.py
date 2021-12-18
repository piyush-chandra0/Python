import random
from stage_logo import stages,logo
import words
chosen_word = random.choice(words.word_list)
print(logo)
print(f'Pssst, the solution is {chosen_word}.')
display=[]
for letter in chosen_word:
  display.append("_")
print(f"{' '.join(display)}")
s=6
end=False
while not end:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You have already guessed {guess}")
  e=0
  n=0
  for letter in chosen_word:
    if letter == guess:
      display[e]=letter
    else:
      n+=1
    e+=1
  print(f"{' '.join(display)}")
  if display.count("_")==0:
    print("You Won.")
    end=True
  if n==len(chosen_word):
    print(f"You guessed {guess}, which is not in the word hence you lose a life.")
    print(stages[s])
    if s==0:
      print("You Lose.")
      end=True
    s=s-1