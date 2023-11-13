
document.addEventListener("DOMContentLoaded", function () {

  generarTabla();
  
  const agregarMateriaButton = document.getElementById("agregar-materia");
  agregarMateriaButton.addEventListener("click", function (event) {
    event.preventDefault();

    
    const horarioSection = document.querySelector(".horario-section");
    const materiaSection = document.createElement("div");
    materiaSection.classList.add("materia-section");

    
    const numMaterias =
      horarioSection.querySelectorAll(".materia-section").length + 1;

    
    materiaSection.innerHTML = `
      <h3>Materia ${numMaterias}</h3>
      <form>
        <label for="materia">Nombre de la Materia:</label>
        <input type="text" id="materia" name="materia" required>
        <div class="horario">
          <h4>Horarios:</h4>
          <div class="horario-dia">
            <label for="dia">Día:</label>
            <select id="dia" name="dia">
              <option value="Lunes">Lunes</option>
              <option value="Martes">Martes</option>
              <option value="Miércoles">Miércoles</option>
              <option value="Jueves">Jueves</option>
              <option value="Viernes">Viernes</option>
              <option value="Sábado">Sábado</option>
            </select>
            <label for="hora_inicio">Hora de Inicio:</label>
            <input type="time" id="hora_inicio" name="hora_inicio" min="07:00" max="20:00" required>
            <p/>
            <label for="hora_fin">Hora de Fin:</label>
            <input type="time" id="hora_fin" name="hora_fin" min="08:00" max="21:00" required>
          </div>
        </div>
        <button class="agregar-horario">Agregar Horario</button>
      </form>
    `;

    
    horarioSection.insertBefore(materiaSection, agregarMateriaButton);

    
    const agregarHorarioButton =
      materiaSection.querySelector(".agregar-horario");
    agregarHorarioButton.addEventListener("click", function (event) {
      event.preventDefault();

      
      const horarioDiv = materiaSection.querySelector(".horario");
      const horarioDiaClone = horarioDiv
        .querySelector(".horario-dia")
        .cloneNode(true);

      
      const horaInicioInput = horarioDiaClone.querySelector("#hora_inicio");
      const horaFinInput = horarioDiaClone.querySelector("#hora_fin");
      horaInicioInput.value = "";
      horaFinInput.value = "";

      
      horarioDiv.appendChild(horarioDiaClone);
    });

    
    const horariosDiaDivs = materiaSection.querySelectorAll(".horario-dia");
    horariosDiaDivs.forEach(function (horarioDiaDiv) {
      const eliminarHorarioButton =
        horarioDiaDiv.querySelector(".eliminar-horario");
      if (eliminarHorarioButton) {
        eliminarHorarioButton.addEventListener("click", function (event) {
          event.preventDefault();
          horarioDiaDiv.remove();
        });
      }
    });
  });

  
  function generarTabla() {
    const horarioSection = document.querySelector(".horario-section");
    const materiaSections = horarioSection.querySelectorAll(".materia-section");
    const tableContainer = document.getElementById("horario-table-container");
    const table = document.createElement("table");
    table.id = "horario-table";
    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");
    const dias = [
      "Lunes",
      "Martes",
      "Miércoles",
      "Jueves",
      "Viernes",
      "Sábado",
    ];
    headerRow.appendChild(document.createElement("th"));
    dias.forEach((dia) => {
      const th = document.createElement("th");
      th.textContent = dia;
      headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    const tbody = document.createElement("tbody");
    const horas = [
      "07:00",
      "08:00",
      "09:00",
      "10:00",
      "11:00",
      "12:00",
      "13:00",
      "14:00",
      "15:00",
      "16:00",
      "17:00",
      "18:00",
      "19:00",
      "20:00",
    ];
    horas.forEach((hora, rowIndex) => {
      const row = document.createElement("tr");
      const horaCell = document.createElement("td");
      horaCell.textContent = hora;
      row.appendChild(horaCell);
      dias.forEach((dia, colIndex) => {
        const cell = document.createElement("td");
        row.appendChild(cell);

        
        if (
          (dia === "Lunes" && hora === "07:00") ||
          (dia === "Jueves" && hora === "07:00") ||
          (dia === "Miércoles" && hora === "07:00")||
          (dia === "Lunes" && hora === "08:00") ||
          (dia === "Jueves" && hora === "08:00") ||
          (dia === "Miércoles" && hora === "08:00")
        ) {
          cell.textContent = "Redes";
        } else if (
          (dia === "Lunes" && hora === "09:00") ||
          (dia === "Martes" && hora === "10:00") ||
          (dia === "Miércoles" && hora === "13:00")||
          (dia === "Lunes" && hora === "10:00") ||
          (dia === "Martes" && hora === "11:00") ||
          (dia === "Miércoles" && hora === "14:00")
        ) {
          cell.textContent = "IA";
        } else if (
          (dia === "Lunes" && hora === "11:00") ||
          (dia === "Lunes" && hora === "12:00") ||
          (dia === "Jueves" && hora === "11:00") ||
          (dia === "Jueves" && hora === "12:00")
        ) {
          cell.textContent = "Eng";
        } else if (
          (dia === "Lunes" && hora === "13:00") ||
          (dia === "Lunes" && hora === "14:00") ||
          (dia === "Martes" && hora === "08:00") ||
          (dia === "Martes" && hora === "09:00") ||
          (dia === "Viernes" && hora === "09:00")||
          (dia === "Viernes" && hora === "10:00")
        ) {
          cell.textContent = "BD";
        }else if (
          (dia === "Martes" && hora === "07:00") ||
          (dia === "Miércoles" && hora === "09:00") ||
          (dia === "Miércoles" && hora === "10:00") ||
          (dia === "Jueves" && hora === "09:00") ||
          (dia === "Jueves" && hora === "10:00")||
          (dia === "Viernes" && hora === "07:00")||
          (dia === "Viernes" && hora === "08:00")
        ) {
          cell.textContent = "AMH";
        }

      });
      tbody.appendChild(row);
    });
    table.appendChild(tbody);

    materiaSections.forEach((materiaSection) => {
      const materiaNombre = materiaSection.querySelector(
        "input[name='materia']"
      ).value;
      const horariosDiaDivs = materiaSection.querySelectorAll(".horario-dia");
    
      horariosDiaDivs.forEach((horarioDiaDiv) => {
        const dia = horarioDiaDiv.querySelector("select[name='dia']").value;
        const horaInicioInput = horarioDiaDiv.querySelector("input[name='hora_inicio']");
        const horaFinInput = horarioDiaDiv.querySelector("input[name='hora_fin']");
        const horaInicio = horaInicioInput.value;
        const horaFin = horaFinInput.value;
    
        
        if (!validarHoraEnPunto(horaInicio) || !validarHoraEnPunto(horaFin)) {
          alert("Las horas de inicio y finalización deben ser en punto (por ejemplo, 7:00, 8:00, 9:00).");
          return; 
        }
    
        const rowIndexInicio = horas.indexOf(horaInicio);
        const rowIndexFin = horas.indexOf(horaFin) - 1; 
    
        if (rowIndexInicio !== -1 && rowIndexFin !== -1) {
          const colIndex = dias.indexOf(dia) + 1;
          if (colIndex !== 0) {
            for (let rowIndex = rowIndexInicio; rowIndex <= rowIndexFin; rowIndex++) {
              const cell = tbody.rows[rowIndex].cells[colIndex];
              if (cell.textContent) {
                cell.textContent += `, ${materiaNombre}`;
              } else {
                cell.textContent = materiaNombre;
              }
            }
          }
        }
      });
    
    });
    

    table.appendChild(tbody);

    const existingTable = document.getElementById("horario-table");
    if (existingTable) {
      tableContainer.replaceChild(table, existingTable);
    } else {
      tableContainer.appendChild(table);
    }
  }

  
  const tableContainer = document.getElementById("horario-table-container");

  const guardarHorarioButton = document.createElement("button");
  guardarHorarioButton.id = "guardar-horario";
  guardarHorarioButton.textContent = "Imprimir horario";
  guardarHorarioButton.addEventListener("click", function () {
      const tableToPrint = tableContainer.cloneNode(true);
      tableToPrint.style.width = "100%";
  
      const printWindow = window.open('', '_blank');
      printWindow.document.write('<html><head><title>Horario</title>');
      
      
      printWindow.document.write('<link rel="stylesheet" type="text/css" href="/static/styles/schedules.css" onload="window.print();">');
      
      printWindow.document.write('</head><body>');
      printWindow.document.body.appendChild(tableToPrint);
      printWindow.document.write('</body></html>');
      printWindow.document.close();
  
      
      window.addEventListener("afterprint", function () {
          printWindow.close();
      });
  });
  
  tableContainer.appendChild(guardarHorarioButton);
  

  
  const imprimirHorarioButton = document.getElementById("imprimir-horario");
  imprimirHorarioButton.addEventListener("click", generarTabla);
  
  function validarHoraEnPunto(hora) {
    const partesHora = hora.split(":");
    if (partesHora.length === 2) {
      const minutos = parseInt(partesHora[1]);
      return minutos === 0;
    }
    return false;
  }
  
});
