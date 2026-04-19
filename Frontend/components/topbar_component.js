class Topbar extends HTMLElement {
connectedCallback(){
this.innerHTML = `
<header class="topbar">
  <h1>📊 School System </h1>
  <button onclick="logout()" class=logout-btn">Salir</button>
</header>
`;
}
}

customElements.define("app-topbar", Topbar);


function logout(){
localStorage.clear();
window.location.href = "login.html";
}