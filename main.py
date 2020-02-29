# -*- coding: utf-8 -*-

readBooks = set()

class Library:
    
    def __init__(self, books, signTime, scan, libId):
        self.books = books
        self.signTime = signTime
        self.scan = scan
        self.libId = libId
        
    def calc_score(self,unreadBooks):
        """
        total = 0
        cnt = 0
        for i in self.books:
            if i not in readBooks:
                total += bookScores[i]
                cnt += 1
        total = (remDay-self.signTime)*self.scan*total/(cnt)
        """
        return self.scan/self.signTime

libraries = []
unreadBooks = []

remDay = 0
openLibs = []

file = open("d_tough_choices.txt","r")
a = file.read()
file.close()
lines = a.split("\n")
firstLine = lines[0].split(" ")

totalBooks = int(firstLine[0])
totalLib = int(firstLine[1])
totalDay = int(firstLine[2])
remDay = totalDay

for i in range(totalBooks):
    unreadBooks.append(i)

bookScores = []

for score in lines[1].split(" "):
    bookScores.append(int(score))

libraryLines = lines[2:]

for i in range(0,totalLib):
    libraryDef = libraryLines[i*2].split(" ")
    libraryBooks = set()
    for book in libraryLines[i*2+1].split(" "):
        libraryBooks.add(int(book))
     
    
    library = Library(libraryBooks,int(libraryDef[1]),int(libraryDef[2]),i)
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

unreadBooks.sort(reverse=True)

def selectBooks():

    result = []
    for lib in openLibs:
        result.append((lib.libId,[]))
        
    for book in unreadBooks:
        #print(book)
        avLibs = set()
        
        for libNo in range(len(openLibs)):
            if len(result[libNo][1]) < openLibs[libNo].scan:
                if book in openLibs[libNo].books: 
                    avLibs.add(openLibs[libNo])
                    #print(libNo)
        
        if len(avLibs) > 0:
            maxLib = 0
            best = 0
            
            for avlib in avLibs:
                
                for i in range(avlib.scan):
                    max
                    

                count = 0
                for bookX in avlib.books:
                    if bookX not in readBooks:
                        count += 1
                if count > best:
                    best = count
                    maxLib = avlib
                    #print(maxLib)
            for lib in result:
                if lib[0] == maxLib.libId:
                    lib[1].append(book)
                    unreadBooks.remove(book)
                    readBooks.add(book)  
    return result
    

remSignDays = 0

resultOut = []
for lib in range(totalLib):
    resultOut.append((lib,[]))

for day in range(totalDay):
    a = selectBooks()

    for lib in a:
        for lib2 in resultOut:
            if lib[0] == lib2[0]:
                for book in lib[1]:
                    lib2[1].append(book)
                    
                    
    if len(openLibs) != totalLib:
        if remSignDays == 0:
            currentLib = pickLib()
            
            if currentLib == 0:
                break
            remSignDays = currentLib.signTime-1
            
            if remSignDays == 0:
                openLibs.append(currentLib)
        else:
            remSignDays -= 1
            if remSignDays == 0: 
                openLibs.append(currentLib)
    remDay -= 1
    print(len(openLibs))
    print(remDay)

out = f"{len(openLibs)}\n"

for lib in openLibs:
    out += f"{lib.libId} "
    for lib2 in resultOut:
        if lib2[0] == lib.libId:
            out += f"{len(lib2[1])}\n"
            for i in lib2[1]:
                out += str(i) + " "
            out += "\n"

            
    

file = open("file.txt", "w")
file.write(out)
file.close()




    



