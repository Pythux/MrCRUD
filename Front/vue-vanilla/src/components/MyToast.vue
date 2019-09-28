<template>
  <div>
    <div
      v-for="(toast) in toasts"
      :key="toast.id"
      class="alert alert-success alert-dismissible offset-md-2 col-md-8"
      role="alert"
    >
      <strong>{{ toast.title }}</strong> {{ toast.content }}
      <button class="close" aria-label="Close" @click="close(toast.id)">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
    computed: {
        toasts () {
            return this.$store.state.toasts
        },
    },
    methods: {
        close (id) {
            this.$store.commit('delete_toast', id)
        },
    },
}
</script>
