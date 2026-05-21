class Sidebar extends HTMLElement {

connectedCallback(){

const rol = localStorage.getItem("rol")

let menu = `

<li onclick="goDashboard()">
  🏠 Inicio
</li>

`

// ADMIN
if(rol === "admin"){

menu += `

<li onclick="goStudents()">
  👨‍🎓 Estudiantes
</li>

<li onclick="goTeachers()">
  👨‍🏫 Docentes
</li>

<li onclick="goSubjects()">
  📚 Materias
</li>

<li onclick="goAlerts()">
  ⚠️ Alertas
</li>

<li onclick="goReports()">
  📊 Reportes
</li>

`
}

// DOCENTE
else if(rol === "docente"){

menu += `

<li onclick="goStudents()">
  👨‍🎓 Estudiantes
</li>

<li onclick="goTeachers()">
  👨‍🏫 Docentes
</li>

<li onclick="goSubjects()">
  📚 Materias
</li>

<li onclick="goAlerts()">
  ⚠️ Alertas
</li>

`
}

// ESTUDIANTE
else if(rol === "estudiante"){

menu += `

<li onclick="goMyReports()">
  📊 Mis Reportes
</li>

`
}

this.innerHTML = `

<aside class="sidebar">

  <div class="sidebar-logo">
    <img src="assets/logo.png" alt="Escudo Universidad">
    <h2>🎓School System</h2>
  </div>

  <ul class="sidebar-menu">
    ${menu}
  </ul>

</aside>

`
}

}

customElements.define("app-sidebar", Sidebar)


/* =========================
   NAVEGACION
========================= */

function goDashboard(){
window.location.href = "dashboard.html"
}

function goStudents(){
window.location.href = "Students.html"
}

function goTeachers(){
window.location.href = "Teachers.html"
}

function goSubjects(){
window.location.href = "Subjects.html"
}

function goAlerts(){
window.location.href = "Alerts.html"
}

function goReports(){
window.location.href = "Reports.html"
}

function goMyReports(){
window.location.href = "MyReports.html"
} 