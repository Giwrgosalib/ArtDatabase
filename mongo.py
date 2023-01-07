import pymongo,datetime,os,time
def mongoprepare():
    global mycol
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db"]

    mycol = mydb["paintings"]
    try:
        listofpaintings=[ {"_id":1,
                           "title": "Mona Lisa",
                           "creationyear":1503 ,
                           "creator":{"name":"Leonardo" ,"surname":"da Vinci","nationality":"Italian"},
                           "art period":"Rennaisance",
                           "loaned to":None,
                           "loaned from": {"Loaner Name":"Louvre" ,"Loan start":"2022-12-1","Loan end":"2023-12-1"},
                           "Exhibited to":"Rennaisance Exhibition",
                           "Put into":{"Room":"EXHIBITION ROOM","Number of position":1}},

                          {"_id":2,
                           "title": "Lady With an Ermine",
                           "creationyear":1489 ,
                           "creator":{"name":"Leonardo" ,"surname":"da Vinci","nationality":"Italian"},
                           "art period":"Rennaisance",
                           "loaned to":None,
                           "loaned from":None,
                           "Exhibited to":"Permanent Display",
                           "Put into":{"Room":"DISPLAY ROOM 1","Number of position":108}},

                          {"_id":3,
                           "title": "Birth of Venus",
                           "creationyear":1486 ,
                           "creator":{"name":"Sandro" ,"surname":"Botticelli","nationality":"Italian"},
                           "art period":"Rennaisance",
                           "loaned to":None,
                           "loaned from": {"Loaner Name":"Uffizi" ,"Loan start":"2022-12-1","Loan end":"2023-12-1"},
                           "Exhibited to":"Rennaisance Exhibition",
                           "Put into":{"Room":"EXHIBITION ROOM","Number of position":2}},

                          {"_id":4,
                           "title": "Gamos",
                           "creationyear":1967 ,
                           "creator":{"name":"Nikos" ,"surname":"Eggonopoylos","nationality":"Greek"},
                           "art period":"Modern",
                           "loaned to":{"Borrower":"Museo del Prado","Loan start":"2022-9-1","Loan end":"2023-2-28"},
                           "loaned from": None,
                           "Exhibited to":None,
                           "Put into":{"Room":None,"Number of position":None}},

                          {"_id":5,
                           "title": "Arravones",
                           "creationyear":1954 ,
                           "creator":{"name":"Nikos" ,"surname":"Eggonopoylos","nationality":"Greek"},
                           "art period":"Modern",
                           "loaned to":{"Borrower":"Museo del Prado","Loan start":"2022-9-1","Loan end":"2023-2-28"},
                           "loaned from": None,
                           "Exhibited to":None,
                           "Put into":{"Room":None,"Number of position":None}},

                          {"_id":6,
                           "title": "O Galatas",
                           "creationyear":1895 ,
                           "creator":{"name":"Nikiforos" ,"surname":"Lytras","nationality":"Greek"},
                           "art period":"Modern",
                           "loaned to":{"Borrower":"Louvre","Loan start":"2022-10-1","Loan end":"2023-2-28"},
                           "loaned from":None,
                           "Exhibited to":None,
                           "Put into":{"Room":None,"Number of position":None}},

                          {"_id":7,
                           "title": "The Return of the Prodigal Son",
                           "creationyear":1669 ,
                           "creator":{"name":"Rembrandt" ,"surname":None,"nationality":"Dutch"},
                           "art period":"Baroque",
                           "loaned to":None,
                           "loaned from": {"Loaner Name":"Hermitage" ,"Loan start":"2022-6-1","Loan end":"2023-6-1"},
                           "Exhibited to":None,
                           "Put into":{"Room":"WAREHOUSE 1","Number of position":4}},

                           {"_id":8,
                           "title": "The Night Watch",
                           "creationyear":1642 ,
                           "creator":{"name":"Rembrandt" ,"surname":None,"nationality":"Dutch"},
                           "art period":"Baroque",
                           "loaned to":None,
                           "loaned from": {"Loaner Name":"Rijksmuseum" ,"Loan start":"2022-6-1","Loan end":"2023-6-1"},
                           "Exhibited to":None,
                           "Put into":{"Room":"WAREHOUSE 1","Number of position":3}},

                          {"_id":9,
                           "title": "Liberty Leading the People",
                           "creationyear":1830 ,
                           "creator":{"name":"Eugene" ,"surname":"Delacroix","nationality":"French"},
                           "art period":"Romanticism",
                           "loaned to":None,
                           "loaned from": None,
                           "Exhibited to":"Permanent Display",
                           "Put into":{"Room":"DISPLAY ROOM 2","Number of position":201}},

                          {"_id":10,
                           "title": "Convergence",
                           "creationyear":1952 ,
                           "creator":{"name":"Jackson" ,"surname":"Pollock","nationality":"American"},
                           "art period":"Modern",
                           "loaned to":None,
                           "loaned from": None,
                           "Exhibited to":"Permanent Display",
                           "Put into":{"Room":"DISPLAY ROOM 3","Number of position":301}},
                          
                          {"_id":11,
                           "title": "Mural",
                           "creationyear":1943 ,
                           "creator":{"name":"Jackson" ,"surname":"Pollock","nationality":"American"},
                           "art period":"Modern",
                           "loaned to":None,
                           "loaned from": None,
                           "Exhibited to":"Permanent Display",
                           "Put into":{"Room":"DISPLAY ROOM 3","Number of position":302}},

                          {"_id":12,
                           "title": "Shot Marilyns",
                           "creationyear":1962 ,
                           "creator":{"name":"Andy" ,"surname":"Warhol","nationality":"American"},
                           "art period":"Modern",
                           "loaned to":None,
                           "loaned from": None,
                           "Exhibited to":"Permanent Display",
                           "Put into":{"Room":"DISPLAY ROOM 3","Number of position":303}},

                          {"_id":13,
                           "title": "Campbell's Soup Cans",
                           "creationyear":1964 ,
                           "creator":{"name":"Andy" ,"surname":"Warhol","nationality":"American"},
                           "art period":"Modern",
                           "loaned to":None,
                           "loaned from": None,
                           "Exhibited to":"Permanent Display",
                           "Put into":{"Room":"DISPLAY ROOM 3","Number of position":304}},

                          {"_id":14,
                           "title": "The Taddei Tondo",
                           "creationyear":1502 ,
                           "creator":{"name":"Michelangelo" ,"surname":None,"nationality":"Italian"},
                           "art period":"Rennaisance",
                           "loaned to":None,
                           "loaned from": None,
                           "Exhibited to":"Permanent Display",
                           "Put into":{"Room":"DISPLAY ROOM 1","Number of position":101}},

                          {"_id":15,
                           "title": "Madonna of Bruges",
                           "creationyear":1504 ,
                           "creator":{"name":"Michelangelo" ,"surname":None,"nationality":"Italian"},
                           "art period":"Rennaisance",
                           "loaned to":None,
                           "loaned from": None,
                           "Exhibited to":"Permanent Display",
                           "Put into":{"Room":"DISPLAY ROOM 1","Number of position":102}},

                          {"_id":16,
                           "title": "The Doni Tondo",
                           "creationyear":1504 ,
                           "creator":{"name":"Michelangelo" ,"surname":None,"nationality":"Italian"},
                           "art period":"Rennaisance",
                           "loaned to":None,
                           "loaned from": None,
                           "Exhibited to":"Permanent Display",
                           "Put into":{"Room":"DISPLAY ROOM 1","Number of position":103}},


                          {"_id":17,
                           "title": "Antique warrior in profile",
                           "creationyear":1472 ,
                           "creator":{"name":"Leonardo" ,"surname":"da Vinci","nationality":"Italian"},
                           "art period":"Rennaisance",
                           "loaned to":None,
                           "loaned from": {"Loaner Name":"British Museum" ,"Loan start":"2022-12-1","Loan end":"2023-12-1"},
                           "Exhibited to":"Rennaisance Exhibition",
                           "Put into":{"Room":"EXHIBITION ROOM","Number of position":5}},


                          {"_id":18,
                           "title": "The Annunciation",
                           "creationyear":1609 ,
                           "creator":{"name":"Leonardo" ,"surname":"da Vinci","nationality":"Italian"},
                           "art period":"Rennaisance",
                           "loaned to":None,
                           "loaned from": None,
                           "Exhibited to":"Rennaisance Exhibition",
                           "Put into":{"Room":"EXHIBITION ROOM","Number of position":6}},


                          {"_id":19,
                           "title": "Pastoral",
                           "creationyear":1924 ,
                           "creator":{"name":"Joan" ,"surname":"Miro","nationality":"Spanish"},
                           "art period":"Modern",
                           "loaned to":None,
                           "loaned from": {"Loaner Name":"Museo Reina Sofia" ,"Loan start":"2022-9-1","Loan end":"2023-9-1"},
                           "Exhibited to":"Joan Miro Exhibition",
                           "Put into":{"Room":"WAREHOUSE 2","Number of position":1}},


                          {"_id":20,
                           "title": "Catalan Landscape",
                           "creationyear":1923 ,
                           "creator":{"name":"Joan" ,"surname":"Miro","nationality":"Spanish"},
                           "art period":"Surrealism",
                           "loaned to":None,
                           "loaned from": {"Loaner Name":"Museum of Modern Art(New York)" ,"Loan start":"2022-9-1","Loan end":"2023-9-1"},
                           "Exhibited to":"Joan Miro Exhibition",
                           "Put into":{"Room":"WAREHOUSE 2","Number of position":2}},

                          {"_id":21,
                           "title": "The Tilled Field",
                           "creationyear":1923 ,
                           "creator":{"name":"Joan" ,"surname":"Miro","nationality":"Spanish"},
                           "art period":"Surrealism",
                           "loaned to":None,
                           "loaned from": {"Loaner Name":"Solomon R. Guggenheim Museum" ,"Loan start":"2022-9-1","Loan end":"2023-9-1"},
                           "Exhibited to":"Joan Miro Exhibition",
                           "Put into":{"Room":"WAREHOUSE 2","Number of position":3}}



                          ]
        mycol.insert_many(listofpaintings)
    except:
        print("Database Already Created!")
