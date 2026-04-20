class Sidebar extends HTMLElement {
connectedCallback(){

this.innerHTML = `
<aside class="sidebar">

  <div class="sidebar-logo">
    <h2>🎓 School System</h2>
  </div>

  <nav class="sidebar-menu">

    <button onclick="goStudents()">👨‍🎓 Estudiantes</button>
    <button onclick="goTeachers()">👨‍🏫 Docentes</button>
    <button onclick="goSubjects()">📚 Materias</button>
    <button onclick="goAlerts()">⚠️ Alertas</button>

  </nav>

</aside>
`;
}
}

customElements.define("app-sidebar", Sidebar);