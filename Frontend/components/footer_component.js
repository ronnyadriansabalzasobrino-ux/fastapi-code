class Footer extends HTMLElement {
connectedCallback(){
this.innerHTML = `
<footer class="footer">
  ©️ 2026 School System - Proyecto académico
</footer>
`;
}
}

customElements.define("app-footer", Footer);