// Importa o módulo HTTP do Node.js
const http = require('http');
const fs = require('fs');
const path = require('path');

// Define a porta do servidor
const PORT = 3001;
// Cria o servidor
const server = http.createServer((req, res) => {
    // Obtém o caminho do arquivo solicitado
    let filePath = '.' + req.url;
    if (filePath === './') {
        filePath = './index.html'; // Página padrão (index.html)
    }
    // Determina a extensão do arquivo
    const extname = String(path.extname(filePath)).toLowerCase();
    const mimeTypes = {
        '.html': 'text/html',
        '.js': 'text/javascript',
        '.css': 'text/css',
        '.json': 'application/json',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.gif': 'image/gif',
        '.svg': 'image/svg+xml',
        '.wav': 'audio/wav',
        '.mp4': 'video/mp4',
    };
    const contentType = mimeTypes[extname] || 'application/octet-stream';
    // Lê o arquivo solicitado
    fs.readFile(filePath, (err, content) => {
        if (err) {
            if (err.code === 'ENOENT') {
                // Arquivo não encontrado
                res.writeHead(404);
                res.end('Arquivo não encontrado');
            } else {
                // Outro erro
                res.writeHead(500);
                res.end(`Erro no servidor: ${err.code}`);
            }
        } else {
            // Arquivo encontrado, retorna o conteúdo
            res.writeHead(200, { 'Content-Type': contentType });
            res.end(content, 'utf-8');
        }
    });
});

// Inicia o servidor
server.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});