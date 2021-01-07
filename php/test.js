const csvtojson = require('csvtojson')

const csvfilepath = "simple.csv"

csvtojson()
.fromFile(csvfilepath)
.then((json) => {
    console.log(json)
})