<template>
  <v-treeview :items="memes">
    <template slot="label" slot-scope="props">
      <v-card color="#385F73" dark>
        <v-card-title class="headline">{{ props.item.name }}</v-card-title>
        <v-card-subtitle>{{ props.item.description }}</v-card-subtitle>
        <v-card-actions>
          <v-btn :to="props.item.to">Details</v-btn>
        </v-card-actions>
      </v-card>
    </template>
  </v-treeview>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      memes: null
    }
  },
  mounted: function () {
    this.FetchMemes()
  },
  methods: {
    CreateNode (meme) {
      var newNode = {
        id: meme.id,
        name: meme.name,
        description: 'Description of Project',
        to: '/meme/' + meme.id,
        children: []
      }

      return newNode
    },
    DFS (node, graph) {
      var app = this
      graph.forEach(edge => {
        if (edge.parent === node.id) {
          var newNode = app.CreateNode(edge)
          app.DFS(newNode, graph)
          node.children.push(newNode)
        }
      })
    },
    CreateTree (data) {
      var app = this
      var tree = []
      data.forEach(meme => {
        if (meme.parent == null) {
          var newNode = app.CreateNode(meme)
          app.DFS(newNode, data)
          tree.push(newNode)
        }
      })
      console.log(tree)
      app.memes = tree
    },
    FetchMemes () {
      var app = this
      axios.get(process.env.API_URL + '/meme')
        .then(function (response) {
          app.CreateTree(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
