<template>
  <v-container fill-height>
    <v-row justify="center">
      <v-col xs="12" sm="8" md="6">
        <v-card :loading="loadingCard">
          <v-form @submit.prevent="submit">
            <v-card-title>
              <v-btn icon fab color="purple" @click="submit">
                <edit-3-icon v-if="!edit" />
                <send-icon v-else />
              </v-btn>
              <v-text-field v-if="edit" v-model="title" label="Title" />
              <template v-else>
                {{ title }}
              </template>
            </v-card-title>
            <v-card-text style="white-space: pre-wrap;">
              <v-textarea v-if="edit" v-model="content" label="Content" auto-grow />
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
            requiered: false,
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
    computed: {
        isCreation() {
            return this.pathPost === undefined
        },
    },
    watch: {
        post(post, _) {
            this.title = post.title
            this.content = post.content
        },
    },
    mounted() {
        if (this.isCreation) {
            this.loadingCard = false
            this.edit = true
        } else {
            this.$http.get(this.pathPost).then(responce => {
                this.post = this.$http.toRelative(responce.data, ['url', 'creator'])
                this.$store.dispatch('check-user', this.post.creator)
                this.loadingCard = false
            })
        }
    },
    methods: {
        submit() {
            if (this.edit) { // save
                this.loadingCard = true
                let saveMethode = payload => this.$http.put(this.pathPost, payload)
                if (this.isCreation) {
                    saveMethode = payload => this.$http.post('/post', payload)
                }
                saveMethode({ title: this.title, content: this.content })
                    .then(response => {
                        this.edit = false
                        this.loadingCard = false
                    })
            } else { // edit
                this.edit = true
            }
        },
    },
}
</script>
