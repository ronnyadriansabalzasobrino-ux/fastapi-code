const API = "https://alertas-backend.onrender.com"

let tableInstance = null

async function loadTeachers(){

try{

const response = await fetch(API + "/get_Teacher/")
const teachers = await response.json()

const table = document.querySelector("#teachersTableDisplay tbody")
if(!table) return

table.innerHTML = ""

if (tableInstance) tableInstance.destroy()

if (!Array.isArray(teachers))return

teachers.forEach(teacher => {

table.innerHTML += `
<tr>
<td>${teacher.name}</td>
<td>${teacher.last_name}</td>
<td>${teacher.mail}</td>
<td>${teacher.phone}</td>
<td>${teacher.specialty}</td>
<td>

<button class="btn-edit"
onclick="editTeacher(
${teacher.id_teaching},
'${teacher.name}',
'${teacher.last_name}',
'${teacher.number_id}',
'${teacher.mail}',
'${teacher.phone}',
'${teacher.specialty}'
)">
Editar
</button>

<button class="btn-delete"
onclick="deleteTeacher(${teacher.id_teaching})">
Eliminar
</button>

</td>
</tr>
`
})

tableInstance = $('#teachersTableDisplay').DataTable()

}catch(error){
console.error("Error cargando docentes:", error)
}
}

async function saveTeacher(){

const id = document.getElementById("teacher_id").value

const teacher = {
name: document.getElementById("name").value,
last_name: document.getElementById("last_name").value,
number_id: document.getElementById("number_id").value,
mail: document.getElementById("mail").value,
phone: document.getElementById("phone").value,
specialty: document.getElementById("specialty").value
}

const url = id === ""
? API + "/create_Teacher"
: API + "/update_Teacher/" + id

const method = id === "" ? "POST" : "PUT"

await fetch(url,{
method,
headers:{"Content-Type":"application/json"},
body: JSON.stringify(teacher)
})

showModal(
"Correcto",
id === "" 
? "Docente creado correctamente"
: "Docente actualizado correctamente"
)

clearForm()
loadTeachers()
}

function editTeacher(id,name,last_name,number,mail,phone,specialty){

document.getElementById("teacher_id").value = id
document.getElementById("name").value = name
document.getElementById("last_name").value = last_name
document.getElementById("number_id").value = number
document.getElementById("mail").value = mail
document.getElementById("phone").value = phone
document.getElementById("specialty").value = specialty

window.scrollTo(0,0)
}

async function deleteTeacher(id){

showConfirmModal(
"¿Eliminar docente?",
"Estás seguro de que deseas eliminar este docente?",
async () => {

await fetch(API + "/delete_Teacher/" + id,{
method:"DELETE"
})

showModal(
"Eliminado",
"Docente eliminado correctamente"
)

loadTeachers()

}
)

}

function clearForm(){

document.getElementById("teacher_id").value=""
document.getElementById("name").value=""
document.getElementById("last_name").value=""
document.getElementById("number_id").value=""
document.getElementById("mail").value=""
document.getElementById("phone").value=""
document.getElementById("specialty").value=""
}

window.addEventListener("DOMContentLoaded", loadTeachers)

window.saveTeacher = saveTeacher
window.clearForm = clearForm
window.editTeacher = editTeacher
window.deleteTeacher = deleteTeacher