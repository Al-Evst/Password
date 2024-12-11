import urwid


def is_very_long(passwd:str):
    return len(passwd) >= 12 

def has_digit(passwd:str):
    return any(symbol.isdigit() for symbol in passwd)

def has_letters(passwd:str):
    return any(symbol.isalpha() for symbol in passwd)

def has_upper_letters(passwd:str):
    return any(symbol.isupper() for symbol in passwd)

def has_lower_letters(passwd:str):
    return any(symbol.islower() for symbol in passwd)
    
def has_symbols(passwd:str):
    return any(not symbol.islower() and not symbol.isalpha() for symbol in passwd)

def rating(passwd, list_of_functions):
    score = 0
    for func in list_of_functions:
        score += 2 if func(passwd) else 0
    return score
    
def on_password_change(edit, new_password):
    reply.set_text(f"Рейтинг пароля: {rating(new_password, functions)}")

if __name__ == '__main__':

    functions = [
        is_very_long, 
        has_digit, 
        has_letters, 
        has_upper_letters,
        has_lower_letters, 
        has_symbols
    ]

    password = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([password, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password, 'change', on_password_change)
    urwid.MainLoop(menu).run()

