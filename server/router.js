const express = require('express')

const app = express()
    // 静态资源托管

app.use('/static', express.static('../')) // 对到data目录

app.listen(3306, () => (console.log('监听3306端口')))

// 命令行 执行nodemon router.js
// http://127.0.0.1:3306/static/data/1/imgs/9.72_12.6_0.png