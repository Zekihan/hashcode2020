# -*- coding: utf-8 -*-



readBooks = set()
futureBooks = set()
libraries = []
unreadBooks = []
remDay = 0
openLibs = []

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j][1] <= pivot[1]: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

class Library:
    
    def __init__(self, books, signTime, scan, libId):
        self.books = books
        self.signTime = signTime
        self.scan = scan
        self.libId = libId
        
    def calc_score(self,unreadBooks):
        """
        total = 0
        t = (remDay-self.signTime)
        speed = self.scan
        
        for i in range(t*speed):
            
            if i == len(self.books):
                break
            
            if self.books[i] not in futureBooks:
                total += bookScores[self.books[i]]
        
        return total
"""
        return len(self.books)

file = open("c_incunabula.txt","r")
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
        if lib not in openLibs:
            s = lib.calc_score(unreadBooks)
            if(best < s):
                best = s
                maxLib = lib
            
    return maxLib

resultOut = {}
libCursor = {}

def selectBooks():
    
    for lib in openLibs:
        for i in range(lib.scan):
            if len(lib.books) <= libCursor[lib.libId]:
                break
            resultOut[lib.libId].append(lib.books[libCursor[lib.libId]])
            libCursor[lib.libId] += 1
        
            
remSignDays = 0


for day in range(totalDay):
    a = selectBooks()
                    
    if len(openLibs) != totalLib:
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
        else:
            remSignDays -= 1
            if remSignDays == 0: 
                openLibs.append(currentLib)
    remDay -= 1
    #print(len(openLibs))
    print(remDay)


out = f"{len(openLibs)}\n"

for k in resultOut:
    out += f"{k} "
    out += f"{len(resultOut[k])}\n"
    for book in resultOut[k]:
        out += str(book) + " "
    out += "\n"        

file = open("out.txt", "w")
file.write(out)
file.close()




    



