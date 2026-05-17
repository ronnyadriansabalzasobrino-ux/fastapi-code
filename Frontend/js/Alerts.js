const API = "https://alertas-backend.onrender.com";

let alertsData = []
let editingId = null
let tableInstance = null

/* =========================
   MODAL FUNCTIONS
========================= */

function showModal(title, message, callback = null){

const modal = document.getElementById("modal")
const modalTitle = document.getElementById("modalTitle")
const modalMessage = document.getElementById("modalMessage")
const modalButtons = document.getElementById("modalButtons")

modalTitle.innerText = title
modalMessage.innerText = message

modalButtons.innerHTML = ""

const okBtn = document.createElement("button")
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

function showConfirmModal(title, message, onYes){

const modal = document.getElementById("modal")
const modalTitle = document.getElementById("modalTitle")
const modalMessage = document.getElementById("modalMessage")
const modalButtons = document.getElementById("modalButtons")

modalTitle.innerText = title
modalMessage.innerText = message

modalButtons.innerHTML = ""

const yesBtn = document.createElement("button")
yesBtn.innerText = "Sí"

const noBtn = document.createElement("button")
noBtn.innerText = "No"

yesBtn.onclick = () => {
modal.style.display = "none"
onYes()
}

noBtn.onclick = () => {
modal.style.display = "none"
}

modalButtons.appendChild(yesBtn)
modalButtons.appendChild(noBtn)

modal.style.display = "flex"
}

/* =========================
   LOAD ALERTS
========================= */

async function loadAlerts(){

try{

const token = localStorage.getItem("access_token")

const response = await fetch(API + "/get_Alerts/", {
headers: {
"Authorization": `Bearer ${token}`
}
})

const alerts = await response.json()

if (!Array.isArray(alerts)) {
console.error("Error en alerts:", alerts)
return
}

alertsData = alerts

const table = document.querySelector("#alertsTableDisplay tbody")

if(!table) return

table.innerHTML = ""

if (tableInstance){
tableInstance.destroy()
}

alerts.forEach(alert => {

table.innerHTML += `
<tr>
<td>${alert.id_student}</td>
<td>${alert.tipo_alert}</td>
<td>${alert.description}</td>
<td>${alert.risk_level ?? "Sin riesgo"}</td>
<td>${alert.state ?? "Sin estado"}</td>

<td>

<button class="btn-edit"
onclick="editAlert(${alert.id_alert})">
Editar
</button>

<button class="btn-delete"
onclick="deleteAlert(${alert.id_alert})">
Eliminar
</button>

</td>

</tr>
`
})

tableInstance = $('#alertsTableDisplay').DataTable()

}catch(error){

console.error(error)

showModal(
"Error",
"Error cargando alertas"
)

}
}

/* =========================
   SAVE ALERT
========================= */

async function saveAlert(){

try{

const token = localStorage.getItem("access_token")

const alert = {

id_student: parseInt(
document.getElementById("id_student").value
),

tipo_alert:
document.getElementById("tipo_alert").value,

description:
document.getElementById("description").value,

generation_date:
document.getElementById("generation_date").value,

risk_level:
document.getElementById("risk_level").value,

state:
document.getElementById("state").value,

id_period: parseInt(
document.getElementById("id_period").value
)

}

const url = editingId === null
? API + "/create_Alerts"
: API + "/update_Alerts/" + editingId

const method = editingId === null
? "POST"
: "PUT"

await fetch(url, {

method,

headers: {
"Content-Type":"application/json",
"Authorization": `Bearer ${token}`
},

body: JSON.stringify(alert)

})

showModal(
"Correcto",
editingId === null
? "Alerta creada correctamente"
: "Alerta actualizada correctamente"
)

editingId = null

clearForm()

loadAlerts()

}catch(error){

console.error(error)

showModal(
"Error",
"Error guardando alerta"
)

}
}

/* =========================
   EDIT ALERT
========================= */

function editAlert(id){

const alert = alertsData.find(
a => a.id_alert === id
)

editingId = id

document.getElementById("id_student").value =
alert.id_student

document.getElementById("tipo_alert").value =
alert.tipo_alert

document.getElementById("description").value =
alert.description

document.getElementById("generation_date").value =
alert.generation_date

document.getElementById("risk_level").value =
alert.risk_level

document.getElementById("state").value =
alert.state

document.getElementById("id_period").value =
alert.id_period

window.scrollTo(0,0)

showModal(
"Modo edición",
"Ahora puedes editar la alerta"
)

}

/* =========================
   DELETE ALERT
========================= */

async function deleteAlert(id){

showConfirmModal(
"Eliminar alerta",
"¿Estás seguro de eliminar esta alerta?",

async () => {

try{

const token = localStorage.getItem("access_token")

await fetch(API + "/delete_Alerts/" + id, {

method:"DELETE",

headers:{
"Authorization": `Bearer ${token}`
}

})

showModal(
"Eliminado",
"Alerta eliminada correctamente"
)

loadAlerts()

}catch(error){

console.error(error)

showModal(
"Error",
"No se pudo eliminar la alerta"
)

}

})

}

/* =========================
   CLEAR FORM
========================= */

function clearForm(){

editingId = null

document.getElementById("id_student").value=""
document.getElementById("tipo_alert").value=""
document.getElementById("description").value=""
document.getElementById("generation_date").value=""
document.getElementById("risk_level").value=""
document.getElementById("state").value=""
document.getElementById("id_period").value=""

}

/* =========================
   INIT
========================= */

window.addEventListener(
"DOMContentLoaded",
loadAlerts
)

/* =========================
   EXPORTS
========================= */

window.editAlert = editAlert
window.deleteAlert = deleteAlert
window.saveAlert = saveAlert
window.clearForm = clearForm