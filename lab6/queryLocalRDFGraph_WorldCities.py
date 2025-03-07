'''
Created on 02 Feb 2021

@author: ejimenez-ruiz
'''
from rdflib import Graph

def queryLocalGraph():

    #Example from  https://www.stardog.com/tutorials/data-model/
   
    #Loads KG
    g = Graph()
    g.parse("./data/worldcities-free-100-task1.ttl", format="ttl")
  
    
    print("Loaded '" + str(len(g)) + "' triples.")
    
    #for s, p, o in g:
    #    print((s.n3(), p.n3(), o.n3()))
    
        
    print("Cities:")
    
    qres = g.query(
    """SELECT ?city where {
      ?city rdf:type wco:City .      
    }""")
    

    for row in qres:
        #Row is a list of matched RDF terms: URIs, literals or blank nodes
        print("%s is a City" % (str(row.city)))
        
    
        
queryLocalGraph()
