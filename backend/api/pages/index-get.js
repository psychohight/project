'use strict'
/* eslint-env node, es6 */

const { readFile } = require('fs')
const { promisify } = require('util')
const path = require('path') // Import du module path
const readFileAsync = promisify(readFile)

module.exports = async () => {
    try {
        // Correction du chemin pour pointer vers le bon dossier
        const indexPath = path.join(__dirname, '../../../frontend/index.html')
        const indexHtml = await readFileAsync(indexPath, 'utf-8')
        return indexHtml
    } catch (error) {
        console.error('Erreur lors de la lecture du fichier index.html:', error)
        throw error
    }
}
