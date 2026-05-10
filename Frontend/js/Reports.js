const API = "https://alertas-backend.onrender.com"

async function generateReport(){

  const risk =
  document.getElementById("risk_level").value

  const state =
  document.getElementById("state").value

  const program =
  document.getElementById("id_program").value

  const response = await fetch(

    `${API}/reports/data?risk_level=${risk}&state=${state}&id_program=${program}`

  )

  const data = await response.json()

  if(data.length === 0){

    alert("No hay datos para generar reporte")
    return

  }

  const { jsPDF } = window.jspdf

  const doc = new jsPDF("landscape")

  // COLORES
  const azulOscuro = [25, 35, 126]
  const azulClaro = [227, 242, 253]
  const azulMedio = [25, 118, 210]

  // HEADER
  doc.setFillColor(...azulOscuro)
  doc.rect(0,0,300,25,"F")

  doc.setTextColor(255,255,255)

  doc.setFontSize(20)

  doc.text(
    "SISTEMA DE ALERTAS ACADÉMICAS",
    148,
    10,
    {align:"center"}
  )

  doc.setFontSize(11)

  doc.text(
    "Proyecto S.A.P.E.R",
    148,
    18,
    {align:"center"}
  )

  // FECHA
  doc.setTextColor(0,0,0)

  doc.setFontSize(10)

  const fecha = new Date().toLocaleDateString()

  doc.text(
    `Fecha generación: ${fecha}`,
    14,
    35
  )

  doc.text(
    `Total registros: ${data.length}`,
    14,
    42
  )

  // TABLA
  const rows = data.map(item => [

    item.id_student,

    item.name + " " + item.last_name,

    item.id_program,

    item.tipo_alert,

    item.risk_level,

    item.state

  ])

  doc.autoTable({

    startY: 55,

    head:[[
      "ID",
      "Estudiante",
      "Programa",
      "Tipo alerta",
      "Riesgo",
      "Estado"
    ]],

    body: rows,

    theme:"grid",

    headStyles:{

      fillColor: azulMedio,
      textColor:[255,255,255],
      fontStyle:"bold"

    },

    alternateRowStyles:{

      fillColor: azulClaro

    },

    styles:{

      fontSize:9

    }

  })

  // FOOTER
  const totalPages =
  doc.internal.getNumberOfPages()

  for(let i=1;i<=totalPages;i++){

    doc.setPage(i)

    doc.setFillColor(...azulOscuro)

    doc.rect(
      0,
      200,
      300,
      10,
      "F"
    )

    doc.setTextColor(255,255,255)

    doc.setFontSize(8)

    doc.text(

      `Proyecto S.A.P.E.R - Página ${i} de ${totalPages}`,

      148,

      205,

      {align:"center"}

    )

  }

  doc.save("reporte_alertas.pdf")
}