const API = "https://alertas-backend.onrender.com"

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

// 🔥 VALIDACIÓN CLAVE
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
<button class="btn-edit" onclick="editStudent(
${student.id_student},
'${student.name ?? ""}',
'${student.last_name ?? ""}',
'${student.number_id ?? ""}',
'${student.mail ?? ""}',
'${student.phone ?? ""}'
)">Editar</button>

<button class="btn-delete" onclick="deleteStudent(${student.id_student})">
Eliminar
</button>
</td>
</tr>
`
})

// 🔥 FIX DATATABLE
if ($.fn.DataTable.isDataTable('#studentsTableDisplay')) {
  $('#studentsTableDisplay').DataTable().clear().destroy();
}

$('#studentsTableDisplay').DataTable();

}catch(error){
console.error("Error cargando estudiantes:", error)
}
}

async function saveStudent(){

try{

const id = document.getElementById("student_id").value

const student = {
name: document.getElementById("name").value,
last_name: document.getElementById("last_name").value,
number_id: document.getElementById("number_id").value,
mail: document.getElementById("mail").value,
phone: document.getElementById("phone").value,
id_program:38,
id_semester:37
}

if(id === ""){
await fetch(API + "/students",{
method:"POST",
headers:{ "Content-Type":"application/json" },
body: JSON.stringify(student)
})
alert("Estudiante creado")
}else{
await fetch(API + "/students/" + id,{
method:"PUT",
headers:{ "Content-Type":"application/json" },
body: JSON.stringify(student)
})
alert("Estudiante actualizado")
}

clearForm()
loadStudents()

}catch(error){
console.error("Error guardando estudiante:", error)
}
}

function editStudent(id,name,last_name,number_id,mail,phone){
document.getElementById("student_id").value = id
document.getElementById("name").value = name
document.getElementById("last_name").value = last_name
document.getElementById("number_id").value = number_id
document.getElementById("mail").value = mail
document.getElementById("phone").value = phone
window.scrollTo(0,0)
}

async function deleteStudent(id){
if(!confirm("¿Eliminar estudiante?")) return

await fetch(API + "/students/" + id,{ method:"DELETE" })
alert("Estudiante eliminado")
loadStudents()
}

function clearForm(){
document.getElementById("student_id").value = ""
document.getElementById("name").value = ""
document.getElementById("last_name").value = ""
document.getElementById("number_id").value = ""
document.getElementById("mail").value = ""
document.getElementById("phone").value = ""
}

// 🔥 REPORTE PDF
function generatePDFStudents(){

const element = document.querySelector(".table-card")

const opt = {
  margin: 0.5,
  filename: 'reporte_estudiantes.pdf',
  image: { type: 'jpeg', quality: 0.98 },
  html2canvas: { scale: 2 },
  jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
};

const titulo = document.createElement("h2")
titulo.innerText = "Reporte de Estudiantes"
titulo.style.textAlign = "center"

element.prepend(titulo)

html2pdf().set(opt).from(element).save().then(() => {
  titulo.remove()
})

}


document.addEventListener("DOMContentLoaded", () => {
setTimeout(loadStudents, 300)
})