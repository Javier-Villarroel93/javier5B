link :

https://javier5b.onrender.com/

# Taller DevOps - Docker con GitHub Actions

**Autor:** Javier  
**Versión:** 1.0.1  
**Método:** GitHub Actions (CI/CD Automatizado)

## 📋 Descripción

Taller práctico de DevOps que incluye:
- Aplicación Flask
- Dockerfile
- GitHub Actions para CI/CD automatizado
- **NO requiere Docker instalado localmente**
- Build y deploy automático en la nube

---

## 🎯 Ventajas de usar GitHub Actions

✅ No necesitas Docker instalado en tu PC  
✅ Build automático en la nube  
✅ CI/CD completamente automatizado  
✅ Historial de builds  
✅ Deploy automático a Docker Hub  

---

## 🚀 PASO A PASO COMPLETO

### **📦 PASO 1: Crear Repositorio en GitHub**

1. Ve a **https://github.com** e inicia sesión
2. Haz clic en **"New repository"** (botón verde)
3. Configura:
   - **Repository name:** `taller-devops-javier`
   - **Description:** `Taller DevOps con Docker y GitHub Actions`
   - **Visibility:** Público o Privado (tu elección)
   - ✅ Marca **"Add a README file"**
4. Haz clic en **"Create repository"**

---

### **🌿 PASO 2: Subir el código al repositorio**

Opción A - **Usando Visual Studio Code (Recomendado):**

```bash
# Abre la terminal en VS Code (Ctrl + `)
cd C:\Users\yavirac12\Desktop\taller-devops-javier

# Inicializar Git
git init

# Configurar usuario
git config user.name "Javier"
git config user.email "tu-email@ejemplo.com"

# Crear rama javier
git checkout -b javier

# Agregar archivos
git add .

# Hacer commit
git commit -m "Initial commit - Taller DevOps con GitHub Actions"

# Conectar con GitHub (REEMPLAZA 'tu-usuario' con tu usuario de GitHub)
git remote add origin https://github.com/tu-usuario/taller-devops-javier.git

# Subir código
git push -u origin javier
```

Opción B - **Usando GitHub Web:**

1. En tu repositorio, haz clic en **"Add file" → "Upload files"**
2. Arrastra todos los archivos del taller
3. Cambia a la rama **"javier"** (crear si no existe)
4. Haz clic en **"Commit changes"**

---

### **🔐 PASO 3: Configurar Secrets en GitHub**

Para que GitHub Actions pueda publicar tu imagen en Docker Hub:

1. **Crea una cuenta en Docker Hub** (si no tienes):
   - Ve a **https://hub.docker.com/signup**
   - Regístrate gratis

2. **En tu repositorio de GitHub:**
   - Ve a **Settings → Secrets and variables → Actions**
   - Haz clic en **"New repository secret"**
   
3. **Agrega estos dos secrets:**

   **Secret 1:**
   - Name: `DOCKER_USERNAME`
   - Secret: `tu-usuario-de-dockerhub`
   
   **Secret 2:**
   - Name: `DOCKER_PASSWORD`
   - Secret: `tu-contraseña-de-dockerhub`

---

### **🚢 PASO 4: Activar GitHub Actions**

1. En tu repositorio, ve a la pestaña **"Actions"**
2. Si te pide habilitar workflows, haz clic en **"I understand my workflows, go ahead and enable them"**
3. Verás el workflow **"DevOps Docker CI/CD - Javier"**

---

### **▶️ PASO 5: Ejecutar el Workflow**

**Método 1 - Push automático:**
```bash
# Haz cualquier cambio y haz push
git add .
git commit -m "Trigger GitHub Actions"
git push origin javier
```

**Método 2 - Manual desde GitHub:**
1. Ve a **Actions → DevOps Docker CI/CD - Javier**
2. Haz clic en **"Run workflow"**
3. Selecciona la rama **"javier"**
4. Haz clic en **"Run workflow"**

---

### **✅ PASO 6: Verificar el Build**

1. Ve a la pestaña **"Actions"**
2. Verás el workflow ejecutándose (ícono amarillo 🟡)
3. Haz clic en el workflow para ver los detalles
4. Cuando termine exitosamente verás un check verde ✅

**El workflow automáticamente:**
- ✅ Construye la imagen `javier:1.0.1`
- ✅ Ejecuta tests
- ✅ Publica en Docker Hub
- ✅ Verifica que funciona

---

### **🐳 PASO 7: Ver tu imagen en Docker Hub**

1. Ve a **https://hub.docker.com**
2. Inicia sesión
3. Verás tu imagen **`tu-usuario/javier:1.0.1`**

---

## 📊 Estructura del Proyecto

```
taller-devops-javier/
├── .github/
│   └── workflows/
│       └── docker-cicd.yml    # ⭐ GitHub Actions workflow
├── app.py                      # Aplicación Flask
├── Dockerfile                  # Configuración Docker
├── docker-compose.yml          # (Opcional, para local)
├── requirements.txt            # Dependencias Python
├── .gitignore                 # Exclusiones Git
└── README.md                  # Esta documentación
```

---

## 🎓 Lo que GitHub Actions hace por ti

```yaml
1. Checkout del código ✅
2. Configura Python ✅
3. Instala dependencias ✅
4. Ejecuta tests ✅
5. Login a Docker Hub ✅
6. Construye imagen Docker ✅
7. Publica en Docker Hub ✅
8. Verifica funcionamiento ✅
```

---

## 🔄 Flujo de Trabajo

```
┌─────────────────┐
│  Haces cambios  │
│   en el código  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   git push      │
│  a rama javier  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ GitHub Actions  │
│  se activa      │
│  automáticamente│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Build Docker   │
│  en la nube     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Imagen lista   │
│  en Docker Hub  │
└─────────────────┘
```

---

## 💻 Comandos Git Útiles

```bash
# Ver estado
git status

