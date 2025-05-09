
console.log("Color.IA JS cargado correctamente");

window.onload = () => {
    const colorBox = document.querySelector("div[style*='background-color']");
    if (colorBox) {
        colorBox.style.border = "2px solid #444";
    }
};
