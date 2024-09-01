document.addEventListener("DOMContentLoaded", () => {
    // Cargar la lista de inscripciones a materias sin filtro al inicio
    loadPersonSubjectList();

    // Manejar el filtro por ID
    document.getElementById("apply-subject-filter").addEventListener("click", () => {
        const filterId = document.getElementById("subject-filter-id").value;
        loadPersonSubjectList(filterId);
    });
});

async function loadPersonSubjectList(filterId = '') {
    const tableBody = document.querySelector("#subject-list-table tbody");
    tableBody.innerHTML = "";

    try {
        let url = "http://localhost:8000/person-subjects/paginated/?skip=0&limit=10";
        if (filterId) {
            url += `&person_subject_id=${filterId}`;
        }
        const response = await fetch(url);
        const enrollments = await response.json();

        // Iterar sobre cada inscripción para obtener los detalles necesarios
        for (const enrollment of enrollments) {
            // Crear una fila en la tabla con los datos obtenidos
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${enrollment.person_subject_id}</td>
                <td>${enrollment.career_name || 'Desconocida'}</td>
                <td>${enrollment.subject_name || 'Desconocida'}</td>
                <td>${enrollment.person_name || 'Desconocido'}</td>
            `;
            tableBody.appendChild(row);
        }
    } catch (error) {
        console.error("Error al cargar las inscripciones a materias:", error);
        document.querySelector("#subject-error").textContent = "Error al cargar las inscripciones a materias.";
    }
}
