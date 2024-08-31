document.addEventListener("DOMContentLoaded", () => {
    const createCareerForm = document.getElementById("create-career-form");

    if (createCareerForm) {
        createCareerForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const careerData = {
                name: document.getElementById("career-name").value.trim(),
                description: document.getElementById("career-description").value.trim()
            };

            // Verificar que el nombre de la carrera no esté vacío
            if (!careerData.name) {
                document.getElementById("create-career-error").textContent = "El nombre de la carrera es requerido.";
                return;
            }

            try {
                const response = await fetch("http://127.0.0.1:8000/careers", {
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
            } catch (error) {
                document.getElementById("create-career-error").textContent = error.message;
            }
        });
    }
});
