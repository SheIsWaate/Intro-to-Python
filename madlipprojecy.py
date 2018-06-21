print("Waate Games Presents...")
print("StoryLibs! The Madlibs where you are control of the story.")
print("What the genre: Romance(1), Adventure(2), or Comedy(3)")
ans = raw_input("enter genre or number: ")
if ans == "1" or ans == "Romance":
    noun1 = raw_input("Enter noun")
    adjective1 = raw_input("Enter adjective")
    number1 = raw_input("Enter random number")
    emotion = raw_input("Enter emotion present tense")
    noun2 = raw_input("Enter noun")
    adjective2 = raw_input("Enter adjective")
    gender1 = raw_input("Enter opposite gender if you want; remember for next time")
    verb1 = raw_input("Enter verb")
    name = raw_input("Enter Celebrity Name")
    gender2 = raw_input("Same gender as the last one")
    adjective3 = raw_input("Enter adjective")
    noun3 = raw_input("Enter noun")
    verb2 = raw_input("Enter verb")
    adjective4 = raw_input("Enter adjective")
    number2 = raw_input("Enter number higher than 25")
    adjective5 = raw_input("Enter adjective")
    madlibs = ("""Today was going to be my first day at %s school. I was feeling
    %s and i had %s friends. My mom said that i should try to be %s to people so
    I could make friends. Well that didn't work. During lunch, I had to sit in
    the %s because there was no more seats in the cafeteria. Then when school 
    ended, this %s %s %s up to me. Hi Im %s what's your name. I told %s my name.
    I'm %s %s. We talked for a while and since the day I met that person, we 
    were best friends. When we were older we would %s school and go on %s 
    adventure. When we were both %s  we got married. And then we lived %s ever 
    after.""")
    print(madlibs %(noun1,adjective1,number1,emotion,noun2,adjective2,gender1,
    verb1,name,gender2,adjective3,noun3,verb2,adjective4,number2,adjective5))
if ans == "2" or ans == "Adventure":
    adjective1 = raw_input("Enter adjective")
    noun1 = raw_input("Enter noun")
    verb1 = raw_input("Enter verb that ends in -ing")
    noun2 = raw_input("Enter noun")
    noun3 = raw_input("Enter noun")
    noun4 = raw_input("Enter noun")
    adjective2 = raw_input("Enter adjective")
    number1 = raw_input("Enter any positive number")
    noun5 = raw_input("Enter noun")
    animal1 = raw_input("Enter animal and remember for next time")
    noun6 = raw_input("Enter noun")
    occupation = raw_input("Enter occupation")
    verb2 = raw_input("Enter verb ending in -ing")
    animal2 = raw_input("Enter same animal as before")
    adjective3 = raw_input("Enter adjective")
    adjective4 = raw_input("Enter adjective")
    verb3 = raw_input("Enter verb that is past tense")
    noun7 = raw_input("Enter noun")
    noun8 = raw_input("Enter noun")
    verb4 = raw_input("Enter verb")
    noun9 = raw_input("Enter noun")
    madlibs = ("""My name is %s %s. And i am the world's first %s robot. My
    creator name is %s %s %s. He was a very %s man. When he was %s years old he
    was the one who invented the %s. He sent me on many adventures. There was 
    this one time where i was fighting a %s and a %s at the same time. I won at
    the end because a %s came to help me by %s the %s. I also flew into a %s 
    volcano to save a %s elderly woman. But the biggest adventure I went on was
    when I %s the President of the United %s because he was a evil %s. I will
    never be the same because of what happened. That day was the day I realized
    I %s %s.""")
    print(madlibs %(adjective1,noun1,verb1,noun2,noun3,noun4,adjective2,number1,
    noun5,animal1,noun6,occupation,verb2,animal2,adjective3,adjective4,verb3,
    noun7,noun8,verb4,noun9))
if ans == "3" or ans == "Comedy":
    adjective1 = raw_input("Enter adjective")
    adjective2 = raw_input("Enter adjective")
    verb1 = raw_input("Enter verb that ends in -ing")
    noun1 = raw_input("Enter noun")
    adjective3 = raw_input("Enter adjective")
    name1 = raw_input("Enter random name")
    noun2 = raw_input("Enter noun")
    name2 = raw_input("Enter random name")
    adjective4 = raw_input("Enter adjective")
    name3 = raw_input("Enter random name")
    noun3 = raw_input("Enter noun")
    noun4 = raw_input("Enter noun")
    verb2 = raw_input("Enter verb")
    plural_noun = raw_input("Enter plural noun")
    adjective5 = raw_input("Enter adjective")
    noun5 = raw_input("Enter noun and remember for next time")
    place1 = raw_input("Enter random place")
    adjective6 = raw_input("Enter adjective")
    noun6 = raw_input("Enter noun")
    noun7 = raw_input("Enter same noun from before")
    body_part1 = raw_input("Enter a random body part")
    noun8 = raw_input("Enter noun")
    madlibs = raw_input("""It was a %s %s night. I was %s back from the %s with
    my friend little %s. See, my friend was given that nickname and so were the
    rest of my friends including me. We all have nicknames. %s is little %s. %s
    is big %s. And %s is crazy %s. As for me, I'm dangerous %s. We all got 
    these nicknames by doing one thing. We all had to %s the %s. It was %s 
    doing that but it was the only way to get %s cred. Now we are known all
    over %s. People know that they should mess with this crew. Oh yeah, we
    have a crew name too: The %s %s! That's a pretty serious name. You don't
    want to mess with us. But since we have this %s cred we could get you 
    anything or anyone just at the snap of our %s. But until next time stranger,
    I hope that you understand the meaning of %s.""")
    print(madlibs %(adjective1.adjective2,verb1,noun1,adjective3,name1,noun2,
    name2,adjective4,name3,noun3,noun4,verb2,pluarl_noun,adjective5,noun5,
    place1,adjective6,noun6,noun7,body_part1,noun8))

    
