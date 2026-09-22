
import networkx as nt
import matplotlib.pyplot as plt
G=nt.Graph()
choice=int(input("How many PCs do you want?"))
conn=int(input("How many connection?"))
for i in range(1,choice+1):
    text = str(i)
    maintext="PC"+text
    G.add_nodes_from([maintext])
for i in range(1,conn+1):
    stpcconn = int(input("Enter the starting PC no. to be connected: "))
    endpcconn = int(input("Enter the end PC no. to be connected: "))
    if stpcconn < 1 or stpcconn > choice or endpcconn < 1 or endpcconn > choice:
        print("Invalid PC number! Connection not added.")
        continue
    stpcconn = "PC" + str(stpcconn)
    endpcconn = "PC" + str(endpcconn)
    G.add_edge(stpcconn,endpcconn)
before_count=0
nt.draw(G, with_labels=True)
plt.show()
source=input("Enter the sourse of the node")
target=input("Enter the destination of the node")
if source not in G or target not in G:
        print("Sorry , Wrong PC Access warning , Access Denited ")
else:
    for path in nt.all_simple_paths(G,source,target):
        before_count=before_count+1
        print(path)
print("THE TOTAL PATH ARE : ",before_count)

remove=int(input("Which PC is offline? IF neither is offline enter 0 :"))
if remove==0:
    print("Ok ! ALL GOOD..")
else:
    remove="PC"+str(remove)
    if remove not in G:
        print("Sorry ! Wrong entry..")
    else:
        G.remove_node(remove)
nt.draw(G, with_labels=True)
plt.show()
count=0
if source not in G or target not in G:
        print("Sorry , Wrong PC Access warning , Access Denited ")
else:
    for path in nt.all_simple_paths(G,source,target):
        count=count+1
        print(path)
if count == 0:
    print("No communication path available between", source, "and", target)
else:
    print("THE TOTAL PATHS ARE:", count)

print("\n--- NETWORK STATUS ---")
print("Paths before failure:", before_count)
print("Paths after failure:", count)
print("")
print("\n===== NETWORK INFORMATION =====")
print("Total PCs:", G.number_of_nodes())
print("Total Connections:", G.number_of_edges())
print("Network Density:", round(nt.density(G), 2))