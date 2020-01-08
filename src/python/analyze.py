#coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt

import json
from collections import OrderedDict


def analyze(jsonfile):

    G=nx.Graph()
    f = open(jsonfile, 'r')

    jsonData = json.load(f)


    nodes = jsonData["nodes"]
    links = jsonData["links"]

    nodes_list = []
    links_list = []

    for node in nodes:
        # print(node)
        # print(node["id"])
        nodes_list.append(node["id"])

    for link in links:
        l = (link["source"], link["target"])
        links_list.append(l)

    G.add_nodes_from(nodes_list)
    G.add_edges_from(links_list)

    num_n = int(nx.number_of_nodes(G))
    num_l = int(nx.number_of_edges(G))

    # 平均最短経路
    #nx.average_shortest_path_length(G)

    # 次数 ⇒　平均次数
    import numpy as np

    deg_list = []

    degree = sorted(G.degree())
    for n in degree:
        deg_list.append(n[1])

    ave_dim = np.average(deg_list)

    # クラスタ係数の平均
    clustering_coef = nx.average_clustering(G)

    # 密度
    density = 2*num_l/(num_n*(num_n-1))

    with open('new.json',"w") as fw:
        jsonData["averageDim"]=ave_dim
        jsonData["clusteringCoef"]=clustering_coef
        jsonData["density"]=density
        json.dump(jsonData, fw, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


if __name__ == '__main__':
    analyze('9.json')