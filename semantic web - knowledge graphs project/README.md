

Below we will describe the steps that should be followed in order to be able to apply queries on the graph through the triple store blaze graph:

1)TRIPLE STORE
1.1) Download the blaze graph triple store.
1.2) Open the command as admin and run the follow command from the directory of the saved file of blaze graph:
Java -Djetty.host=0.0.0.0 -Djetty.port=8080 -jar blazegraph.jar 
1.3) Go to  http://localhost/blazegraph/namespaces   and create Namespace: kde1

2)CREATE AND UPLOAD RDF GRAPHS
2.1) Run the script Retrieve_WikiData_Links in order to retrieve the links for the MotoGP drivers from the wiki data. Alternatively, use the wikidata_result.csv beacauce the script need aproximatly 1.5 hour to be completed.
2.2) Run the scripts KDE_FORMULA_ONE, KDE_MOTO_GP_P and KDE_MOTO_GP_S in order to create the ttl files for the rdf graphs of FormulaOne and MotoGP or you can find the ttls in the folder ttl_files.
2.3) Run the script Store_graph_to_BlazeG in order to store all the ttl in the blazegraph.

3)QUERIES
3.1) You can retrieve the queries from the file Queries in order to apply them using the blazegraph.
