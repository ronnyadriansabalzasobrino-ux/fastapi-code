const API = "https://alertas-backend.onrender.com"

/* =========================
   CARGAR ESTUDIANTES
========================= */
async function loadStudents(){

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
<button onclick="editStudent(
${student.id_student},
'${student.name}',
'${student.last_name}',
'${student.number_id}',
'${student.mail}',
'${student.phone}'
)">Editar</button>

<button onclick="deleteStudent(${student.id_student})">Eliminar</button>
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

/* =========================
   CARGAR PROGRAMAS
========================= */
async function loadPrograms(){
const res = await fetch(API + "/programs")
const data = await res.json()

const select = document.getElementById("program_id")
select.innerHTML = `<option value="">Seleccionar programa</option>`

data.forEach(p => {
select.innerHTML += `<option value="${p.id_program}">${p.name}</option>`
})
}

/* =========================
   CARGAR SEMESTRES
========================= */
async function loadSemesters(){
const res = await fetch(API + "/semesters")
const data = await res.json()

const select = document.getElementById("semester_id")
select.innerHTML = `<option value="">Seleccionar semestre</option>`

data.forEach(s => {
select.innerHTML += `<option value="${s.id_semester}">${s.name}</option>`
})
}

/* =========================
   GUARDAR ESTUDIANTE
========================= */
async function saveStudent() {
try {

const get = (id) => {
const el = document.getElementById(id)
if (!el) {
throw new Error(`No existe el elemento #${id}`)
}
return el.value
}

const id = get("student_id")

const programValue = document.getElementById("program_id")?.value
const semesterValue = document.getElementById("semester_id")?.value

const student = {
name: get("name"),
last_name: get("last_name"),
number_id: get("number_id"),
mail: get("mail"),
phone: get("phone"),
id_program: parseInt(programValue),
id_semester: parseInt(semesterValue)
}

// validación segura
if (
!student.name ||
!student.last_name ||
!student.number_id ||
!student.mail ||
!student.phone ||
isNaN(student.id_program) ||
isNaN(student.id_semester)
) {
alert("Completa todos los campos")
return
}

if (id === "") {
await fetch(API + "/students", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(student)
})
alert("Estudiante creado")
} else {
await fetch(API + "/students/" + id, {
method: "PUT",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(student)
})
alert("Estudiante actualizado")
}

clearForm()
loadStudents()

} catch (error) {
console.error("Error guardando estudiante:", error)
}
}

/* =========================
   EDITAR
========================= */
function editStudent(id,name,last_name,number_id,mail,phone){

document.getElementById("student_id").value = id
document.getElementById("name").value = name
document.getElementById("last_name").value = last_name
document.getElementById("number_id").value = number_id
document.getElementById("mail").value = mail
document.getElementById("phone").value = phone

window.scrollTo(0,0)
}

/* =========================
   ELIMINAR
========================= */
async function deleteStudent(id){

if(!confirm("¿Eliminar estudiante?")) return

await fetch(API + "/students/" + id,{ method:"DELETE" })
alert("Estudiante eliminado")
loadStudents()
}

/* =========================
   LIMPIAR
========================= */
function clearForm(){
document.getElementById("student_id").value = ""
document.getElementById("name").value = ""
document.getElementById("last_name").value = ""
document.getElementById("number_id").value = ""
document.getElementById("mail").value = ""
document.getElementById("phone").value = ""
document.getElementById("program_id").value = ""
document.getElementById("semester_id").value = ""
}

/* =========================
   PDF
========================= */
function generatePDFStudents(){

const original = document.querySelector("#studentsTableDisplay")
const clone = original.cloneNode(true)

clone.querySelectorAll("td:last-child, th:last-child")
.forEach(el => el.remove())

const container = document.createElement("div")

const titulo = document.createElement("h2")
titulo.innerText = "Reporte de Estudiantes"
titulo.style.textAlign = "center"

container.appendChild(titulo)
container.appendChild(clone)

html2pdf().from(container).save("reporte_estudiantes.pdf")
}

/* =========================
   INIT
========================= */
document.addEventListener("DOMContentLoaded", () => {
setTimeout(loadStudents, 300)
loadPrograms()
loadSemesters()
})