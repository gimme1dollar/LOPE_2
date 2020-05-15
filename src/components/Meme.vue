<template>
    <v-card>
    <v-toolbar flat color="primary" dark>
      <v-toolbar-title>FLEMG</v-toolbar-title>
    </v-toolbar>
    <v-tabs vertical>
      <v-tab v-for="detail in GetCategories(details)" v-bind:key="detail.category">
        {{ detail.category }}
      </v-tab>

      <v-tab-item v-for="detail in GetCategories(details)" v-bind:key="detail.category">
        <v-card flat>
          <div v-for="{summary, description, id} in detail.contents" :key="id">
            <h3>{{ summary }}</h3>
            <p>{{ description }}</p>
          </div>
        </v-card>
      </v-tab-item>
    </v-tabs>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  props: ['id'],
  data () {
    return {
      details: null
    }
  },
  mounted: function () {
    this.FetchDetails()
  },
  methods: {
    FetchDetails () {
      var app = this
      axios.get(process.env.API_URL + '/detail/meme/' + app.id)
        .then(function (response) {
          var details = new Map()
          response.data.forEach(detail => {
            if (!details.has(detail.category)) {
              details.set(detail.category, [])
            }

            details.get(detail.category).push({
              'summary': detail.summary,
              'description': detail.description
            })
          })

          app.details = details
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    GetCategories (m) {
      if (m != null) {
        var arr = []
        m.forEach((value, key) => {
          arr.push({
            'category': key,
            'contents': value
          })
        })
        return arr
      }
      return null
    }
  },
  name: 'Meme'
}
</script>
