from os import name, system, path, mkdir

def where_am_i():
    if name == 'nt':
        return 'windows'
    else:
        return 'linux/macos'

def clear():
    sys = where_am_i()

    if sys == 'windows':
        system('cls')
    else:
        system('clear')
        
def home():
    home_dir = path.expanduser("~")
    return home_dir

def image_location():
    my_home = home()
    extra =  "/Documents/Instagram_Bot"

    try: 
        my_path = my_home + extra
        mkdir(my_path)
        return my_home + extra
    
    except FileExistsError:
        return my_home + extra
    
image_location()