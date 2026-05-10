const API = "https://alertas-backend.onrender.com"

let reportsData = []
let table = null

/* =========================
   LOAD REPORTS
========================= */
async function loadReports(){

try{

const response = await fetch(API + "/reports/data")
const data = await response.json()

reportsData = data

renderCards(data)
renderPrograms(data)
renderTable(data)

}catch(error){
console.error(error)
}

}

/* =========================
   CARDS
========================= */
function renderCards(data){

document.getElementById("totalAlerts").innerText = data.length

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

const tbody = document.querySelector("#reportsTable tbody")

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

if(table) table.destroy()

table = $("#reportsTable").DataTable()

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
document.getElementById("searchStudent").value.toLowerCase()

let filtered = reportsData.filter(item => {

return (
(!risk || item.risk_level === risk) &&
(!state || item.state === state) &&
(!program || item.program === program) &&
(
item.student.toLowerCase().includes(search)
)
)

})

renderCards(filtered)
renderTable(filtered)

}

/* =========================
   PDF
========================= */
async function generatePDF(){

const { jsPDF } = window.jspdf

const doc = new jsPDF("landscape")

doc.setFillColor(25,118,210)
doc.rect(0,0,300,25,"F")

doc.setTextColor(255,255,255)
doc.setFontSize(18)

doc.text(
"SISTEMA DE ALERTAS ACADÉMICAS S.A.P.E.R",
105,
15
)

doc.setTextColor(0,0,0)

doc.setFontSize(11)

doc.text(
"Reporte de estudiantes en riesgo",
14,
35
)

const rows = []

document.querySelectorAll("#reportsTable tbody tr")
.forEach(tr => {

const cols = tr.querySelectorAll("td")

rows.push([
cols[0].innerText,
cols[1].innerText,
cols[2].innerText,
cols[3].innerText,
cols[4].innerText,
cols[5].innerText,
cols[6].innerText
])

})

doc.autoTable({

startY:45,

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

doc.save("Reporte_SAPER.pdf")

}

window.addEventListener("DOMContentLoaded",loadReports)