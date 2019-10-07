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

async function throttling(returned) {
    return new Promise(resolve => {
        setTimeout(() => { resolve(returned) }, 2000)
    })
}

axiosAuth.interceptors.request.use(config => {
    return throttling(config)
}, error => {
    return Promise.reject(error)
})

const toRelative = absURL => {
    const base = axiosAuth.defaults.baseURL
    if (absURL.startsWith(base)) {
        return absURL.substr(base.length)
    }
    return null
}

axiosAuth.toRelative = (absURLorObj, listAttr) => {
    if (listAttr === undefined) {
        return toRelative(absURLorObj)
    }
    let obj = Object.assign({}, absURLorObj) // no side effect
    listAttr.forEach(el => {
        if (obj[el] instanceof Array) {
            obj[el] = obj[el].map(toRelative)
        } else {
            obj[el] = toRelative(obj[el])
        }
    })
    return obj
}

export default axiosAuth
