class SubjectsTable extends HTMLElement {

connectedCallback(){

this.innerHTML = `
<div class="table-card">

  <div class="table-header">
    <h2>📚 Materias</h2>
  </div>

  <table id="subjectsTableDisplay">
    <thead>
      <tr>
        <th>Materia</th>
        <th>Créditos</th>
        <th>Programa</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>

</div>
`;
}
}

customElements.define("subjects-table", SubjectsTable);