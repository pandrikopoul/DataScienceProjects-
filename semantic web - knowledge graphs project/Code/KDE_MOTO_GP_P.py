import csv
import time
from rdflib import Graph, URIRef, Literal, RDF, Namespace, OWL ,RDFS,XSD,BNode


# OWL axioms section
g = Graph()
ns=Namespace("http://example.org/motor-sports/motoGP/")
f1namespace=Namespace("http://example.org/motor-sports/formula-one/") # na to alaksw
f1namespaceForF1events = Namespace("http://example.org/motor-sports/formula-one/races-circuits/")

# OWL Riders
dbr=Namespace("https://dbpedia.org/resource/")
dbo=Namespace("https://dbpedia.org/ontology/")
msp = Namespace('http://example.org/motor-sports/')
# Classes axioms
g.add((ns.Rider, RDF.type, OWL.Class))
g.add((msp.Racer, RDF.type, OWL.Class))
g.add((ns.Rider, RDFS.subClassOf,msp.Racer ))
g.add((msp.Racer, RDFS.subClassOf, dbo.Person))
g.add((dbr.Person, OWL.equivalentClass, dbo.Human))
g.add((ns.Rider, OWL.disjointWith, f1namespace.Driver))# na to vgalw ?

BnodeFOrdisjoinUnion=BNode()
g.add((msp.Racer, OWL.equivalentClass,BnodeFOrdisjoinUnion ))
g.add((BnodeFOrdisjoinUnion, OWL.disjointUnionOf,ns.Rider))
g.add((BnodeFOrdisjoinUnion, OWL.disjointUnionOf,f1namespace.Driver))


#Properties axioms
g.add((ns.HadFirstPlaces, RDF.type, OWL.DatatypeProperty))
g.add((ns.HadFirstPlaces, RDFS.domain, ns.Rider))
g.add((ns.HadFirstPlaces, RDFS.range, XSD.int))

g.add((ns.HadSecondPlaces, RDF.type, OWL.DatatypeProperty))
g.add((ns.HadSecondPlaces, RDFS.domain, ns.Rider))
g.add((ns.HadSecondPlaces, RDFS.range, XSD.int))

g.add((ns.HadThirdPlaces, RDF.type, OWL.DatatypeProperty))
g.add((ns.HadThirdPlaces, RDFS.domain, ns.Rider))
g.add((ns.HadThirdPlaces, RDFS.range, XSD.int))

g.add((ns.HadPolePositions, RDF.type, OWL.DatatypeProperty))
g.add((ns.HadPolePositions, RDFS.domain, ns.Rider))
g.add((ns.HadPolePositions, RDFS.range, XSD.int))

g.add((ns.HadRaceFastestLapUntil2022, RDF.type, OWL.DatatypeProperty))
g.add((ns.HadRaceFastestLapUntil2022, RDFS.domain, ns.Rider))
g.add((ns.HadRaceFastestLapUntil2022, RDFS.range, XSD.int))

g.add((ns.HadWorldChampionchips, RDF.type, OWL.DatatypeProperty))
g.add((ns.HadWorldChampionchips, RDFS.domain, ns.Rider))
g.add((ns.HadWorldChampionchips, RDFS.range, XSD.int))

# OWL grand prix event

# Classes axioms
g.add((ns.Track, RDF.type, OWL.Class))


# Properties axioms
g.add((ns.timesThatHeldOn, RDF.type, OWL.DatatypeProperty))
g.add((ns.timesThatHeldOn, RDFS.domain, ns.Track))
g.add((ns.timesThatHeldOn, RDFS.range, XSD.int))

# OWL constructor

# Classes axioms
g.add((msp.Constructors, RDF.type, OWL.Class))
g.add((msp.Constructors, RDFS.subClassOf, dbo.Company))

# OWL winners

# Classes axioms
g.add((ns.MotoRaceEvents, RDF.type, OWL.Class))
g.add((msp.MotorSportsEvents, RDF.type, OWL.Class))
g.add((ns.MotoRaceEvents, RDFS.subClassOf, msp.MotorSportsEvents))
g.add((ns.MotoRaceEvents, OWL.equivalentClass, dbr.Grand_Prix_motorcycle_racing))
g.add((ns.MotoRaceEvents, OWL.disjointWith, f1namespaceForF1events.F1RaceEvents)) #neo

# auto malon den einai swsto 
BnodeFOrdisjoinUnion=BNode()
g.add((msp.MotorSportsEvents, OWL.equivalentClass,BnodeFOrdisjoinUnion ))
g.add((BnodeFOrdisjoinUnion, OWL.disjointUnionOf,ns.MotoRaceEvents))
g.add((BnodeFOrdisjoinUnion, OWL.disjointUnionOf,f1namespaceForF1events.F1RaceEvents))

