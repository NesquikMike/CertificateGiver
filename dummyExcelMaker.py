import pandas as pd
import random as rd
import sys

firstNames = (
    "Wilbert", "Monroe", "Dylan", "Bruno", "Tony", "Ronald", "Gordon", "Buster", "Federico", "Doyle",
    "Jackson", "Marlon", "Mauro", "Samuel", "Stuart", "Sidney", "Gayle", "Roy", "Elmer", "Dominick",
    "Normand", "Kristopher", "Jamar", "Leandro", "Myron", "Asa", "Alejandro", "Jan", "Sonny", "Barney",
    "Jimmie", "Jarrod", "Bryan", "Cortez", "Mason", "Taylor", "Tyler", "Clark", "Branden", "Carmine",
    "Garrett", "Clint", "Bradly", "Lupe", "Sydney", "Curtis", "Arturo", "Winfred", "Joel",
    "Mary", "Ed", "Clay", "Larae", "Janet", "Wynell", "Chrissy", "Lizzette", "Dorthey", "Scarlet", "Julienne",
    "Cassy", "Queenie", "Charline", "Doretha", "Lan", "Mirtha", "Marya", "Juliane", "Juliann", "Benita",
    "Meri", "Maybelle", "Dianne", "Yadira", "Pilar", "Isela", "Marybelle", "Stephane", "Roseann", "Cornelia",
    "Lucie", "Katelin", "Kandra", "Janeen", "Danette", "Starla", "Ashlyn", "Gayla", "Dina", "Codi", "Neomi",
    "Kara", "Lizbeth", "Filomena", "Bess",
    "Aaron", "Richie", "Willie", "Wes", "Vito", "Parker", "Louis", "Wayne", "Stacey", "Omar", "Jessie",
    "Jamey", "Felipe", "Nelson", "Burt", "Lenard", "Ward", "Stanton", "Ivory", "Fritz", "Josiah", "John",
    "Patricia", "Byron", "Willis", "Marvin", "Jed", "Jefferson", "Emmett", "Kerry", "Angel", "Isaiah", "Dan",
    "Chadwick", "Roman", "Johnson", "Victor", "Gregory", "Rufus", "Kelly", "Errol", "Leroy", "Clifton",
    "Bill", "Bennie", "Ivan", "Theron", "Kenton", "Xavier", "Jerome",
    "Alease", "Stephenie", "Hannelore", "Apolonia", "Shana", "Leatha", "Monica", "Angelo", "Hank", "Isidro",
    "Elmer", "Foster", "Wilmer", "Kenton", "Darren", "Darnell", "Jacinto", "Thomas", "Blake", "Carmelo",
    "Damon", "Drew", "Mckinley", "Santos", "Clement", "Oren", "Kennith", "Renato", "Jewell", "Donn", "Jay",
    "Vance", "Abram", "Walker", "Vince", "Cory", "Colin", "Brain", "Isaiah", "Parker", "Lane", "Federico",
    "Michael", "Augustine", "Mariano", "Cordell", "Dudley",
    "Mckinley", "Freeman", "Russell", "Antonia", "Nickolas", "Carmine", "Darius", "Reynaldo", "Dorsey",
    "Weldon", "Emmitt", "Bruce", "Ignacio", "Del", "Milo", "Reid", "Deangelo", "Man", "Lemuel", "Justin",
    "Guadalupe", "Phillip", "Ollie", "Denny", "Maurice", "Kelly", "Tory", "Gerardo", "Harlan", "Max", "Angel",
    "Van", "Scot", "Warner", "Joel", "Long", "Marcelino", "Franklin", "Everett", "Shad", "Judson", "Elbert",
    "Wilbur", "Jc", "Samuel", "Kenton", "Elvis", "Irwin", "Toney",
    "Kristofer", "Alfonso", "Gaston", "Josh", "Luther", "Brad", "Edison", "Tyree", "Rob", "Donn", "Gil",
    "Kanisha", "Corliss", "Nada", "Marjory", "Sebrina", "Bettye", "Palma", "Soila", "Verena", "Marchelle",
    "Gabrielle", "Dori", "Jolanda", "Georgetta", "Clarisa", "Bernice", "Santa", "Cortney", "Laureen", "Dinah",
    "Joleen", "Loreen", "Desirae", "Natasha", "Fern", "Bridgett", "Ernestina", "Cecile", "Kirstin", "Marylou",
    "Herminia", "Glenna", "Cristal", "Shiloh", "Marceline",
    "Lue", "Ophelia", "Dalia", "Rosamaria", "Tanya", "Fallon", "Leonila", "Devorah", "Ailene", "Yan",
    "Georgine", "Tobie", "Calandra", "Tiffaney", "Hedwig", "Lorenza", "Ute", "Lavonia", "Mikaela",
    "Jacquelyn", "Tisa", "Rafaela", "Estella", "Renea", "Ping", "Keturah", "Lasonya", "Angelika", "Marianna",
    "Elodia", "Marx", "Kaylene", "Bong", "Liliana", "Larae", "Lurlene", "Reagan", "Monica", "Terra", "Annis",
    "Tracie", "Annalisa", "Cecila", "Chaya", "Oralee", "Elmira", "Pok",
    "Yolanda", "Jeri", "Vallie", "Karmen", "Emogene", "Georgianne", "Marti", "Nova", "Mittie", "Julienne",
    "Lauran", "Eleanor", "Luisa", "Miesha", "Anjelica", "Yee", "Kassandra", "Stormy", "Luna", "Cami",
    "Loreen", "Fay", "Jaye", "Hermila", "Jovita", "Honey", "Venice", "Goldie", "Deja", "Blanch", "Arie",
    "Vergie", "Tosha", "Teisha", "Meredith", "Ladonna", "Mee", "Precious", "Minnie", "Niesha", "Nicki",
    "Susanne", "Nidia", "Jerrica", "Verena", "Lenna", "Tonita", "Mimi",
    "Danna", "Ilona", "Ka", "Margherita", "Taneka", "Agustina", "Kellie", "Raquel", "Lorene", "Tracie",
    "Melodi", "Inge", "Margrett", "Jesusa", "Sommer", "Arminda", "Velvet", "Elsie", "Lala"
)

