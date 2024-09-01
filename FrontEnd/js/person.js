document.addEventListener("DOMContentLoaded", () => {
    const personForm = document.getElementById("person-form");
    
    if (personForm) {

    personForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const personData = {
            name: document.getElementById("name").value,
            surname: document.getElementById("last_name").value,
            email: document.getElementById("email").value,
            address: document.getElementById("address").value,
            phone: document.getElementById("phone").value
        };

        try {
            const response = await fetch("http://127.0.0.1:8000/persons/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(personData)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "Error al registrar la persona");
            }

            alert("Persona registrada con éxito");
            personForm.reset();
            document.getElementById("person-error").textContent = "";

            // Cargar las personas después de registrar una nueva persona
            loadPersons();

            // Asegurarse de actualizar todos los selectores de personas globalmente
            if (typeof window.loadPersons === "function") {
                window.loadPersons();
            }
        } catch (error) {
            document.getElementById("person-error").textContent = error.message;
        }
    });

    async function loadPersons() {
        try {
            const personSelect = document.getElementById("person-select");
            personSelect.innerHTML = "";
            const response = await fetch("http://127.0.0.1:8000/persons/");
            const data = await response.json();

            if (data.length === 0) {
                personSelect.innerHTML = `<option>No existen personas cargadas...</option>`;
            } else {
                personSelect.innerHTML = `<option value="">Seleccione una persona...</option>` + 
                data.map(person => `<option value="${person.id}">${person.name} ${person.surname}</option>`).join("");
            }
        } catch (error) {
            console.error("Error al cargar las personas:", error);
        }
    }

    // Exponer la función loadPersons globalmente
    window.loadPersons = loadPersons;
}
});
