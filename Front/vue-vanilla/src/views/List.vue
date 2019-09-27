<template>
  <div class="row justify-content-center pt-4">
    <div v-for="post in post_list" :key="post.id" class="col-md-4">
      <div class="card p-4 shadow-lg" style="height: 400px;">
        <div class="card-body">
          <h2>{{ post.title }}</h2>
          <hr>
          <p>{{ post.content }}...</p>
        </div>
        <router-link :to="{name:'detail', params:{id:post.id}}" class="btn-circle align-self-center btn btn-outline-info d-flex justify-content-center">
          <span class="align-self-center">GO</span>
        </router-link>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card p-4 shadow-lg" style="height: 400px;">
        <div class="card-body">
          <h2>Create a new post ?</h2>
          <hr>
        </div>
        <router-link :to="{name:'create'}" class="btn-circle align-self-center btn btn-outline-primary d-flex justify-content-center">
          <span class="align-self-center">Create</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
    data () {
        return {
            post_list: [],
        }
    },
    mounted () {
        this.$http.get('/post').then(response => { this.post_list = response.data.results })
    },
}
</script>

<style lang="stylus" scoped>
.btn-circle
    width 60px
    height 60px
</style>
