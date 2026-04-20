class TeachersTable extends HTMLElement {

connectedCallback(){

this.innerHTML = `
<div class="table-card">

  <div class="table-header">
    <h2>👨‍🏫 Docentes</h2>
  </div>

  <table id="teachersTableDisplay">
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Apellido</th>
        <th>Email</th>
        <th>Teléfono</th>
        <th>Especialidad</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>

</div>
`;
}
}

customElements.define("teachers-table", TeachersTable);