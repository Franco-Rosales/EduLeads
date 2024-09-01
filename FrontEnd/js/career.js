document.addEventListener("DOMContentLoaded", () => {
    const careerForm = document.getElementById("career-form");

    // Cargar personas
    loadPersons();

    // Cargar carreras
    loadCareers();

    // Exponer la función globalmente
    window.loadCareers = loadCareers;

    // Cargar la lista de inscripciones a carreras cuando se cargue el formulario
    loadPersonCareerList();

    careerForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const personId = document.getElementById("person-select").value;
        const careerIds = Array.from(document.getElementById("career-select").selectedOptions).map(option => option.value);
        const timeTaken = document.getElementById("time-taken").value;

        if (!personId || careerIds.length === 0 || !timeTaken) {
            document.getElementById("career-error").textContent = "Debe seleccionar una persona, al menos una carrera y proporcionar el tiempo de cursado.";
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:8000/person-careers/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ person_id: personId, career_id: careerIds[0], time_taken: timeTaken })
            });

            if (!response.ok) throw new Error("Error al inscribir en carreras");

            const result = await response.json();
            alert(`Inscripción en carrera realizada con éxito, código de seguimiento: ${result.person_career_id}`);
            careerForm.reset();
            document.getElementById("career-error").textContent = "";

            // Actualizar la lista de inscripciones a carreras después de crear una nueva inscripción
            loadPersonCareerList();
        } catch (error) {
            document.getElementById("career-error").textContent = error.message;
        }
    });

    async function loadPersons() {
        try {
            const response = await fetch("http://127.0.0.1:8000/persons/");
            const data = await response.json();
            if (data.length === 0) {
                personSelect.innerHTML = `<option>No existen personas cargadas...</option>`
            }
            const personSelect = document.getElementById("person-select");
            personSelect.innerHTML = `<option value="">Seleccione una persona...</option>` + 
            data.map(person => `<option value="${person.id}">${person.name} ${person.surname}</option>`).join("");
        } catch (error) {
            console.error("Error al cargar las personas:", error);
        }
    }

    async function loadCareers() {
        try {
            const careerSelect = document.getElementById("career-select");
            careerSelect.innerHTML = ""
            const response = await fetch("http://127.0.0.1:8000/careers/");
            const data = await response.json();
            if (data.length === 0) {
                careerSelect.innerHTML = `<option>No existen carreras cargadas...</option>`
                subjectSelect.innerHTML = "";
                return;
            }

            careerSelect.innerHTML = data.map(career => `<option value="${career.id}">${career.name}</option>`).join("");
        } catch (error) {
            console.error("Error al cargar las carreras:", error);
        }
    }

    // función para cargar la lista de inscripciones a carreras
    async function loadPersonCareerList() {
        try {
            const response = await fetch("http://localhost:8000/person-careers/");
            const personCareerData = await response.json();

            // Limpiar la tabla antes de cargar nuevos datos
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
});
