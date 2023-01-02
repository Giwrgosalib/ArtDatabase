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
        (None,"Leonardo","Da Vinci","Italian"),
        (None,"Claude","Monet","French"),
        (None,"Vincent","Van Gogh", "Dutch"),
        (None,"Jackson","Pollock","American"),
        (None,"Sandro","Botticelli","Italian"),
        (None,"Salvador","Dali","Spanish"),
        (None,"Domenikos","Theotokopoulos","Greek"),
        (None,"Andy","Warhol","American"),
        (None,"Jan","van Eyck","Dutch"),
        (None,"Eugene","Delacroix","French"),
        (None,"Michelangelo",None,"Italian"),
        (None,"Caravaggio",None,"Italian"),
        (None,"Raphael",None,"Italian"),
        (None,"Pablo","Picasso","Spanish"),
        (None,"Andrea","del Verrochio","Italian"),
        (None,"Joan","Miro","Spanish"),
        (None,"Rembrandt",None,"Dutch"),
        (None,"Edvard","Munch","Norwegian"),
        (None,"Nikos", "Eggonopoylos","Greek"),
        (None,"Nikiforos","Lytras","Greek")
        ]



    paintings=[
	(None,"Mona Lisa",1503,"Rennaisance",1,"EXHIBITION ROOM",1),
        (None,"Lady with an Ermine",1489,"Rennaisance",1,"DISPLAY ROOM 1",108),
	(None,"Starry Night",1889,"Impressionism",3,"DISPLAY ROOM 2",203),
	(None,"The Potato Eaters",1885,"Impressionism",3,"DISPLAY ROOM 2",204),
	(None,"Van Gogh self-portrait",1889,"Impressionism",3,"DISPLAY ROOM 2",205),
	(None,"Liberty Leading the People",1830,"Romanticism",10,"DISPLAY ROOM 2",201),
	(None,"The Massacre at Chios",1824,"Romanticism",10,"DISPLAY ROOM 2",202),
	(None,"Wild Poppies",1873,"Impressionism",2,"WAREHOUSE 1",1),
	(None,"Impression, Sunrise",1873,"Impressionism",2,"WAREHOUSE 1",2),
	(None,"Convergence",1952,"Modern",4,"DISPLAY ROOM 3" , 301),
	(None,"Mural",1943,"Modern",4,"DISPLAY ROOM 3" , 302),
        (None,"The Birth of Venus",1486,"Rennaisance",5,"EXHIBITION ROOM",2),
        (None,"Primavera",1480,"Rennaisance",5,"EXHIBITION ROOM",3),
        (None,"The Disrobing of Christ",1579,"Rennaisance",7,"DISPLAY ROOM 1",107),
	(None,"The Adoration of the Shepherds",1614,"Rennaisance",7,"DISPLAY ROOM 1",106),
	(None,"Shot Marilyns",1964,"Modern",8,"DISPLAY ROOM 3",303),
	(None,"Campbell's Soup Cans",1962,"Modern",8,"DISPLAY ROOM 3",304),
        (None,"The Persistence of Memory",1931,"Surrealism",6,"DISPLAY ROOM 3",305),
        (None,"The Disintegration of the Persistence of Memory",1954,"Surrealism",6,"DISPLAY ROOM 3",306),
        (None,"Guernica",1937,"Surrealism",14,"DISPLAY ROOM 3",307),
        (None,"The Old Guitarist",1904,"Expressionism",14,"DISPLAY ROOM 3",308),
        (None,"The Scream",1893,"Expressionism",18,"DISPLAY ROOM 2",206),
        (None,"Love and Pain",1895,"Expressionism",18,"DISPLAY ROOM 2",207),
        (None,"The Night Watch",1642,"Baroque",17,"WAREHOUSE 1",3),
        (None,"The Return of the Prodigal Son",1669,"Baroque",17,"WAREHOUSE 1",4),
        (None,"Virgin and Child with Canon van der Paele",1434,"Rennaisance",9,"DISPLAY ROOM 1",109),
        (None,"Madonna of Chancellor Rolin",1435,"Rennaisance",9,"EXHIBITION ROOM",4),
        (None,"Portrait of Jan de Leeuw", 1436, "Rennaisance",9,"WAREHOUSE 1",5),
        (None,"The Taddei Tondo", 1502,"Rennaisance",11,"DISPLAY ROOM 1" , 101),
        (None,"Madonna of Bruges", 1504,"Rennaisance",11,"DISPLAY ROOM 1" , 102),
        (None,"The Doni Tondo", 1504,"Rennaisance",11,"DISPLAY ROOM 1" , 103),
        (None,"Antique warrior in profile",1472,"Rennaisance",1,"EXHIBITION ROOM",5),
        (None,"The Annunciation", 1609,"Rennaisance", 7,"EXHIBITION ROOM",6),
        (None,"The Supper at Emmaus",1601,"Baroque", 12,"WAREHOUSE 1",6),
        (None,"Portrait of Dora Maar",1937,"Surrealism",14,"WAREHOUSE 1",7),
        (None,"The Raising of Lazarus",1609,"Baroque", 12,"WAREHOUSE 1",8),
        (None,"The Seven Works of Mercy",1607,"Baroque", 12,"WAREHOUSE 1",9 ),
        (None,"The Ansidei Madonna",1505,"Rennaisance",13,"DISPLAY ROOM 1" , 104),
        (None,"The Madonna of the Meadow",1506,"Rennaisance",13,"DISPLAY ROOM 1" , 105),
        (None,"Saint Catherine of Alexandria",1507,"Rennaisance",13,"DISPLAY ROOM 1" , 110),
        (None,"Deposition of Christ",1507,"Rennaisance",13,"DISPLAY ROOM 1" , 111),
        (None,"Madonna of the Pinks",1506,"Rennaisance",13,"DISPLAY ROOM 1" , 112),
        (None,"Pastoral",1924,"Surrealism",16,"WAREHOUSE 1",10),
        (None,"Catalan Landscape",1923,"Surrealism",16,"WAREHOUSE 2",1),
        (None,"The Tilled Field",1923,"Surrealism",16,"WAREHOUSE 2",2),
        (None,"Madonna and Child",1488,"Rennaisance",15,"WAREHOUSE 2",3),
        (None,"Virgin and Child with Two Angels",1478,"Rennaisance",15,"WAREHOUSE 2",4),
        (None,"Adoration of the Child",1484,"Rennaisance",15,"WAREHOUSE 2",5),
        (None,"Baptism of Christ",1473,"Rennaisance",15,"WAREHOUSE 2",6),
        (None,"Tobias and the Angel",1480,"Rennaisance",15,"WAREHOUSE 2",7),
        (None,"Gamos",1957,"Modern",19,None,None),
        (None,"Odisseys kai kalypso",1956,"Modern",19,None,None),
        (None,"Arravones",1954,"Modern",19,None,None),
        (None,"O Galatas",1895,"Modern",20,None,None),
        (None,"I Antigoni Empros sto Nekro Polyneiki",1865,"Modern",20,None,None),
        (None,"Kalanta",1872,"Modern",20,None,None),
        
        ]

    exhibitions=[(None,"Baroque Period",datetime.date(2022,6,1),datetime.date(2022,8,31)),
            (None,"Joan Miro",datetime.date(2022,9,1),datetime.date(2022,12,1)),
            (None,"Rennaisance Painters",datetime.date(2022,12,1),datetime.date(2023,2,28)),
            (None,"Andrea del Verocchio",datetime.date(2023,3,1),datetime.date(2023,5,31)),
            (None,"Surrealist Ideas",datetime.date(2023,6,1),datetime.date(2023,8,31))]

    onview=[(1,34),(1,36),(1,25),(1,24),
        (2,43),(2,44),(2,45),
        (3,1),(3,12),(3,13),(3,27),(3,32),(3,33),
        (4,46),(4,47),(4,48),(4,49),(4,50),
        (5,43),(5,44),(5,45),(5,35)]
    try:
        conn.executemany("INSERT INTO Painting VALUES (?,?,?,?,?,?,?)",paintings)
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
    except:
       print("Data already inserted")



