def convert_upper(func):
    def warapper(word):
        return func(word).upper()
    return warapper 

@convert_upper
def show_word(word):
    return word

print(show_word("vivek"))



def remove_punctuations(func):
    def warapper():
        return func().replace(","," ")
    return warapper

@remove_punctuations
def take_sentance():
    sent = input("Enter a sentance: ")
    return sent

print(take_sentance())