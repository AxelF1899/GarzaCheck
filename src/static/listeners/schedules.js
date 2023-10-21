// Espera a que el documento HTML se cargue completamente
document.addEventListener("DOMContentLoaded", function () {
  // Manejo del botón "Agregar Materia"
  const agregarMateriaButton = document.getElementById("agregar-materia");
  agregarMateriaButton.addEventListener("click", function (event) {
    event.preventDefault();

    // Creación de la sección de materia
    const horarioSection = document.querySelector(".horario-section");
    const materiaSection = document.createElement("div");
    materiaSection.classList.add("materia-section");

    // Generación de un número único para la materia
    const numMaterias =
      horarioSection.querySelectorAll(".materia-section").length + 1;

    // Contenido de la sección de materia
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

    // Agregar la sección de materia a la sección de horarios
    horarioSection.insertBefore(materiaSection, agregarMateriaButton);

    // Manejo del botón "Agregar Horario" dentro de la sección de materia
    const agregarHorarioButton =
      materiaSection.querySelector(".agregar-horario");
    agregarHorarioButton.addEventListener("click", function (event) {
      event.preventDefault();

      // Clonar un horario de día
      const horarioDiv = materiaSection.querySelector(".horario");
      const horarioDiaClone = horarioDiv
        .querySelector(".horario-dia")
        .cloneNode(true);

      // Limpia los campos de hora inicio y fin
      const horaInicioInput = horarioDiaClone.querySelector("#hora_inicio");
      const horaFinInput = horarioDiaClone.querySelector("#hora_fin");
      horaInicioInput.value = "";
      horaFinInput.value = "";

      // Agregar el horario de día clonado
      horarioDiv.appendChild(horarioDiaClone);
    });

    // Manejo de la eliminación de horarios de día
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

  // Función para generar la tabla de horarios en el formato deseado
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
    horas.forEach((hora) => {
      const row = document.createElement("tr");
      const horaCell = document.createElement("td");
      horaCell.textContent = hora;
      row.appendChild(horaCell);
      dias.forEach(() => {
        const emptyCell = document.createElement("td");
        row.appendChild(emptyCell);
      });
      tbody.appendChild(row);
    });

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
    
        // Validar que las horas de inicio y finalización sean en punto
        if (!validarHoraEnPunto(horaInicio) || !validarHoraEnPunto(horaFin)) {
          alert("Las horas de inicio y finalización deben ser en punto (por ejemplo, 7:00, 8:00, 9:00).");
          return; // Detener la generación de la tabla si no son horas en punto
        }
    
        const rowIndexInicio = horas.indexOf(horaInicio);
        const rowIndexFin = horas.indexOf(horaFin) - 1; // Restar 1 para obtener la hora anterior
    
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

  // Llamar a la función para generar la tabla en el formato deseado cuando se hace clic en "Imprimir Horario"
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
