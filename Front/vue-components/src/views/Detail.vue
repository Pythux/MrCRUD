<template>
  <v-row justify="center">
    <v-col xs="12" sm="8" md="6">
      <v-card :loading="loadingCard" @click.native="$emit('click', $event)">
        <v-form @submit.prevent="submit">
          <v-card-title>
            <v-btn v-if="permissions.edit" icon fab color="purple" @click="submit">
              <edit-3-icon v-if="!edit" />
              <send-icon v-else />
            </v-btn>
            <v-text-field v-if="edit" v-model="title" :error-messages="errors.title" label="Title" />
            <template v-else>
              {{ title }}
            </template>
          </v-card-title>
          <v-card-text style="white-space: pre-wrap;">
            <v-textarea v-if="edit" v-model="content" :error-messages="errors.content" label="Content" auto-grow />
            <template v-else>
              {{ content }}
            </template>
            <!-- {{ $store.state.users[post.creator] }} -->
            <v-divider />
            <v-card max-width="200" style="margin-top: 10px">
              <!-- class="d-flex align-center justify-start" on v-card do the same thing -->
              <v-row align="center" justify="start">
                <lottie
                  v-if="animationData"
                  style="margin: 0; margin-left: 14px; margin-top: 2px; margin-bottom: 2px;"
                  :options="{animationData}"
                  :height="100"
                  :width="100"
                />
                <div class="username">
                  {{ $store.state.users[post.creator].username }}
                </div>
              </v-row>
            </v-card>
          </v-card-text>

          <v-card-actions v-if="edit">
            <v-btn type="submit">
              <save-icon />
            </v-btn>
            <v-btn v-if="permissions.delete" @click="deletePost">
              <trash-2-icon />
            </v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-col>
  </v-row>
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
            permissions: { edit: false, delete: false },
            errors: { title: null, content: null },
            userProfile: undefined,
            animation: {
                anim: undefined,
            },
        }
    },
    computed: {
        isCreation() {
            return this.pathPost === undefined
        },
        animationData() {
            if (this.post) {
                return this.$store.state.users[this.post.creator].lottie
            }
            return undefined
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
            this.$http.get(this.pathPost).then(response => {
                this.genPermissions(new Set(response.headers.allow.split(', ')))
                this.post = this.$http.toRelative(response.data, ['url', 'creator'])
                this.$store.dispatch('check-user', this.post.creator)
                this.loadingCard = false
            })
        }
    },
    methods: {
        handleAnimation(anim) {
            this.animation.anim = anim
            // anim.play()
        },
        genPermissions(allowSet) {
            this.permissions.edit = allowSet.has('PUT')
            this.permissions.delete = allowSet.has('DELETE')
        },
        submit() {
            if (this.edit) { // save
                this.errors = { title: null, content: null }
                this.loadingCard = true
                let saveMethode = payload => this.$http.put(this.pathPost, payload)
                if (this.isCreation) {
                    saveMethode = payload => this.$http.post('/post', payload)
                }
                saveMethode({ title: this.title, content: this.content })
                    .then(response => {
                        this.edit = false
                        if (this.isCreation) {
                            this.$router.push({ name: 'home' })
                        }
                    })
                    .catch(error => {
                        this.errors.title = error.response.data.title
                        this.errors.content = error.response.data.content
                    })
                    .finally(() => { this.loadingCard = false })
            } else { // edit
                this.edit = true
            }
        },
        deletePost() {
            this.loadingCard = true
            this.$http.delete(this.pathPost).then(response => this.$emit('deleted'))
        },
    },
}
</script>

<style lang="stylus" scoped>
.username
    color blue
    text-shadow 1px 1px red
</style>
