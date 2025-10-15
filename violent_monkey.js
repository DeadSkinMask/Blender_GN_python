// ==UserScript==
// @name         Descargar imágenes manga_pic
// @namespace    manga_downloader
// @version      2.0
// @description  Descarga todas las imágenes con clase "manga_pic" individualmente o en ZIP
// @match        *://*/*
// @grant        GM_xmlhttpRequest
// @grant        unsafeWindow
// ==/UserScript==

(function () {
    "use strict";

    let downloadedImages = [];

    // Función para verificar si existen imágenes manga_pic
    const checkAndShowButton = () => {
        const imgs = document.querySelectorAll("img.manga_pic");
        if (imgs.length > 0 && !document.getElementById('manga-download-btn')) {
            createButtons();
        }
    };

    // Crear botones flotantes
    const createButtons = () => {
        const container = document.createElement("div");
        container.id = 'manga-download-btn';
        Object.assign(container.style, {
            position: "fixed",
            bottom: "20px",
            right: "20px",
            zIndex: 999999,
            display: "flex",
            flexDirection: "column",
            gap: "10px",
        });

        // Botón principal de descarga
        const btnDownload = document.createElement("button");
        btnDownload.id = 'btn-download-images';
        btnDownload.textContent = "⬇️ Descargar imágenes";
        Object.assign(btnDownload.style, {
            background: "#2d2d2d",
            color: "white",
            border: "none",
            borderRadius: "8px",
            padding: "10px 16px",
            cursor: "pointer",
            fontSize: "14px",
            boxShadow: "0 2px 6px rgba(0,0,0,0.3)",
        });

        container.appendChild(btnDownload);
        document.body.appendChild(container);

        attachDownloadListener(btnDownload, container);
    };

    const fetchBlob = (url) => new Promise((resolve, reject) => {
        GM_xmlhttpRequest({
            url,
            responseType: "blob",
            timeout: 30000,
            onload: (res) => {
                if (res.status === 200 || res.status === 0) {
                    resolve(res.response);
                } else {
                    reject(new Error(`HTTP ${res.status}`));
                }
            },
            ontimeout: () => reject(new Error("Timeout")),
            onerror: reject,
        });
    });

    const downloadFile = (blob, filename) => {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        
        setTimeout(() => {
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }, 100);
    };

    const attachDownloadListener = (btn, container) => {
        btn.addEventListener("click", async () => {
            btn.disabled = true;
            btn.textContent = "⏳ Descargando...";

            const imgs = [...document.querySelectorAll("img.manga_pic")];
            if (!imgs.length) {
                alert("No se encontraron imágenes con clase 'manga_pic'");
                btn.disabled = false;
                btn.textContent = "⬇️ Descargar imágenes";
                return;
            }

            downloadedImages = [];
            let completed = 0;
            let success = 0;
            let failed = 0;

            for (let i = 0; i < imgs.length; i++) {
                const img = imgs[i];
                const url = img.currentSrc || img.src;
                const index = String(i + 1).padStart(3, "0");
                const ext = (url.split(".").pop().split("?")[0] || "jpg").toLowerCase();
                const name = `${index}.${["jpg","jpeg","png","webp","gif"].includes(ext) ? ext : "jpg"}`;

                btn.textContent = `📸 ${completed + 1}/${imgs.length}`;

                try {
                    const blob = await fetchBlob(url);
                    if (blob.size > 0) {
                        downloadedImages.push({ name, blob, url });
                        success++;
                        console.log(`✅ ${name} (${(blob.size/1024).toFixed(1)} KB)`);
                    } else {
                        failed++;
                        console.warn(`⚠️ ${name} está vacío (${url})`);
                    }
                } catch (err) {
                    failed++;
                    console.warn(`❌ Error en ${name}:`, err);
                }

                completed++;
                await new Promise(r => setTimeout(r, 100));
            }

            console.log(`--- Descarga completa ---`);
            console.log(`Total: ${imgs.length}, Exitosas: ${success}, Fallidas: ${failed}`);

            if (!success) {
                alert("No se descargó ninguna imagen válida.");
                btn.disabled = false;
                btn.textContent = "⬇️ Descargar imágenes";
                return;
            }

            btn.textContent = "✅ Listo!";

            // Crear botón de guardar ZIP
            if (!document.getElementById('btn-save-zip')) {
                const btnZip = document.createElement("button");
                btnZip.id = 'btn-save-zip';
                btnZip.textContent = "📦 Crear ZIP";
                Object.assign(btnZip.style, {
                    background: "#1a73e8",
                    color: "white",
                    border: "none",
                    borderRadius: "8px",
                    padding: "10px 16px",
                    cursor: "pointer",
                    fontSize: "14px",
                    boxShadow: "0 2px 6px rgba(0,0,0,0.3)",
                });
                container.appendChild(btnZip);
                attachZipListener(btnZip);
            }

            // Crear botón de descargar individuales
            if (!document.getElementById('btn-save-individual')) {
                const btnIndividual = document.createElement("button");
                btnIndividual.id = 'btn-save-individual';
                btnIndividual.textContent = "💾 Descargar c/u";
                Object.assign(btnIndividual.style, {
                    background: "#34a853",
                    color: "white",
                    border: "none",
                    borderRadius: "8px",
                    padding: "10px 16px",
                    cursor: "pointer",
                    fontSize: "14px",
                    boxShadow: "0 2px 6px rgba(0,0,0,0.3)",
                });
                container.appendChild(btnIndividual);
                attachIndividualListener(btnIndividual);
            }

            setTimeout(() => {
                btn.disabled = false;
                btn.textContent = "⬇️ Descargar imágenes";
            }, 2000);
        });
    };

    const attachZipListener = (btn) => {
        btn.addEventListener("click", async () => {
            if (!downloadedImages.length) {
                alert("Primero debes descargar las imágenes");
                return;
            }

            btn.disabled = true;
            btn.textContent = "📦 Creando ZIP...";

            // Cargar JSZip dinámicamente
            if (typeof JSZip === 'undefined') {
                const script = document.createElement('script');
                script.src = 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js';
                
                await new Promise((resolve, reject) => {
                    script.onload = resolve;
                    script.onerror = reject;
                    document.head.appendChild(script);
                });

                await new Promise(r => setTimeout(r, 500)); // Esperar que JSZip esté listo
            }

            try {
                const zip = new JSZip();
                const folder = zip.folder("manga");

                downloadedImages.forEach(({ name, blob }) => {
                    folder.file(name, blob);
                });

                console.log("Generando ZIP...");
                const zipBlob = await zip.generateAsync({
                    type: "blob",
                    compression: "STORE"
                });

                console.log(`✅ ZIP generado: ${(zipBlob.size/1024/1024).toFixed(2)} MB`);
                downloadFile(zipBlob, "manga_pics.zip");
                
                btn.textContent = "✅ ZIP guardado!";
                setTimeout(() => {
                    btn.textContent = "📦 Crear ZIP";
                    btn.disabled = false;
                }, 3000);

            } catch (err) {
                console.error("Error al crear ZIP:", err);
                alert("Error al crear ZIP: " + err.message);
                btn.textContent = "📦 Crear ZIP";
                btn.disabled = false;
            }
        });
    };

    const attachIndividualListener = (btn) => {
        btn.addEventListener("click", async () => {
            if (!downloadedImages.length) {
                alert("Primero debes descargar las imágenes");
                return;
            }

            btn.disabled = true;
            const originalText = btn.textContent;

            for (let i = 0; i < downloadedImages.length; i++) {
                const { name, blob } = downloadedImages[i];
                btn.textContent = `💾 ${i + 1}/${downloadedImages.length}`;
                downloadFile(blob, name);
                await new Promise(r => setTimeout(r, 300)); // Pausa entre descargas
            }

            btn.textContent = "✅ Todas guardadas!";
            setTimeout(() => {
                btn.textContent = originalText;
                btn.disabled = false;
            }, 3000);
        });
    };

    // Verificar al cargar la página
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', checkAndShowButton);
    } else {
        checkAndShowButton();
    }

    // Observer para detectar imágenes que se cargan dinámicamente
    const observer = new MutationObserver(() => {
        checkAndShowButton();
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
})();
