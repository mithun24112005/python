words = [
    {"spanish": "el", "english": "the"}, {"spanish": "la", "english": "the"}, {"spanish": "de", "english": "of"},
    {"spanish": "que", "english": "that"}, {"spanish": "y", "english": "and"}, {"spanish": "a", "english": "to"},
    {"spanish": "en", "english": "in"}, {"spanish": "un", "english": "a"}, {"spanish": "ser", "english": "be"},
    {"spanish": "se", "english": "itself"}, {"spanish": "no", "english": "no"}, {"spanish": "haber", "english": "to have"},
    {"spanish": "por", "english": "for"}, {"spanish": "con", "english": "with"}, {"spanish": "su", "english": "his/her"},
    {"spanish": "para", "english": "for"}, {"spanish": "como", "english": "like"}, {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"}, {"spanish": "le", "english": "him/her"}, {"spanish": "lo", "english": "it"},
    {"spanish": "todo", "english": "all"}, {"spanish": "pero", "english": "but"}, {"spanish": "más", "english": "more"},
    {"spanish": "hacer", "english": "to do"}, {"spanish": "o", "english": "or"}, {"spanish": "poder", "english": "can"},
    {"spanish": "decir", "english": "to say"}, {"spanish": "este", "english": "this"}, {"spanish": "ir", "english": "to go"},
    {"spanish": "otro", "english": "other"}, {"spanish": "ese", "english": "that"}, {"spanish": "si", "english": "if"},
    {"spanish": "me", "english": "me"}, {"spanish": "ya", "english": "already"}, {"spanish": "ver", "english": "to see"},
    {"spanish": "porque", "english": "because"}, {"spanish": "dar", "english": "to give"}, {"spanish": "cuando", "english": "when"},
    {"spanish": "él", "english": "he"}, {"spanish": "muy", "english": "very"}, {"spanish": "sin", "english": "without"},
    {"spanish": "vez", "english": "time"}, {"spanish": "mucho", "english": "much"}, {"spanish": "saber", "english": "to know"},
    {"spanish": "qué", "english": "what"}, {"spanish": "sobre", "english": "about"}, {"spanish": "mi", "english": "my"},
    {"spanish": "alguno", "english": "some"}, {"spanish": "mismo", "english": "same"}, {"spanish": "yo", "english": "I"},
    {"spanish": "también", "english": "also"}, {"spanish": "hasta", "english": "until"}, {"spanish": "año", "english": "year"},
    {"spanish": "dos", "english": "two"}, {"spanish": "querer", "english": "to want"}, {"spanish": "entre", "english": "between"},
    {"spanish": "así", "english": "so"}, {"spanish": "primero", "english": "first"}, {"spanish": "desde", "english": "since"},
    {"spanish": "grande", "english": "big"}, {"spanish": "eso", "english": "that"}, {"spanish": "ni", "english": "nor"},
    {"spanish": "nos", "english": "us"}, {"spanish": "llegar", "english": "to arrive"}, {"spanish": "pasar", "english": "to happen"},
    {"spanish": "tiempo", "english": "time"}, {"spanish": "ella", "english": "she"}, {"spanish": "sí", "english": "yes"},
    {"spanish": "bien", "english": "well"}, {"spanish": "puede", "english": "can"}, {"spanish": "uno", "english": "one"},
    {"spanish": "donde", "english": "where"}, {"spanish": "mientras", "english": "while"}, {"spanish": "parte", "english": "part"},
    {"spanish": "poner", "english": "to put"}, {"spanish": "trabajo", "english": "work"}, {"spanish": "día", "english": "day"},
    {"spanish": "muy", "english": "very"}, {"spanish": "hora", "english": "hour"}, {"spanish": "modo", "english": "way"},
    {"spanish": "tener", "english": "to have"}, {"spanish": "nada", "english": "nothing"}, {"spanish": "hacer", "english": "to do"},
    {"spanish": "año", "english": "year"}, {"spanish": "casa", "english": "house"}, {"spanish": "vida", "english": "life"},
    {"spanish": "después", "english": "after"}, {"spanish": "poco", "english": "little"}, {"spanish": "otra", "english": "other"},
    {"spanish": "aunque", "english": "although"}, {"spanish": "gente", "english": "people"}, {"spanish": "vez", "english": "time"},
    {"spanish": "ojos", "english": "eyes"}, {"spanish": "fin", "english": "end"}, {"spanish": "ciudad", "english": "city"},
    {"spanish": "cualquier", "english": "any"}, {"spanish": "semana", "english": "week"}, {"spanish": "día", "english": "day"},
    {"spanish": "momento", "english": "moment"}, {"spanish": "mano", "english": "hand"}, {"spanish": "parte", "english": "part"},
    {"spanish": "lugar", "english": "place"}, {"spanish": "agua", "english": "water"}, {"spanish": "mes", "english": "month"},
    {"spanish": "tierra", "english": "land"}
]

import random

def quiz_user(words):
    random.shuffle(words)
    score=0

    for word in words:
        print(f"what is the english translation of {word['spanish']}?")
        ans=input("your answer: ").strip().lower()
        corr_ans=word['english'].lower()
        if ans=="q":
            quit()
        elif ans==corr_ans:
            print("correct!!\n")
            score+=1
        else:
            print(f"wrong the correct ans is {word['english']} .\n")
    print(f"quiz complete your score: {score}/{len(words)}")

def main():
    print("welcome to the language learning app ")
    start=input("enter y to start the quiz and q to quit: ")
    if start=="y":
        quiz_user(words)
    else:
        quit()

if __name__=="__main__":
    main()



