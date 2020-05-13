<template>
    <v-card>
    <v-toolbar flat color="primary" dark>
      <v-toolbar-title>{{ id }}</v-toolbar-title>
    </v-toolbar>
    <v-tabs vertical>
      <v-tab v-for="detail in details" v-bind:key="detail.id">
        {{ detail.category }}
      </v-tab>

      <v-tab-item v-for="detail in details" v-bind:key="detail.id">
        <v-card flat>
          <h1>hello, world!</h1>
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
          app.details = response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  name: 'Meme'
}
</script>
