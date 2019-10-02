<template>
  <v-container>
    <v-row justify="space-around">
      <v-col v-for="modulo_i in 3" :key="modulo_i" cols="12" sm="6" md="4">
        <v-card v-for="post in get_posts_modulo(3, modulo_i)" :key="post.id" hover>
          <v-card-title>{{ post.title }}</v-card-title>
          <v-card-text style="white-space: pre-wrap;">
            {{ post.content }}
          </v-card-text>
          <v-card-actions>yolo</v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
    data() {
        return {
            posts: [],
        }
    },
    created() {
        this.get_posts()
    },
    methods: {
        get_posts() {
            this.$http.get('/post').then(response => { this.posts = response.data.results })
        },
        get_posts_modulo(modulo, i) {
            i--
            return this.posts.filter((post, index) => {
                return index % modulo === i
            })
        },
    },
}
</script>

<style>

</style>
