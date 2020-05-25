languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

format_string = "{:s} was created by {:s}"
for key in languages:
    t = (key, languages[key])
    print(format_string.format(*t))
