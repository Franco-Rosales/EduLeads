document.addEventListener("DOMContentLoaded", () => {
    async function loadPersonCareerList(filterId = '') {
        try {
            let url = "http://localhost:8000/person-careers/paginated/?skip=0&limit=10";
            if (filterId) {
                url += `&person_career_id=${filterId}`;
            }
            const response = await fetch(url);
            const personCareerData = await response.json();

            const tableBody = document.querySelector("#career-list-table tbody");
            tableBody.innerHTML = "";

            for (const item of personCareerData) {
                // Crear una fila en la tabla con los datos
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${item.person_career_id}</td>
                    <td>${item.career_name}</td>
                    <td>${item.person_name}</td>
                `;
                tableBody.appendChild(row);
            }
        } catch (error) {
            console.error("Error al cargar las inscripciones a carreras:", error);
        }
    }

    // Llamar a la función para cargar la lista de inscripciones cuando se muestre la pantalla
    document.getElementById("show-person-career-list").addEventListener("click", () => {
        showScreen("person-career-list");
        loadPersonCareerList(); // Cargar sin filtro al inicio
    });

    // Manejar el filtro por ID
    document.getElementById("apply-filter").addEventListener("click", () => {
        const filterId = document.getElementById("filter-id").value;
        loadPersonCareerList(filterId);
    });
});
