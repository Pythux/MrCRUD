<template>
  <div class="home">
    <img
      alt="Vue logo"
      src="../assets/logo.png"
    >
    <HelloWorld msg="Welcome to Your Vue.js App" />
    {{ get }}
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
    name: 'Home',
    components: {
        HelloWorld,
    },
    data () {
        return {
            get: '',
        }
    },
    mounted () {
        this.$http.get('/')
            .then(response => { this.get = response })
    },
}
</script>
