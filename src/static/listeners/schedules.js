// Espera a que el documento HTML se cargue completamente
document.addEventListener("DOMContentLoaded", function () {
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
                        <label for="hora_fin">Hora de Fin:</label>
                        <input type="time" id="hora_fin" name="hora_fin" min="08:00" max="21:00" required>
                    </div>
                </div>
                <button class="agregar-horario">Agregar Horario</button>
            </form>
        `;

    horarioSection.insertBefore(materiaSection, agregarMateriaButton);

    // Agrega evento para agregar horario
    const agregarHorarioButton =
      materiaSection.querySelector(".agregar-horario");
    agregarHorarioButton.addEventListener("click", function (event) {
      event.preventDefault();

      const horarioDiv = materiaSection.querySelector(".horario");
      const horarioDiaClone = horarioDiv
        .querySelector(".horario-dia")
        .cloneNode(true);

      // Limpia los campos de hora inicio y fin
      const horaInicioInput = horarioDiaClone.querySelector("#hora_inicio");
      const horaFinInput = horarioDiaClone.querySelector("#hora_fin");
      horaInicioInput.value = "";
      horaFinInput.value = "";

      horarioDiv.appendChild(horarioDiaClone);
    });

    // Agrega evento para eliminar horario
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

  // Obtener el contenedor de la tabla
  const tableContainer = document.getElementById("horario-table-container");

  // Crear una tabla HTML
  const table = document.createElement("table");
  table.id = "horario-table";

  // Crear la cabecera de la tabla con los días
  const thead = document.createElement("thead");
  const headerRow = document.createElement("tr");
  const dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];

  // Agregar una columna vacía para las horas
  headerRow.appendChild(document.createElement("th"));

  dias.forEach((dia) => {
    const th = document.createElement("th");
    th.textContent = dia;
    headerRow.appendChild(th);
  });

  thead.appendChild(headerRow);
  table.appendChild(thead);

  // Crear el cuerpo de la tabla con las horas
  const tbody = document.createElement("tbody");
  const horas = ["07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"];

  horas.forEach((hora) => {
    const row = document.createElement("tr");

    // Agregar una celda para la hora
    const horaCell = document.createElement("td");
    horaCell.textContent = hora;
    row.appendChild(horaCell);

    // Agregar celdas vacías para los días
    dias.forEach(() => {
      const emptyCell = document.createElement("td");
      row.appendChild(emptyCell);
    });

    tbody.appendChild(row);
  });

  // Iterar a través de las materias y llenar las celdas correspondientes
  materiaSections.forEach((materiaSection) => {
    const materiaNombre = materiaSection.querySelector("input[name='materia']").value;
    const horariosDiaDivs = materiaSection.querySelectorAll(".horario-dia");

    horariosDiaDivs.forEach((horarioDiaDiv) => {
      const dia = horarioDiaDiv.querySelector("select[name='dia']").value;
      const horaInicio = horarioDiaDiv.querySelector("input[name='hora_inicio']").value;
      const horaFin = horarioDiaDiv.querySelector("input[name='hora_fin']").value;

      // Encontrar la celda correspondiente en la tabla
      const rowIndex = horas.indexOf(horaInicio);
      const colIndex = dias.indexOf(dia) + 1; // Sumar 1 para omitir la columna de las horas

      if (rowIndex !== -1 && colIndex !== 0) {
        const cell = tbody.rows[rowIndex].cells[colIndex];
        // Agregar la materia a la celda sin reemplazar el contenido anterior
        if (cell.textContent) {
          cell.textContent += `, ${materiaNombre}`;
        } else {
          cell.textContent = materiaNombre;
        }
      }
    });
  });

  table.appendChild(tbody);

  // Reemplazar la tabla existente (si la hay) en el contenedor
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

});
