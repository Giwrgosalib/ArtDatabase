import sqlite3,datetime,time,os

def load_data():
    global conn
    loanedto = [
(38,"Uffizi",datetime.date(2020,12,1),datetime.date(2021,12,1)),
(51,"Museo del Prado",datetime.date(2022,9,1),datetime.date(2023,2,28)),
(52,"Museo del Prado",datetime.date(2022,9,1),datetime.date(2023,2,28)),
(53,"Uffizi",datetime.date(2022,12,1),datetime.date(2023,12,1)),
(54,"Louvre",datetime.date(2022,10,1),datetime.date(2023,2,28)),
(55,"Museo del Prado",datetime.date(2022,9,1),datetime.date(2023,3,31)),
(56,"Uffizi",datetime.date(2022,12,1),datetime.date(2023,12,1)),
(8,"British Museum",datetime.date(2023,12,1),datetime.date(2024,12,1)),
(9,"British Museum",datetime.date(2023,12,1),datetime.date(2024,12,1))
]
    Idioktitos = [(2,),(3,),(4,),(5,),(6,),(7,),(8,),(9,),(10,),
              (11,),(14,),(15,),(16,),(17,),(18,),(19,),
              (20,),(21,),(22,),(23,),(26,),(28,),(29,),
              (30,),(31,),(37,),(38,),(39,),
              (40,),(41,),(42,),
              (51,),(52,),(53,),(54,),(55,),(56,)]
    loanedpaintings=[(34,datetime.date(2022,6,1),datetime.date(2023,6,1),"National Gallery (London)"),
                 (36,datetime.date(2022,6,1),datetime.date(2023,6,1),"Museo Regionale (Messina)"),
                 (25,datetime.date(2022,6,1),datetime.date(2023,6,1),"Hermitage"),
                 (24,datetime.date(2022,6,1),datetime.date(2023,6,1),"Rijksmuseum"),
                 (43,datetime.date(2022,9,1),datetime.date(2023,9,1),"Museo Reina Sofia"),
                 (44,datetime.date(2022,9,1),datetime.date(2023,9,1),"Museum of Modern Art(New York)"),
                 (45,datetime.date(2022,9,1),datetime.date(2023,9,1),"Solomon R. Guggenheim Museum"),
                 (35,datetime.date(2022,9,1),datetime.date(2023,9,1),"Musée Picasso"),
                 (1,datetime.date(2022,12,1),datetime.date(2023,12,1),"Louvre"),
                 (12,datetime.date(2022,12,1),datetime.date(2023,12,1),"Uffizi"),
                 (13,datetime.date(2022,12,1),datetime.date(2023,12,1),"Uffizi"),
                 (27,datetime.date(2022,12,1),datetime.date(2023,12,1),"Louvre"),
                 (32,datetime.date(2022,12,1),datetime.date(2023,12,1),"British Museum"),
                 (33,datetime.date(2022,12,1),datetime.date(2023,12,1),"Uffizi"),
                 (46,datetime.date(2023,1,1),datetime.date(2024,1,1),"Gemäldegalerie Berlin"),
                 (47,datetime.date(2023,1,1),datetime.date(2024,1,1),"National Gallery (London)"),
                 (48,datetime.date(2023,1,1),datetime.date(2024,1,1),"National Gallery (London)"),
                 (49,datetime.date(2023,1,1),datetime.date(2024,1,1),"Uffizi"),
                 (50,datetime.date(2023,1,1),datetime.date(2024,1,1),"National Gallery (London)")]
    galleries =[("Uffizi",) , ("Hermitage",), ("Louvre",), ("British Museum",),("Museo del Prado",),
            ("National Gallery (London)",),("Museum of Modern Art(New York)",),("Museo Regionale (Messina)",),("Rijksmuseum",),
            ("Museo Reina Sofia",),("Solomon R. Guggenheim Museum",),("Musée Picasso",),("Gemäldegalerie Berlin",)]

    categories =[("Rennaisance",),
             ("Impressionism",),
             ("Modern",),
             ("Romanticism",),
             ("Surrealism",),
             ("Expressionism",),
             ("Baroque",)]

    positions=[("DISPLAY ROOM 1" , 101, False,True),
           ("DISPLAY ROOM 1" , 102, False,True),
           ("DISPLAY ROOM 1" , 103, False,True),
           ("DISPLAY ROOM 1" , 104, False,True),
           ("DISPLAY ROOM 1" , 105, False,True),
           ("DISPLAY ROOM 1" , 106, False,True),
           ("DISPLAY ROOM 1" , 107, False,True),
           ("DISPLAY ROOM 1" , 108, False,True),
           ("DISPLAY ROOM 1" , 109, False,True),
           ("DISPLAY ROOM 1" , 110, False,True),
           ("DISPLAY ROOM 1" , 111, False,True),
           ("DISPLAY ROOM 1" , 112, False,True),
           ("DISPLAY ROOM 1" , 113, False,True),
           ("DISPLAY ROOM 2" , 201, False,True),
           ("DISPLAY ROOM 2" , 202, False,True),
           ("DISPLAY ROOM 2" , 203, False,True),
           ("DISPLAY ROOM 2" , 204, False,True),
           ("DISPLAY ROOM 2" , 205, False,True),
           ("DISPLAY ROOM 2" , 206, False,True),
           ("DISPLAY ROOM 2" , 207, False,True),
           ("DISPLAY ROOM 2" , 208, False,True),
           ("DISPLAY ROOM 3" , 301, False,True),
           ("DISPLAY ROOM 3" , 302, False,True),
           ("DISPLAY ROOM 3" , 303, False,True),
           ("DISPLAY ROOM 3" , 304, False,True),
           ("DISPLAY ROOM 3" , 305, False,True),
           ("DISPLAY ROOM 3" , 306, False,True),
           ("DISPLAY ROOM 3" , 307, False,True),
           ("DISPLAY ROOM 3" , 308, False,True),
           ("EXHIBITION ROOM",1,False,True),
           ("EXHIBITION ROOM",2,False,True),
           ("EXHIBITION ROOM",3,False,True),
           ("EXHIBITION ROOM",4,False,True),
           ("EXHIBITION ROOM",5,False,True),
           ("EXHIBITION ROOM",6,False,True),
           ("WAREHOUSE 1",1,True,False),
           ("WAREHOUSE 1",2,True,False),
           ("WAREHOUSE 1",3,True,False),
           ("WAREHOUSE 1",4,True,False),
           ("WAREHOUSE 1",5,True,False),
           ("WAREHOUSE 1",6,True,False),
           ("WAREHOUSE 1",7,True,False),
           ("WAREHOUSE 1",8,True,False),
           ("WAREHOUSE 1",9,True,False),
           ("WAREHOUSE 1",10,True,False),
           ("WAREHOUSE 2",1,True,False),
           ("WAREHOUSE 2",2,True,False),
           ("WAREHOUSE 2",3,True,False),
           ("WAREHOUSE 2",4,True,False),
           ("WAREHOUSE 2",5,True,False),
           ("WAREHOUSE 2",6,True,False),
           ("WAREHOUSE 2",7,True,False),
           ("WAREHOUSE 2",8,True,False),
           ("WAREHOUSE 2",9,True,False),
           ("WAREHOUSE 2",10,True,False)]

    artists = [
        (1,"Leonardo","Da Vinci","Italian"),
        (2,"Claude","Monet","French"),
        (3,"Vincent","Van Gogh", "Dutch"),
        (4,"Jackson","Pollock","American"),
        (5,"Sandro","Botticelli","Italian"),
        (6,"Salvador","Dali","Spanish"),
        (7,"Domenikos","Theotokopoulos","Greek"),
        (8,"Andy","Warhol","American"),
        (9,"Jan","van Eyck","Dutch"),
        (10,"Eugene","Delacroix","French"),
        (11,"Michelangelo",None,"Italian"),
        (12,"Caravaggio",None,"Italian"),
        (13,"Raphael",None,"Italian"),
        (14,"Pablo","Picasso","Spanish"),
        (15,"Andrea","del Verrochio","Italian"),
        (16,"Joan","Miro","Spanish"),
        (17,"Rembrandt",None,"Dutch"),
        (18,"Edvard","Munch","Norwegian"),
        (19,"Nikos", "Eggonopoylos","Greek"),
        (20,"Nikiforos","Lytras","Greek")
        ]



    paintings=[
	(1,"Mona Lisa",1503,"Rennaisance",1,"EXHIBITION ROOM",1),
        (2,"Lady with an Ermine",1489,"Rennaisance",1,"DISPLAY ROOM 1",108),
	(3,"Starry Night",1889,"Impressionism",3,"DISPLAY ROOM 2",203),
	(4,"The Potato Eaters",1885,"Impressionism",3,"DISPLAY ROOM 2",204),
	(5,"Van Gogh self-portrait",1889,"Impressionism",3,"DISPLAY ROOM 2",205),
	(6,"Liberty Leading the People",1830,"Romanticism",10,"DISPLAY ROOM 2",201),
	(7,"The Massacre at Chios",1824,"Romanticism",10,"DISPLAY ROOM 2",202),
	(8,"Wild Poppies",1873,"Impressionism",2,"WAREHOUSE 1",1),
	(9,"Impression, Sunrise",1873,"Impressionism",2,"WAREHOUSE 1",2),
	(10,"Convergence",1952,"Modern",4,"DISPLAY ROOM 3" , 301),
	(11,"Mural",1943,"Modern",4,"DISPLAY ROOM 3" , 302),
        (12,"The Birth of Venus",1486,"Rennaisance",5,"EXHIBITION ROOM",2),
        (13,"Primavera",1480,"Rennaisance",5,"EXHIBITION ROOM",3),
        (14,"The Disrobing of Christ",1579,"Rennaisance",7,"DISPLAY ROOM 1",107),
	(15,"The Adoration of the Shepherds",1614,"Rennaisance",7,"DISPLAY ROOM 1",106),
	(16,"Shot Marilyns",1964,"Modern",8,"DISPLAY ROOM 3",303),
	(17,"Campbell's Soup Cans",1962,"Modern",8,"DISPLAY ROOM 3",304),
        (18,"The Persistence of Memory",1931,"Surrealism",6,"DISPLAY ROOM 3",305),
        (19,"The Disintegration of the Persistence of Memory",1954,"Surrealism",6,"DISPLAY ROOM 3",306),
        (20,"Guernica",1937,"Surrealism",14,"DISPLAY ROOM 3",307),
        (21,"The Old Guitarist",1904,"Expressionism",14,"DISPLAY ROOM 3",308),
        (22,"The Scream",1893,"Expressionism",18,"DISPLAY ROOM 2",206),
        (23,"Love and Pain",1895,"Expressionism",18,"DISPLAY ROOM 2",207),
        (24,"The Night Watch",1642,"Baroque",17,"WAREHOUSE 1",3),
        (25,"The Return of the Prodigal Son",1669,"Baroque",17,"WAREHOUSE 1",4),
        (26,"Virgin and Child with Canon van der Paele",1434,"Rennaisance",9,"DISPLAY ROOM 1",109),
        (27,"Madonna of Chancellor Rolin",1435,"Rennaisance",9,"EXHIBITION ROOM",4),
        (28,"Portrait of Jan de Leeuw", 1436, "Rennaisance",9,"WAREHOUSE 1",5),
        (29,"The Taddei Tondo", 1502,"Rennaisance",11,"DISPLAY ROOM 1" , 101),
        (30,"Madonna of Bruges", 1504,"Rennaisance",11,"DISPLAY ROOM 1" , 102),
        (31,"The Doni Tondo", 1504,"Rennaisance",11,"DISPLAY ROOM 1" , 103),
        (32,"Antique warrior in profile",1472,"Rennaisance",1,"EXHIBITION ROOM",5),
        (33,"The Annunciation", 1609,"Rennaisance", 1,"EXHIBITION ROOM",6),
        (34,"The Supper at Emmaus",1601,"Baroque", 12,"WAREHOUSE 1",6),
        (35,"Portrait of Dora Maar",1937,"Surrealism",14,"WAREHOUSE 1",7),
        (36,"The Raising of Lazarus",1609,"Baroque", 12,"WAREHOUSE 1",8),
        (37,"The Seven Works of Mercy",1607,"Baroque", 12,"WAREHOUSE 1",9 ),
        (38,"The Ansidei Madonna",1505,"Rennaisance",13,"DISPLAY ROOM 1" , 104),
        (39,"The Madonna of the Meadow",1506,"Rennaisance",13,"DISPLAY ROOM 1" , 105),
        (40,"Saint Catherine of Alexandria",1507,"Rennaisance",13,"DISPLAY ROOM 1" , 110),
        (41,"Deposition of Christ",1507,"Rennaisance",13,"DISPLAY ROOM 1" , 111),
        (42,"Madonna of the Pinks",1506,"Rennaisance",13,"DISPLAY ROOM 1" , 112),
        (43,"Pastoral",1924,"Surrealism",16,"WAREHOUSE 1",10),
        (44,"Catalan Landscape",1923,"Surrealism",16,"WAREHOUSE 2",1),
        (45,"The Tilled Field",1923,"Surrealism",16,"WAREHOUSE 2",2),
        (46,"Madonna and Child",1488,"Rennaisance",15,"WAREHOUSE 2",3),
        (47,"Virgin and Child with Two Angels",1478,"Rennaisance",15,"WAREHOUSE 2",4),
        (48,"Adoration of the Child",1484,"Rennaisance",15,"WAREHOUSE 2",5),
        (49,"Baptism of Christ",1473,"Rennaisance",15,"WAREHOUSE 2",6),
        (50,"Tobias and the Angel",1480,"Rennaisance",15,"WAREHOUSE 2",7),
        (51,"Gamos",1957,"Modern",19,None,None),
        (52,"Odisseys kai kalypso",1956,"Modern",19,None,None),
        (53,"Arravones",1954,"Modern",19,None,None),
        (54,"O Galatas",1895,"Modern",20,None,None),
        (55,"I Antigoni Empros sto Nekro Polyneiki",1865,"Modern",20,None,None),
        (56,"Kalanta",1872,"Modern",20,None,None),
        
        ]

    exhibitions=[(1,"Baroque Period",datetime.date(2022,6,1),datetime.date(2022,8,31)),
            (2,"Joan Miro",datetime.date(2022,9,1),datetime.date(2022,12,1)),
            (3,"Rennaisance Painters",datetime.date(2022,12,1),datetime.date(2023,2,28)),
            (4,"Andrea del Verocchio",datetime.date(2023,3,1),datetime.date(2023,5,31)),
            (5,"Surrealist Ideas",datetime.date(2023,6,1),datetime.date(2023,8,31))]

    onview=[(1,34),(1,36),(1,25),(1,24),
        (2,43),(2,44),(2,45),
        (3,1),(3,12),(3,13),(3,27),(3,32),(3,33),
        (4,46),(4,47),(4,48),(4,49),(4,50),
        (5,43),(5,44),(5,45),(5,35)]
    try:
        conn.executemany("INSERT INTO Painting VALUES (?,?,?,?,?,?,?)",paintings)#Insert from a list of tuples
        conn.executemany("INSERT INTO Artist VALUES (?,?,?,?)",artists)
        conn.executemany("INSERT INTO ArtPeriod VALUES (?)",categories)
        conn.executemany("INSERT INTO Exhibition VALUES (?,?,?,?)",exhibitions)
        conn.executemany("INSERT INTO Associate_Gallery VALUES (?)",galleries)
        conn.executemany("INSERT INTO Owned VALUES (?)",Idioktitos)
        conn.executemany("INSERT INTO Loan VALUES (?,?,?,?)",loanedpaintings)
        conn.executemany("INSERT INTO Position VALUES (?,?,?,?)",positions)
        conn.executemany("INSERT INTO Takes VALUES (?,?,?,?)",loanedto)
        conn.executemany("INSERT INTO IsDisplayed VALUES (?,?)",onview)
        conn.commit()
        print("Data Inserted Succesfully\n")
        time.sleep(2)
    except:
       print("Data already inserted") #try except to manage a second run of the app
       time.sleep(2)



