document.addEventListener("DOMContentLoaded", () => {
    const personForm = document.getElementById("person-form");

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
            // Verificar si la persona ya existe
            const checkResponse = await fetch(`http://127.0.0.1:8000/persons/persons/?email=${personData.email}`);
            const checkData = await checkResponse.json();

            if (checkData.length > 0) {
                document.getElementById("person-error").textContent = "La persona ya está registrada.";
                return;
            }

            const response = await fetch("http://127.0.0.1:8000/persons/persons/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(personData)
            });

            if (!response.ok) throw new Error("Error al registrar la persona");

            alert("Persona registrada con éxito");
            personForm.reset();
            document.getElementById("person-error").textContent = "";
        } catch (error) {
            document.getElementById("person-error").textContent = error.message;
        }
    });
});
