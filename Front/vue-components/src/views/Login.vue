<template>
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
          <v-form ref="form" v-model="valid" lazy-validation @submit.prevent="submit">
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
              <v-btn type="submit" :disabled="!valid" color="primary" style="text-transform: none">
                {{ actionTxt }}
              </v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

export default {
    props: {
        action: {
            type: String,
            required: true,
            default: 'sign-in',
            validator(value) { // this function is not run on --production mode
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
    data() {
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
    computed: {
        isActionLogin() { return this.action === 'login' },
        otherAction() { return this.isActionLogin ? 'sign-in' : 'login' },
        otherActionTxt() {
            return this.txt[this.otherAction]
        },
        actionTxt() {
            return this.txt[this.action]
        },
    },
    watch: {
        action() {
            // on switch of action:
            this.loginRules = this.loginRules.slice(0, 2)
            this.resetValidation()
        },
    },
    methods: {
        submit() {
            const catcher = response => {
                if (response.response.data.username) {
                    this.addLoginErrorValidation(response.response.data.username[0])
                } else return Promise.reject(response)
            }
            const login = () => this.$http.get('/login', { auth: { username: this.login, password: this.password } })
                .then(result => {
                    this.$store.dispatch('login', { token: result.data.jwt, username: this.login })
                    this.$router.push({ name: 'home' })
                })
                .catch(catcher)
            if (this.$refs.form.validate()) {
                if (this.isActionLogin) {
                    login()
                } else {
                    this.$http.post('/user', { username: this.login, password: this.password })
                        .then(result => login())
                        .catch(catcher)
                }
            }
        },
        addLoginErrorValidation(errorMsg) {
            let login = this.login
            this.loginRules.push(v => v !== login || errorMsg)
            this.$refs.form.validate()
        },
        resetValidation() {
            this.$refs.form.resetValidation()
        },
    },
}
</script>
