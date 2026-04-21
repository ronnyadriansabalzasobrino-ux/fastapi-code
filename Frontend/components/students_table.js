class studentsTable extends HTMLElement {

connectedCallback(){

this.innerHTML = `
<div class="table-card">

  <div class="table-header">
    <h2>👨‍🎓 Estudiantes</h2>
  </div>

  <table id="studentsTableDisplay" class="display">
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Apellido</th>
        <th>Email</th>
        <th>Teléfono</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>

</div>
`;
}
}

customElements.define("students-table", studentsTable);