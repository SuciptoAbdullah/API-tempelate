from services.databaseService import connection
from controllers.queryController import *

logicList:list = ["and", "or", "nor"]

def logicValidation( logic:str, conditionList:list):
    if logic not in logicList:
        return False
    
    logicBefore = conditionList[len(conditionList)-1].strip().lower()
    
    if logicBefore not in logicList:
        return False
    
    return True
    
def conditionValidation( conditionList:list ):
    conditionLength = len(conditionList)
    
    if conditionLength > 0:
        logicBefore = conditionList[len(conditionList)-1].strip().lower()
        if logicBefore not in logicList:
            return False
    
    return True

def getWhereString(columnConditionList:list):
    result = ""
    
    length = len(columnConditionList)
    
    if length < 1:
        return ''
    
    result += "WHERE "
    for i in range(0, length):
        result += columnConditionList[i]
    return result

class Table:
    tableName:str = ''
    primaryKeyColumn:str = 'id'
    
    def __init__(self):
        self.query = f"SELECT * FROM {self.tableName} "
        self.columnSelectList = []
        self.columnConditionList = []
        self.join= ''
        self.orderByColumn = ''
    
    def select(self, *column:str):
        for i in range(0, len(column)):
            self.columnSelectList.append(column[i])
        return self
    
    def where(self, column:str, operator:str, value):
        if conditionValidation(self.columnConditionList):
            value = f"'{value}'" if type(value) == str else value
            self.columnConditionList.append(f"{column} {operator} {value} ")
        return self
    
    def orderBy(self, filter:str = "ASC", *columnList:str):
        columnListStr = ""
        for columnName in columnList:
            columnListStr += columnName
            if columnName != columnList[-1]:
                columnListStr += ", "
            
        self.orderByColumn = f"ORDER BY {columnListStr} {filter}"
        return self
    
    def innerJoin(self, colomn:str, tableTargetName:str, tableTargetColomn):
        self.join = f"INNER JOIN {tableTargetName} ON {self.tableName}.{colomn} = {tableTargetName}.{tableTargetColomn}"
        return self
    
    def leftJoin(self, colomn:str, tableTargetName:str, tableTargetColomn):
        self.join = f"LEFT JOIN {tableTargetName} ON {self.tableName}.{colomn} = {tableTargetName}.{tableTargetColomn}"
        return self
    
    def rightJoin(self, colomn:str, tableTargetName:str, tableTargetColomn):
        self.join = f"RIGHT JOIN {tableTargetName} ON {self.tableName}.{colomn} = {tableTargetName}.{tableTargetColomn}"
        return self
    
    def addLogic(self, logic:str):
        if not logicValidation(logic, self.columnConditionList):
            self.columnConditionList.append(f"{logic} ")
        return self
    
    def getQuery(self):
        queryResult = f"SELECT "
        
        queryResult += listToStringQuery(self.columnSelectList)
        queryResult += f" FROM {self.tableName} "
        queryResult += getWhereString(self.columnConditionList)
        queryResult += self.join + " "
        queryResult += self.orderByColumn
        self.query = queryResult + ";"
        print(self.query)
        return self.query
        
    
    def get(self):
        listResult:list = []
        queryCategory = self.query.split()[0]
        connection.cursor.execute(self.getQuery())
        
        for row in connection.cursor.fetchall():
            lengthRow = len(row)
            map:dict = {}
            key = [col[0] for col in connection.cursor.description]
            for index in range(0, lengthRow):
                map[key[index]] = row[index]
            listResult.append(map)
                
        return listResult
    
    def insert(self, row:dict):
        try:
            query = f"INSERT INTO {self.tableName} VALUES("
            
            key:list = list(row.keys())
            value:list = list(row.values())
            
            
            
            query += f");"
            return True
        except:
            return False
        
    def delete(self,):
        pass
    
    def all(self):
        pass