document.addEventListener("DOMContentLoaded", () => {
    const createCareerForm = document.getElementById("create-career-form");

    if (createCareerForm) {
        createCareerForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const careerData = {
                name: document.getElementById("career-name").value.trim(),
                description: document.getElementById("career-description").value.trim()
            };

            if (!careerData.name) {
                document.getElementById("create-career-error").textContent = "El nombre de la carrera es requerido.";
                return;
            }

            try {
                const response = await fetch("http://127.0.0.1:8000/careers/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(careerData)
                });

                if (!response.ok) {
                    throw new Error("Error al crear la carrera");
                }

                alert("Carrera creada con éxito");
                createCareerForm.reset();
                document.getElementById("create-career-error").textContent = "";

                // Llamar a loadCareers para actualizar los selects después de crear la carrera
                loadCareers();
            } catch (error) {
                document.getElementById("create-career-error").textContent = error.message;
            }
        });

        async function loadCareers() {
            try {
                const careerSelect = document.getElementById("career-select");
                careerSelect.innerHTML = "";
                const response = await fetch("http://127.0.0.1:8000/careers/");
                const data = await response.json();
                if (data.length === 0) {
                    careerSelect.innerHTML = `<option>No existen carreras cargadas...</option>`;
                    subjectSelect.innerHTML = "";
                    return;
                }

                careerSelect.innerHTML = data.map(career => `<option value="${career.id}">${career.name}</option>`).join("");
            } catch (error) {
                console.error("Error al cargar las carreras:", error);
            }
        }
    }
});
