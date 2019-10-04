<template>
  <v-container fill-height>
    <v-row justify="center">
      <v-col xs="12" sm="8" md="6">
        <v-card v-if="post">
          <v-card-title>
            {{ post.title }}
          </v-card-title>
          <v-card-text style="white-space: pre-wrap;">
            {{ post.content }}
          </v-card-text>
          <v-card-actions>
            by: {{ $store.state.users[post.creator] }}
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
    props: {
        pathPost: {
            type: String,
            requiered: true,
            default: undefined,
        },
    },
    data() {
        return {
            post: undefined,
        }
    },
    mounted() {
        this.$http.get(this.pathPost).then(responce => { this.post = responce.data })
    },
}
</script>
