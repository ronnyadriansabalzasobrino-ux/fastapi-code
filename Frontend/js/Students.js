const API = "https://alertas-backend.onrender.com"


async function loadstudents(){

try{

const response = await fetch(API + "/students")
const students = await response.json()

const tableBody = document.querySelector("#studentsTableDisplay tbody")

if(!tableBody){
  console.error("No existe studentsTableDisplay")
  return
}

tableBody.innerHTML = ""

if (!Array.isArray(students)) {
  console.error("Error en students:", students)
  return
}

students.forEach(student => {

tableBody.innerHTML += `
<tr>
<td>${student.name ?? ""}</td>
<td>${student.last_name ?? ""}</td>
<td>${student.mail ?? ""}</td>
<td>${student.phone ?? ""}</td>
<td>
<button class="btn-edit" onclick="editstudent(
${student.id_student},
'${student.name ?? ""}',
'${student.last_name ?? ""}',
'${student.number_id ?? ""}',
'${student.mail ?? ""}',
'${student.phone ?? ""}',
'${student.id_program ?? ""}',
'${student.id_semester ?? ""}'
)">Editar</button>

<button class="btn-delete" onclick="deletestudent(${student.id_student})">
Eliminar
</button>
</td>
</tr>
`
})

if ($.fn.DataTable.isDataTable('#studentsTableDisplay')) {
  $('#studentsTableDisplay').DataTable().clear().destroy();
}

$('#studentsTableDisplay').DataTable();

}catch(error){
console.error("Error cargando estudiantes:", error)
}
}

async function loadPrograms(){

try{

const res = await fetch(API + "/programs")
const programs = await res.json()

const select = document.getElementById("id_program")

if(!select) return

select.innerHTML = `<option value="">Seleccione programa</option>`

programs.forEach(p => {
select.innerHTML += `
<option value="${p.id_program}">
${p.name}
</option>
`
})

}catch(error){
console.error("Error programas:", error)
}
}


async function loadSemesters(){

try{

const res = await fetch(API + "/semesters")
const semesters = await res.json()

const select = document.getElementById("id_semester")

if(!select) return

select.innerHTML = `<option value="">Seleccione semestre</option>`

semesters.forEach(s => {
select.innerHTML += `
<option value="${s.id_semester}">
${s.name}
</option>
`
})

}catch(error){
console.error("Error semestres:", error)
}
}


async function savestudent(){

try{

const id = document.getElementById("student_id").value

const program = document.getElementById("program_id")?.value
const semester = document.getElementById("semester_id")?.value

if(!program || !semester){
showModal(
  "error",
  "Selecciona programa y semestre"
)
return
}

const student = {
name: document.getElementById("name").value,
last_name: document.getElementById("last_name").value,
number_id: document.getElementById("number_id").value,
mail: document.getElementById("mail").value,
phone: document.getElementById("phone").value,

id_program: parseInt(program),
id_semester: parseInt(semester)
}

if(id === ""){
await fetch(API + "/students",{
method:"POST",
headers:{ "Content-Type":"application/json" },
body: JSON.stringify(student)
})
showModal(
  "exito",
  "Estudiante creado correctamente")
}else{
await fetch(API + "/students/" + id,{
method:"PUT",
headers:{ "Content-Type":"application/json" },
body: JSON.stringify(student)
})
showModal(
  "exito",
  "Estudiante actualizado correctamente")
}

clearForm()
loadstudents()

}catch(error){
console.error("Error guardando estudiante:", error)
showModal(
  "error",
  "no se pudo guardar el estudiante"
)
}
}


function editstudent(
id,
name,
last_name,
number,
mail,
phone,
program,
semester
){

document.getElementById("student_id").value = id
document.getElementById("name").value = name
document.getElementById("last_name").value = last_name
document.getElementById("number_id").value = number
document.getElementById("mail").value = mail
document.getElementById("phone").value = phone

document.getElementById("program_id").value = program
document.getElementById("semester_id").value = semester

window.scrollTo(0,0)
}



async function deletestudent(id){
confirmModal(
  "¿estas seguro de eliminar este estudiante?",
  async () => {
await fetch(API + "/students/" + id,{ method:"DELETE" })

showModal(
  "elimindo",
  "Estudiante eliminado correctamente"
)

loadstudents()
  }
)
}


function clearForm(){
document.getElementById("student_id").value = ""
document.getElementById("name").value = ""
document.getElementById("last_name").value = ""
document.getElementById("number_id").value = ""
document.getElementById("mail").value = ""
document.getElementById("phone").value = ""

const p = document.getElementById("program_id")
const s = document.getElementById("semester_id")

if(p) p.value = ""
if(s) s.value = ""
}


document.addEventListener("DOMContentLoaded", () => {
setTimeout(loadstudents, 300)
})