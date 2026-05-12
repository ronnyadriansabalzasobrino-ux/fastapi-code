class LoginComponent extends HTMLElement {

connectedCallback() {

this.innerHTML = `
<div class="login-container">

  <div class="login-card">

    <h1>📌 Sistema de Alertas</h1>

    <input id="mail" type="email" placeholder="Correo electrónico">
    <input id="password" type="password" placeholder="Contraseña">

    <label>Selecciona tu rol</label>

    <div style="display:flex; gap:10px; margin-bottom:10px;">
      <button class="rolBtn" data-rol="admin">Admin</button>
      <button class="rolBtn" data-rol="docente">Docente</button>
      <button class="rolBtn" data-rol="estudiante">Estudiante</button>
    </div>

    <button id="loginBtn">Iniciar sesión</button>

  </div>

</div>
`;

let selectedRol = null;

// seleccionar rol
this.querySelectorAll(".rolBtn").forEach(btn => {
  btn.addEventListener("click", () => {

    selectedRol = btn.dataset.rol;

    this.querySelectorAll(".rolBtn")
      .forEach(b => b.style.background = "");

    btn.style.background = "#4CAF50";
  });
});

// login
this.querySelector("#loginBtn").addEventListener("click", async () => {

  const mail = this.querySelector("#mail").value.trim();
  const password = this.querySelector("#password").value.trim();

  if (!mail || !password) {
    alert("Ingresa correo y contraseña");
    return;
  }

  if (!selectedRol) {
    alert("Selecciona un rol");
    return;
  }

  try {

    const res = await fetch(
      "https://alertas-backend.onrender.com/login",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ mail, password })
      }
    );

    if (!res.ok) {
      alert("Error en login");
      return;
    }

    const data = await res.json();

    // 🔥 STORAGE LIMPIO
    localStorage.setItem("access_token", data.access_token);
    localStorage.setItem("rol", selectedRol);
    localStorage.setItem("name", data.name);
    sessionStorage.setItem("mail", mail);

    console.log("LOGIN OK:", {
      mail: sessionStorage.getItem("mail"),
      rol: localStorage.getItem("rol")
    });

    alert("Login correcto");

    window.location.href = "dashboard.html";

  } catch (err) {
    console.error(err);
    alert("Error conectando con el servidor");
  }

});

}

}

customElements.define("app-login", LoginComponent);