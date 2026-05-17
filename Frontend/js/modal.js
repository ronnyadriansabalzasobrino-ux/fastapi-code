/* =========================
   OPEN MODAL
========================= */

function openModal(title, message){

document.getElementById("modalTitle")
.innerText = title;

document.getElementById("modalMessage")
.innerText = message;

document.getElementById("modal")
.style.display = "flex";

}

/* =========================
   CLOSE MODAL
========================= */

function closeModal(){

document.getElementById("modal")
.style.display = "none";

}

/* =========================
   SUCCESS MODAL
========================= */

function successModal(message){

openModal(
"Éxito",
message
);

document.getElementById("modalActions")
.innerHTML = `
<button onclick="closeModal()">
Cerrar
</button>
`;

}

/* =========================
   CONFIRM MODAL
========================= */

function confirmModal(message, callback){

openModal(
"Confirmación",
message
);

document.getElementById("modalActions")
.innerHTML = `

<button id="confirmYes">
Sí
</button>

<button id="confirmNo">
No
</button>

`;

document
.getElementById("confirmYes")
.onclick = () => {

callback();

closeModal();

};

document
.getElementById("confirmNo")
.onclick = closeModal;

}