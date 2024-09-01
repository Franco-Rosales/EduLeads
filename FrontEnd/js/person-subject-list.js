document.addEventListener("DOMContentLoaded", () => {
    loadPersonSubjectList();
});

async function loadPersonSubjectList() {
    const tableBody = document.querySelector("#subject-list-table tbody");
    tableBody.innerHTML = "";

    try {
        // Obtener todas las inscripciones a materias
        const response = await fetch("http://localhost:8000/person-subjects/");
        const enrollments = await response.json();

        // Iterar sobre cada inscripción para obtener los detalles necesarios
        for (const enrollment of enrollments) {
            const personResponse = await fetch(`http://localhost:8000/persons/${enrollment.person_id}`);
            const personData = await personResponse.json();

            const careerResponse = await fetch(`http://localhost:8000/careers/${enrollment.career_id}`);
            const careerData = await careerResponse.json();

            const subjectResponse = await fetch(`http://localhost:8000/subjects/${enrollment.subject_id}`);
            const subjectData = await subjectResponse.json();

            // Crear una fila en la tabla con los datos obtenidos
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${enrollment.person_subject_id}</td>
                <td>${careerData.name}</td>
                <td>${subjectData.name}</td>
                <td>${personData.name} ${personData.surname}</td>
            `;
            tableBody.appendChild(row);
        }
    } catch (error) {
        console.error("Error al cargar las inscripciones a materias:", error);
        document.querySelector("#subject-error").textContent = "Error al cargar las inscripciones a materias.";
    }
}
