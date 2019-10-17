<template>
  <v-container class="mt-5">
    <v-row justify="center">
      <lottie
        v-if="animationData"
        :key="animationChanged"
        :options="{animationData}"
        :height="100"
        :width="100"
      />
      <p v-else>
        You have no profile animation
      </p>
    </v-row>
    <v-row justify="center">
      <v-btn v-if="!formProfile" @click="formProfile = true">
        <template v-if="animationData">
          change the
        </template>
        <template v-else>
          add a
        </template>
        profile animation
      </v-btn>
    </v-row>
    <v-row justify="center">
      <v-form v-if="formProfile" v-model="valid" lazy-validation @submit.prevent="submit">
        give a lottie JSON via url to the JSON or directly the JSON:
        <v-text-field v-model="urlLottie" label="url to lottie json" />
        <v-textarea v-model="rawLottie" label="lottie json" :rules="JsonRules" />
        <v-row justify="space-around">
          <v-btn type="sumbit" :disabled="!valid" color="success" style="text-transform: none">
            Send
          </v-btn>
          <v-btn color="primary" style="text-transform: none;" @click="formProfile = false; urlLottie = ''; rawLottie = ''">
            Cancel
          </v-btn>
        </v-row>
      </v-form>
    </v-row>
  </v-container>
</template>

<script>
export default {
    data() {
        return {
            formProfile: false,
            urlLottie: undefined,
            rawLottie: undefined,
            valid: true,
            JsonRules: [v => {
                if (v === '') {
                    return true
                }
                try {
                    JSON.parse(v)
                    return true
                } catch (e) {
                    return 'It\'s no a valide JSON'
                }
            }],
            animationChanged: 1,
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
    watch: {
        animationData() {
            this.animationChanged += 1
        },
    },
    methods: {
        submit() {
            if (!this.urlLottie && !this.rawLottie) {
                this.formProfile = false
            }
            if (this.urlLottie) {

            } else {
                const changeUserLottie = response => {
                    this.rawLottie = ''
                    this.formProfile = false
                    this.$store.commit('set-user-lottie', { userPath: this.user.url, lottie: JSON.parse(response.data.lottie_json) })
                }
                if (this.animationData) {
                    this.$http.patch(`/user_lottie/${this.user.id}`, { lottie_json: this.rawLottie }).then(changeUserLottie)
                } else {
                    this.$http.post('/user_lottie', { user: this.user.id, lottie_json: this.rawLottie }).then(changeUserLottie)
                }
            }
        },
    },
}
</script>

<style>

</style>
