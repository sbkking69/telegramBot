for obj in listObj:
        obj.Update()        
        if obj.y <= 500:
            TimeList.append(obj)
    listObj = TimeList