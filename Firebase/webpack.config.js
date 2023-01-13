const { watch } = require("fs")
const path = require("path")

module.exports = {
    mode: "development", //modet som körs i
    entry: "./src/index.js", // från index 
    output: {
        path: path.resolve(__dirname, "dist"), // lägger __dirmane i dist foldern
        filename: "bundle.js" // namnet på filen som ska skapas
    },
    watch: true // krävs för att path ska funka
}