def createdatabase():
    global conn
    conn=sqlite3.connect("ArtMuseum.db") # table definitions
    table1="""CREATE TABLE Painting ( 
	artid INTEGER ,
	Title varchar NOT NULL,
	Creationyear INTEGER,
	ArtPeriod_name varchar,
	ArtistID integer,
	Room varchar,
	Pos_no integer,
	PRIMARY KEY (artid) ,
	FOREIGN KEY (ArtPeriod_name) REFERENCES ArtPeriod(Name)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (ArtistID) REFERENCES Artist(ID)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (Room,Pos_no) REFERENCES Position(Room,Pos_no)
	ON	DELETE	SET NULL	ON	UPDATE		CASCADE,
        UNIQUE(Room, Pos_no),
        UNIQUE(Title,ArtistID)
);"""
    table2="""CREATE TABLE Artist (
	ID INTEGER ,
	Name varchar NOT NULL,
	Surname varchar,
	Nationality varchar,
	PRIMARY KEY (ID),
	UNIQUE(Name,Surname)
);"""
    table3="""CREATE TABLE ArtPeriod (
	Name varchar,
	PRIMARY KEY (Name)
);"""
    table4="""CREATE TABLE Exhibition (
	ID INTEGER ,
	Subject varchar NOT NULL,
	StartDate date NOT NULL,
	EndDate date NOT NULL,
	PRIMARY KEY (ID),
	CONSTRAINT dates CHECK (StartDate<EndDate)
);"""
    table5="""CREATE TABLE Associate_Gallery (
	Name varchar, 
	PRIMARY KEY (Name)
);"""
    table6="""CREATE TABLE Owned (
	artid integer,
	PRIMARY KEY(artid),
	FOREIGN KEY (artid) REFERENCES Painting(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE
);
"""
    table7="""CREATE TABLE Loan (
	artid integer,
	LoanStart date NOT NULL,
	LoanEnd date NOT NULL,
	OriginName varchar NOT NULL,
	PRIMARY KEY (artid),
	FOREIGN KEY(artid) REFERENCES Painting(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (OriginName) REFERENCES Associate_Gallery(Name)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	CONSTRAINT dates CHECK (LoanStart<LoanEnd)
	
);"""
    table8="""CREATE TABLE Position (
	Room varchar,
	Pos_no integer,
	Storage boolean,
	In_Display boolean,
	PRIMARY KEY (Room,Pos_no),
	CONSTRAINT TWOPLACE CHECK (Storage <> In_Display)
);"""
    table9="""CREATE TABLE Takes (
	artid integer ,
	BorrowerName VARCHAR,
	LoanStart date NOT NULL,
	LoanEnd date NOT NULL,
	PRIMARY KEY (artid, BorrowerName),
	FOREIGN KEY (artid) REFERENCES Owned(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (BorrowerName) REFERENCES Associate_Gallery(Name)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	CONSTRAINT dates CHECK (LoanStart<LoanEnd)
);"""
    table10="""CREATE TABLE IsDisplayed (
	ExhibitionId integer,
	artid integer,
	PRIMARY KEY (artid, ExhibitionId),
	FOREIGN KEY (artid) REFERENCES Loan(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (ExhibitionId) REFERENCES Exhibition(ID)
	ON	DELETE CASCADE		ON	UPDATE		CASCADE
);"""
    try:
        conn.execute(table1) #table creations
        conn.execute(table2)
        conn.execute(table3)
        conn.execute(table4)
        conn.execute(table5)
        conn.execute(table6)
        conn.execute(table7)
        conn.execute(table8)
        conn.execute(table9)
        conn.execute(table10)
        print("Art Museum DataBase Succesfully Created")
        time.sleep(2)
    except:
        print("DB Already Created")
        time.sleep(2)
    
