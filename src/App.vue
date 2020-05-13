<template>
  <div id="app">
  <v-app>
  <v-app-bar app/>

  <v-content>
    <v-container fluid>
      <router-view></router-view>
    </v-container>
  </v-content>

  <v-footer app/>
</v-app>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
