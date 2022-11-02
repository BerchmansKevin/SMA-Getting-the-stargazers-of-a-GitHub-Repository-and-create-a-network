#!/usr/bin/env python
# coding: utf-8

# ## `Berchmans Kevin S`

# ## `Getting the stargazers of a GitHub Repository and create a network`

# In[1]:


import requests
from pprint import pprint
username = "BerchmansKevin"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
pprint(user_data)


# In[2]:


pip install pyGithub


# In[3]:


import base64
from github import Github
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

username = "BerchmansKevin"
g = Github()
user = g.get_user(username)

for repo in user.get_repos():
    print(repo)


# In[4]:



ACCESS_TOKEN ="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"

USER = 'ptwobrussell'
REPO = 'Mining-the-Social-Web'

client = Github(ACCESS_TOKEN, per_page=100)
user = client.get_user(USER)
repo = user.get_repo(REPO)
stargazers = [s for s in repo.get_stargazers()]
print("Number of stargazers", len(stargazers))


# In[5]:


get_ipython().system('pip install networkx')


# In[6]:


import matplotlib.pyplot as plt
import networkx as nx


# In[7]:



import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edges_from([('Berchmans', 'Karthi'), ('Gookle', 'Client'),	('Brath', 'Cimil'), ('Evilin', 'Filo'),('David', 'Emeden'), ('samuvel', 'udam'),('Disvid', 'Grasvelinal'), ('Kevin', 'Filimal'),('yed', 'Fazil'), ('Edwin', 'Helan')])
ego = 'Berchmans'
ego1 = 'Karthi'
pos = nx.spring_layout(G)

nx.draw(G, pos, node_color = "lavender",
		node_size = 9000, with_labels = True)

options = {"node_size": 120000, "node_color": "r"}

nx.draw_networkx_nodes(G, pos, nodelist=[ego,ego1], **options)
plt.show()


# In[8]:


import networkx as nx
g = nx.DiGraph()
g.add_node(repo.name + '(repo)',type='repo',lang=repo.language,owner=user.login)

for sg in stargazers:
    g.add_node(sg.login + '(user)',type='user')
    g.add_edge(sg.login + "(user)",repo.name + '(repo)',type="gazes")


# In[9]:


print (nx.info(g))


# In[10]:


import networkx as nx 

g = nx.DiGraph() 
g.add_node(repo.name + '(repo)', type='repo', lang=repo.language, owner=user.login)
stargazers = [ s for s in repo.get_stargazers() ] 
print("Number of stargazers", len(stargazers)) 

for sg in stargazers:
           g.add_node(sg.login + '(user)', type='user') 
           g.add_edge(sg.login + '(user)', repo.name + '(repo)', type='gazes') 


# In[11]:


from operator import itemgetter 
from IPython.display import HTML 
from IPython.core.display import display 

kkg = nx.generators.small.krackhardt_kite_graph() 
print("Degree Centrality") 
print(sorted(nx.degree_centrality(kkg).items(), key=itemgetter(1), reverse=True))
print("Betweenness Centrality") 
print(sorted(nx.betweenness_centrality(kkg).items(), key=itemgetter(1), reverse=True)) 
print("Closeness Centrality") 
print(sorted(nx.closeness_centrality(kkg).items(), key=itemgetter(1), reverse=True))


# In[ ]:


import sys 
for i, sg in enumerate(stargazers):
    try:
        for follower in sg.get_followers():
            if follower.login + '(user)' in g:
                g.add_edge(follower.login + '(user)', sg.login + '(user)', type='follows')
    except Exception as e:
        print("Encountered an error fetching followers for", sg.login, "Skipping.", file=sys.stderr)
        print(e, file=sys.stderr) 
        print("Processed", i+1, " stargazers. Num nodes/edges in graph", g.number_of_nodes(), "/", g.number_of_edges())
        print("Rate limit remaining", client.rate_limiting) 

nx.write_gpickle(g, "github.gpickle.1") 


# In[ ]:


print(nx.info(g)) 


# In[ ]:


print(len([e for e in g.edges(data=True) if e[2]['type'] == 'follows'])) 


# In[ ]:


mtsw_users = [n for n in g if g.nodes[n]['type'] == 'user'] 
h = g.subgraph(mtsw_users) 
print("Stats on the extracted subgraph") 
print(nx.info(h))


# In[ ]:


import warnings 
warnings.filterwarnings("ignore") 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')

fig = plt.figure(figsize=(15,15)) 
ax = fig.add_subplot(111) 
labels = dict([(n, n.split('(user)')[0]) for n in h.nodes()]) 
nx.draw(h, 
        pos=nx.spring_layout(h), 
        arrows=False, 
        ax=ax, 
        node_size=50, 
        edge_color='red', 
        alpha=0.8, 
        labels=labels, 
        font_size=8) 


# In[ ]:




