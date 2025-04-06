// Função para decompor o número em potências de 2
function decomposeNumber() {
    const decimalInput = document.getElementById('decimal').value;
    const decimal = parseInt(decimalInput, 10);
  
    if (isNaN(decimal) || decimal < 0) {
      alert('Por favor, insira um número decimal válido e não negativo.');
      return;
    }
  
    const result = [];
    let remainingValue = decimal;
  
    // Itera sobre as potências de 2, começando de 0 até 31 (32 bits)
    for (let i = 0; i < 32; i++) {
      const powerOfTwo = Math.pow(2, i);
      if ((remainingValue & powerOfTwo) !== 0) {
        result.push({
          power: i,
          decimalValue: powerOfTwo,
          hexValue: `0x${powerOfTwo.toString(16).padStart(8, '0')}`
        });
        remainingValue -= powerOfTwo;
      }
    }
  
    // Exibe os resultados na tabela
    const tableBody = document.querySelector('#result-table tbody');
    tableBody.innerHTML = ''; // Limpa a tabela antes de inserir novos resultados
  
    result.forEach(item => {
      const row = document.createElement('tr');
  
      const powerCell = document.createElement('td');
      powerCell.textContent = `2^${item.power}`;
  
      const decimalCell = document.createElement('td');
      decimalCell.textContent = item.decimalValue;
  
      const hexCell = document.createElement('td');
      hexCell.textContent = item.hexValue;
  
      row.appendChild(powerCell);
      row.appendChild(decimalCell);
      row.appendChild(hexCell);
      tableBody.appendChild(row);
    });
  }