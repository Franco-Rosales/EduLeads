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

                // funciones para actualizar el listado de carreras
                updateCareerList();
            } catch (error) {
                document.getElementById("create-career-error").textContent = error.message;
            }
        });

        async function updateCareerList() {
            // Verificar si la función existe en el contexto global
            if (window.loadCareersForSubjectCreation) {
                await window.loadCareersForSubjectCreation();
            } else {
                console.error("La función loadCareersForSubjectCreation no está definida.");
            }

            // Verificar si la función loadCareers existe en el contexto global
            if (window.loadCareers) {
                await window.loadCareers();
            } else {
                console.error("La función loadCareers no está definida.");
            }
        }
    }
});
