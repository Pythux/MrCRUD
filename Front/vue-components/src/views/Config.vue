<template>
  <div>
    <lottie
      v-if="animationData"
      style=""
      :options="{animationData}"
      :height="100"
      :width="100"
    />
    <p v-else>
      No profile<br>
      animation
    </p>
    <v-btn v-if="!formProfile" @click="formProfile = true">
      <template v-if="animationData">
        change the
      </template>
      <template v-else>
        add a
      </template>
      profile animation
    </v-btn>

    <v-form v-else>
      give a lottie JSON via url to the JSON or directly the JSON:
      <v-text-field v-model="urlLottie" label="url to lottie json" />
      <v-textarea v-model="rawLottie" label="lottie json" />
      <v-btn type="sumbit">
        Send
      </v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
    data() {
        return {
            formProfile: false,
            urlLottie: undefined,
            rawLottie: undefined,
        }
    },
    computed: {
        user() {
            if (this.$store.state.users[this.$store.state.authUserPath]) {
                return this.$store.state.users[this.$store.state.authUserPath]
            }
            return ''
        },
        animationData() {
            if (this.user) {
                return this.user.lottie
            }
            return undefined
        },
    },
}
</script>

<style>

</style>