def createdatabase():
    global conn
    conn=sqlite3.connect("ArtMuseum.db")
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
        UNIQUE(Room, Pos_no)
);"""
    table2="""CREATE TABLE Artist (
	ID INTEGER ,
	Name varchar NOT NULL,
	Surname varchar,
	Nationality varchar,
	PRIMARY KEY (ID) 
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
	artid integer,
	ExhibitionId integer,
	PRIMARY KEY (artid, ExhibitionId),
	FOREIGN KEY (artid) REFERENCES Loan(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (ExhibitionId) REFERENCES Exhibition(ID)
	ON	DELETE CASCADE		ON	UPDATE		CASCADE
);"""
    try:
        conn.execute(table1)
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
    except:
        print("DB Already Created")
    
def insertrec():
    global curr,conn
    os.system('cls')
    curr=conn.cursor()
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
                print("The art period does not exist you must also insert it to the Data\n")
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
            room = input("Give The Room of the Painting:\n")
            pos_no = int(input("Give the position number of the painting:\n"))
            conn.execute("INSERT into Painting (artid,Title, Creationyear, ArtPeriod_name, ArtistID, Room, Pos_no) VALUES(?,?,?,?,?,?,?)",(None,Title,Creationyear,ArtPeriod_name,Artid,room,pos_no))
            conn.commit()
            print("Successfully Inserted\n")
            curr.execute("SELECT artid FROM PAINTING where Title='"+Title+"';")
            res=curr.fetchone()
            artid=res[0]
            q=input("Is the painting loaned ? (y/n)\n")
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
                conn.execute("INSERT INTO Loan(artid,LoanStart,LoanEnd,OriginName) VALUES (?,?,?,?)",artid,datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday),gall)
                conn.commit()
            elif(q=="n" or q=="N"):
                conn.execute("INSERT INTO Owned(artid) VALUES(?)",(artid,))
                conn.commit()
        except:
            print("Wrong Values.")    
    elif(x=="2"):
        try:
            os.system('cls')
            startyear=int(input("Desired start year:\n"))
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
            curr.execute("Select artid from Painting natural join Owned where title = '"+ Title+"';")
            res = curr.fetchone()
            if(res==None):
                print("No Such Owned Painting\n")
            else:
                artid = res[0]
                origin=input("Desired gallery:\n")
                conn.execute("INSERT INTO Takes Set (BorrowerName,LoanStart,LoanEnd,artid) VALUES(?,?,?,?)",(origin,datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday),artid))
                conn.commit()
        except:
            print("Wrong Value")
    elif(x=="4"):
       
        os.system('cls')
        room=input("Enter Room to be inserted:\n")
        posno=int(input("Enter position number to be inserted:\n"))
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
            art=input("Enter desired art to be displayed:\n")
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
            os.system('cls')
            gall=input("Enter Gallery to be inserted:")
            conn.execute("INSERT INTO Associate_Gallery(Name) Values (?)",(gall,))
            conn.commit()
        except:
            print("Wrong Value")
def updaterec():
    global curr,conn
    os.system('cls')
    conn.execute("PRAGMA foreign_keys = ON")
    x=input("""1)Update Painting
