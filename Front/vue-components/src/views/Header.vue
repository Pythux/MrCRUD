<template>
  <v-app-bar app color="cyan">
    <v-row align="center">
      <v-col offset-sm="2" offset-md="3" cols="6" align-self="center" justify-self="center">
        <router-link style="text-decoration: none" :to="{name: 'home'}">
          <v-row justify="center" align="center">
            <h1 style="color: #f9f0e1">
              Creative's Mind
            </h1>
            <div class="quote ml-2 align-self-end">
              Mr. CRUD
            </div>
          </v-row>
        </router-link>
      </v-col>
      <v-col>
        <v-row justify="end" align="center">
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <router-link :to="{name: 'create'}">
                <v-btn color="success" fab class="mr-2" v-on="on">
                  <PlusCircleIcon />
                </v-btn>
              </router-link>
            </template>
            <span>Create a post</span>
          </v-tooltip>

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
        </v-row>
      </v-col>
    </v-row>
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

<style lang="stylus">
@import url('https://fonts.googleapis.com/css?family=Lobster&display=swap%27');

h1, h2, h3 {
    font-family: 'Lobster', cursive;
}

.quote {
    font-family: 'Lobster', cursive;
    font-size: 80%
    color: #d9e9fe
    font-style: italic

    &::before {
        content: "\2014 \00A0" // em dash, nbsp
    }
}
</style>
