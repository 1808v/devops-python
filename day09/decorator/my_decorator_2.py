def convert_upper(func):
    def warapper(word):
        return func(word).upper()
    return warapper 

@convert_upper
def show_word(word):
    return word

print(show_word("vivek"))

