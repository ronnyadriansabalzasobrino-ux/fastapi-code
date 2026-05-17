class Topbar extends HTMLElement {

connectedCallback(){

this.innerHTML = `

<header class="topbar">

  <div class="topbar-left">
    <h1>📊 School System</h1>
  </div>

  <div class="topbar-right">

    <span class="user-info">
      👤 ${localStorage.getItem("name") ?? "Usuario"}
    </span>

    <button onclick="logout()" class="btn-logout">
      🚪 Salir
    </button>

  </div>

</header>

<!-- MODAL -->

<div id="modal" class="modal">

  <div class="modal-content">

    <h2 id="modalTitle"></h2>

    <p id="modalMessage"></p>

    <div id="modalButtons"></div>

  </div>

</div>

`;

}

}

customElements.define("app-topbar", Topbar);

/* =========================
   MODAL FUNCTIONS
========================= */

function showModal(title, message, callback = null){

const modal =
document.getElementById("modal")

const modalTitle =
document.getElementById("modalTitle")

const modalMessage =
document.getElementById("modalMessage")

const modalButtons =
document.getElementById("modalButtons")

modalTitle.innerText = title
modalMessage.innerText = message

modalButtons.innerHTML = ""

const okBtn =
document.createElement("button")

okBtn.innerText = "Aceptar"

okBtn.onclick = () => {

modal.style.display = "none"

if(callback){
callback()
}

}

modalButtons.appendChild(okBtn)

modal.style.display = "flex"

}

/* =========================
   CONFIRM MODAL
========================= */

function showConfirmModal(
title,
message,
onYes
){

const modal =
document.getElementById("modal")

const modalTitle =
document.getElementById("modalTitle")

const modalMessage =
document.getElementById("modalMessage")

const modalButtons =
document.getElementById("modalButtons")

modalTitle.innerText = title
modalMessage.innerText = message

modalButtons.innerHTML = ""

/* BOTON SI */

const yesBtn =
document.createElement("button")

yesBtn.innerText = "Sí"

yesBtn.onclick = () => {

modal.style.display = "none"

onYes()

}

/* BOTON NO */

const noBtn =
document.createElement("button")

noBtn.innerText = "No"

noBtn.onclick = () => {

modal.style.display = "none"

}

modalButtons.appendChild(yesBtn)
modalButtons.appendChild(noBtn)

modal.style.display = "flex"

}

/* =========================
   LOGOUT
========================= */

function logout(){

showConfirmModal(

"Cerrar sesión",

"¿Estás seguro de querer salir?",

() => {

localStorage.clear()

window.location.href =
"/login.html"

}

)

}