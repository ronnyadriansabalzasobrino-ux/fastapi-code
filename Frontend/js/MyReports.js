const API = "https://alertas-backend.onrender.com"

const id_user =
localStorage.getItem("id_user")

let reportsData = []

let filteredData = []

let table = null

/* =========================
   LOAD REPORTS
========================= */

async function loadReports(){

try{

const response = await fetch(
API + "/reports/student/" + id_user
)

const data = await response.json()

reportsData = data
filteredData = data

renderPrograms(data)

renderTable(data)

}catch(error){

console.error(error)

}

}

/* =========================
   PROGRAM FILTER
========================= */

function renderPrograms(data){

const select =
document.getElementById("programFilter")

select.innerHTML = `
<option value="">
Todos los programas
</option>
`

const programs =
[...new Set(data.map(x => x.program))]

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

function applyFilters(){

const risk =
document.getElementById("riskFilter").value

const state =
document.getElementById("stateFilter").value

const program =
document.getElementById("programFilter").value

filteredData = reportsData.filter(item => {

return (

(!risk || item.risk_level === risk) &&

(!state || item.state === state) &&

(!program || item.program === program)

)

})

renderTable(filteredData)

}

/* =========================
   INIT
========================= */

window.addEventListener(
"DOMContentLoaded",
loadReports
)