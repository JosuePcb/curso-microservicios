const submitFile = document.getElementById("submitFile");
const filePreview = document.getElementById("filePreview");
const fileThumb = document.getElementById("fileThumb");
const fileName = document.getElementById("fileName");
const removeFile = document.getElementById("removeFile");
const textarea = document.getElementById("request");

const enlace = "http://localhost:5500";

// CAMBIO MODO OSCURO/CLARO
const themeToggle = document.getElementById("themeToggle");
const themeIcon = themeToggle.querySelector("i");
const isLight = document.body.classList.contains("light-mode");

// Ajustar el tamaño del textarea

textarea.addEventListener("input", () => {
  textarea.style.height = "auto";
  textarea.style.height = textarea.scrollHeight + "px";
});

// File preview
submitFile.addEventListener("change", () => {
  const file = submitFile.files[0];
  if (!file) return;

  fileName.textContent = file.name;

  if (file.type.startsWith("image/")) {
    const reader = new FileReader();
    reader.onload = (e) => {
      fileThumb.src = e.target.result;
      fileThumb.style.display = "block";
    };
    reader.readAsDataURL(file);
  } else {
    // Para archivos no imagen muestra un ícono genérico
    fileThumb.src = "";
    fileThumb.style.display = "none";
  }

  filePreview.style.display = "block";
});

// Eliminar archivo
removeFile.addEventListener("click", () => {
  submitFile.value = "";
  filePreview.style.display = "none";
  fileThumb.src = "";
  fileName.textContent = "";
});

// CAMBIO MODO OSCURO/CLARO
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("light-mode");
  themeIcon.setAttribute("data-lucide", isLight ? "moon" : "sun");
  lucide.createIcons();
});

// Envio de datos
const generateBtn = document.getElementById("sendBtn");

generateBtn.addEventListener("click", async function (e) {
  // Prevenir que el form haga submit clásico
  e.preventDefault();

  const text = textarea.value.trim();

  if (!text) {
    alert("Por favor ingresa texto para continuar");
    return;
  }

  generateBtn.disabled = true;

  try {
    const response = await fetch(enlace + "/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: text }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || "Error al generar");
    }

    const data = await response.json();
    console.log("Respuesta:", data.response);
    // Aquí puedes mostrar data.response en el DOM
    alert(data.response);
  } catch (error) {
    alert("Error: " + error.message);
  } finally {
    generateBtn.disabled = false;
  }
});
