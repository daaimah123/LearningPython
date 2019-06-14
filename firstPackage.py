from termcolor import colored
# print(dir(termcolor))
# print(help(termcolor))

text = colored("Hi There", color='cyan', on_color='on_magenta', attrs=["blink"])
print(text)