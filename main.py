# -*- coding: utf-8 -*-

readBooks = set()
futureBooks = set()
libraries = []
unreadBooks = []
remDay = 0
openLibs = []
unpickableLibs = set()

def partition(arr,low,high): 
    i = ( low-1 )         
    pivot = arr[high]    
  
    for j in range(low , high): 
  
        if   arr[j][1] <= pivot[1]: 
    
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
def quickSort(arr,low,high): 
    if low < high: 

        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

class Library:
    
    def __init__(self, books, signTime, scan, libId):
        self.books = books
        self.signTime = signTime
        self.scan = scan
        self.libId = libId
        
    def calc_score(self,unreadBooks):
        
        uniqueBookCount = 0
        uniqueBookPoints = 0
        
        t = (remDay-self.signTime)
        if t < 0:
            t = 0
        speed = self.scan
    
        for i in range(t*speed):
            if i == len(self.books):
                break
            
            if book not in futureBooks:
                uniqueBookCount += 1
                uniqueBookPoints += bookScores[book]
        
        return (1/self.signTime)*(uniqueBookCount**2.5)

file = open("f_libraries_of_the_world.txt","r")
a = file.read()
file.close()
lines = a.split("\n")
firstLine = lines[0].split(" ")

totalBooks = int(firstLine[0])
totalLib = int(firstLine[1])
totalDay = int(firstLine[2])
remDay = totalDay

bookScores = []

for score in lines[1].split(" "):
    bookScores.append(int(score))
    

bookDB = []
i = 0
for book in bookScores:
    bookDB.append([i,book])
    i += 1
 
quickSort(bookDB, 0, len(bookDB) - 1)
print("yay")
bookDB.reverse()

for book in bookDB:
    unreadBooks.append(book[0])

libraryLines = lines[2:]

cnt = 0
for i in range(0,totalLib):
    libraryDef = libraryLines[i*2].split(" ")

    libraryBooks = [None] * totalBooks
    
    for book in libraryLines[i*2+1].split(" "):
        book = int(book)
       
        place = unreadBooks.index(book)
        libraryBooks[place] = book
        
    res = [] 
    for val in libraryBooks: 
        if val != None : 
            res.append(val)
    cnt += 1
    print(cnt)
    
    library = Library(res,int(libraryDef[1]),int(libraryDef[2]),i)
    libraries.append(library)
    

def pickLib():

    maxLib = 0
    best = 0
    for lib in libraries:
        #print(count)
        if lib not in unpickableLibs:
            s = lib.calc_score(unreadBooks)
            if(best < s):
                best = s
                maxLib = lib
            
    return maxLib

resultOut = {}
libCursor = {}

def selectBooks():
    
    for lib in openLibs:
        if len(lib.books) > libCursor[lib.libId]:
            for i in range(lib.scan):
                if len(lib.books) <= libCursor[lib.libId]:
                    break
                bk = lib.books[libCursor[lib.libId]]
                if bk in readBooks:
                    libCursor[lib.libId] += 1
                    continue
                resultOut[lib.libId].append(bk)
                libCursor[lib.libId] += 1
        else:
            openLibs.remove(lib)
            
remSignDays = 0


for day in range(totalDay):
    a = selectBooks()
                    
    if len(unpickableLibs) != totalLib:
        if remSignDays == 0:
            currentLib = pickLib()
            
            if currentLib == 0:
                break
            
            resultOut[currentLib.libId] = []
            libCursor[currentLib.libId] = 0
            
            t = (remDay-currentLib.signTime)
            speed = currentLib.scan
        
            for i in range(t*speed):
                if i == len(currentLib.books):
                    break
                futureBooks.add(currentLib.books[i])
            
            remSignDays = currentLib.signTime-1
            
            if remSignDays == 0:
                openLibs.append(currentLib)
                unpickableLibs.add(currentLib)
        else:
            remSignDays -= 1
            if remSignDays == 0: 
                openLibs.append(currentLib)
                unpickableLibs.add(currentLib)
    remDay -= 1
    #print(len(openLibs))
    print(remDay)


out = f"{len(unpickableLibs)}\n"

for k in resultOut:
    out += f"{k} "
    out += f"{len(resultOut[k])}\n"
    for book in resultOut[k]:
        out += str(book) + " "
    out += "\n"        

file = open("out.txt", "w")
file.write(out)
file.close()




