class ModalComponent extends HTMLElement {

connectedCallback(){

this.innerHTML = `

<div id="modal" class="modal">

  <div class="modal-content">

    <h2 id="modalTitle"></h2>

    <p id="modalMessage"></p>

    <div id="modalActions"></div>

  </div>

</div>

`;

}

}

customElements.define(
"app-modal",
ModalComponent
);