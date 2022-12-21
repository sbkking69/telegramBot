def DownloadDataBase(path, dataList):
    with open(path, 'r+') as file:
        for line in file:
            line = line.split('~')
            if line[0] == '#':
                dataList.append({'id'})
