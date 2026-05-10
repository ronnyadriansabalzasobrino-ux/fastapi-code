class Sidebar extends HTMLElement {

connectedCallback(){

this.innerHTML = `

<aside class="sidebar">

  <div class="sidebar-logo">
    <h2>🎓 School System</h2>
  </div>

  <ul class="sidebar-menu">

    <li onclick="goDashboard()">
      🏠 Inicio
    </li>

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

  </ul>

</aside>

`;

}

}

customElements.define("app-sidebar", Sidebar);


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