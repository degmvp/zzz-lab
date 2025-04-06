// Simulated auxiliary table: maps bit values to permission names
const permissionFlags = [
    { bitValue: 1, permissionName: "Can Create" },
    { bitValue: 2, permissionName: "Can Read" },
    { bitValue: 4, permissionName: "Can Update" },
    { bitValue: 8, permissionName: "Can Delete" },
    { bitValue: 16, permissionName: "Can Execute" },
    { bitValue: 32, permissionName: "Can Backup" },
    { bitValue: 64, permissionName: "Can Restore" },
    { bitValue: 128, permissionName: "Sys Adm" }
  ];
  
  // Função para exibir a tabela de referência
  function displayPermissionTable() {
    const tableBody = document.querySelector('#permission-table tbody');
    permissionFlags.forEach(flag => {
      const row = document.createElement('tr');
  
      const bitValueCell = document.createElement('td');
      bitValueCell.textContent = flag.bitValue;
  
      const permissionNameCell = document.createElement('td');
      permissionNameCell.textContent = flag.permissionName;
  
      row.appendChild(bitValueCell);
      row.appendChild(permissionNameCell);
      tableBody.appendChild(row);
    });
  }
  
  // Função para decodificar permissões
  function decodePermissions() {
    const input = document.getElementById('permissions').value;
    const permissions = parseInt(input, 10);
  
    if (isNaN(permissions) || permissions < 0) {
      document.getElementById('result').textContent = 'Please enter a valid non-negative integer.';
      return;
    }
  
    // Decodifica as permissões
    const decodedPermissions = permissionFlags
      .filter(flag => (permissions & flag.bitValue) === flag.bitValue)
      .map(flag => flag.permissionName);
  
    // Exibe o resultado
    if (decodedPermissions.length === 0) {
      document.getElementById('result').textContent = 'No permissions found for this value.';
    } else {
      document.getElementById('result').textContent = `Decoded Permissions: ${decodedPermissions.join(', ')}`;
    }
  }
  
  // Exibe a tabela de referência ao carregar a página
  window.onload = displayPermissionTable;