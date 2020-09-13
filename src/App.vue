<template>
  <div id="app">
    <v-app>
      <v-main>
        <v-container fluid>
          <v-app-bar>
            <v-toolbar-title>Cross</v-toolbar-title>
            <v-spacer/>
            <v-btn text to="/">Home</v-btn>
            <v-btn text to="/meme">Memes</v-btn>
          </v-app-bar>
          <router-view/>
        </v-container>
      </v-main>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
