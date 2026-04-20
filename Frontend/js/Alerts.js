const API = "https://alertas-backend.onrender.com";

let alertsData = []
let editingId = null
let tableInstance = null

async function loadAlerts(){

try{

const token = localStorage.getItem("access_token")
console.log("TOKEN:", token)

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

const table = document.getElementById("alertsTable")

if(!table){
  console.error("No existe alertsTable")
  return
}

table.innerHTML = ""

if (tableInstance) {
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
<button onclick="editAlert(${alert.id_alert})">Editar</button>
<button onclick="deleteAlert(${alert.id_alert})">Eliminar</button>
</td>
</tr>
`
})

tableInstance = $('#alertsTableDisplay').DataTable()

}catch(error){
console.error("Error cargando alertas:", error)
}
}

async function saveAlert(){

const token = localStorage.getItem("access_token")

const alert = {
id_student: document.getElementById("id_student").value,
tipo_alert: document.getElementById("tipo_alert").value,
description: document.getElementById("description").value,
generation_date: document.getElementById("generation_date").value,
risk_level: document.getElementById("risk_level").value,
state: document.getElementById("state").value,
id_period: document.getElementById("id_period").value
}

if(editingId){

await fetch(API + "/update_Alerts/" + editingId,{
method:"PUT",
headers:{
"Content-Type":"application/json",
"Authorization": `Bearer ${token}`
},
body: JSON.stringify(alert)
})

editingId = null

}else{

await fetch(API + "/create_Alerts",{
method:"POST",
headers:{
"Content-Type":"application/json",
"Authorization": `Bearer ${token}`
},
body: JSON.stringify(alert)
})

}

clearForm()
await loadAlerts()
}

function editAlert(id){

const alert = alertsData.find(a => a.id_alert === id)

editingId = id

document.getElementById("id_student").value = alert.id_student
document.getElementById("tipo_alert").value = alert.tipo_alert
document.getElementById("description").value = alert.description
document.getElementById("generation_date").value = alert.generation_date
document.getElementById("risk_level").value = alert.risk_level
document.getElementById("state").value = alert.state
document.getElementById("id_period").value = alert.id_period

}

async function deleteAlert(id){

if(!confirm("¿Eliminar alerta?")) return

const token = localStorage.getItem("access_token")

await fetch(API + "/delete_Alerts/" + id,{
method:"DELETE",
headers:{
"Authorization": `Bearer ${token}`
}
})

loadAlerts()
}

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

// PDF
async function generatePDFAlerts(){

await loadAlerts()

setTimeout(() => {

const element = document.querySelector(".table-card")

const acciones = element.querySelectorAll("td:last-child, th:last-child")
acciones.forEach(el => el.style.display = "none")

const opt = {
  margin: 0.5,
  filename: 'reporte_alertas.pdf',
  image: { type: 'jpeg', quality: 0.98 },
  html2canvas: { scale: 2 },
  jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
};

const titulo = document.createElement("h2")
titulo.innerText = "Reporte de Alertas"
titulo.style.textAlign = "center"

element.prepend(titulo)

html2pdf().set(opt).from(element).save().then(() => {
  titulo.remove()
  acciones.forEach(el => el.style.display = "")
})

}, 600)

}

// FIX window.onload
window.addEventListener("load", () => {
  loadAlerts()
})

window.editAlert = editAlert
window.deleteAlert = deleteAlert
window.saveAlert = saveAlert
window.clearForm = clearForm