class AlertsTable extends HTMLElement {

connectedCallback(){

this.innerHTML = `
<div class="table-card alert-card">

  <div class="table-header">
    <h2>⚠️ Alertas</h2>
  </div>

  <table id="alertsTableDisplay">
    <thead>
      <tr>
        <th>Estudiante</th>
        <th>Tipo</th>
        <th>Descripción</th>
        <th>Riesgo</th>
        <th>Estado</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>

</div>
`;
}
}

customElements.define("alerts-table", AlertsTable);