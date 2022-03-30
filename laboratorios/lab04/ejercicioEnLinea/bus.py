from collections import deque


def rutaBarata(morningRoute, afternoonRoute, drivers, hours, extraSalary):
    
    
    
    morningDrivers = drivers//2
    
    afternoonDrivers = drivers // 2
    
    morningExtra = 0
    afternoonExtra = 0
    
    morningTotal = 0
    
    afternoonTotal = 0
    
    for i in morningRoute:
        
        morningTotal += i
        
        if morningTotal >= hours:
            break
            
    
    for i in afternoonRoute:
        
        afternoonTotal += i
        
        if afternoonTotal >= hours:
            break
            
    if drivers % 2 != 0:
        if morningTotal <= afternoonTotal:
            morningDrivers += 1
        else:
            afternoonDrivers += 1
            
            
    if afternoonTotal > hours:
        afternoonExtra = extraSalary*afternoonDrivers*(afternoonTotal-hours)
    
    
    if morningTotal > hours:
        morningExtra = extraSalary*morningDrivers*(morningTotal-hours)
        
        
    return morningExtra + afternoonExtra    
    
    
    
def main():
    
    outputList = deque()
    
    mainEntry = input().split()

    while mainEntry != ['0','0','0']:
    
        numBuses = int(mainEntry[0])
        normalHours = int(mainEntry[1])
        extraHoursFee = int(mainEntry[2])
    
    
        morningRouteDuration = input().split()
        afternoonRouteDuration = input().split()
        
        output = rutaBarata(map(lambda x : int(x),morningRouteDuration).sorted(),map(lambda x : int(x),afternoonRouteDuration).sorted(),numBuses,normalHours,extraHoursFee)
        
        outputList.append(output)
        
        mainEntry = input().split()
    
    
    for i in outputList:
    
        print(i)
    
        
        
def test():
    
    print(rutaBarata([10,15],[10,10],3,20,5))
    
        
        
        



if __name__=='__main__':
    
    test()