class CardComponent extends HTMLElement {

connectedCallback(){

const text = this.getAttribute("text");
const action = this.getAttribute("action");
const icon = this.getAttribute("icon") || "📌";

this.innerHTML = `
<div class="card" onclick="${action}">
  <div class="card-icon">${icon}</div>
  <div class="card-text">${text}</div>
</div>
`;
}

}

customElements.define("dashboard-card", CardComponent);