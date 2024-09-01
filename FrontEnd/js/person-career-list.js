document.addEventListener("DOMContentLoaded", () => {
    async function loadPersonCareerList() {
        try {
            const response = await fetch("http://localhost:8000/person-careers/");
            const personCareerData = await response.json();

            const tableBody = document.querySelector("#career-list-table tbody");
            tableBody.innerHTML = "";

            for (const item of personCareerData) {
                // Obtener datos de la persona
                const personResponse = await fetch(`http://localhost:8000/persons/${item.person_id}`);
                const personData = await personResponse.json();

                // Obtener datos de la carrera
                const careerResponse = await fetch(`http://localhost:8000/careers/${item.career_id}`);
                const careerData = await careerResponse.json();

                // Crear una fila en la tabla con los datos
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${item.person_career_id}</td>
                    <td>${careerData.name}</td>
                    <td>${personData.name} ${personData.surname}</td>
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
        loadPersonCareerList();
    });
});
