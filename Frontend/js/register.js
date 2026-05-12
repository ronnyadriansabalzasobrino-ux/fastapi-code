const API = "https://alertas-backend.onrender.com";

async function register() {

  const name = document.getElementById("name").value.trim();
  const last_name = document.getElementById("last_name").value.trim();
  const mail = document.getElementById("mail").value.trim();
  const password = document.getElementById("password").value.trim();
  const rol = document.getElementById("rol").value;

  if (!name || !last_name || !mail || !password || !rol) {
    alert("Completa todos los campos");
    return;
  }

  const res = await fetch(API + "/register", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      name,
      last_name,
      mail,
      password,
      rol
    })
  });

  if (!res.ok) {
    alert("Error al registrar");
    return;
  }

  alert("Usuario registrado correctamente");

  window.location.href = "login.html";
}