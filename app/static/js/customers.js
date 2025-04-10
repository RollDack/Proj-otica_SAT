
document.getElementById("customerForm").addEventListener("submit", function (event) {
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();

    // Validação simples
    if (!name || !email || !phone) {
        event.preventDefault();
        alert("Por favor, preencha todos os campos corretamente!");
    } else if (!validateEmail(email)) {
        event.preventDefault();
        alert("Por favor, insira um email válido!");
    } else if (!validatePhone(phone)) {
        event.preventDefault();
        alert("Por favor, insira um telefone válido!");
    }
});

// Função para validar email
function validateEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

// Função para validar telefone (somente números e 10 a 11 dígitos)
function validatePhone(phone) {
    const phonePattern = /^\d{10,11}$/;
    return phonePattern.test(phone);
}

function editCustomer(id, name, email, phone) {
    console.log("Edit button clicked:", id, name, email, phone); // Debugging

    document.getElementById("customer_id").value = id;
    document.getElementById("name").value = name;
    document.getElementById("email").value = email;
    document.getElementById("phone").value = phone;

    // Alterar o botão de submit
    const submitButton = document.getElementById("submitButton");
    submitButton.textContent = "Atualizar Cliente";

    // Alterar a ação do formulário para atualização
    const form = document.getElementById("customerForm");
    form.action = `/customers/update/${id}`;
    form.method = "POST";
}
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("customerForm");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const formData = new FormData(form);

        try {
            const response = await fetch("/customers/add", {
                method: "POST",
                body: formData
            });

            const result = await response.json();

            if (!response.ok) {
                alert(result.error); // Exibe erro na tela se email for duplicado
            } else {
                alert(result.success);
                location.reload(); // Atualiza a página para mostrar o novo cliente
            }
        } catch (error) {
            console.error("Erro ao adicionar cliente:", error);
            alert("Erro ao processar o cadastro.");
        }
    });
});