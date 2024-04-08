import os 
def main():
    try:
        book_list=[]
        infile=open("bookstore.txt","r")
        line=infile.readline()
        while line:
            book_list.append(line.rstrip("\n").split(","))
            line=infile.readline()
        infile.close()
    
    except FileNotFoundError:
        print("the book list file not found")
        print("starting a new book list!")
        book_list=[]
    
    choice=0
    while True:
        print("** books manager ***")
        print("1) Add a book")
        print("2) look for a book")
        print("3) display all books")
        print("4) quit")
        choice=int(input())

        if choice==1:
            print("adding a book")
            book=input("enter the name of the book: ").lower()
            author=input("enter the name of the authhor: ").lower()
            npages=input("enter the num of pages: ").lower()
            book_list.append([book,author,npages])
        
        elif choice==2:
            print("looking up for a book!!!!!!! ")
            keyword=input("enter the search term: ").lower()
            for book in book_list:
                if keyword in book:
                    print(book)
        
        elif choice==3:
            print("dispaying all books!!!!!")
            for i in range(len(book_list)):
                print(book_list[i])
        
        elif choice==4:
            print("quitting program")
            outfile=open("bookstore.txt","a")
            for book in book_list:
                outfile.write(",".join(book) +"\n")
            outfile.close()
            quit()

if __name__=="__main__":
    main()