const submitFile = document.getElementById('submitFile');
const filePreview = document.getElementById('filePreview');
const fileThumb = document.getElementById('fileThumb');
const fileName = document.getElementById('fileName');
const removeFile = document.getElementById('removeFile');
const textarea = document.getElementById('request');

// CAMBIO MODO OSCURO/CLARO
const themeToggle = document.getElementById('themeToggle');
const themeIcon = themeToggle.querySelector('i');
const isLight = document.body.classList.contains('light-mode');

// Ajustar el tamaño del textarea

textarea.addEventListener('input', () => {
    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight + 'px';
});



// File preview
submitFile.addEventListener('change', () => {
    const file = submitFile.files[0];
    if (!file) return;

    fileName.textContent = file.name;

    if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = (e) => {
            fileThumb.src = e.target.result;
            fileThumb.style.display = 'block';
        };
        reader.readAsDataURL(file);
    } else {
        // Para archivos no imagen muestra un ícono genérico
        fileThumb.src = '';
        fileThumb.style.display = 'none';
    }

    filePreview.style.display = 'block';
});

// Eliminar archivo
removeFile.addEventListener('click', () => {
    submitFile.value = '';
    filePreview.style.display = 'none';
    fileThumb.src = '';
    fileName.textContent = '';
});

// CAMBIO MODO OSCURO/CLARO
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('light-mode');
    themeIcon.setAttribute('data-lucide', isLight ? 'moon' : 'sun');
    lucide.createIcons();
});