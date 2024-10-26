'use strict'
/* eslint-env node, es6 */

// importe le pacquet express
const express = require('express')

const path = require('path')

// cree une application express
const app = express()

// importe la fonction genererPageAccueil
const genererPageAccueil = require('./pages/index-get')

app.get('/', async(req, res) => {
    const indexHtml = await genererPageAccueil()
    
    res.send(indexHtml)
})
// retourne les images
app.use('/images', express.static(path.join(__dirname, '../../../frontend/images')));

// retourne tout le dossier frontend comme statique
app.use(express.static(path.join(__dirname, '../../../style.css')));


// demarre le serveur sur le port 5500
const PORT = 5500
app.listen(PORT, () => {
    console.log(`serveur demarré http://localhost:${PORT}`)
    })