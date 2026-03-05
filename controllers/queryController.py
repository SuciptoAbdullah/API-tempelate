def listToStringQuery( queryList:list ):
    result = ""
    listLength = len(queryList)
    if listLength < 1:
        result += "* "
    else:
        for i in range(0, listLength):
            result += queryList[i]
            
            if i < listLength - 1:
                result += ", "
    return result