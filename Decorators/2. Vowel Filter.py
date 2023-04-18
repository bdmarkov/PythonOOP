def vowel_filter(function):
    def wrapper():
        letters = function()
        result = [el for el in letters if el.lower() in "aoiuey" ]
        return result
    return wrapper



@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
