<template>
  <v-container fill-height>
    <v-row justify="center">
      <v-col xs="12" sm="8" md="6">
        <v-card :loading="loadingCard">
          <v-form @submit.prevent="submit">
            <v-card-title>
              <v-btn icon fab color="purple" @click="editBtn">
                <edit-3-icon v-if="!edit" />
                <send-icon v-else />
              </v-btn>
              <v-text-field v-if="edit" v-model="title" />
              <template v-else>
                {{ title }}
              </template>
            </v-card-title>
            <v-card-text style="white-space: pre-wrap;">
              <v-textarea v-if="edit" v-model="content" auto-grow />
              <template v-else>
                {{ content }}
              </template>
            </v-card-text>
            <v-card-actions v-if="edit">
              <!-- {{ $store.state.users[post.creator] }} -->
              <v-btn type="submit">
                <save-icon />
              </v-btn>
            </v-card-actions>
          </v-form>
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
            loadingCard: true,
            edit: false,
            title: undefined,
            content: undefined,
        }
    },
    watch: {
        post(post, _) {
            this.title = post.title
            this.content = post.content
        },
    },
    mounted() {
        this.$http.get(this.pathPost).then(responce => {
            this.post = this.$http.toRelative(responce.data, ['url', 'creator'])
            this.$store.dispatch('check-user', this.post.creator)
            this.loadingCard = false
        })
    },
    methods: {
        editBtn() {
            if (this.edit) {
                // save
                this.loadingCard = true
                this.$http.patch(this.pathPost, { title: this.title, content: this.content })
                    .then(response => {
                        this.edit = false
                        this.loadingCard = false
                    })
            } else {
                // edit
                this.edit = !this.edit
            }
        },
        submit() { this.editBtn() },
    },
}
</script>
