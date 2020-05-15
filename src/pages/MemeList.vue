<template>
  <div>
    <meme v-for="meme in memes" :key="meme.id" :id="meme.id"/>
  </div>
</template>

<script>
import axios from 'axios'
import Meme from '@/components/Meme'

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
    FetchMemes () {
      var app = this
      axios.get(process.env.API_URL + '/meme')
        .then(function (response) {
          app.memes = response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  components: {
    Meme
  }
}
</script>