def insertrec():
    global curr,conn
    os.system('cls')
    curr=conn.cursor() #insert main menu
    x=input("""1)Insert Painting
2)Insert Exhibition
3)Insert Given painting
4)Insert Position
5)Insert Displayed Painting
6)Insert Associate Gallery\n""")
    if(x=="1"):
        try:
            os.system('cls')
            Title = input("The name of the Painting:\n")
            Creationyear = int(input("The creation year of the painting:\n"))
            ArtPeriod_name = input("The art period name of the painting:\n")
            curr.execute("SELECT distinct ArtPeriod_name from Painting join ArtPeriod on Name = ArtPeriod_name WHERE ArtPeriod_name='"+ArtPeriod_name+"';")
            res = curr.fetchone()
            if(res==None):
                print("The art period does not exist you must also insert it to the Data\n") #in order to insert a painting first insert its period name and artisti into the db
                ArtPeriod_name = input("The art period name of the painting:\n")
                conn.execute("INSERT INTO ArtPeriod(Name) VALUES(?)",(ArtPeriod_name,))
                conn.commit()           
            else:
                ArtPeriod_name = res[0]        
            Artist_name = input("Give the artist name:\n")            
            curr.execute("SELECT distinct ArtistID from Painting join Artist on ID=ArtistID WHERE (Name||' '||COALESCE(Surname,''))='" +Artist_name+"';")
            res = curr.fetchone()
            if(res==None):
                print("The artist does not exist you must also insert him to the data base\n")
                Artist_name = input("Give the artist first name:\n")
                Artist_surname = input("Give the artist surname:\n")    
                Artist_nat= input("Give the artist nationality\n")
                conn.execute("INSERT INTO Artist (ID,Name,Surname,nationality) VALUES(?,?,?,?)",(None,Artist_name,Artist_surname,Artist_nat))
                conn.commit()
                curr.execute("SELECT ID FROM Artist WHERE (Name||' '||COALESCE(Surname,''))= '" +Artist_name+" "+Artist_surname+"';")
                res = curr.fetchone()
                Artid = res[0]          
            else:
                Artid = res[0] 
            room = input("Give The Room of the Painting:\n").upper()
            pos_no =input("Give the position number of the painting:\n")
            if(room=="" and pos_no==""): #do not put painting in any available position
                room=None
                pos_no=None
            else:
                no=int(pos_no)
            conn.execute("INSERT into Painting (artid,Title, Creationyear, ArtPeriod_name, ArtistID, Room, Pos_no) VALUES(?,?,?,?,?,?,?)",(None,Title,Creationyear,ArtPeriod_name,Artid,room,pos_no))
            conn.commit()
            print("Successfully Inserted\n")
            curr.execute("SELECT artid FROM PAINTING where Title='"+Title+"';")
            res=curr.fetchone()
            artid=res[0]
            q=input("Is the painting loaned ? (y/n)\n") #check if the painting is owned by us in order to put it in the correct table
            if(q=="y" or q=="Y"):
                startyear=int(input("Desired start year:\n"))
                startmonth=int(input("Desired start month:\n"))
                startday=int(input("Desired start day:\n"))
                endyear=int(input("Desired end year:\n"))
                endmonth=int(input("Desired end month:\n"))
                endday=int(input("Desired end day:\n"))
                gall=input("Desired gallery:\n")
                curr.execute("SELECT Name FROM Associate_Gallery WHERE Name='"+gall+"';")
                res=curr.fetchone()
                if(res==None):
                    conn.execute("INSERT INTO Associate_Gallery(Name) VALUES(?)",(gall,))
                conn.execute("INSERT INTO Loan(artid,LoanStart,LoanEnd,OriginName) VALUES (?,?,?,?)",(artid,datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday),gall))
                conn.commit()
            elif(q=="n" or q=="N"):
                conn.execute("INSERT INTO Owned(artid) VALUES(?)",(artid,))
                conn.commit()
        except:
            print("Wrong Values.")    
    elif(x=="2"):
        try:
            os.system('cls')
            startyear=int(input("Desired start year:\n")) #new exhibition
            startmonth=int(input("Desired start month:\n"))
            startday=int(input("Desired start day:\n"))
            endyear=int(input("Desired end year:\n"))
            endmonth=int(input("Desired end month:\n"))
            endday=int(input("Desired end day:\n"))
            subject=input("Desired subject:\n")
            conn.execute("INSERT INTO Exhibition (ID,Subject,StartDate,EndDate) VALUES (?,?,?,?)",(None,subject,datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday)))
            conn.commit()
        except:
            print("Wrong Value.")
    elif(x=="3"):
        try:
            os.system('cls')
            startyear=int(input("Desired start year:\n")) 
            startmonth=int(input("Desired start month:\n"))
            startday=int(input("Desired start day:\n"))
            endyear=int(input("Desired end year:\n"))
            endmonth=int(input("Desired end month:\n"))
            endday=int(input("Desired end day:\n"))
            title = input("Desired painting name:\n")
            curr.execute("Select artid from Painting natural join Owned where title = '"+ title+"';") #loan one of the owned paintings to another gallery
            res = curr.fetchone()
            if(res==None):
                print("No Such Owned Painting\n")
            else:
                artid = res[0]
                origin=input("Desired gallery:\n")
                conn.execute("INSERT INTO Takes (BorrowerName,LoanStart,LoanEnd,artid) VALUES(?,?,?,?)",(origin,datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday),artid))
                conn.commit()
        except:
            print("Wrong Value")
    elif(x=="4"):
       
        os.system('cls')
        room=input("Enter Room to be inserted:\n").upper()
        posno=int(input("Enter position number to be inserted:\n")) #new position
        boole=input("Is inserted position a display position ?(y/n)")
        if(boole=="y" or boole=="Y"):
            conn.execute("INSERT INTO Position(Room,Pos_no,Storage,In_Display) Values (?,?,?,?)",(room,posno,False,True))
            conn.commit()
        else:
            conn.execute("INSERT INTO Position(Room,Pos_no,Storage,In_Display) Values (?,?,?,?)",(room,posno,True,False))
            conn.commit()

    elif(x=="5"):
        try:
            os.system('cls')
            art=input("Enter desired art to be displayed:\n")#new displayed painting at exhibition
            exh=input("Enter desired exhibition:\n")
            curr.execute("Select artid from Loan natural join Painting where Title='"+art+"';")
            id1=curr.fetchone()
            if(id1==None):
                print("No such Loaned Painting to be displayed\n")
            else:
                artid=id1[0]
                curr.execute("Select ID from Exhibition where Subject='"+exh+"';")
                id2=curr.fetchone()
                if(id2==None):
                    print("No such Exhibition\n")
                else:    
                    exhid=id2[0]
                    conn.execute("INSERT INTO IsDisplayed(artid,ExhibitionId) VALUES (?,?)",(artid,exhid))
                    conn.commit()
        except:
            print("Wrong Values")
    elif(x=="6"):
        try:
            os.system('cls') #new associate galley
            gall=input("Enter Gallery to be inserted:")
            conn.execute("INSERT INTO Associate_Gallery(Name) Values (?)",(gall,))
            conn.commit()
        except:
            print("Wrong Value")
