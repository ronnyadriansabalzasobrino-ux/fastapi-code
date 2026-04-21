class DashboardCards extends HTMLElement {

connectedCallback(){

const rol = localStorage.getItem("rol");

if (!rol) {
  window.location.href = "login.html";
  return;
}

let cards = [];

if (rol === "admin") {
  cards = [
    {text:"Estudiantes", action:"goStudents()", icon:"👨‍🎓"},
    {text:"Docentes", action:"goTeachers()", icon:"👨‍🏫"},
    {text:"Materias", action:"goSubjects()", icon:"📚"},
    {text:"Alertas", action:"goAlerts()", icon:"⚠️"},
    {text:"Reportes", action:"goReports()", icon:"📈"}
  ];
}

if (rol === "docente") {
  cards = [
    {text:"Estudiantes", action:"goStudents()", icon:"👨‍🎓"},
    {text:"Materias", action:"goSubjects()", icon:"📚"},
    {text:"Alertas", action:"goAlerts()", icon:"⚠️"}
  ];
}

if (rol === "estudiante") {
  cards = [
    {text:"Materias", action:"goSubjects()", icon:"📚"}
  ];
}

this.innerHTML = `
<section class="dashboard">

  ${cards.map(c => `
    <div class="card" onclick="${c.action}">
      <div class="card-icon">${c.icon}</div>
      <div class="card-text">${c.text}</div>
    </div>
  `).join("")}

</section>
`;

}

}

customElements.define("dashboard-cards", DashboardCards);