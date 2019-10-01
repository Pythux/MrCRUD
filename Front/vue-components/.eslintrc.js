module.exports = {
    "root": true,
    "env": {
        "node": true
    },
    "extends": [
        "plugin:vue/recommended",
        "@vue/standard"
    ],
    "rules": {
        'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        "indent": [
            1,
            4
        ],
        "comma-dangle": [
            "error",
            "always-multiline"
        ],
        "vue/max-attributes-per-line": [
            "error",
            {
                "singleline": 8,
                "multiline": {
                    "max": 1,
                    "allowFirstLine": false
                }
            }
        ]
    },
    "parserOptions": {
        "parser": "babel-eslint"
    }
}
