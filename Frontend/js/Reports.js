const API = "https://alertas-backend.onrender.com"

/* =========================
   📄 GENERAR REPORTE PDF
========================= */
function generateReport(){

const risk = document.getElementById("risk_level").value
const state = document.getElementById("state").value
const program = document.getElementById("id_program").value

const url = `${API}/reports/pdf?risk_level=${risk}&state=${state}&id_program=${program}`

// abre descarga del PDF
window.open(url, "_blank")

}