# Properties axioms
g.add((ns.Has, RDF.type, OWL.DatatypeProperty))
g.add((ns.Has, RDFS.domain,ns.MotoRaceEvents))

g.add((ns.Held_On, RDF.type, OWL.DatatypeProperty))
g.add((ns.Held_On, RDFS.range, ns.Track))

g.add((ns.HasWinnerTeam, RDF.type, OWL.DatatypeProperty))
g.add((ns.HasWinnerTeam, RDFS.range, ns.Constructor))

g.add((ns.TeamRider, RDF.type, OWL.DatatypeProperty))
g.add((ns.TeamRider, RDFS.range, ns.Rider))

g.add((ns.RiderNationality, RDF.type, OWL.DatatypeProperty))
g.add((ns.RiderNationality, RDFS.range, XSD.string))

g.add((ns.InSeason, RDF.type, OWL.DatatypeProperty))
g.add((ns.InSeason, RDFS.range, XSD.int))

#End of OWL axioms section

# Read CSVs And Cteate RDF Triples section

def convert_to_uri(value):
    # Delete spaces and replace with "_"
    uri_value = value.replace(" ", "_")
    # Delete non chars , numbers or  "_"
    uri_value = ''.join(c for c in uri_value if c.isalnum() or c == "_")
    # Construct a URI
    uri = f"http://example.org/motor-sports/motoGP/{uri_value}"
    return URIRef(uri)

# Graph for Tracks=============================================
print("Tracks=============================================")
# Read the CSV
csv_path = r'C:\Users\panos\Downloads\grand-prix-events-held.csv' # please update  with your file path

