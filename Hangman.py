import random

def hangman(word):
    
    lista = ["svjetsko prvenstvo", "dzozluke", "secerlama", "brodogradilište", "ravnopravnost", "elektroprivreda", "pluskvamperfekt", "kontinentalnost", "automehaničar", "otorinolaringologija", "poguzija", "dnevna soba", "morski pas", "kružni tok", "evanđelje", "podzemnica", "ležeći policajac", "mutvak", "čaršaf", "vremensko razdoblje", "kvantna fizika", "nuklearna elektrana", "resozijalizacija", "živo biće", "krizni štab", "venov dijagram", "interferentnost", "kriminalsitika", "onomatopeja", "koordinatni sistem", "ekonomska računica", "multipla skleroza" ]

    word = random.choice(lista)
    
    lista_word_in_dashes = ["_"] * len(word)
    
    for i in range(len(word)):
        if word[i] == " ":
            lista_word_in_dashes[i] = " " 
    
    print("The word is: " + str(" ".join(lista_word_in_dashes)))
    
    already_guessed_list = []
    
    lives = 5
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZŠĐČĆŽ"
    
    alphabet_lower = alphabet.lower() 
    
    hangman_list = [""" 
                   
                   -----
                       |
                       |
                          
                       
                        
                       
                          
                ===============""", """
    
    
        
                  -----
                      |
                      |
                      
                      O
                      
                      
                      
               ================""", """



                 -----
                     |
                     |
                     
                     O
                     |
                     
                                   
                     
              =================""", """
    
    
    
                 -----
                     |
                     |
                     
                     O
                    /|\\   
                      
                     
                        
              =================""", """
    
    

                -----
                    |
                    |
                    
                    O
                   /|\\
                   /
                   
                   
                   
             =================""", """
    
    
    
               -----
                   |
                   |
                   
                   O
                  /|\\
                  / \\
                      
                      
                      
            ================="""]      
            
    
    print(hangman_list[0])
    
    
    
    
    
    
    
    
    
    
    
    while (lives >0):
            
            
        enter_letter = input("Enter a letter: ")
        
        letter = enter_letter.lower()
        
    
        if letter in word:
            if (letter in already_guessed_list) and (len(letter) == 1):
                print("********************************\nYou already guessed that letter, try again\n")
                lives = lives - 1
                print("Lives remaining: " + str(lives))
                print("Already guessed letters: " + str(" ".join(already_guessed_list)))
                if len(hangman_list) == 2:
                    hangman_list.pop(0)
                    print(hangman_list[0])
                   
                    
                    
                else:    
                    hangman_list.pop(0)
                    print(hangman_list[0])
                    
                
            for i in range(len(word)):
                if letter not in already_guessed_list:
                    already_guessed_list.append(letter)
                if str(word[i]) == letter:    
                    lista_word_in_dashes[i] = letter
           
    
            print("********************************\n'" + str(letter) + "' is part of the word\n")
            print("Current word: " + str(" ".join(lista_word_in_dashes)))
            print("Lives remaining: " + str(lives))
            print("Already guessed letters: " + str(" ".join(already_guessed_list)))
            print(hangman_list[0])
           
            
    
        if letter not in word:
            
            if letter in already_guessed_list:
                print("********************************\nYou already guessed that letter, try again\n")
                print("Current word: " + str(" ".join(lista_word_in_dashes)))
                lives = lives - 1
                print("Lives remaining: " + str(lives))
                print("Already guessed letters: " + str(",".join(already_guessed_list)))
                if len(hangman_list) == 2:
                    hangman_list.pop(0)
                    print(hangman_list[0])
                   
                     
                    
                else:    
                    hangman_list.pop(0)
                    print(hangman_list[0]) 
                    
                    
            
            if (letter not in already_guessed_list) and (len(letter) == 1):
                already_guessed_list.append(letter)
                print("********************************\nThe letter is not part of the word, try again\n")
                print("Current word: " + str(" ".join(lista_word_in_dashes)))
                lives = lives - 1
                print("Lives remaining: " + str(lives))
                print("Already guessed letters: " + str(" ".join(already_guessed_list)))
           
                if (len(hangman_list) == 2) and (len(letter) == 1):
                    hangman_list.pop(0)
                    print(hangman_list[0])
                    
                     
                
                else:    
                    hangman_list.pop(0)
                    print(hangman_list[0])
                    
            

        if (letter not in alphabet) and (letter not in alphabet_lower) or (len(letter) > 1):
            print("********************************\nInvalid input, try again\n")
            print("Current word: " + str(" ".join(lista_word_in_dashes)))
            print("Lives remaining: " + str(lives))
            print("Already guessed letters: " + str(" ".join(already_guessed_list)))
            print(hangman_list[0])
           
       
        if(lives == 0):
            print("\nYou have no more lives\n")
            print("The word was: " + str(word))
            break
        
        elif(lista_word_in_dashes == list(word)):
            print("The word is correct!")
            break
        
        

       
    return "\nThank you for playing!"


    
    
        
        

    
   
    
   
    
   
    
   
    
    
word2 = ""
    
print(hangman(word2))           
