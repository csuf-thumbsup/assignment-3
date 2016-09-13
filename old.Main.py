import re
def get_data_list(filename):
    # get list of each line in the file
    datalist = open(filename).readlines()
    return datalist

def has_terminator(x):
    terms = [',', ';', '+', '-', '*', '/', '=']
    # find match by set intersection
    if len(set(x) & set(terms)) > 0:
        return True
    else:
        return False

def reformat_text(text_str):
    if has_terminator(text_str):
        split_text_str = re.split('([-,;+*\/])', text_str)
        print(split_text_str)
        formated_text = ' '.join(split_text_str)

    else:
        formated_text = text_str + ' '

    return formated_text

def beautify(datalist):
    beautified_text = ''

    for str_line in datalist:
        # check if line is empty space then skip
        if str_line.isspace():
            continue
        # if first 2 chars are // then skip over
        if str_line[:2] == '//':
            continue
        # inline comment somewhere near the end of the line
        elif '//' in str_line:
            # chop off that comment
            str_line = str_line[:str_line.index('//')]

        #print(line.split())

        for x in str_line.split():
            # simple cases
            if len(x) == 1 and has_terminator(x):
                beautified_text += x + ' '
            else:
                beautified_text += reformat_text(x)

        # add newline before moving on
        beautified_text += '\n'

    return beautified_text

def save_changes(text_to_save):
    with open("newdata.txt", "w") as textfile:
        textfile.write(text_to_save)

if __name__ == '__main__':

    datalist = get_data_list("data.txt")
    beautified_text = beautify(datalist)
    save_changes(beautified_text)
    print('\n\n--------------------------------\n' + beautified_text)


