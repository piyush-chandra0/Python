import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','.','!','?',',','0','1','2','3','4','5','6','7','8','9']
print(art.logo)
def greet(name,location):
  print(f"Hello {name} from {location}")
  print(f"Welcome To Ceasar Cipher {name}")
  print(f"Ready when you are {name}")
greet(name="MOFO",location="Nowhere")
def cipher(choice):
  if choice=="encode":
    message=input("Type you message.   >")
    shift=int(input("Enter the shift number.   >"))
    def encrypt(m,s):
      if s>26:
        s=s%26
      e_message=" "
      m=m.lower()
      for letter in m:
        i=alphabet.index(letter)
        new_pos=i+s
        if i>=26:
          e_message+=letter
        elif new_pos>26:
          new_pos=new_pos-26
          e_message+=alphabet[new_pos]
        else:
          e_message+=alphabet[new_pos]
      print(f"Encoded Message is:   >{e_message}")
    encrypt(m=message,s=shift)
  elif choice=="decode":
    message=input("Type you message.   >")
    shift=int(input("Enter the shift number.   >"))
    def decrypt(m,s):
      if s>26:
        s=s%26
      d_message=""
      m=m.lower()
      for letter in m:
        i=alphabet.index(letter)
        new_pos=i-s
        if i>=26:
          d_message+=letter
        elif new_pos<0:
          new_pos=new_pos-15
          d_message+=alphabet[new_pos]
        else:
          d_message+=alphabet[new_pos]
      print(f"Decoded Message is:   >{d_message}")
    decrypt(m=message,s=shift)
  else:
    print("We don't do that here.")
should_end = False
while not should_end:
  decide=input("Do you want to encode or decode?   >")
  cipher(choice=decide)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
