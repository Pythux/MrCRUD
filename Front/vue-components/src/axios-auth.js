import Axios from 'axios'
import store from './store'

const axiosAuth = Axios.create(
    {
        baseURL: 'http://localhost:8000/api',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
    }
)

axiosAuth.interceptors.request.use(
    config => {
        if (store.state.authToken) {
            config.headers['Authorization'] = `Bearer ${store.state.authToken}`
        }
        return config
    }, error => {
        Promise.reject(error)
    }
)

axiosAuth.getRelative = absURL => {
    const base = axiosAuth.defaults.baseURL
    if (absURL.startsWith(base)) {
        return absURL.substr(base.length)
    }
    return null
}

export default axiosAuth
