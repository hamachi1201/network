import os
import networkx as nx
from networkx.readwrite import json_graph
from flask import Flask, jsonify, g, request
from itertools import chain
import json
from collections import OrderedDict

app = Flask(__name__)

@app.route('/api/network', methods=['GET'])

def generate_link_list(jsonfile):

    jsonData = json.load(f)
    links = jsonData["links"]
    links_list = []

    for link in links:
        l = [('{}'.format(link["source"]), '{}'.format(link["target"]))]
        links_list.append(l)

    return links_list

def genes_correlations():
    G = nx.MultiDiGraph()

    list = [[('1','2')],[('2','3')],[('3','4')],[('2','4')]]
    for link in list:
        l = link
        #links_list.append(l)

        # G.add_nodes_from(nodes_list)
        G.add_edges_from(l)

    #G.add_edges_from([('node1', 'node2')])
    #G.add_edges_from([('node1', 'node3')])
    #G.add_edges_from([('node1', 'node4')])
    #G.add_edges_from([('node2', 'node5')])
    #G.add_edges_from([('node3', 'node5')])
    #G.add_edges_from([('node4', 'node5')])

    return jsonify(json_graph.node_link_data(G))

"""
def genes_correlations():

    G = nx.MultiDiGraph()


    #f = open("../../../data/origin/FDGIB/high-mid/9.json", 'r')
    #f = open("../data/origin/FDGIB/low-mid/9.json", "r")
    #この読み込みができていなさそう。

    f = {
        "links":[
        {
            "id": 0,
            "source": 0,
            "target": 8,
            "value": 1
        },
        {
            "id": 1,
            "source": 0,
            "target": 11,
            "value": 1
        },
        {
            "id": 2,
            "source": 5,
            "target": 9,
            "value": 1
        },
        {
            "id": 3,
            "source": 11,
            "target": 13,
            "value": 1
        },
        {
            "id": 4,
            "source": 15,
            "target": 23,
            "value": 1
        },
        {
            "id": 5,
            "source": 15,
            "target": 24,
            "value": 1
        },
        {
            "id": 6,
            "source": 16,
            "target": 20,
            "value": 1
        },
        {
            "id": 7,
            "source": 17,
            "target": 20,
            "value": 1
        },
        {
            "id": 8,
            "source": 26,
            "target": 31,
            "value": 1
        },
        {
            "id": 9,
            "source": 26,
            "target": 35,
            "value": 1
        },
        {
            "id": 10,
            "source": 27,
            "target": 29,
            "value": 1
        },
        {
            "id": 11,
            "source": 28,
            "target": 30,
            "value": 1
        },
        {
            "id": 12,
            "source": 29,
            "target": 30,
            "value": 1
        },
        {
            "id": 13,
            "source": 29,
            "target": 35,
            "value": 1
        },
        {
            "id": 14,
            "source": 29,
            "target": 36,
            "value": 1
        },
        {
            "id": 15,
            "source": 33,
            "target": 36,
            "value": 1
        },
        {
            "id": 16,
            "source": 37,
            "target": 47,
            "value": 1
        },
        {
            "id": 17,
            "source": 41,
            "target": 43,
            "value": 1
        },
        {
            "id": 18,
            "source": 41,
            "target": 45,
            "value": 1
        },
        {
            "id": 237,
            "source": 42,
            "target": 452,
            "value": 1
        },
        {
            "id": 235,
            "source": 43,
            "target": 316,
            "value": 1
        },
        {
            "id": 236,
            "source": 44,
            "target": 307,
            "value": 1
        },
        {
            "id": 19,
            "source": 46,
            "target": 47,
            "value": 1
        },
        {
            "id": 20,
            "source": 48,
            "target": 50,
            "value": 1
        },
        {
            "id": 21,
            "source": 50,
            "target": 52,
            "value": 1
        },
        {
            "id": 22,
            "source": 50,
            "target": 53,
            "value": 1
        },
        {
            "id": 239,
            "source": 50,
            "target": 341,
            "value": 1
        },
        {
            "id": 238,
            "source": 52,
            "target": 59,
            "value": 1
        },
        {
            "id": 23,
            "source": 55,
            "target": 57,
            "value": 1
        },
        {
            "id": 240,
            "source": 56,
            "target": 345,
            "value": 1
        },
        {
            "id": 24,
            "source": 59,
            "target": 65,
            "value": 1
        },
        {
            "id": 25,
            "source": 60,
            "target": 67,
            "value": 1
        },
        {
            "id": 26,
            "source": 62,
            "target": 66,
            "value": 1
        },
        {
            "id": 27,
            "source": 62,
            "target": 70,
            "value": 1
        },
        {
            "id": 28,
            "source": 64,
            "target": 69,
            "value": 1
        },
        {
            "id": 29,
            "source": 64,
            "target": 70,
            "value": 1
        },
        {
            "id": 30,
            "source": 65,
            "target": 69,
            "value": 1
        },
        {
            "id": 31,
            "source": 66,
            "target": 70,
            "value": 1
        },
        {
            "id": 32,
            "source": 70,
            "target": 71,
            "value": 1
        },
        {
            "id": 33,
            "source": 78,
            "target": 81,
            "value": 1
        },
        {
            "id": 34,
            "source": 82,
            "target": 89,
            "value": 1
        },
        {
            "id": 35,
            "source": 82,
            "target": 93,
            "value": 1
        },
        {
            "id": 36,
            "source": 84,
            "target": 87,
            "value": 1
        },
        {
            "id": 37,
            "source": 85,
            "target": 87,
            "value": 1
        },
        {
            "id": 38,
            "source": 85,
            "target": 92,
            "value": 1
        },
        {
            "id": 39,
            "source": 86,
            "target": 93,
            "value": 1
        },
        {
            "id": 40,
            "source": 90,
            "target": 91,
            "value": 1
        },
        {
            "id": 41,
            "source": 90,
            "target": 92,
            "value": 1
        },
        {
            "id": 42,
            "source": 94,
            "target": 104,
            "value": 1
        },
        {
            "id": 43,
            "source": 95,
            "target": 97,
            "value": 1
        },
        {
            "id": 44,
            "source": 96,
            "target": 99,
            "value": 1
        },
        {
            "id": 45,
            "source": 96,
            "target": 103,
            "value": 1
        },
        {
            "id": 46,
            "source": 96,
            "target": 104,
            "value": 1
        },
        {
            "id": 47,
            "source": 105,
            "target": 109,
            "value": 1
        },
        {
            "id": 48,
            "source": 105,
            "target": 115,
            "value": 1
        },
        {
            "id": 49,
            "source": 106,
            "target": 111,
            "value": 1
        },
        {
            "id": 50,
            "source": 107,
            "target": 111,
            "value": 1
        },
        {
            "id": 51,
            "source": 110,
            "target": 113,
            "value": 1
        },
        {
            "id": 52,
            "source": 110,
            "target": 114,
            "value": 1
        },
        {
            "id": 53,
            "source": 110,
            "target": 116,
            "value": 1
        },
        {
            "id": 54,
            "source": 117,
            "target": 123,
            "value": 1
        },
        {
            "id": 55,
            "source": 119,
            "target": 120,
            "value": 1
        },
        {
            "id": 56,
            "source": 119,
            "target": 124,
            "value": 1
        },
        {
            "id": 57,
            "source": 119,
            "target": 126,
            "value": 1
        },
        {
            "id": 58,
            "source": 121,
            "target": 122,
            "value": 1
        },
        {
            "id": 241,
            "source": 121,
            "target": 160,
            "value": 1
        },
        {
            "id": 59,
            "source": 123,
            "target": 125,
            "value": 1
        },
        {
            "id": 242,
            "source": 124,
            "target": 165,
            "value": 1
        },
        {
            "id": 60,
            "source": 129,
            "target": 133,
            "value": 1
        },
        {
            "id": 61,
            "source": 130,
            "target": 141,
            "value": 1
        },
        {
            "id": 62,
            "source": 132,
            "target": 140,
            "value": 1
        },
        {
            "id": 63,
            "source": 133,
            "target": 140,
            "value": 1
        },
        {
            "id": 64,
            "source": 136,
            "target": 140,
            "value": 1
        },
        {
            "id": 65,
            "source": 138,
            "target": 140,
            "value": 1
        },
        {
            "id": 66,
            "source": 143,
            "target": 156,
            "value": 1
        },
        {
            "id": 67,
            "source": 144,
            "target": 156,
            "value": 1
        },
        {
            "id": 68,
            "source": 145,
            "target": 149,
            "value": 1
        },
        {
            "id": 69,
            "source": 145,
            "target": 152,
            "value": 1
        },
        {
            "id": 70,
            "source": 145,
            "target": 153,
            "value": 1
        },
        {
            "id": 71,
            "source": 147,
            "target": 151,
            "value": 1
        },
        {
            "id": 72,
            "source": 151,
            "target": 155,
            "value": 1
        },
        {
            "id": 73,
            "source": 152,
            "target": 153,
            "value": 1
        },
        {
            "id": 74,
            "source": 157,
            "target": 158,
            "value": 1
        },
        {
            "id": 75,
            "source": 158,
            "target": 162,
            "value": 1
        },
        {
            "id": 76,
            "source": 158,
            "target": 163,
            "value": 1
        },
        {
            "id": 77,
            "source": 160,
            "target": 163,
            "value": 1
        },
        {
            "id": 78,
            "source": 162,
            "target": 165,
            "value": 1
        },
        {
            "id": 79,
            "source": 162,
            "target": 169,
            "value": 1
        },
        {
            "id": 80,
            "source": 167,
            "target": 169,
            "value": 1
        },
        {
            "id": 81,
            "source": 172,
            "target": 181,
            "value": 1
        },
        {
            "id": 82,
            "source": 175,
            "target": 179,
            "value": 1
        },
        {
            "id": 83,
            "source": 183,
            "target": 188,
            "value": 1
        },
        {
            "id": 84,
            "source": 185,
            "target": 192,
            "value": 1
        },
        {
            "id": 85,
            "source": 188,
            "target": 189,
            "value": 1
        }]}
    #リストに変換してここにかいたらええねん

    jsonData = json.load(f)

    #nodes = jsonData["nodes"]
    links = jsonData["links"]
    #links = f

    #nodes_list = []
    links_list = []

    #for node in nodes:
        # print(node)
        # print(node["id"])
        #nodes_list.append(node["name"])


    for link in links:
        l = [(link["source"], link["target"])]
        #links_list.append(l)

        G.add_edges_from(l)




    return jsonify(json_graph.node_link_data(G))

"""




if __name__ == '__main__':
    app.run()
