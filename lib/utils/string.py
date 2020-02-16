def teachers_dict_to_teacher(teachers):
    if len(teachers) == 0 or teachers[0] == '':
        return ''
    first = teachers[0]
    splitted = first.split(" ")
    name = "{}.{}".format(splitted[1][0],splitted[0])
    return str(name)