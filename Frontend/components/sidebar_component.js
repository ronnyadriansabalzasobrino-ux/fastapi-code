class Sidebar extends HTMLElement {
  
connectedCallback(){

this.innerHTML = `
<aside class="sidebar">

<h2 class="logo">School System</h2>

<ul>

<li onclick="goStudents()">👨‍🎓 Estudiantes</li>

<li onclick="goTeachers()">👨‍🏫 Docentes</li>

<li onclick="goSubjects()">📚 Materias</li>

<li onclick="goAlerts()">⚠️ Alertas</li>



</ul>

</aside>
`;

}

}

customElements.define("app-sidebar", Sidebar);