def updaterec():
    global curr,conn
    curr=conn.cursor()
    os.system('cls')
    conn.execute("PRAGMA foreign_keys = ON") #enforce foreign key constraints
    x=input("""1)Update Painting
2)Update Exhibitions
3)Update Loaned Paintings
4)Update Given paintings\n""")
    if(x=="1"):
        try:
            os.system('cls')
            i=input("Enter Painting Title to update:\n")
            ct=int(input("Desired year to update:\n"))
            ArtPeriod_name = input("The art period name of the painting:\n")
            curr.execute("SELECT distinct ArtPeriod_name from Painting join ArtPeriod on Name = ArtPeriod_name WHERE ArtPeriod_name='"+ArtPeriod_name+"';")
            res = curr.fetchone()
            if(res==None):
                print("The art period does not exist you must also insert it to the Data\n")
                ArtPeriod_name = input("The art period name of the painting:\n")
                conn.execute("INSERT INTO ArtPeriod(Name) VALUES(?)",(ArtPeriod_name,))
                conn.commit()           
            else:
                ArtPeriod_name = res[0]        
            Artist_name = input("Give the artist name:\n")            
            curr.execute("SELECT distinct ArtistID from Painting join Artist on ID=ArtistID WHERE (Name||' '||COALESCE(Surname,''))='" +Artist_name+"';")#in order to use an artist or an art period, they must first be inserted into the db if they do not already exist
            res = curr.fetchone()
            if(res==None):
                print("The artist does not exist you must also insert him to the data base\n")
                Artist_name = input("Give the artist first name:\n")
                Artist_surname = input("Give the artist surname:\n")    
                Artist_nat= input("Give the artist nationality\n")
                conn.execute("INSERT INTO Artist (ID,Name,Surname,nationality) VALUES(?,?,?,?)",(None,Artist_name,Artist_surname,Artist_nat))
                conn.commit()
                curr.execute("SELECT ID FROM Artist WHERE (Name||' '||COALESCE(Surname,''))= '" +Artist_name+" "+Artist_surname+"';")
                res = curr.fetchone()
                Artid = res[0]          
            else:
                Artid = res[0] 
            room=input("Desired room(Press enter for none):\n").upper()
            no=input("Desired position number(Press enter for none):\n")
            if(room=="" and no==""): #do not put painting in any available position
                room=None
                no=None
            else:
                no=int(no)
            conn.execute("Update Painting Set Creationyear=?,Artperiod_name=?,Room=?,Pos_no=?,ArtistID=? where Title='"+i+"';",(ct,ArtPeriod_name,room,no,Artid))
            conn.commit()
        except:
            print("Wrong values")
    elif(x=="2"):
        try:
            os.system('cls')
            startyear=int(input("Desired start year:\n"))
            startmonth=int(input("Desired start month:\n"))#update exhibition info
            startday=int(input("Desired start day:\n"))
            endyear=int(input("Desired end year:\n"))
            endmonth=int(input("Desired end month:\n"))
            endday=int(input("Desired end day:\n"))
            subjectold=input("Desired old subject to find:\n")
            subjectnew=input("Desired subject new subject to update:\n")
            conn.execute("Update Exhibition Set StartDate=?,EndDate=? where Subject='"+subjectold+"';",(datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday)))
            conn.commit()
        except:
            print("Wrong values")
    elif(x=="3"):
        try:
            os.system('cls')
            startyear=int(input("Desired start year:\n"))
            startmonth=int(input("Desired start month:\n"))
            startday=int(input("Desired start day:\n"))
            endyear=int(input("Desired end year:\n"))#update loan info
            endmonth=int(input("Desired end month:\n"))
            endday=int(input("Desired end day:\n"))
            title=input("Desired art title:\n")
            curr.execute("Select artid from Painting natural join Loan where title = '"+ title+"';")
            res=curr.fetchone()
            if (res==None):
                print("No such painting to update")
            else:
                origin=input("Desired gallery:\n")
                curr.execute("SELECT Name FROM Associate_Gallery WHERE Name='"+origin+"';")#insert associate gallery if it does not exist in the db
                res=curr.fetchone()
                if(res==None):
                    conn.execute("INSERT INTO Associate_Gallery(Name) VALUES(?)",(origin,))
                    conn.commit()
                conn.execute("Update Loan Set OriginName=?,LoanStart=?,LoanEnd=? where artid='"+artid+"';",(origin,datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday)))
                conn.commit()
        except:
            print("Wrong values")
    elif(x=="4"):
        try:
            os.system('cls')
            startyear=int(input("Desired start year:\n"))
            startmonth=int(input("Desired start month:\n"))
            startday=int(input("Desired start day:\n"))
            endyear=int(input("Desired end year:\n"))
            endmonth=int(input("Desired end month:\n"))
            endday=int(input("Desired end day:\n"))
            title=input("Desired art title:\n")
            curr.execute("Select artid from Painting natural join Owned natural join Takes where title = '"+ title+"';")
            res=curr.fetchone()
            if (res==None):
                print("No such painting to update")
            else:
                borr=input("Desired gallery:\n")
                curr.execute("SELECT Name FROM Associate_Gallery WHERE Name='"+borr+"';")
                res=curr.fetchone()
                if(res==None):
                    conn.execute("INSERT INTO Associate_Gallery(Name) VALUES(?)",(borr,))
                    conn.commit()
                conn.execute("Update Takes Set BorrowerName=?,LoanStart=?,LoanEnd=? where artid='"+artid+"';",(borr,datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday)))
                conn.commit()
        except:
            print("Wrong values")
