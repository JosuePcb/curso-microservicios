const API_URL = "http://127.0.0.1:8000";

const submitFile   = document.getElementById("submitFile");
const filePreview  = document.getElementById("filePreview");
const fileThumb    = document.getElementById("fileThumb");
const fileNameEl   = document.getElementById("fileName");
const removeFileBtn = document.getElementById("removeFile");
const textarea     = document.getElementById("request");
const sendBtn      = document.getElementById("sendBtn");
const messagesEl   = document.getElementById("chat-container");
const mainEl       = document.getElementById("main");
const themeToggle  = document.getElementById("themeToggle");
const themeIcon    = themeToggle.querySelector("i");

// Historial de conversación
const conversationHistory = [];

// Contadores de tokens acumulados en la sesión
let sessionInputTokens  = 0;
let sessionOutputTokens = 0;
let sessionTotalTokens  = 0;

const tokenBar    = document.getElementById("token-bar");
const tokInput    = document.getElementById("tok-input");
const tokOutput   = document.getElementById("tok-output");
const tokTotal    = document.getElementById("tok-total");

// ===== Auto-resize textarea =====
textarea.addEventListener("input", () => {
  textarea.style.height = "auto";
  textarea.style.height = Math.min(textarea.scrollHeight, 120) + "px";
});

// Enter envía, Shift+Enter = nueva línea
textarea.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    handleSend();
  }
});

// ===== File preview =====
submitFile.addEventListener("change", () => {
  const file = submitFile.files[0];
  if (!file) return;

  fileNameEl.textContent = file.name;

  if (file.type.startsWith("image/")) {
    const reader = new FileReader();
    reader.onload = (e) => {
      fileThumb.src = e.target.result;
      fileThumb.style.display = "block";
    };
    reader.readAsDataURL(file);
  } else {
    fileThumb.style.display = "none";
  }

  filePreview.style.display = "block";
});

removeFileBtn.addEventListener("click", () => {
  submitFile.value = "";
  filePreview.style.display = "none";
  fileThumb.src = "";
  fileNameEl.textContent = "";
});

// ===== Tema =====
themeToggle.addEventListener("click", () => {
  const isLight = document.body.classList.toggle("light-mode");
  themeIcon.setAttribute("data-lucide", isLight ? "moon" : "sun");
  lucide.createIcons();
});

// ===== Envío =====
sendBtn.addEventListener("click", handleSend);

async function handleSend() {
  const text = textarea.value.trim();
  const file = submitFile.files[0];
  if (!text && !file) return;

  // Activar modo chat (título pequeño, input ancho)
  mainEl.classList.add("has-messages");
  messagesEl.style.display = "flex";

  // Mostrar mensaje del usuario
  const userImageSrc = file && file.type.startsWith("image/") ? fileThumb.src : null;
  addMessage("user", text, userImageSrc);

  // Limpiar input
  const sentText = text;
  const sentFile = file;
  textarea.value = "";
  textarea.style.height = "auto";
  submitFile.value = "";
  filePreview.style.display = "none";
  fileThumb.src = "";
  fileNameEl.textContent = "";

  sendBtn.disabled = true;
  const typingEl = addTypingIndicator();

  try {
    let data;

    if (sentFile) {
      const formData = new FormData();
      formData.append("text", sentText || "Describe esta imagen");
      formData.append("file", sentFile);

      const res = await fetch(`${API_URL}/generate-with-image`, {
        method: "POST",
        body: formData,
      });
      if (!res.ok) { const e = await res.json(); throw new Error(e.detail); }
      data = await res.json();

    } else {
      const res = await fetch(`${API_URL}/generate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: sentText, history: conversationHistory }),
      });
      const rawText = await res.text();
      console.log("Respuesta del servidor:", rawText);
      if (!res.ok) throw new Error("Error " + res.status + ": " + rawText);
      data = JSON.parse(rawText);
    }

    typingEl.remove();

    conversationHistory.push({ role: "user",  text: sentText });
    conversationHistory.push({ role: "model", text: data.response });

    // Actualizar tokens
    if (data.tokens) {
      sessionInputTokens  += data.tokens.input_tokens;
      sessionOutputTokens += data.tokens.output_tokens;
      sessionTotalTokens  += data.tokens.total_tokens;
      updateTokenBar(data.tokens.input_tokens, data.tokens.output_tokens);
    }

    addMessage("model", data.response);

  } catch (error) {
    typingEl.remove();
    addMessage("model", `⚠️ Error: ${error.message}`);
  } finally {
    sendBtn.disabled = false;
    textarea.focus();
  }
}

// ===== Helpers =====

function addMessage(role, text, imageSrc = null) {
  const wrapper = document.createElement("div");
  wrapper.className = `message ${role}`;

  const label = document.createElement("div");
  label.className = "message-label";
  label.textContent = role === "user" ? "Tú" : "Gemini";
  wrapper.appendChild(label);

  if (imageSrc) {
    const img = document.createElement("img");
    img.src = imageSrc;
    img.className = "message-image";
    wrapper.appendChild(img);
  }

  const bubble = document.createElement("div");
  bubble.className = "message-bubble";
  bubble.textContent = text;
  wrapper.appendChild(bubble);

  messagesEl.appendChild(wrapper);
  scrollToBottom();
}

function addTypingIndicator() {
  const wrapper = document.createElement("div");
  wrapper.className = "message model";

  const label = document.createElement("div");
  label.className = "message-label";
  label.textContent = "Gemini";
  wrapper.appendChild(label);

  const indicator = document.createElement("div");
  indicator.className = "typing-indicator";
  indicator.innerHTML = `
    <div class="typing-dot"></div>
    <div class="typing-dot"></div>
    <div class="typing-dot"></div>
  `;
  wrapper.appendChild(indicator);

  messagesEl.appendChild(wrapper);
  scrollToBottom();
  return wrapper;
}

function scrollToBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}


// ===== Token bar =====
function updateTokenBar(inputToks, outputToks) {
  tokenBar.style.display = "flex";
  tokInput.textContent  = inputToks.toLocaleString();
  tokOutput.textContent = outputToks.toLocaleString();
  tokTotal.textContent  = sessionTotalTokens.toLocaleString();
  lucide.createIcons();
}