with open(csv_path, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = [row for row in csvreader]

# Create a namespace for the URL

ns=Namespace("http://example.org/motor-sports/motoGP/")

# Create RDF triples
for row in data:
    event_uri = convert_to_uri(row['Track'])
    TrackNameForThedpedia = row['Track'].split(' ')  # convert the name in order to fit to the db pedia structure to add it on the link for more info from db pedia
    titled_case_name = '_'.join(word.title() for word in TrackNameForThedpedia)  # the name is now in the right frmat
    titled_Track_name_uri = URIRef(dbr[titled_case_name]) # convert it to URI
    g.add((event_uri, RDF.type, ns.Track))
    g.add((event_uri, ns.timesThatHeldon, Literal(row['Times'], datatype=XSD.float)))
    g.add((event_uri, ns.track, Literal(row['Track'])))
    g.add((event_uri, ns.country, Literal(row['Country'])))
    g.add((event_uri, RDFS.seeAlso , titled_Track_name_uri)) # link with db pedia
# Print RDF triples
print(g.serialize(format='turtle'))

# Graph for Grand Prix Winners ====================================================================================

print("Grand Prix Winners  ====================================================================================")

# Read the CSV
csv_path = r'C:\Users\panos\Downloads\grand-prix-race-winners.csv' # please update  with your file path
with open(csv_path, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = [row for row in csvreader]

# Create namespace for the URL

ns=Namespace("http://example.org/motor-sports/motoGP/")
Season_node = BNode()

# Create RDF triples
for row in data:
   # if row['Rider'].upper() == 'VALENTINO ROSSI':
        Season_node = BNode()

        circuit_uri = convert_to_uri("/"+row['Circuit'])
        #season_uri = convert_to_uri(row['Season'])
        class_uri = convert_to_uri(row['Class'])
        class_uri=circuit_uri + '_' + row['Class']
        season_uri=circuit_uri + '/' + row['Class'] + '/' + row['Season']
        if 'Constructor' in row and row['Constructor'] and row['Constructor'] != "Unknown": # Because in our data the constructor is sometimes unknown or empty
             team_uri = convert_to_uri(row['Constructor'])
        else:
            team_uri = convert_to_uri('Unknown')
        team_uri = convert_to_uri(row['Constructor'])
        rider_uri = convert_to_uri(row['Rider'].upper()) # convers the name to upper case in order to match the structure of riders
        circuit_class_uri = circuit_uri
        g.add((class_uri, ns.Has, Season_node))
        g.add((Season_node, ns.Held_On, convert_to_uri(row['Circuit'])))
      #  g.add((ns.MotoRaceEvents, RDF.type, ns.MotorSportsEvents)) # na to vgalw ??
        g.add((class_uri, RDF.type, ns.MotoRaceEvents))
        g.add((Season_node, ns.HasWinnerTeam, team_uri))
        g.add((Season_node, ns.TeamRider,rider_uri))
        g.add((Season_node, ns.WinnerRiderNationality, Literal(row['Country'])))
        g.add((Season_node, ns.season, Literal(row['Season'], datatype=XSD.int)))
        g.add((Season_node, ns.InCategory, Literal(row['Class'])))

# Print RDF triples
print(g.serialize(format='turtle'))

# Graph for Riders ===========================================================================
print("Riders ===========================================================================")

# Read the CSV
csv_path = r'C:\Users\panos\Downloads\riders-info.csv' # please update  with your file path
with open(csv_path, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = [row for row in csvreader]

# Create a namespace for the URL
ns=Namespace("http://example.org/motor-sports/motoGP/")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
# Create RDF triples
for row in data:

        rider_name = row['Riders All Time in All Classes']

        uppercase_name = rider_name.upper() # make the full name upper case because now is name in lowercase and surname in capital
        splited_name= uppercase_name.split(' ') # reverse the name to be in the same order like in winners section above
        search_name = splited_name[0]  # First name
        uppercase_name = ' '.join(splited_name[1:])+" "+search_name

        RiderNameForThedpedia = uppercase_name.split(' ')  # convert the name in order to fit to the db pedia structure to add it on the link for more info from db pedia
        titled_case_name = '_'.join(word.title() for word in RiderNameForThedpedia)  # Now the name is converted properly
        titled_case_name_uri = URIRef(dbr[titled_case_name]) # Convert the name to a uri

        Riders = convert_to_uri(uppercase_name) #convert the full name to Uri
        name,surname = uppercase_name.split(' ',1) # Split the full name in to name and surname to add those as literals
        PolePositions = convert_to_uri(row["Pole positions from '74 to 2022"])
        RaceFastestLapUntil2022 = convert_to_uri(row["Race fastest lap to 2022"])
        WorldChampionships = convert_to_uri(row["World Championships"])

        victories = Literal(row['Victories'], datatype=XSD.float) if row['Victories'] else Literal("0", datatype=XSD.float)
        second_places = Literal(row['2nd places'], datatype=XSD.float) if row['2nd places'] else Literal("0" , datatype=XSD.float) # put 0 if its empty and also make the data type float
        third_places = Literal(row['3rd places'], datatype=XSD.float) if row['3rd places'] else Literal("0", datatype=XSD.float)
        pole_positions = Literal(row["Pole positions from '74 to 2022"], datatype=XSD.float) if row["Pole positions from '74 to 2022"] else Literal("0", datatype=XSD.float)
        race_fastest_lap = Literal(row["Race fastest lap to 2022"], datatype=XSD.float) if row["Race fastest lap to 2022"] else Literal("0", datatype=XSD.float)
        world_championships = Literal(row["World Championships"], datatype=XSD.float) if row["World Championships"] else Literal("0", datatype=XSD.float)

        g.add((Riders, RDF.type, ns.Rider))
        g.add((Riders,FOAF.firstName, Literal(name)))
        g.add((Riders, FOAF.surname, Literal(surname)))
        g.add((Riders, RDFS.seeAlso,titled_case_name_uri)) # link with db pedia
        g.add((Riders, ns.HadFirstPlaces, victories))
        g.add((Riders, ns.HadSecondPlaces, second_places))
        g.add((Riders, ns.HadThirdPlaces, third_places))
        g.add((Riders, ns.HadPolePositions, pole_positions))
        g.add((Riders, ns.HadRaceFastestLapUntil2022, race_fastest_lap))
        g.add((Riders, ns.HadWorldChampionchips, world_championships))
#==========================LinkRider with WikiData
        csv_path = r'C:/Users/panos/PycharmProjects/pythonProject/venv/wikidata_results.csv' # please update  with your file path.This is the csv file that is crated from Retrieve_WikiData_Links.py
        with open(csv_path, 'r', encoding='utf-8') as csvfile:
            csvreader1 = csv.DictReader(csvfile)
            data1 = [row1 for row1 in csvreader1]
           # print("upperprinto wikidata:"+str(uppercase_name))
        for row1 in data1 :
            if uppercase_name == row1["Name"].upper() :
                wikiData_uri = URIRef(row1["wiki data link"])
                g.add((Riders, RDFS.seeAlso, wikiData_uri))
#==========================End of LinkRider with WikiData code

 #PrintRDF triples
print(g.serialize(format='turtle'))

# Store RDF triples in a ttl file
g.serialize('MotoGp_P_FinalOutPut.ttl', format='turtle')

# End of Read CSVs And Cteate RDF Triples section

