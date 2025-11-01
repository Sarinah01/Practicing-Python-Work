while True:
    print("-------------Hiiii, Welcome to Text Analyzer and Formatter--------------")
    n = input("Write Something : ")
    temp = n
    print("Step 1: Cleaning the text:")
    print(temp.strip())
    print("Replacing multiple spaces it single space:")
    print(temp.replace("  "," "))
    print("Step 2: Analyzing the text:")
    print("Total characters are: " , len(temp))
    print("Total words are: ", len(temp.split() ) + len(temp.split(".")) -1)
    print("Sentences are: ", temp.count(("."))+1)
    print("Step 3: Finding the first and last occurence of the word you want:")
    n1 = input("Enter the word u want to search!")
    print("Not found" if temp.find(n1) == -1 else f"First index: {temp.find(n1)}, Last index: {temp.rfind(n1)}")
    print("Step 4: Checking if it is printable , identifier, starts with or end with some specific word?")
    print(f"It is printable!" if (temp.isprintable()) else print("Not printable"))
    n2 = input("Enter the word u want to search that it start with!")
    print(f"It is starts with {n2}!" if (temp.startswith(n2)) else print("Not starts with tht!"))
    n3 = input("Enter the word u want to search that it ends with!") 
    print(f"It is end with {n3}!" if (temp.endswith(n3)) else print("Not end with it!"))
    print("Step 5: Checking if it is Extractable or Manipulated")
    print("Splitting the paragraph into sentences: ", " | ".join(temp.split(".")))
    print("Step 6: ecoding and Decoding:")
    print("Encoding into UTF-8", temp.encode())
    print("ecoding into the bytes to string", temp.encode() , " to " ,temp.encode().decode() )
    n4  = input("Enter the partitioning word:")
    print("The word partitioned by: ", n4 , temp.partition(n4))
    print("Step 6 : Checking for isidentifier, a digit , numeric or alnum , is capitalize")
    print(f''' Is digit: {temp.isdigit()} , 
          Is numeric: {temp.isnumeric()}
          Is alnumeric : {temp.isalnum()}
          Is Capitalize : {temp[0].isupper()}
          ''')
    n5 = input("Enter 0 to exit!")
    if (n5=="0"):
        print("-------Exiting the System-------")
        break
    else:
        print("Enter the next Word/Sentence!")
        continue
    
    

  

    

    
        