<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar color="primary" dark flat>
              <v-toolbar-title>{{ actionTxt }}:</v-toolbar-title>
              <v-spacer />
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <router-link :to="{name: otherAction}">
                    <v-btn large fab color="purple" v-on="on">
                      <UserPlusIcon v-if="isActionLogin" size="1.5x" />
                      <TerminalIcon v-else />
                    </v-btn>
                  </router-link>
                </template>
                <span>{{ otherActionTxt }}</span>
              </v-tooltip>
            </v-toolbar>
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-card-text>
                <v-text-field v-model="login" label="Login" name="login" :rules="loginRules" prepend-icon="mdi-account-question" type="text" />
                <v-text-field v-model="password" label="Password" name="password" type="password" :rules="passwordRules">
                  <template v-slot:prepend>
                    <key-icon />
                  </template>
                </v-text-field>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn :disabled="!valid" color="primary" style="text-transform: none" @click="validate">
                  {{ actionTxt }}
                </v-btn>
              </v-card-actions>
            </v-form>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>

export default {
    props: {
        action: {
            type: String,
            required: true,
            default: 'sign-in',
            validator (value) { // this function is not run on --production mode
                const valideVal = ['sign-in', 'login']
                if (valideVal.indexOf(value) === -1) {
                    // eslint-disable-next-line
                    console.error(`"${value}" is not a valide action`)
                    // eslint-disable-next-line
                    console.warn(`valide action are in ${valideVal}`)
                    return false
                }
                return true
            },
        },
    },
    data () {
        return {
            valid: true,
            loginRules: [
                value => !!value || 'Required.',
                value => (value || '').length <= 20 || 'Max 20 characters',
            ],
            passwordRules: [v => !!v || 'Required.'],
            txt: { 'sign-in': 'Sign In', 'login': 'Login' },
            login: '',
            password: '',
        }
    },
    beforeRouteEnter (to, from, next) {
        console.log('beforeRouteEnter')
        // check if already logged in
        next()
    },
    computed: {
        isActionLogin () { return this.action === 'login' },
        otherAction () { return this.isActionLogin ? 'sign-in' : 'login' },
        otherActionTxt () {
            return this.txt[this.otherAction]
        },
        actionTxt () {
            return this.txt[this.action]
        },
    },
    watch: {
        action () {
            // on switch of action:
            this.resetValidation()
        },
    },
    methods: {
        validate () {
            if (this.$refs.form.validate()) {
                if (this.isActionLogin) {
                    this.$http.get('/login', { auth: { username: this.login, password: this.password } })
                        .then(result => this.$store.commit('set_authToken', result.data.jwt))
                        .catch(response => {
                            if (response.response.data.username) {
                                let username = this.login
                                let errormsg = response.response.data.username[0]
                                this.loginRules.push(v => v !== username || errormsg)
                            }
                            this.$refs.form.validate()
                        })
                } else {
                    this.$http.post('/user', { username: this.login, password: this.password })
                        .then(result => console.log(result))
                        .catch(response => {
                            if (response.response.data.username) {
                                let username = this.login
                                let errormsg = response.response.data.username[0]
                                this.loginRules.push(v => v !== username || errormsg)
                            }
                            this.$refs.form.validate()
                        })
                }
            }
        },
        resetValidation () {
            this.$refs.form.resetValidation()
        },
    },
}
</script>
