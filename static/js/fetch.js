function fetchSupplier() {
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
}


setInterval(fetchSupplier, 5000);
fetchSupplier();