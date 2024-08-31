document.addEventListener("DOMContentLoaded", () => {
    const careerForm = document.getElementById("career-form");

    // Cargar personas
    loadPersons();

    // Cargar carreras
    loadCareers();

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
            const response = await fetch("http://127.0.0.1:8000/person-careers/person-careers/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ person_id: personId, career_id: careerIds[0], time_taken: timeTaken })
            });

            if (!response.ok) throw new Error("Error al inscribir en carreras");

            alert("Inscripción en carreras realizada con éxito");
            careerForm.reset();
            document.getElementById("career-error").textContent = "";
        } catch (error) {
            document.getElementById("career-error").textContent = error.message;
        }
    });

    async function loadPersons() {
        try {
            const response = await fetch("http://127.0.0.1:8000/persons/persons/");
            const data = await response.json();

            const personSelect = document.getElementById("person-select");
            personSelect.innerHTML = data.map(person => `<option value="${person.id}">${person.name} ${person.surname}</option>`).join("");
        } catch (error) {
            console.error("Error al cargar las personas:", error);
        }
    }

    async function loadCareers() {
        try {
            const response = await fetch("http://127.0.0.1:8000/careers/careers/");
            const data = await response.json();

            const careerSelect = document.getElementById("career-select");
            careerSelect.innerHTML = data.map(career => `<option value="${career.id}">${career.name}</option>`).join("");
        } catch (error) {
            console.error("Error al cargar las carreras:", error);
        }
    }
});
