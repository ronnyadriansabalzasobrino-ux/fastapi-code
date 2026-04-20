class Topbar extends HTMLElement {
connectedCallback(){
this.innerHTML = `
<header class="topbar">
  <div class="topbar-left">
    <h1>📊 School System</h1>
  </div>

  <div class="topbar-right">
    <span class="user-info">👤 ${localStorage.getItem("name") ?? "Usuario"}</span>
    <button onclick="logout()" class="btn-logout">🚪 Salir</button>
  </div>
</header>
`;
}
}

customElements.define("app-topbar", Topbar);

function logout(){
localStorage.clear();
window.location.href = "/login.html";
}