<template>
  <div>
      <div class="wrapper">
        <Hello />
      </div>
    <eg-renderer
      ref="gene"
      width="600"
      height="400"
      graph-nodes-property="nodes"
      graph-links-property="links"
      node-id-property="id"
      link-source-property="source"
      link-target-property="target"
      link-type-property="$none"
      default-node-fill-color="#000"
      default-link-stroke-width="1"
      default-link-stroke-color="#000"
    ></eg-renderer>
    <button @click="layout">描画する</button>
  </div>

</template>

<script>

import Hello from '@/components/HelloWorld.vue'

import '@webcomponents/custom-elements'
import axios from 'axios'
import {
  Graph,
  GraphAttributes,
  NodeList,
  FMMMLayout
} from 'emogdf'
import 'eg-renderer'
import egraph from './egraph'

const applyOGDF = (graphData) => {
  const indexToNode = new Map()
  const indexToEdge = new Map()
  const graph = new Graph()
  for (const u of graphData.nodes) {
    indexToNode.set(u.id, graph.newNode())
    indexToEdge.set(u.id, new Map())
  }
  for (const link of graphData.links) {
    indexToEdge.get(link.source).set(link.target, graph.newEdge(indexToNode.get(link.source), indexToNode.get(link.target)))
  }

  const {nodeGraphics, edgeGraphics, nodeStyle, edgeStyle} = GraphAttributes
  const attributes = new GraphAttributes(graph, nodeGraphics | edgeGraphics | nodeStyle | edgeStyle)
  const nodes = new NodeList()
  graph.allNodes(nodes)

  const layout = new FMMMLayout()
  layout.unitEdgeLength = 200
  layout.call(attributes)

  for (const u of graphData.nodes) {
    const node = indexToNode.get(u.id)
    u.x = attributes.x(node)
    u.y = attributes.y(node)
  }
}

const applyEdgeBundling = (graphData, mod) => {
  const { Graph: EGraph, ForceDirectedEdgeBundling } = mod
  const indexToNode = new Map()
  const graph = new EGraph()
  graphData.nodes.forEach((node, i) => {
    indexToNode.set(node.id, i)
    graph.addNode(i, node)
  })
  for (const link of graphData.links) {
    if (link.visibility) {
      graph.addEdge(indexToNode.get(link.source), indexToNode.get(link.target), link)
    }
  }
  const edgeBundling = new ForceDirectedEdgeBundling()
  const bends = edgeBundling.call(graph, graphData.nodes)
  Array.from(graph.edges()).forEach(([u, v], i) => {
    graph.edge(u, v).bends = bends[i].bends.map(({ x, y }) => [x, y])
  })
}

const layout = (graphData) => {
  return egraph().then((mod) => {
    applyOGDF(graphData)
    applyEdgeBundling(graphData, mod)
  })
}

export default {
  components: { Hello },
  name: 'App',
  data: function () {
    return {
      graph: {}
    }
  },
  created: function () {
    this.data = {
      nodes: [],
      links: []
    }
    axios.get('/api/network').then(res => {
      this.graph = res.data
    })
  },
  mounted: function () {
    this.$refs.gene.load(this.data)

    let graphData = this.graph
    layout(graphData).then(() => {
      Object.assign(this.data, graphData)
      this.$refs.gene.update()
      this.$refs.gene.autoCentering = false
    })
  },
  methods: {
    layout () {
      console.log(this.graph)
      let graphData = this.graph
      layout(graphData).then(() => {
        Object.assign(this.data, graphData)
        this.$refs.gene.update()
        this.$refs.gene.autoCentering = false
      })
    }
  }
}

</script>

<style>
</style>
