# Question 6

import random
class  Astrologer(object):
    predicted_past_life = {} 
    predicted_next_life = {}

    def __init__(self, name, past_life = "", next_life= "", past_or_next = ""):
        self.name = name
        self. past_life = past_life
        self.next_life = next_life
        self.past_or_next = past_or_next


    def get_past_life(self, name, past_or_next = ""):
        """Module level function to compute and return return past life of the person in astroloy by take name as argument

        """ 
        past_life_list = ["You were a mathematician in your past life",
        "You were a animal in your past life",
        "You were a doctor in your past life",
        "You were a poet in your past life",
        "You were a politician in your past life",
        "you were a bird in your past life",
        "you were a teacher in your past life",
        "you were a artist in your past life",
        "you were a singer in your past life",
        "you were a sports person in your past life"]
        
        self.past_or_next = "past"

        rand_num_for_name = random.randrange(0, 9)
    
        if self.name in self.predicted_past_life:
            self.past_life = self.predicted_past_life.get(self.name)
        else:
            self.past_life = past_life_list[rand_num_for_name]
            self.predicted_past_life[self.name] = self.past_life
        
        return self.past_life





    def get_next_life(self, name, past_or_next = ""):
        """Module level function to compute and return return next life of the person in astroloy by take name as argument

        """ 
    
        next_life_list = ["You will be a animal in your next life",
        "You will be a doctor in your next life",
        "You will be a storts person in your next life",
        "You will be a bird in your next life"]

        self.past_or_next = "next"

        rand_num_for_name = random.randrange(0, 3)
    
        if self.name in self.predicted_next_life:
            self.next_life = self.predicted_next_life.get(self.name)
        else:
            self.next_life = next_life_list[rand_num_for_name]
            self.predicted_next_life[self.name] = self.next_life
        
        return self.next_life

    def __str__(self):
        if(self.past_or_next == "past"):
            print("\n{} {}".format(self.name,self.past_life))
        else:
            print("\n{} {}".format(self.name,self.next_life))

# code to know about past
try_again = "1"
print("\nKnow about your past life by your name")
while(try_again == "1"):
    name = (str)(input("\nPlease enter your name to know about your past life : "))

    if(name == ""):
        print("\nSorry we cann't predict about your past life, because you doesn't enter any name")
    else:
        name = name.upper()
        astro_past = Astrologer(name)
        astro_past.past_life = astro_past.get_past_life(name)
        astro_past.__str__()
    try_again = (str)(input("\nPlease enter 1 if you want to try again otherwise enter any key : "))
print("\nThank you...")


# code to predict next life
try_again = "1"
print("Know about your next life by your name\n")
while(try_again == "1"):
    name = (str)(input("Please enter your name to know about your next life : "))

    if(name == ""):
        print("\nSorry we cann't predict about your next life, because you doesn't enter any name")
    else:
        name = name.upper()
        astro_next = Astrologer(name)
        astro_next.next_life = astro_next.get_next_life(name)
        astro_next.__str__()
    try_again = (str)(input("\nPlease enter 1 if you want to try again otherwise enter any key : "))
print("\nThank you...")



