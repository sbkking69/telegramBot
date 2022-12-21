from classes import * 

def plugTypeUser(val) -> TypeUser:
    for item in TypeUser:
        if val == item.value[0]:
            return item

def DownloadDataBase(path, dataList):
    with open(path, 'r+') as file:
        for line in file:
            line = line.split('~')
            if line[0] == '#':
                dataList.append(WorkShop(id=line[0], title=line[1], authour=line[2], data=line[3], prise=line[4]))
            elif line[0] != '#':
                dataList.append(User(id=line[0], name=line[1], type=line[2]))
