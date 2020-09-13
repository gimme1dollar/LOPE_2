<template>
  <v-card>
    <v-tabs v-model="tab" centered>
      <v-tabs-slider color="black"></v-tabs-slider>
      <v-tab v-for="item in items" :key="item.key">{{item.name}}</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item v-for="item in items" :key="item.key">
        <v-treeview :items="item.memes">
          <template slot="label" slot-scope="props">
            <v-chip-group>
              <router-link :to="props.item.to" style="margin-right:10px; text-decoration: none; color: inherit;">
                <div :style="TextStyle(props.item)">{{props.item.name}}</div>
              </router-link>
              <v-chip x-small v-for="property in props.item.properties" :key="property.property">
                {{property.property}}
              </v-chip>
            </v-chip-group>
          </template>
        </v-treeview>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      tab: null,
      items: [
        {'key': 'HUMAN', 'name': '인류문명', 'memes': []},
        {'key': 'MATH', 'name': '수학도구', 'memes': []},
        {'key': 'ROBOT', 'name': '지능로봇', 'memes': []},
        {'key': 'SPACE', 'name': '은하건설', 'memes': []},
        {'key': 'REALITY', 'name': '현실구조', 'memes': []}
      ]
    }
  },
  mounted: function () {
    this.FetchMemes()
  },
  methods: {
    TextStyle (meme) {
      let color = 'black'
      if (meme.type === 'PROJECT') {
        color = 'green'
      } else if (meme.type === 'SMALLC') {
        color = 'red'
      } else if (meme.type === 'LARGEC') {
        color = 'blue'
      }
      return 'color: ' + color
    },
    CreateNode (meme) {
      return {
        id: meme.id,
        name: meme.name,
        type: meme.type,
        properties: meme.properties,
        to: '/meme/' + meme.id,
        children: []
      }
    },
    DFS (node, graph) {
      const app = this
      graph.forEach(edge => {
        if (edge.parent === node.id) {
          const newNode = app.CreateNode(edge)
          app.DFS(newNode, graph)
          node.children.push(newNode)
        }
      })
    },
    CreateTree (data) {
      const app = this
      const tree = []
      data.forEach(meme => {
        if (meme.parent === null) {
          const newNode = app.CreateNode(meme)
          app.DFS(newNode, data)
          tree.push(newNode)
        }
      })
      return tree
    },
    FetchMemes () {
      const app = this
      const requests = []
      for (let item of app.items) {
        const request = axios.get(process.env.API_URL + '/meme/' + item.key)
        requests.push(request)
      }

      axios.all(requests).then(axios.spread((...responses) => {
        for (let i = 0; i < responses.length; i++) {
          app.items[i].memes = app.CreateTree(responses[i].data)
        }
      }))
    }
  }
}
</script>
