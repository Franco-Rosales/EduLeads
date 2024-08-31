document.addEventListener("DOMContentLoaded", () => {
    const personSelect = document.getElementById("person-select-subject");
    const careerSelect = document.getElementById("career-select-subject");
    const subjectSelect = document.getElementById("subject-select");
    const subjectForm = document.getElementById("subject-form");
    const errorElement = document.getElementById("subject-error");

    // Cargar personas al cargar la página
    loadPersons();

    // Evento para cuando se selecciona una persona
    personSelect.addEventListener("change", async () => {
        const personId = personSelect.value;
        console.log(`Persona seleccionada: ${personId}`);
        if (personId) {
            await loadCareersForPerson(personId);
        } else {
            careerSelect.innerHTML = "";
            subjectSelect.innerHTML = "";
        }
    });

    // Evento para cuando se selecciona una carrera
    careerSelect.addEventListener("change", async () => {
        const careerId = careerSelect.value;
        console.log(`Carrera seleccionada: ${careerId}`); // Agregado para depuración
        if (careerId) {
            await loadSubjectsForCareer(careerId);
        } else {
            subjectSelect.innerHTML = "";
        }
    });

    // Evento para el envío del formulario
    subjectForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const personId = personSelect.value;
        const careerId = careerSelect.value;
        const subjectIds = Array.from(subjectSelect.selectedOptions).map(option => option.value);

        if (!personId || !careerId || subjectIds.length === 0) {
            errorElement.textContent = "Debe seleccionar una persona, una carrera y al menos una materia.";
            return;
        }

        for (const subjectId of subjectIds) {
            await registerPersonToSubject(personId, careerId, subjectId);
        }

        alert("Inscripción en materias realizada con éxito");
        subjectForm.reset();
        careerSelect.innerHTML = ""; // Resetear selector de carreras después de la inscripción
        subjectSelect.innerHTML = ""; // Resetear selector de materias después de la inscripción
    });

    async function loadPersons() {
        try {
            errorElement.textContent = "";
            const response = await fetch("http://127.0.0.1:8000/persons/?skip=0&limit=100");
            const persons = await response.json();
            console.log("Personas cargadas:", persons); // Log para verificar datos
            if (persons.length === 0){
                personSelect.innerHTML = `<option>No existen personas cargadas...</option>`
            }
            personSelect.innerHTML = `<option value="">Seleccione una persona...</option>` + 
            persons.map(person => `<option value="${person.id}">${person.name} ${person.surname}</option>`).join("");        
        } catch (error) {
            console.error("Error al cargar las personas:", error);
            errorElement.textContent = "Error al cargar las personas.";
        }
    }

    async function loadCareersForPerson(personId) {
        try {
            errorElement.textContent = "";
            const response = await fetch(`http://127.0.0.1:8000/person-careers/${personId}`);
            const careers = await response.json();
            if (careers.length === 0) {
                careerSelect.innerHTML = `<option>La persona no tiene carreras asignadas</option>`
                subjectSelect.innerHTML = "";
                return;
            }
            console.log("Carreras cargadas para la persona:", careers); // Log para verificar datos
            careerSelect.innerHTML = ""; // Asegúrate de vaciar el selector primero

            for (const career of careers) {
                const careerResponse = await fetch(`http://127.0.0.1:8000/careers/${career.career_id}`);
                const careerData = await careerResponse.json();
                careerSelect.innerHTML += `<option value="${careerData.id}">${careerData.name}</option>`;
            }

            // Forzar evento 'change' para actualizar materias si solo hay una carrera cargada
            if (careers.length === 1) {
                careerSelect.dispatchEvent(new Event('change'));
            }
        } catch (error) {
            console.error("Error al cargar las carreras:", error);
            errorElement.textContent = "Error al cargar las carreras.";
        }
    }

    async function loadSubjectsForCareer(careerId) {
        try {
            errorElement.textContent = "";
            const response = await fetch(`http://127.0.0.1:8000/subjects/subjects_by_career/${careerId}`);
            const subjects = await response.json();
            console.log("Materias cargadas para la carrera:", subjects); // Log para verificar datos
            subjectSelect.innerHTML = ""; // Asegúrate de vaciar el selector primero
            subjectSelect.innerHTML = subjects.map(subject => `<option value="${subject.id}">${subject.name}</option>`).join("");
        } catch (error) {
            console.error("Error al cargar las materias:", error);
            errorElement.textContent = "Error al cargar las materias.";
        }
    }

    async function registerPersonToSubject(personId, careerId, subjectId) {
        try {
            const enrollmentData = {
                person_id: parseInt(personId),
                career_id: parseInt(careerId),
                subject_id: parseInt(subjectId),
                times_taken: 0,
                enrollment_year: new Date().getFullYear()
            };

            const response = await fetch("http://127.0.0.1:8000/person-subjects", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(enrollmentData)
            });

            if (!response.ok) throw new Error("Error al inscribir en materias");
        } catch (error) {
            console.error("Error al registrar la inscripción:", error);
            errorElement.textContent = "Error al registrar la inscripción.";
        }
    }
});
