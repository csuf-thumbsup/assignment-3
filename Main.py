# CPSC 323
# Group 11

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

        # strip leading/following whitespace
        str_line.strip()

        # update terminals with spaces
        str_list = list(str_line)
        for char in str_list:
            if char in [',', ';', '+', '-', '*', '/', '=']:
                str_list[str_list.index(char)] = ' ' + str(char) + ' '

        # rejoin list and now split by spaces into another list
        str_list = ''.join(str_list).split()

        # rejoin list with spaces inbetween
        str_list = ' '.join(str_list)

        # split into a list by semicolons
        str_list = str_list.split(';')

        # reformat the line and add to beautified_text
        for x in str_list:
            # ignore empty elements
            if x:
                beautified_text += x.strip() + ' ;\n'

    return beautified_text

def save_changes(text_to_save):
    with open("newdata.txt", "w") as textfile:
        textfile.write(text_to_save)

if __name__ == '__main__':
    datalist = get_data_list("data.txt")
    beautified_text = beautify(datalist)
    save_changes(beautified_text)