secondNames = (
    "Torres", "Muhlenkamp", "Bourbonnais", "Siliezar", "Oberst", "Goring", "Ditucci", "Che", "Behme", "Ehrhardt",
    "Bringle",
    "Isabella", "Eisenhaver", "Tatsuta", "Ternasky", "Steinert", "Claytor", "Hoelscher", "Erath", "Stipp", "Durnin",
    "Osterberger", "Sniezek", "Lawary", "Delea", "Berrell", "Winkey", "Konick", "Nosworthy", "Flaggs", "Glasper",
    "Andringa", "Heart", "Blixt", "Pflanz", "Bolden", "Schlieter", "Fontanilla", "Zlotnick", "Drust", "Olcus", "Toth",
    "Mangas",
    "Havermann", "Phanthavongsa", "Raybould", "Katzaman", "Seurer", "Mode", "Len", "Miene", "Stieb", "Pontoriero",
    "Digeorgio", "Aldape", "Anglada", "Sholar", "Lillard", "Striegel", "Jalkut", "Bolay", "Demosthenes", "Dougan",
    "Coxum",
    "Demaris", "Shaer", "Shimon", "Skeldon", "Bramlett", "Cannedy", "Berrong", "Mushrush", "Eoff", "Lebeouf", "Tritle",
    "Wanty", "Brodmerkel", "Taylan", "Teque", "Kalish", "Sanlatte", "Beer", "Fougere", "Ravelo", "Wandel", "Covarrubia",
    "Golida", "Null", "Catanach", "Harriger", "Smith", "Bakken", "Lillian", "Jastrzebski", "Ehlke", "Senosk",
    "Radcliffe",
    "Kinkelaar", "Vangemert", "Mcglockton", "Toppins", "Gouldie", "Hofstetter", "Bonett", "Mcclaugherty", "Brenda",
    "Manzo",
    "Korgie", "Smyers", "Menson", "Belkin", "Aujla", "Gore", "Dolph", "Coiro", "Raff", "Kortright", "Reisman",
    "Craigen",
    "Daking", "Sylney", "Deuschel", "Guzewicz", "Walwyn", "Rutkin", "Saephan", "Kochmanski", "Pulte", "Thang",
    "Derastel", "Estrem", "Cardozo", "Csensich", "Neisius", "Jim", "Strohmeyer", "Iarossi", "Drevs", "Mantegna",
    "Tamburello", "Kelso", "Pacella", "Carstensen", "Pierro", "Whyne", "Leiby", "Moulton", "Landry", "Corner", "Hubric",
    "Illich", "Lagorio", "Schleimer", "Vellutini", "Hegre", "Nesline", "Pizzini", "Kanas", "Nevilles", "Bali", "Pronto",
    "Dieffenbach", "Shamas", "Valis", "Schwuchow", "Kauzlarich", "Schelp", "Kinnie", "Skowron", "Teall", "Chabez",
    "Averyt",
    "Penrod", "Senate", "Agre", "Deneui", "Pote", "Evenson", "Vant", "Studwell", "Boroughs", "Brookshier", "Wyms",
    "Shaheen", "Seiple", "Amezcua", "Vandorp", "Gruben", "Hedge", "Skordahl", "Nembhard", "Jasinski", "Espenschied",
    "Perteet", "Hagerty", "Mcmillon", "Mcnertney", "Vanderbilt", "Conigliaro", "Raif", "Woehrle", "Taton", "Hoekman",
    "Disandro", "Batch", "Gilstad", "Garverick", "Mall", "Haza", "Mccargo", "Liberato", "Klingelhoets", "Palmatier",
    "Wohner",
    "Loyborg", "Styborski", "Fredricks", "Trivette", "Lowes", "Buffum", "Correale", "Goodie", "Berbes", "Boundy",
    "Soppeland", "Kanno", "Minock", "Provence", "Izaquirre", "Grumbach", "Pourvase", "Garron", "Dimariano", "Iguina",
    "Hollingworth", "Londagin", "Pro", "Cotsis", "Raleigh", "Sams", "Menges", "Cheatam", "Osterholt", "Semonis",
    "Bullaro",
    "Zerko", "Steinhart", "Pardall", "Trompeter", "Demmert", "Kela", "Steeb", "Hazell", "Gadway", "Cuartas", "Buntain",
    "Baron", "Etsitty", "Aurrichio", "Maloff", "Coenen", "Rabenstein", "Nogueira", "Derosia", "Beacham", "Wojenski",
    "Groman", "Sek", "Metzel", "Alliston", "Balis", "Satmary", "Ellars", "Duenas", "Nilson", "Herbig", "Polikoff",
    "Kassay",
    "Kaid", "Hollender", "Vanmatre", "Testani", "Thurrell", "Merati", "Setlak", "Siers", "Frick", "Minecci", "Haggberg",
    "Rabbe", "Sulzer", "Vargas", "Sterba", "Logoleo", "Roberie", "Henrichs", "Saulters", "Verplanck", "Kobialka",
    "Knutson", "Didier", "Florey", "Maharaj", "Bahde", "Schweinfurth", "Aagaard", "Pool", "Bobsin", "Dotson", "Queal",
    "Dippel", "Curling", "Kordas", "Brickett", "Hueckman", "Hutcheson", "Rupinski", "Poduska", "Mccrumb", "Vanaller",
    "Rodkin", "Hansell", "Truan", "Loa", "Nienaber", "Boebinger", "Aquil", "Rzeszutko", "Wallack", "Zoellner",
    "Hargenrader", "Saris", "Hesson", "Dragan", "Klemisch", "Robblee", "Mabray", "Stankiewicz", "Kraus", "Wik",
    "Pickett",
    "Laskosky", "Hayn", "Loche", "Kotaki", "Thramer", "Baranick", "Geier", "Carrington", "Neufeld", "Shone", "Poles",
    "Hyten", "Hendryx", "Naz", "Gallian", "Colbath", "Guardia", "Nishi", "Lemarie", "Kittleson", "Stenberg", "Stoodley",
    "Mcgregor", "Steptoe", "Parduhn", "Solages", "Shatley", "Skanes", "Wittbrodt", "Womac", "Gorley", "Moorman"
)

classNames = []

classSize = 0

try:
    classSize = int(sys.argv[1])
except IndexError:
    print("ERROR: Please insert a value for class size, e.g. for a class of 30 please type in 30 after the program"
          " name")
    exit()

while len(classNames) < classSize:
    name = firstNames[rd.randint(0, len(firstNames) - 1)] + " " + secondNames[rd.randint(0, len(secondNames) - 1)]
    classNames.append(name)

frame = {'Names': classNames}

df = pd.DataFrame.from_dict(frame)

print(df.head(15))

df.to_csv("classSpreadsheet.csv", index=False)
