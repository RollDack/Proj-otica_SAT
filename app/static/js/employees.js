const employeeForm = document.getElementById("employeeForm");
if (employeeForm) {
  employeeForm.addEventListener("submit", function (event) {
    const name = document.getElementById("name").value.trim();
    const cpf = document.getElementById("cpf").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const birthdate = document.getElementById("birthdate").value.trim();
    const position = document.getElementById("position").value.trim();
    const salary = document.getElementById("salary").value.trim();
    const access_key = document.getElementById("access_key").value.trim();

    if (!name || !cpf || !email || !phone || !birthdate || !position || !salary || !access_key) {
      event.preventDefault();
      alert("Por favor, preencha todos os campos corretamente!");
    } else if (!validateEmail(email)) {
      event.preventDefault();
      alert("Por favor, insira um email válido!");
    } else if (!validateCPF(cpf)) {
      event.preventDefault();
      alert("Por favor, insira um CPF válido!");
    } else if (!validatePhone(phone)) {
      event.preventDefault();
      alert("Por favor, insira um telefone válido!");
    }
  });
}

function validateEmail(email) {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailPattern.test(email);
}

function validatePhone(phone) {
  const phonePattern = /^\d{10,11}$/;
  return phonePattern.test(phone);
}

function validateCPF(cpf) {
  const cpfPattern = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
  return cpfPattern.test(cpf);
}

function editEmployee(id, name, cpf, email, phone, birthdate, position, salary, access_key) {
  document.getElementById("edit-id").value = id;
  document.getElementById("edit-name").value = name;
  document.getElementById("edit-cpf").value = cpf;
  document.getElementById("edit-email").value = email;
  document.getElementById("edit-phone").value = phone;
  document.getElementById("edit-birthdate").value = birthdate;
  document.getElementById("edit-position").value = position;
  document.getElementById("edit-salary").value = salary;
  document.getElementById("edit-access-key").value = access_key;

  const form = document.getElementById("editEmployeeForm");
  form.action = `/employee/edit_employee/${id}`;
  form.method = "POST";
  document.getElementById("editEmployeeFormContainer").style.display = "block";
}