def deleterec():
    global curr,conn
    curr=conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON")#enforce foreign key constraints
    x=input("""1)Delete Painting
2)Delete Artist
3)Delete Exhibition
4)Delete Loaned Painting
5)Delete Given painting
6)Delete Position
7)Delete Displayed Painting\n""")
    if(x=="1"):
        os.system('cls')
        z=input("Desired Painting Title to delete:\n")
        try:
            curr.execute(" Delete from Painting where Title = ?;",(z,))
            conn.commit()
        except:
            print("Wrong value")
    elif(x=="2"):
        os.system('cls')
        z=input("Desired Artist Name to delete:\n")
        try:
            curr.execute(" Delete from Artist where (Name||' '||COALESCE(Surname,'') = ?;",(z,))#delete artist and all associated paintings
            conn.commit()
        except:
            print("Wrong value")
    elif(x=="3"):
        os.system('cls')
        z=int(input("Desired Exhibition Subject to delete:\n"))
        try:
            curr.execute(" Delete from Exhibition where Subject = ?;",(z,))#delete exhibition and all associate to be displayed paintings from db
            conn.commit()
        except:
            print("Wrong value")
    elif(x=="4"):
        os.system('cls')
        z=input("Desired Painting title to delete:\n")
        try:
            curr.execute("Delete from Loan where artid in (SELECT artid FROM Loan natural join Painting where Title = ?);",(z,))#delete a loan 
            curr.execute("Update Painting Set Room = NULL , Pos_no = NULL where Title = '"+z+"';")
            conn.commit()
        except:
            print("Wrong Value")
            
    
    elif(x=="5"):
        os.system('cls')
        z=input("Desired Given Painting Title to delete:\n")
        try:
            curr.execute(" Delete from  Takes WHERE artid in(SELECT artid FROM Painting natural join Owned natural join Takes where Title= ?);",(z,))#delete a taken
            room=input("Desired room(Press enter for none):\n").upper()
            no=input("Desired position number(Press enter for none):\n")
            if(room=="" and no==""): #do not put painting in any available position
                room=None
                no=None
            else:
                no=int(no)
            conn.execute("Update Painting Set Room=?,Pos_no where Title='"+z+"';",(room,no))
            conn.commit()
        except:
            print("Wrong value")
    elif(x=="6"):
        os.system('cls')
        z=input("Desired Room  to delete:\n").upper()
        y=int(input("Desired Room position to delete:\n"))#delete a position
        try:
            curr.execute(" Delete from Position where Room=? AND Pos_no=?;",(z,y))
            conn.commit()
        except:
            print("Wrong value")
    elif(x=="7"):
        os.system('cls')
        z=input("Desired Display Painting Title to delete:\n")#delete a displayed
        try:
            curr.execute(" Delete from IsDisplayed WHERE artid in (SELECT artid FROM Painting natural join Loan natural join IsDisplayed where Title= ?);",(z,))
            conn.commit()
        except:
            print("Wrong value")
        
    
def menu():
    while True:
        os.system('cls')#application main menu 
        x=input("1)Add new record\n2)Update Record\n3)Delete Record\n4)Exit\n")
        if(x=="1"):
            os.system('cls')
            insertrec()
        elif(x=="2"):
            os.system('cls')
            updaterec()
        elif(x=="3"):
            os.system('cls')
            deleterec()
        elif(x=="4"):
            os.system('cls')
            print("Have a nice day.")
            conn.close()
            time.sleep(2)
            break
        else:
            print("Wrong input. Try again.\n")

if __name__=="__main__":
    createdatabase()
    load_data()
    menu()
