<template>
  <div class="col-md-10 offset-md-1  pt-4">
    <div v-if="post !== undefined" class="card p-4 shadow-lg" style="height: 400px;">
      <div class="card-body">
        <h2>{{ post.title }}</h2>
        <hr>
        <p>{{ post.content }}</p>
      </div>
      <div class="d-flex justify-content-around">
        <router-link
          :to="{name:'update', params:{pk:post.id}}"
          class="btn btn-outline-info d-flex justify-content-center"
          style="height: 100px;width:100px;"
        >
          <span class="align-self-center">Update</span>
        </router-link>

        <button
          class="btn btn-outline-danger"
          style="height: 100px;width:100px;"
          @click="deleteItem"
        >
          <span class="align-self-center">Delete</span>
        </button>
      </div>
    </div>
    <div v-if="id === undefined">
      id not given
    </div>
  </div>
</template>

<script>
export default {
    props: {
        id: { type: [String, Number], default: undefined, required: true },
    },
    data () {
        return {
            post: undefined,
        }
    },
    mounted () {
        if (this.id !== undefined) {
            this.$http.get(`/post/${this.id}`).then(result => { this.post = result.data })
        }
    },
    methods: {
        deleteItem () {
            this.$http.delete(`/post/${this.id}`).then(() => {
                this.$store.dispatch('toast', { title: 'post deleted successfully !' })
                this.$router.push({ name: 'home' })
            })
        },
    },
}
</script>
