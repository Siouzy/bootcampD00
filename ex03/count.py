import re


def text_analyzer(text="", *argv):
    if len(argv) > 0:
        print("ERROR")
    elif text == "":
        text = input("What is the text to analyze?\n")
        text_analyzer(text)
    else:
        total_len = len(text)
        up_len = len(re.findall(r'[A-Z]', text))
        down_len = len(re.findall(r'[a-z]', text))
        space_len = text.count(' ')
        punc_len = len(re.findall(r"\.|,|:|'|&|\;|!|\?|\*|\(|\)|\-", text))
        print('The text contains ', str(total_len), ' characters:')
        print('- ', str(up_len), ' upper letters')
        print('- ', str(down_len), ' lower letters')
        print('- ', str(punc_len), ' punctuation marks')
        print('- ', str(space_len), ' spaces')
