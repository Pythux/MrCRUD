<template>
  <div v-if="id === undefined || (post !== undefined)" class="col-md-10 offset-1">
    <form @submit.prevent="submit">
      <div class="form-group pt-4">
        <div class="d-flex">
          <label for="id_title" class="col-md-2">Title:</label>
        </div>

        <input
          id="id_title"
          v-model="title"
          class="form-control"
          type="text"
          name="title"
        >
      </div>
      <div class="form-group">
        <div class="d-flex">
          <label for="id_content" class="col-md-2">Content:</label>
        </div>
        <textarea
          id="id_content"
          v-model.lazy="content"
          class="form-control"
          name="content"
          rows="8"
          cols="80"
        />
      </div>
      <input
        id="submit"
        type="submit"
        value="Submit"
        class="btn btn-success"
      >
    </form>
  </div>
</template>

<script>
export default {
    props: {
        id: { type: [String, Number], default: undefined, required: false },
    },
    data () {
        return {
            post: undefined,
            title: '',
            content: '',
        }
    },
    mounted () {
        if (this.id !== undefined) {
            this.$http.get(`/post/${this.id}`).then(result => {
                this.post = result.data
                this.title = this.post.title
                this.content = this.post.content
            })
        }
    },
    methods: {
        submit () {
            let payload = { title: this.title, content: this.content }
            let complement = ''
            let action = 'created'
            let http = this.$http.post
            if (this.id !== undefined) {
                http = this.$http.put
                complement = `/${this.id}`
                action = 'updated'
            }
            http(`/post${complement}`, payload)
                .then(result => {
                    this.$store.commit('toast', { title: `post ${action} successfully !` })
                    this.$router.push({ name: 'home' })
                })
        },
    },
}
</script>
