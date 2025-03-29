function fetchDatabase() {
    fetch('/get-supplier')  
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("supplierTable");
            tableBody.innerHTML = "";  

            data.forEach(supplier => {
                let row = `<tr>
                            <td>${supplier.supplierID}</td>
                            <td>${supplier.name}</td>
                            <td>${supplier.contactInfo}</td>
                           </tr>`;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error('Error:', error));

        fetch('/get-inventory')  
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("inventoryTable");
            tableBody.innerHTML = "";  

            data.forEach(inventory => {
                let row = `<tr>
                            <td>${inventory.itemID}</td>
                            <td>${inventory.name}</td>
                            <td>${inventory.quantity}</td>
                            <td>${inventory.supplierID1}</td>
                            <td>${inventory.supplierID2}</td>
                            <td>${inventory.lastRestockDate}</td>
                           </tr>`;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error('Error:', error));
}


setInterval(fetchDatabase, 5000);
fetchDatabase();