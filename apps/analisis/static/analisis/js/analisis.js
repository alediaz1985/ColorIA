console.log("JS de Color.IA cargado correctamente");

/**
 * Activa u oculta el formulario según la selección del usuario.
 * También enciende la cámara si se elige la opción "camara".
 */
function cambiarFormulario() {
    const tipo = document.querySelector('input[name="tipo_entrada"]:checked').value;
    const archivo = document.getElementById('form-archivo');
    const camara = document.getElementById('form-camara');

    if (tipo === "archivo") {
        archivo.style.display = 'block';
        camara.style.display = 'none';
    } else {
        archivo.style.display = 'none';
        camara.style.display = 'block';

        // Activar la cámara si aún no está activa
        const video = document.getElementById('video');
        if (video && !video.srcObject) {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(stream => {
                    video.srcObject = stream;
                })
                .catch(err => {
                    alert("No se pudo acceder a la cámara: " + err);
                });
        }
    }
}

/**
 * Captura una imagen del elemento <video> y la convierte a base64
 * para enviarla por el formulario oculto.
 */
function capturarImagen(videoId, canvasId, inputId) {
    const video = document.getElementById(videoId);
    const canvas = document.getElementById(canvasId);
    const input = document.getElementById(inputId);

    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const dataURL = canvas.toDataURL('image/jpeg');
    input.value = dataURL;
}

/**
 * Mejora visual del cuadro de color
 */
window.addEventListener("DOMContentLoaded", () => {
    cambiarFormulario();  // aplicar el estado inicial

    const colorBox = document.querySelector(".color-box");
    if (colorBox) {
        colorBox.style.border = "2px solid #444";
        colorBox.style.margin = "10px auto";
        colorBox.style.width = "100px";
        colorBox.style.height = "100px";
        colorBox.style.borderRadius = "8px";
        colorBox.style.boxShadow = "0 0 10px rgba(0, 0, 0, 0.3)";
    }
});