2)Update Artists
3)Update Exhibitions
4)Update Loaned Paintings
5)Update Given paintings\n""")
    if(x=="1"):
        try:
            os.system('cls')
            i=int(input("Enter Painting id to update:\n"))
            y=input("Desired Title to update:\n")
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
            room=input("Desired room(Press enter for none):\n")
            no=input("Desired position number(Press enter for none):\n")
            if(room=="" and no=""):
                room=None
                no=None
            else:
                no=int(no)
            conn.execute("Update Painting Set Creationyear=?,Artperiod_name=?,Title=?,Room=?,Pos_no=?,ArtistID=? where artid='"+i+"';",(ct,ArtPeriod_name,y,room,no,Artid))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong values")
    elif(x=="2"):
        try:
            os.system('cls')
            artist=int(input("Desired artist ID:\n"))
            name=input("Update Name:\n")
            surname=input("Update Surname:\n")
            nat=input("Update Nationality:\n")
            conn.execute("Update Artist Set Name=?,Surname=?,Nationality=? where ID='"+artist+"';",(name,surname,nat))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong values")
    elif(x=="3"):
        try:
            os.system('cls')
            startyear=int(input("Desired start year:\n"))
            startmonth=int(input("Desired start month:\n"))
            startday=int(input("Desired start day:\n"))
            endyear=int(input("Desired end year:\n"))
            endmonth=int(input("Desired end month:\n"))
            endday=int(input("Desired end day:\n"))
            exid=int(input("Desired exhibition ID:\n"))
            subject=input("Desired subject:\n")
            conn.execute("Update Exhibition Set Subject=?,StartDate=?,EndDate=? where ID='"+exid+"';",(subject,datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday)))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
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
            artid=int(input("Desired art ID:\n"))
            origin=input("Desired gallery:\n")
            curr.execute("SELECT Name FROM Associate_Gallery WHERE Name='"+origin+"';")
            res=curr.fetchone()
            if(res==None):
                conn.execute("INSERT INTO Associate_Gallery(Name) VALUES(?)",(origin,))
                conn.commit()
            conn.execute("Update Loan Set OriginName=?,LoanStart=?,LoanEnd=? where artid='"+artid+"';",(origin,datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday)))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong values")
    elif(x=="5"):
        try:
            os.system('cls')
            startyear=int(input("Desired start year:\n"))
            startmonth=int(input("Desired start month:\n"))
            startday=int(input("Desired start day:\n"))
            endyear=int(input("Desired end year:\n"))
            endmonth=int(input("Desired end month:\n"))
            endday=int(input("Desired end day:\n"))
            artid=int(input("Desired art ID:\n"))
            borr=input("Desired gallery:\n")
            curr.execute("SELECT Name FROM Associate_Gallery WHERE Name='"+borr+"';")
            res=curr.fetchone()
            if(res==None):
                conn.execute("INSERT INTO Associate_Gallery(Name) VALUES(?)",(borr,))
                conn.commit()
            conn.execute("Update Takes Set BorrowerName=?,LoanStart=?,LoanEnd=? where artid='"+artid+"';",(borr,datetime.date(startyear,startmonth,startday),datetime.date(endyear,endmonth,endday)))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong values")
def deleterec():
    global curr,conn
    conn.execute("PRAGMA foreign_keys = ON")
    x=input("""1)Delete Painting