# Ver ramas
git branch

# Cambiar de rama
git checkout javier

# Ver historial
git log --oneline

# Hacer cambios y subirlos
git add .
git commit -m "Descripción del cambio"
git push origin javier
```

---

## 🔍 Ver logs de GitHub Actions

1. Ve a **Actions** en tu repositorio
2. Haz clic en cualquier workflow ejecutado
3. Haz clic en cada paso para ver detalles
4. Revisa errores si algo falla

---

## 🛠️ Solución de Problemas

**❌ Error: "Docker login failed"**
→ Verifica que los secrets DOCKER_USERNAME y DOCKER_PASSWORD estén correctos

**❌ Error: "Permission denied"**
→ Verifica que tu token de Docker Hub tenga permisos de escritura

**❌ Error: "Image not found"**
→ Asegúrate de que el Dockerfile esté en la raíz del proyecto

**❌ Error: "Workflow no se activa"**
→ Verifica que el archivo esté en `.github/workflows/`

---

## 📝 Checklist del Taller

- [ ] Crear repositorio en GitHub
- [ ] Subir código a rama `javier`
- [ ] Crear cuenta en Docker Hub
- [ ] Configurar secrets (DOCKER_USERNAME y DOCKER_PASSWORD)
- [ ] Activar GitHub Actions
- [ ] Hacer push para ejecutar workflow
- [ ] Verificar build exitoso (✅ verde)
- [ ] Verificar imagen en Docker Hub

---

## 🎉 Resumen del Taller

✅ **Repositorio Git:** `taller-devops-javier`  
✅ **Rama:** `javier`  
✅ **Imagen Docker:** `javier:1.0.1`  
✅ **CI/CD:** GitHub Actions  
✅ **Registry:** Docker Hub  
✅ **Sin Docker local:** Todo en la nube ☁️

---

## 🚀 Próximos Pasos

1. Modifica `app.py` (cambia el mensaje)
2. Haz commit y push
3. GitHub Actions automáticamente:
   - Construirá nueva imagen
   - La publicará en Docker Hub
4. ¡DevOps automatizado! 🎊

---

## 📚 Recursos Adicionales

- **GitHub Actions:** https://docs.github.com/en/actions
- **Docker Hub:** https://hub.docker.com
- **Flask:** https://flask.palletsprojects.com
- **Git:** https://git-scm.com/doc

---

**¡Felicidades! Has completado el taller DevOps con GitHub Actions** 🎓✨

*No necesitas Docker en tu PC, todo el proceso de CI/CD ocurre en la nube de GitHub.*
