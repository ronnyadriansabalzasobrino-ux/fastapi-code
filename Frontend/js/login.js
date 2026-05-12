console.log("LOGIN JS NUEVO");

const API = "https://alertas-backend.onrender.com";

async function login() {

  const mail =
  document.getElementById("mail").value.trim();

  const password =
  document.getElementById("password").value.trim();

  if (!mail || !password) {

    alert("Por favor ingresa correo y contraseña");

    return;

  }

  try {

    const response = await fetch(`${API}/login`, {

      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        mail,
        password
      })

    });

    if (!response.ok) {

      const errData = await response.json();

      alert(
        errData.detail ||
        "Correo o contraseña incorrectos"
      );

      return;

    }

    const data = await response.json();

    console.log(data);

    localStorage.setItem(
      "access_token",
      data.access_token
    );

    localStorage.setItem(
      "rol",
      data.rol
    );

    localStorage.setItem(
      "name",
      data.name
    );

    localStorage.setItem(
      "mail",
      mail
    );

    alert("Login correcto");

    window.location.href =
    "dashboard.html";

  }

  catch (error) {

    console.error(error);

    alert(
      "Error conectando con el servidor"
    );

  }

}

window.login = login;