def queries():
    global mycol
    while True:
        os.system('cls')
        x=input("""Select MONGODB query:
1)Find all paintings beginning from a certain letter.
2)Paintings owned by us 
3)Count of art period Paintings
4)Count of paintings drawn from 1800 to 2000
5)Exit\n""")
        if(x=="1"):
            os.system('cls')
            initial=input("Enter Desired letter:")
            dbquery={"title":{"$regex":"^"+initial}}
            res=mycol.find(dbquery,{"_id":0,"title":1})
            for i in res:
                print(i)
            input("\nPress Enter to continue:")
        elif(x=="2"):
            os.system('cls')
            dbquery={"loaned from":None}
            res=mycol.find(dbquery,{"title":1})
            for i in res:
                print(i)
            input("\nPress Enter to continue:")
        elif(x=="3"):
            os.system('cls')
            des=input("Enter Desired Art Period:")
            dbquery={"art period":des}
            res=mycol.find(dbquery)
            count=0
            for i in res:
                count=count+1
            print("Count of paintings is:",count)
            input("\nPress Enter to continue:")
        elif(x=="4"):
            os.system('cls')
            dbquery={"creationyear":{"$gt":1800,"$lt":2000}}
            res=mycol.find(dbquery,{"title":1})
            count=0
            for x in res:
                count=count+1
            print("Count of paintings is:",count)
            input("\nPress Enter to continue:")
            
        elif(x=="5"):
            os.system('cls')
            print("Have a nice day")
            break

if __name__ == "__main__":
    mongoprepare()
    queries()
        
                   
                   
