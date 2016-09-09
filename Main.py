import re
def get_data_list(filename):
    # get list of each line in the file
    datalist = open(filename).readlines()
    return datalist

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

        # replace terminals with spaces
        str_list = list(str_line)
        for char in str_list:
            if char in [',', ';', '+', '-', '*', '/', '=']:
                str_list[str_list.index(char)] = ' ' + str(char) + ' '

        # rejoin list and now split by spaces so every char has proper format
        str_list = ''.join(str_list).split()

        # rejoin one last time with proper spacing
        str_list = ' '.join(str_list)

        # add beatufied str to text
        beautified_text +=  str_list + '\n'

    return beautified_text

def save_changes(text_to_save):
    with open("newdata.txt", "w") as textfile:
        textfile.write(text_to_save)

if __name__ == '__main__':
    datalist = get_data_list("data.txt")
    beautified_text = beautify(datalist)
    save_changes(beautified_text)
    print('\n\n--------------------------------\n' + beautified_text)


'''
IGNORE
#special case - look for multiple semicolons per line and add newline accordingly
        rx = re.split('(;)', str_list)
        print('rx: ')
        print(rx)
        y = ''
        for el in rx:
            if el != ';':
                y += el
            else:
                y += el + '\n'
        print('y og: ' + y)
        y = ''.join(y).split()
        y = ' '.join(y)

        print('y mod: ' + y)
'''
