def first_word(text: str) -> str:
    all_word = text.split()
    return all_word[-1]


print(first_word("Hola como te ha ido ?"))
print(first_word("Hello world"))
print(first_word("greeting from CheckiO Planet"))

