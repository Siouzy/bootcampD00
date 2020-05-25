phrase = "The right format"

format_str = "{:->42s}"
print(format_str.format(phrase)[:42], end='')
