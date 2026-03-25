#----WELCOME TO THE REALM OF SECRETS----

#---HERE YOU HAVE TO SOLVE THE CODE TO GET TO THE NEXT LOCATION---

#YOU ARE PROVIDED WITH A PARAGRAPH
#THE CLUE IS HIDDEN WITHIN THE PARAGRAPH
#YOU KNOW WHAT THEY SAY "NUMBERS CAN BE FOUND IN WORDS"!!!!

#AFTER FINDING THE POSITIONS COPY THE CODE INTO ANY PYTHON COMPILER 



#                  ----PARAGRAPH----

text="Long After Midnight, When The City Had Almost Forgotten its Own Noise, a Sudden Burst of Confusion Spread Through The Narrow Streets as Distant Flashing Reflections Appeared on Glass Windows, While Scattered Lights From Passing Vehicles Flickered Unpredictably and People Rushed Outside in Panic, Hearing Faint Cries and The Growing Sound of Screaming Voices Mixed With Urgency Before The Sharp Wail Of Sirens Cut Through Everything."


words=text.split()


#THE POSITION OF FIVE WORDS NEED TO BE FOUND

positions=[  , , , ,  ]

print("THE NEXT CLUE IS:\n")   
for p in positions:
    print(words[p-1], end=" ")   

print("\nCOME FIND ME!!!!")    
    



#THE POSITIONS CLUES CAN BE FOUND IN THE OTHER FILE
#FIND THEM AND PLACE THEM IN THE CODE
    
    
