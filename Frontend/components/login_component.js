class LoginComponent extends HTMLElement {

connectedCallback() {

this.innerHTML = `
<div class="login-container">

  <div class="login-card">

    <h1>📌 Sistema de Alertas</h1>

    <input id="mail" type="email" placeholder="Correo electrónico">
    <input id="password" type="password" placeholder="Contraseña">

    <div class="roles">
      <button class="rolBtn" data-rol="admin">Admin</button>
      <button class="rolBtn" data-rol="docente">Docente</button>
      <button class="rolBtn" data-rol="estudiante">Estudiante</button>
    </div>

    <button id="loginBtn">Iniciar sesión</button>

  </div>

</div>
`;

let selectedRol = null;

this.querySelectorAll(".rolBtn").forEach(btn => {
  btn.addEventListener("click", () => {
    selectedRol = btn.dataset.rol;

    this.querySelectorAll(".rolBtn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
  });
});

this.querySelector("#loginBtn").addEventListener("click", async () => {

  if (!selectedRol) return alert("Selecciona un rol");

  const mail = document.getElementById("mail").value;
  const password = document.getElementById("password").value;

  const res = await fetch("https://alertas-backend.onrender.com/login", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({mail, password})
  });

  if(!res.ok) return alert("Error login");

  const data = await res.json();

  localStorage.setItem("rol", selectedRol);
  localStorage.setItem("access_token", data.access_token);
  localStorage.setItem("name", data.name);

  window.location.href = "dashboard.html";
});

}

}

customElements.define("app-login", LoginComponent);