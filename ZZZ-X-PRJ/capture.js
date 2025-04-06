const puppeteer = require('puppeteer');

(async () => {
    // Inicializa o navegador
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // Carrega a página HTML local ou remota
    await page.goto('file:///H:/ZZZ-X-PRJ/xchtml/xp3.html'); // Para arquivos locais
    // Ou use: await page.goto('http://localhost:8000/app.html'); // Para servidor local

    // Captura a tela e salva como imagem
    await page.screenshot({ path: 'img1.jpg', fullPage: true });

    // Fecha o navegador
    await browser.close();
})();