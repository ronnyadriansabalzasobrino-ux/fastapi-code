const API = "https://alertas-backend.onrender.com"

let reportsData = []
let filteredData = []
let table = null

/* =========================
   LOAD REPORTS
========================= */
async function loadReports(){

try{

const response = await fetch(API + "/reports/data")
const data = await response.json()

reportsData = data
filteredData = data

renderPrograms(data)
renderCards(data)
renderTable(data)

}catch(error){
console.error(error)
}

}

/* =========================
   CARDS
========================= */
function renderCards(data){

document.getElementById("totalAlerts").innerText =
data.length

document.getElementById("highAlerts").innerText =
data.filter(x => x.risk_level === "high").length

document.getElementById("mediumAlerts").innerText =
data.filter(x => x.risk_level === "medium").length

document.getElementById("lowAlerts").innerText =
data.filter(x => x.risk_level === "low").length

}

/* =========================
   PROGRAM FILTER
========================= */
function renderPrograms(data){

const select = document.getElementById("programFilter")

select.innerHTML = `
<option value="">
Todos los programas
</option>
`

const programs = [...new Set(data.map(x => x.program))]

programs.forEach(program => {

select.innerHTML += `
<option value="${program}">
${program}
</option>
`

})

}

/* =========================
   TABLE
========================= */
function renderTable(data){

const tbody =
document.querySelector("#reportsTable tbody")

tbody.innerHTML = ""

data.forEach(item => {

tbody.innerHTML += `
<tr>
<td>${item.student}</td>
<td>${item.document}</td>
<td>${item.program}</td>
<td>${item.risk_level}</td>
<td>${item.state}</td>
<td>${item.tipo_alert}</td>
<td>${item.generation_date}</td>
</tr>
`

})

if(table){
table.destroy()
}

table = $("#reportsTable").DataTable({

pageLength:5,
responsive:true,
destroy:true

})

}

/* =========================
   FILTERS
========================= */

document.getElementById("riskFilter")
.addEventListener("change",applyFilters)

document.getElementById("stateFilter")
.addEventListener("change",applyFilters)

document.getElementById("programFilter")
.addEventListener("change",applyFilters)

document.getElementById("searchStudent")
.addEventListener("keyup",applyFilters)

function applyFilters(){

const risk =
document.getElementById("riskFilter").value

const state =
document.getElementById("stateFilter").value

const program =
document.getElementById("programFilter").value

const search =
document.getElementById("searchStudent")
.value
.toLowerCase()

filteredData = reportsData.filter(item => {

return (

(!risk || item.risk_level === risk) &&

(!state || item.state === state) &&

(!program || item.program === program) &&

(
item.student.toLowerCase().includes(search)
)

)

})

renderCards(filteredData)
renderTable(filteredData)

}

/* =========================
   PDF
========================= */
async function generatePDF(){

const { jsPDF } = window.jspdf

const doc = new jsPDF("landscape")

/* HEADER */

doc.setFillColor(25,118,210)

doc.rect(0,0,300,25,"F")

doc.setTextColor(255,255,255)

doc.setFontSize(18)

doc.text(
"SISTEMA DE ALERTAS ACADÉMICAS S.A.P.E.R",
75,
15
)

/* SUBTITLE */

doc.setTextColor(0,0,0)

doc.setFontSize(11)

doc.text(
"Reporte generado con filtros aplicados",
14,
35
)

/* FILTERS INFO */

const risk =
document.getElementById("riskFilter").value || "Todos"

const state =
document.getElementById("stateFilter").value || "Todos"

const program =
document.getElementById("programFilter").value || "Todos"

doc.text(`Riesgo: ${risk}`,14,43)
doc.text(`Estado: ${state}`,70,43)
doc.text(`Programa: ${program}`,130,43)

/* TABLE */

const rows = filteredData.map(item => [

item.student,
item.document,
item.program,
item.risk_level,
item.state,
item.tipo_alert,
item.generation_date

])

doc.autoTable({

startY:50,

head:[[
"Estudiante",
"Documento",
"Programa",
"Riesgo",
"Estado",
"Tipo",
"Fecha"
]],

body:rows,

theme:"grid",

headStyles:{
fillColor:[25,118,210]
},

alternateRowStyles:{
fillColor:[227,242,253]
}

})
const blob = doc.output("blob")

const reader = new FileReader()

reader.onloadend = async function(){

const base64 =
reader.result.split(",")[1]

await fetch(

API + "/reports/send",

{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

pdf:base64

})

}

)

}

reader.readAsDataURL(blob)

   doc.save("reporte_alertas.pdf")
showModal(
   "correcto",
   "PDF generado correctamente"
)





}

/* =========================
   INIT
========================= */

window.addEventListener(
"DOMContentLoaded",
loadReports
)