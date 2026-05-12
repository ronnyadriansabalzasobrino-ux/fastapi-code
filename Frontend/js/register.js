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

  try {

    const res = await fetch(API + "/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name,
        last_name,
        mail,
        password,
        rol
      })
    });

    if (!res.ok) {
      const err = await res.json();
      alert(err.detail || "Error al registrar");
      return;
    }

    const data = await res.json();

    alert("Usuario registrado correctamente");

    // opcional: auto login
    localStorage.setItem("mail", mail);
    localStorage.setItem("rol", rol);

    window.location.href = "login.html";

  } catch (error) {
    console.error(error);
    alert("Error conectando con el servidor");
  }
}

window.register = register;