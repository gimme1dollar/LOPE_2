<template>
  <meme :id="this.id"/>
</template>

<script>
import Meme from '@/components/Meme'

export default {
  props: ['id'],
  components: {
    Meme
  }
}
</script>
