# simple library script

def AddBook(library):  # Bad function name (should be snake_case)
    """Adds a book to the library"""
    Title = input("Title: ")  # Bad variable name (should be lowercase)
    Author = input("Author: ")
    Year = input("Year: ")

    if not Year.isdigit():
        print("Year must be a number.")
        return

    book = {"title": Title, "author": Author, "year": int(Year)}
    library.append(book)
    print("Added!\n")

def listBooks(lib):  # Bad function name, bad parameter name
    if len(lib)==0:  # Missing spaces
        print("Library empty\n")
        return

    for i in range(len(lib)):  # Should use enumerate
        b = lib[i]
        print(i+1,'.',b["title"],"by",b["author"],"(",b["year"],")")
    print()

def MAIN():  # Should be 'main'
    l=[]  # Bad variable name
    while True:
        print("1 - Add\n2 - List\n3 - Exit")
        c=input("Choice? ")

        if c=='1':
            AddBook(l)
        elif c=='2':
            listBooks(l)
        elif c=='3':
            print("Bye")
            break
        else:
            print("Invalid\n")

if __name__=="__main__":
    MAIN()


