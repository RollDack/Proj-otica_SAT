document.getElementById("productForm").addEventListener("submit", function (event) {
    const name = document.getElementById("name").value.trim();
    const price = parseFloat(document.getElementById("price").value);
    const stock = parseInt(document.getElementById("stock").value);

    // Validação simples
    if (!name || isNaN(price) || price <= 0 || isNaN(stock) || stock < 0) {
        event.preventDefault();
        alert("Por favor, preencha todos os campos corretamente!");
    }
});