# Funcionamiento del chatbot

## ⚙️ Requisitos

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (gestor de paquetes)
- API Key de Google Gemini → [aistudio.google.com](https://aistudio.google.com)
- Live Server (extensión de VS Code) para el frontend


## 🚀 Instalación y configuración

### 1. Instalar dependencias

```bash
uv sync
```

### 2. Configurar la API Key

Crea un archivo `.env` en la raíz del proyecto (junto a `pyproject.toml`):

```env
GEMINI_API_KEY=tu_api_key_aqui
```

### 3. Iniciar el backend

```bash
# Desde la raíz del proyecto
uv run uvicorn Chatbot.src.main:app --reload
```

El servidor queda disponible en: `http://127.0.0.1:8000`

Puedes verificar que funciona abriendo: `http://127.0.0.1:8000/docs`

### 4. Iniciar el frontend

Abre `Static/index.html` con **Live Server** en VS Code.

> Click derecho sobre `index.html` → **Open with Live Server**

El frontend queda disponible en: `http://127.0.0.1:5500`

## 🛠️ Modelo usado

```
gemini-2.5-flash
```

## ⚠️ Notas

- La API Key nunca debe subirse al repositorio. Asegúrate de tener `.env` en tu `.gitignore`.
- El historial de conversación se guarda en memoria y se pierde al recargar la página.
- La cuota gratuita de Gemini puede agotarse. Si recibes error 429, espera unos minutos o cambia a otro modelo.