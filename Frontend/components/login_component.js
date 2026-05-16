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

      <button class="rolBtn" data-rol="admin">
        Admin
      </button>

      <button class="rolBtn" data-rol="docente">
        Docente
      </button>

      <button class="rolBtn" data-rol="estudiante">
        Estudiante
      </button>

    </div>

    <button id="loginBtn">
      Iniciar sesión
    </button>

    <p>
      ¿No tienes cuenta?
      <a href="register.html">
        Regístrate aquí
      </a>
    </p>

  </div>

  <!-- MODAL -->
  <div id="modal" class="modal">

    <div class="modal-content">

      <h2 id="modalTitle"></h2>

      <p id="modalMessage"></p>

      <button id="modalClose">
        Cerrar
      </button>

    </div>

  </div>

</div>
`;

let selectedRol = null;

/* =========================
   MODAL
========================= */

function showModal(title, message){

const modal =
document.getElementById("modal");

document.getElementById("modalTitle")
.innerText = title;

document.getElementById("modalMessage")
.innerText = message;

modal.style.display = "flex";

}

function closeModal(){

document.getElementById("modal")
.style.display = "none";

}

setTimeout(() => {

document
.getElementById("modalClose")
.addEventListener("click", closeModal);

}, 100);

/* =========================
   SELECT ROL
========================= */

this.querySelectorAll(".rolBtn")
.forEach(btn => {

btn.addEventListener("click", () => {

selectedRol = btn.dataset.rol;

this.querySelectorAll(".rolBtn")
.forEach(b => b.style.background = "");

btn.style.background = "#4CAF50";

});

});

/* =========================
   LOGIN
========================= */

this.querySelector("#loginBtn")
.addEventListener("click", async () => {

const mail =
this.querySelector("#mail")
.value.trim();

const password =
this.querySelector("#password")
.value.trim();

if (!mail || !password) {

showModal(
"Error",
"Ingresa correo y contraseña"
);

return;

}

if (!selectedRol) {

showModal(
"Error",
"Selecciona un rol"
);

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

body: JSON.stringify({
mail,
password
})

}
);

if (!res.ok) {

showModal(
"Error",
"Correo o contraseña incorrectos"
);

return;

}

const data = await res.json();

/* =========================
   STORAGE
========================= */

localStorage.setItem(
"access_token",
data.access_token
);

localStorage.setItem(
"rol",
selectedRol
);

localStorage.setItem(
"name",
data.name
);

localStorage.setItem(
"mail",
mail
);

console.log("LOGIN OK:", {

mail: localStorage.getItem("mail"),

rol: localStorage.getItem("rol")

});

/* =========================
   SUCCESS
========================= */

showModal(
"Éxito",
"Has iniciado sesión correctamente"
);

setTimeout(() => {

window.location.href =
"dashboard.html";

}, 1500);

}

catch (err) {

console.error(err);

showModal(
"Error",
"Error conectando con el servidor"
);

}

});

}

}

customElements.define(
"app-login",
LoginComponent
);