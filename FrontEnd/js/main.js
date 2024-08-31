document.addEventListener("DOMContentLoaded", () => {
    // Inicialmente mostrar la pantalla de registro de personas
    showScreen("person-registration");

    // Navegación entre pantallas
    document.getElementById("show-person-registration").addEventListener("click", () => {
        showScreen("person-registration");
    });

    document.getElementById("show-career-registration").addEventListener("click", () => {
        showScreen("career-registration");
    });

    document.getElementById("show-subject-registration").addEventListener("click", () => {
        showScreen("subject-registration");
    });

    document.getElementById("show-create-career").addEventListener("click", () => {
        showScreen("create-career");
    });

    document.getElementById("show-create-subject").addEventListener("click", () => {
        showScreen("create-subject");
    });
});

function showScreen(screenId) {
    const screens = document.querySelectorAll(".screen");
    screens.forEach(screen => {
        screen.style.display = "none";
    });
    document.getElementById(screenId).style.display = "block";
}
