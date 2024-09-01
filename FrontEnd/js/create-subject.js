document.addEventListener("DOMContentLoaded", () => {
    const createSubjectForm = document.getElementById("create-subject-form");

    // Exponer la función globalmente
    window.loadCareersForSubjectCreation = async function() {
        try {
            const response = await fetch("http://127.0.0.1:8000/careers/");
            const data = await response.json();

            const careerSelect = document.getElementById("subject-careers");
            careerSelect.innerHTML = data.map(career => `<option value="${career.id}">${career.name}</option>`).join("");
        } catch (error) {
            console.error("Error al cargar las carreras:", error);
        }
    };

    // Cargar carreras al inicio
    loadCareersForSubjectCreation();

    createSubjectForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        // Obtener valores de los campos del formulario
        const subjectData = {
            name: document.getElementById("subject-name").value.trim(),
            description: document.getElementById("subject-description").value.trim(),
            career_ids: Array.from(document.getElementById("subject-careers").selectedOptions).map(option => option.value)
        };

        // Verificar si hay al menos una carrera seleccionada
        if (subjectData.career_ids.length === 0) {
            document.getElementById("create-subject-error").textContent = "Debe seleccionar al menos una carrera.";
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:8000/subjects/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(subjectData)
            });

            if (!response.ok) throw new Error("Error al crear la materia");

            alert("Materia creada con éxito");
            createSubjectForm.reset();
            
            document.getElementById("create-subject-error").textContent = "";

            // Llamar  para actualizar el listado de carreras
            loadCareersForSubjectCreation();
        } catch (error) {
            document.getElementById("create-subject-error").textContent = error.message;
        }
    });
});
