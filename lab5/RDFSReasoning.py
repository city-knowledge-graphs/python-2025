from rdflib import Graph

import owlrl


def RDFSInference():
    
    g = Graph()
    
    g.parse("data/lab5-rdfs.ttl", format="ttl")    
    
    print("Loaded '" + str(len(g)) + "' triples.")
    
    #Performs RDFS reasoning
    owlrl.DeductiveClosure(owlrl.RDFS_Semantics, axiomatic_triples=True, datatype_axioms=False).expand(g)
    
    
    print("After inference rules: '" + str(len(g)) + "' triples.")

    #Check if entailments hold
    print("\nChecking entailments: ")
    triple1 = ":Father rdfs:subClassOf :Person ."     
    checkEntailment(g, triple1)


    
    print("\nSaving extended graph")
    g.serialize(destination='data/lab5-rdfs-extended.ttl', format='ttl')



def checkEntailment(g, triple):
    
    #We use an ASK query instead of a select. It could be done with SELETCT and then checking that the results are not empty 
    qres = g.query(
    """ASK {""" + triple + """ }""")

    #Single row with one boolean vale
    for row in qres:
        print("Does '" + triple + "' hold? " + str(row))
        
    
RDFSInference()

