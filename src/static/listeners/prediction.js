document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("prediction-form");
    const predictButton = document.getElementById("predict-button");

    predictButton.addEventListener("click", function () {
        // Obtener los valores de los semestres ingresados por el usuario
        const semesterValues = [];
        for (let i = 1; i <= 9; i++) {
            const input = form.elements[`semester${i}`];
            if (input) {
                const value = parseFloat(input.value);
                if (!isNaN(value)) {
                    semesterValues.push(value);
                }
            }
        }

        // Calcular las predicciones para los semestres restantes
        const predictionResults = [];
        let currentAverage = 0.0;
        for (let i = 0; i < semesterValues.length; i++) {
            currentAverage += semesterValues[i];
        }
        const semestersRemaining = 9 - semesterValues.length;
        if (semestersRemaining > 0) {
            currentAverage /= semesterValues.length;
            for (let i = 1; i <= semestersRemaining; i++) {
                // Aplica tu lógica de predicción aquí (por ejemplo, asumiremos 9.0 para todos los semestres)
                currentAverage = (currentAverage + 9.0) / 2.0;
                predictionResults.push({
                    semester: semesterValues.length + i,
                    prediction: currentAverage.toFixed(2),
                });
            }
        }

        // Llenar la tabla de resultados con las predicciones
        const resultTable = document.getElementById("prediction-result-table");
        resultTable.innerHTML = `
            <tr>
                <th>Semestre</th>
                <th>Predicción</th>
            </tr>
            ${predictionResults
                .map((result) => `<tr><td>Semestre ${result.semester}</td><td>${result.prediction}</td></tr>`)
                .join("")}
        `;
    });
});