2)Delete Artist
3)Delete Exhibition
4)Delete Loaned Painting
5)Delete Given painting
6)Delete Position
7)Delete Displayed Painting\n""")
    if(x=="1"):
        os.system('cls')
        z=int(input("Desired PaintingId to delete:\n"))
        try:
            conn.execute(" Delete from Painting where artid = ?;",(z,))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong value")
    elif(x=="2"):
        os.system('cls')
        z=int(input("Desired ArtistID to delete:\n"))
        try:
            conn.execute(" Delete from Artist where ID = ?;",(z,))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong value")
    elif(x=="3"):
        os.system('cls')
        z=int(input("Desired ExhibitionID to delete:\n"))
        try:
            conn.execute(" Delete from Exhibition where ID = ?;",(z,))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong value")
    elif(x=="4"):
        os.system('cls')
        z=int(input("Desired PaintingId to delete:\n"))
        try:
            conn.execute("Delete from Loaned where artid = ?;",(z,))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong value")
    elif(x=="5"):
        os.system('cls')
        z=int(input("Desired Loaned PaintingId to delete:\n"))
        try:
            conn.execute(" Delete from Takes where artid = ?;",(z,))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong value")
    elif(x=="6"):
        os.system('cls')
        z=input("Desired Room  to delete:\n")
        y=int(input("Desired Room position to delete:\n"))
        try:
            conn.execute(" Delete from Position where Room=? AND Pos_no=?;",(z,y))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong value")
    elif(x=="7"):
        os.system('cls')
        z=int(input("Desired Display PaintingId to delete:\n"))
        try:
            conn.execute(" Delete from IsDisplayed where artid =?;",(z,))
            conn.commit()
            conn.execute("PRAGMA foreign_keys = OFF")
        except:
            print("Wrong value")
        
    
def menu():
    while True:
        os.system('cls')
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
