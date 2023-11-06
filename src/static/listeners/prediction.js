document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("prediction-form");
    const predictButton = document.getElementById("predict-button");
    const resultTable = document.getElementById("prediction-result-table");

    predictButton.addEventListener("click", function () {
        // Obtener los valores de los semestres ingresados por el usuario
        const semesterValues = Array.from(form.querySelectorAll("input[type='number']"))
            .map((input) => parseFloat(input.value))
            .filter((value) => !isNaN(value));

        // Hacer la solicitud POST para calcular las predicciones
        fetch("/prediction", {
            method: "POST",
            body: new FormData(form),
            headers: {
                // No es necesario definir el encabezado "Content-Type" aquí.
            },
        })
        
            .then((response) => response.json())
            .then((data) => {
                // Llenar la tabla de resultados con las predicciones
                resultTable.innerHTML = `
                    <tr>
                        <th>Semestre</th>
                        <th>Predicción</th>
                    </tr>
                    ${data
                        .map((result) => `<tr><td>Semestre ${result.semester}</td><td>${result.prediction}</td></tr>`)
                        .join("")}
                `;
            });
    });
});
