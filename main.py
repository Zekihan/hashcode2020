# -*- coding: utf-8 -*-

class Library:
    
    def __init__(self, books, signTime, scan, libId):
        self.books = books
        self.signTime = signTime
        self.scan = scan
        self.libId = libId
        
    def calc_score(self,unreadBooks):
        total = 0
        for i in self.books:
            if i in unreadBooks:
                total += bookScores[i]
        total = (remDay-self.signTime)*self.scan*total/len(self.books)
        return total

libraries = []
unreadBooks = []
remDay = 0
openLibs = []

file = open("f_libraries_of_the_world.txt","r")

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
    libraryBooks = []
    for book in libraryLines[i*2+1].split(" "):
        libraryBooks.append(int(book))
     
    
    library = Library(libraryBooks,int(libraryDef[1]),int(libraryDef[2]),i)
    libraries.append(library)
    

def pickLib():
    maxLib = 0
    best = 0
    for lib in libraries:
        if lib not in openLibs:
            s = lib.calc_score(unreadBooks)
            if(best < s):
                best = s
                maxLib = lib
    return maxLib

def sortUnread(unreadBooks):
    sortedUnread = []
    for i in range(len(unreadBooks)):
        maxBook = 0
        best = 0
        for book in unreadBooks:
            s = bookScores[book]
            if(best < s):
                best = s
                maxBook = book
        unreadBooks.remove(maxBook)
        sortedUnread.append(maxBook)
    
    return sortedUnread

unreadBooks = sortUnread(unreadBooks)
def selectBooks():
    result = []
    for lib in openLibs:
        result.append((lib.libId,[]))
    for book in unreadBooks:
        avLibs = []
        for lib in range(len(openLibs)):
            if len(result[lib][1]) < openLibs[lib].scan:
                
                if book in openLibs[lib].books:
#                    print(f"{book} {openLibs[lib].books}" )
                    avLibs.append(openLibs[lib])

        if len(avLibs) > 0:
            maxLib = 0
            best = 0
            for avlib in avLibs:
                count = 0
                for bookX in avlib.books:
                    if bookX in unreadBooks:
                        count += 1
                if count > best:
                    best = count
                    maxLib = avlib
            for lib in result:
                if lib[0] == maxLib.libId:
                    lib[1].append(book)
                    unreadBooks.remove(book)
                    break
            
    return result
    

remSignDays = 0

result = []
for lib in range(totalLib):
    result.append((lib,[]))

for day in range(totalDay):
    a = selectBooks()
    for lib in a:
        for lib2 in result:
            if lib[0] == lib2[0]:
                for book in lib[1]:
                    lib2[1].append(book)
    if len(openLibs) != totalLib:
        
        if remSignDays == 0:
            
            currentLib = pickLib();
            remSignDays = currentLib.signTime-1
            
        else:
            remSignDays -= 1
            if remSignDays == 0:
                openLibs.append(currentLib)

out = f"{len(openLibs)}\n"

for lib in openLibs:
    out += f"{lib.libId} "
    for lib2 in result:
        if lib2[0] == lib.libId:
            out += f"{len(lib2[1])}\n"
            for i in lib2[1]:
                out += str(i) + " "
            out += "\n"

            
    
    
file = open("file.txt", "w")
file.write(out)
file.close()




    



