class Sidebar extends HTMLElement {
connectedCallback(){

this.innerHTML = `
<aside class="sidebar">

  <div class="sidebar-logo">
    <h2>🎓 School System</h2>
  <ul>

  <div class="sidebar-menu">

    <li><button onclick="goStudents()">👨‍🎓 Estudiantes</button></li>


    <li><button onclick="goTeachers()">👨‍🏫 Docentes</button></li>


    <li><button onclick="goSubjects()">📚 Materias</button></li>


    <li><button onclick="goAlerts()">⚠️ Alertas</button></li>



  </ul>

</aside>
`;
}
}

customElements.define("app-sidebar", Sidebar);