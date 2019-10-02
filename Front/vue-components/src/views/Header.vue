<template>
  <v-app-bar app color="cyan">
    <v-spacer />
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn color="primary" dark style="text-transform: none" v-on="on">
          <LayersIcon />{{ username }}
        </v-btn>
      </template>
      <v-btn @click="logout">
        logout
      </v-btn>
    </v-menu>
  </v-app-bar>
</template>

<script>
export default {
    computed: {
        username() {
            return this.$store.state.username
        },
    },
    methods: {
        logout() {
            this.$store.dispatch('logout')
            this.$router.push({ name: 'login' })
        },
    },
}
</script>

<style>

</style>
