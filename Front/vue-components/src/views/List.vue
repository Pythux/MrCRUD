<template>
  <v-container>
    <v-row>
      <v-col v-for="modulo_i in 3" :key="modulo_i" cols="12" sm="6" md="4">
        <transition-group name="slide">
          <v-card v-for="post in get_posts_modulo(3, modulo_i)" :key="post.url" class="mt-5" hover>
            <v-card-title v-highlight:color.delayed="'green'">
              {{ post.title }}
            </v-card-title>
            <v-card-text style="white-space: pre-wrap;">
              {{ post.content }}
            </v-card-text>
            <v-card-actions>
              by: {{ $store.state.users[post.creator] }}
              <router-link :to="{name: 'detail', params:{ pathPost: post.url }}">
                <v-btn>yo</v-btn>
              </router-link>
            </v-card-actions>
          </v-card>
        </transition-group>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
    directives: {
        highlight: {
            bind(el, binding, vnode) {
                let delay = 0
                if (binding.modifiers['delayed']) {
                    delay = 2000
                }
                let oldStyle = { color: el.style.color }
                setTimeout(() => {
                    if (binding.arg === 'color') {
                        el.style.color = binding.value
                    }
                }, delay)
                if (binding.modifiers['disapear']) {
                    setTimeout(() => { el.style = { ...el.style, ...oldStyle } }, delay + 2000)
                }
            },
        },
    },
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
            this.$http.get('/post').then(response => {
                this.posts = response.data.results.map(post => {
                    post = this.$http.toRelative(post, ['creator', 'url'])
                    this.$store.dispatch('check-user', post.creator)
                    return post
                })
            })
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

<style lang="stylus">

.slide-enter
    opacity 0

.slide-enter-active
    animation slide-in 1s ease-out
    transition opacity 1s

@keyframes slide-in
    from
        transform translateY(20px)
    to
        transform translateY(0)

</style>
