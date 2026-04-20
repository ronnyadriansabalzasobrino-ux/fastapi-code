const API = "https://alertas-backend.onrender.com"

let tableInstance = null

async function loadSubjects(){
    try{

const response = await fetch(API + "/subjects")
const subjects = await response.json()

const table = document.getElementById("subjectsTable")
if(table) return

table.innerHTML = ""

if (tableInstance) tableInstance.destroy()

subjects.forEach(subject => {
table.innerHTML += `
<tr>
<td>${subject.name_subject}</td>
<td>${subject.credits}</td>
<td>${subject.id_program}</td>

<td>
<button onclick="editSubject(this, ${subject.id_subject})">Editar</button>
<button onclick="deleteSubject(${subject.id_subject})">Eliminar</button>
</td>
</tr>
`
})

tableInstance = $('#subjectsTableDisplay').DataTable()
}catch(error){
    console.error("Error materias:", error)
}
}
async function saveSubject(){
const id = document.getElementById("subject_id").value

const subject = {
name_subject: document.getElementById("name").value,
credits: document.getElementById("credits").value,
id_program: document.getElementById("teacher_id").value
}

const url = id === ""
? API + "/subjects"
: API + "/subjects/" + id

const method = id === "" ? "POST" : "PUT"

await fetch(url, {
method,
headers: {"Content-Type":"application/json"},
body: JSON.stringify(subject)
})

alert(id === "" ? "Materia creada" : "Materia actualizada")

clearForm()
loadSubjects()
}

function editSubject(btn, id){
const row = btn.closest("tr")

document.getElementById("subject_id").value = id
document.getElementById("name").value = row.children[0].innerText
document.getElementById("credits").value = row.children[1].innerText
document.getElementById("teacher_id").value = row.children[2].innerText
}

async function deleteSubject(id){
if(!confirm("¿Eliminar materia?")) return

await fetch(API + "/subjects/" + id,{ method:"DELETE" })
loadSubjects()
}

function clearForm(){
document.getElementById("subject_id").value=""
document.getElementById("name").value=""
document.getElementById("credits").value=""
document.getElementById("teacher_id").value=""
}

window.saveSubject = saveSubject
window.clearForm = clearForm
window.editSubject = editSubject
window.deleteSubject = deleteSubject

window.addEventListener("DOMContentLoaded", () => {
setTimeout(loadSubjects, 300)
})