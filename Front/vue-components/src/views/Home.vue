<template>
  <div>
    <template v-if="username">
      hellow {{ username }} !
      <v-btn @click="logout">
        logout
      </v-btn>
    </template>
    <template v-else>
      <router-link :to="{name: 'login'}">
        login
      </router-link>
      {{ }}
    </template>
  </div>
</template>

<script>
export default {
    computed: {
        username () {
            return this.$store.state.username
        },
    },
    methods: {
        logout () {
            this.$store.dispatch('logout')
        },
    },

}
</script>
