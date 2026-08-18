/**
 * All-in-One Utility Hub Frontend Script
 */

document.addEventListener('DOMContentLoaded', () => {
    try { initDashboardSearchAndFilter(); } catch (e) { console.error('Dashboard init error:', e); }
    try { initGlobalSearch(); } catch (e) { console.error('Global search init error:', e); }
    try { initDropzoneAndFileUpload(); } catch (e) { console.error('Dropzone init error:', e); }
    try { initToolFormSubmission(); } catch (e) { console.error('Form submission init error:', e); }
    try { initLiveTextWatchers(); } catch (e) { console.error('Live watchers init error:', e); }
    try { lucide.createIcons(); } catch (e) { console.error('Lucide icons error:', e); }
});

/* =========================================================================
   1. Dashboard Search & Category Filtering
   ========================================================================= */
function initDashboardSearchAndFilter() {
    const searchInput = document.getElementById('dashboard-search-input');
    const filterBtns = document.querySelectorAll('.cat-filter-btn');
    
    if (searchInput) {
        searchInput.addEventListener('input', () => filterDashboardTools());
    }

    if (filterBtns && filterBtns.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                filterBtns.forEach(b => {
                    b.classList.remove('bg-slate-900', 'text-white', 'shadow-sm');
                    b.classList.add('text-slate-600', 'hover:text-slate-900', 'hover:bg-slate-100');
                });
                btn.classList.add('bg-slate-900', 'text-white', 'shadow-sm');
                btn.classList.remove('text-slate-600', 'hover:text-slate-900', 'hover:bg-slate-100');

                filterDashboardTools(btn.getAttribute('data-category'));
            });
        });
    }
}

function filterDashboardTools(selectedCat = null) {
    const searchInput = document.getElementById('dashboard-search-input');
    const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
    
    if (!selectedCat) {
        const activeBtn = document.querySelector('.cat-filter-btn.bg-slate-900');
        selectedCat = activeBtn ? activeBtn.getAttribute('data-category') : 'all';
    }

    const cards = document.querySelectorAll('.tool-card');
    const noResults = document.getElementById('no-tools-found');
    let visibleCount = 0;

    cards.forEach(card => {
        const cat = card.getAttribute('data-category');
        const name = card.getAttribute('data-name');
        const desc = card.getAttribute('data-desc');

        const matchesCat = (selectedCat === 'all' || cat === selectedCat);
        const matchesQuery = (!query || name.includes(query) || desc.includes(query));

        if (matchesCat && matchesQuery) {
            card.classList.remove('hidden');
            visibleCount++;
        } else {
            card.classList.add('hidden');
        }
    });

    if (noResults) {
        if (visibleCount === 0) {
            noResults.classList.remove('hidden');
        } else {
            noResults.classList.add('hidden');
        }
    }
}

/* =========================================================================
   2. Global Navigation Search & Shortcuts
   ========================================================================= */
function initGlobalSearch() {
    const globalSearch = document.getElementById('global-tool-search');
    
    window.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
            e.preventDefault();
            if (globalSearch) globalSearch.focus();
        }
    });

    if (globalSearch) {
        globalSearch.addEventListener('input', (e) => {
            const val = e.target.value;
            const dashboardInput = document.getElementById('dashboard-search-input');
            if (dashboardInput) {
                dashboardInput.value = val;
                filterDashboardTools();
            } else {
                if (e.key === 'Enter' && val) {
                    window.location.href = `/?search=${encodeURIComponent(val)}`;
                }
            }
        });
    }

    const urlParams = new URLSearchParams(window.location.search);
    const searchParam = urlParams.get('search');
    if (searchParam && document.getElementById('dashboard-search-input')) {
        document.getElementById('dashboard-search-input').value = searchParam;
        filterDashboardTools();
    }
}

/* =========================================================================
   3. Drag & Drop File Upload Handling
   ========================================================================= */
function initDropzoneAndFileUpload() {
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('file-input');

    if (!dropzone || !fileInput) return;

    ['dragenter', 'dragover'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.add('dropzone-active');
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.remove('dropzone-active');
        }, false);
    });

    dropzone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files && files.length > 0) {
            fileInput.files = files;
            handleFilesSelected(files);
        }
    });

    fileInput.addEventListener('change', () => {
        if (fileInput.files && fileInput.files.length > 0) {
            handleFilesSelected(fileInput.files);
        }
    });
}

function handleFilesSelected(files) {
    const defaultContent = document.getElementById('dropzone-default-content');
    const previewContainer = document.getElementById('dropzone-file-preview');
    const fileListPreview = document.getElementById('file-list-preview');
    const imgPreviewContainer = document.getElementById('image-thumbnail-preview');
    const imgPreviewTag = document.getElementById('preview-img-tag');

    if (!previewContainer || !fileListPreview) return;

    defaultContent.classList.add('hidden');
    previewContainer.classList.remove('hidden');
    fileListPreview.innerHTML = '';
    imgPreviewContainer.classList.add('hidden');

    Array.from(files).forEach((file, idx) => {
        const badge = document.createElement('div');
        badge.className = 'inline-flex items-center gap-2 px-3 py-1.5 rounded-xl bg-white border border-slate-200 text-xs font-semibold text-slate-700 shadow-sm';
        
        const sizeFormatted = formatFileSize(file.size);
        badge.innerHTML = `
            <span class="w-2 h-2 rounded-full bg-teal-500"></span>
            <span class="max-w-[160px] truncate" title="${file.name}">${file.name}</span>
            <span class="text-[10px] text-slate-400 font-mono">(${sizeFormatted})</span>
        `;
        fileListPreview.appendChild(badge);

        if (idx === 0 && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imgPreviewTag.src = e.target.result;
                imgPreviewContainer.classList.remove('hidden');
                imgPreviewContainer.classList.add('flex');
            };
            reader.readAsDataURL(file);
        }
    });
}

function formatFileSize(bytes) {
    if (!bytes || bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
}

/* =========================================================================
   4. Client-side Instant Text Engine (0ms Zero Latency Transform)
   ========================================================================= */
function transformTextClientSide(toolId, form) {
    if (toolId === 'case-converter') {
        const input = form.querySelector('[name="text_input"]')?.value ?? '';
        const style = form.querySelector('[name="case_style"]')?.value ?? 'title';
        if (!input) return '';

        if (style === 'upper') return input.toUpperCase();
        if (style === 'lower') return input.toLowerCase();
        if (style === 'title') {
            return input.toLowerCase().replace(/(?:^|\s|\b)\w/g, c => c.toUpperCase());
        }
        if (style === 'snake') {
            return input.trim().replace(/[\s\-]+/g, '_').toLowerCase();
        }
        if (style === 'kebab') {
            return input.trim().replace(/[\s\_]+/g, '-').toLowerCase();
        }
        if (style === 'camel') {
            const words = input.trim().split(/[\s\_\-]+/);
            return words[0].toLowerCase() + words.slice(1).map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join('');
        }
        if (style === 'pascal') {
            const words = input.trim().split(/[\s\_\-]+/);
            return words.map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join('');
        }
        return input;
    } 
    
    if (toolId === 'url-encoder-decoder') {
        const mode = form.querySelector('[name="url_mode"]')?.value ?? 'encode';
        const input = form.querySelector('[name="url_input"]')?.value ?? '';
        if (!input) return '';

        if (mode === 'encode') {
            return encodeURIComponent(input);
        } else {
            try { return decodeURIComponent(input); } catch (e) { return input; }
        }
    } 
    
    if (toolId === 'base64-codec') {
        const hasFile = form.querySelector('#file-input')?.files?.length > 0;
        if (hasFile) return null; // let server handle binary file

        const mode = form.querySelector('[name="codec_mode"]')?.value ?? 'encode';
        const input = form.querySelector('[name="input_text"]')?.value ?? '';
        if (!input) return '';

        if (mode === 'encode') {
            try { return btoa(unescape(encodeURIComponent(input))); } catch (e) { return null; }
        } else {
            try { return decodeURIComponent(escape(atob(input))); } catch (e) { return null; }
        }
    }

    return null;
}

/* =========================================================================
   5. Tool Form Submission & Interactive AJAX Result Rendering
   ========================================================================= */
function initToolFormSubmission() {
    const form = document.getElementById('tool-process-form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        e.stopPropagation();
        await executeToolProcessing(form);
    });
}

window.submitToolForm = async function(e) {
    if (e) {
        e.preventDefault();
        e.stopPropagation();
    }
    const form = document.getElementById('tool-process-form');
    if (form) {
        await executeToolProcessing(form);
    }
};

async function executeToolProcessing(form) {
    if (!form) return;

    const toolId = form.getAttribute('data-tool-id') || (typeof TOOL_ID !== 'undefined' ? TOOL_ID : '');
    const isTextTool = form.getAttribute('data-is-text-tool') === 'true';
    const isDirectInput = form.getAttribute('data-is-direct-input') === 'true';
    const fileInput = document.getElementById('file-input');

    // Client-side quick check
    if (fileInput && !fileInput.files.length && !isDirectInput) {
        const textareas = form.querySelectorAll('textarea, input[type="text"]');
        let hasText = false;
        textareas.forEach(t => { if (t.value.trim().length > 0) hasText = true; });

        if (!hasText) {
            alert('Please enter text or choose a file before processing.');
            return;
        }
    }

    const workspace = document.getElementById('tool-workspace');
    const processingState = document.getElementById('processing-state');
    const resultCard = document.getElementById('result-card');
    const submitBtn = document.getElementById('submit-btn');
    const submitBtnText = document.getElementById('submit-btn-text');
    const origText = submitBtnText ? (submitBtnText.getAttribute('data-original-text') || submitBtnText.textContent) : "Process";

    // 1. Instant client-side execution for pure text transformations (0ms response)
    const localResult = transformTextClientSide(toolId, form);
    if (localResult !== null && localResult !== undefined) {
        renderInlineTextResult({ text_content: localResult });
    }

    // 2. Manage loading UI state
    if (isTextTool) {
        if (submitBtn) submitBtn.disabled = true;
        if (submitBtnText) submitBtnText.textContent = "Processing...";
    } else {
        if (workspace) workspace.classList.add('hidden');
        if (processingState) processingState.classList.remove('hidden');
        if (resultCard) resultCard.classList.add('hidden');
    }

    try {
        const formData = new FormData(form);
        const actionUrl = form.getAttribute('action') || `/process/${toolId}`;

        const response = await fetch(actionUrl, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        });

        const data = await response.json();

        if (data.success) {
            // Always display text in inline output box if text_content is present
            if (data.text_content !== undefined && data.text_content !== null) {
                renderInlineTextResult(data);
            }
            
            // For non-text tools or when extra cards/previews are present
            if (!isTextTool || data.preview_type !== 'text') {
                renderToolSuccessResult(data);
            }
        } else {
            alert(data.error || 'An error occurred while processing your request.');
            resetToolWorkspace();
        }
    } catch (err) {
        console.error('Processing request error:', err);
        if (localResult === null) {
            alert('A network error occurred while processing your request. Please try again.');
            resetToolWorkspace();
        }
    } finally {
        if (isTextTool) {
            if (submitBtn) submitBtn.disabled = false;
            if (submitBtnText) submitBtnText.textContent = origText;
        } else {
            if (processingState) processingState.classList.add('hidden');
        }
        lucide.createIcons();
    }
}

/* =========================================================================
   6. Dedicated On-Page Text Result Handler
   ========================================================================= */
function renderInlineTextResult(data) {
    const inlineBox = document.getElementById('inline-text-result-box');
    const inlineOutput = document.getElementById('inline-text-output');
    const inlineStats = document.getElementById('inline-text-stats');
    const inlineDownload = document.getElementById('inline-download-link');

    if (!inlineBox || !inlineOutput) return;

    const text = data.text_content !== undefined ? String(data.text_content) : '';
    inlineOutput.value = text;
    
    // Compute character and word statistics
    const charCount = text.length;
    const wordCount = text.trim() ? text.trim().split(/\s+/).length : 0;
    if (inlineStats) {
        inlineStats.textContent = `${charCount} chars | ${wordCount} words`;
    }

    if (data.download_url && inlineDownload) {
        inlineDownload.href = data.download_url;
        inlineDownload.setAttribute('download', data.filename || 'result.txt');
        inlineDownload.classList.remove('hidden');
    }

    inlineBox.classList.remove('hidden');
    inlineBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    lucide.createIcons();
}

function copyInlineResult() {
    const outputEl = document.getElementById('inline-text-output');
    if (!outputEl) return;

    navigator.clipboard.writeText(outputEl.value).then(() => {
        const copyText = document.getElementById('inline-copy-text');
        if (copyText) {
            const orig = copyText.textContent;
            copyText.textContent = "Copied!";
            setTimeout(() => { copyText.textContent = orig; }, 2000);
        }
        showToast('Text copied to clipboard!');
    }).catch(err => {
        console.error('Copy failed: ', err);
        // Fallback selection copy
        outputEl.select();
        document.execCommand('copy');
        showToast('Text copied to clipboard!');
    });
}

function swapInputWithOutput() {
    const outputEl = document.getElementById('inline-text-output');
    const primaryInput = document.querySelector('.primary-text-input');
    
    if (outputEl && primaryInput) {
        primaryInput.value = outputEl.value;
        showToast('Output moved to input!');
        primaryInput.focus();
        
        // Trigger live transform for instant update
        const form = document.getElementById('tool-process-form');
        const toolId = form?.getAttribute('data-tool-id');
        if (toolId && form) {
            const localResult = transformTextClientSide(toolId, form);
            if (localResult !== null) {
                renderInlineTextResult({ text_content: localResult });
            }
        }
    }
}

function clearPrimaryInput() {
    const primaryInput = document.querySelector('.primary-text-input');
    const inlineBox = document.getElementById('inline-text-result-box');
    const fileInput = document.getElementById('file-input');

    if (primaryInput) primaryInput.value = '';
    if (fileInput) fileInput.value = '';
    if (inlineBox) inlineBox.classList.add('hidden');
    
    const previewContainer = document.getElementById('dropzone-file-preview');
    const defaultContent = document.getElementById('dropzone-default-content');
    if (previewContainer) previewContainer.classList.add('hidden');
    if (defaultContent) defaultContent.classList.remove('hidden');
}

/* =========================================================================
   7. Live Options Watchers (Auto-update for Selectors & Text Inputs)
   ========================================================================= */
function initLiveTextWatchers() {
    const selects = document.querySelectorAll('.tool-option-select');
    const primaryInput = document.querySelector('.primary-text-input');
    const form = document.getElementById('tool-process-form');

    if (!form) return;
    const toolId = form.getAttribute('data-tool-id');

    if (selects) {
        selects.forEach(sel => {
            sel.addEventListener('change', () => {
                if (primaryInput && primaryInput.value.trim().length > 0) {
                    const localRes = transformTextClientSide(toolId, form);
                    if (localRes !== null) {
                        renderInlineTextResult({ text_content: localRes });
                    } else {
                        executeToolProcessing(form);
                    }
                }
            });
        });
    }

    if (primaryInput && toolId in {'case-converter': 1, 'url-encoder-decoder': 1, 'base64-codec': 1}) {
        primaryInput.addEventListener('input', () => {
            if (primaryInput.value.trim().length > 0) {
                const localRes = transformTextClientSide(toolId, form);
                if (localRes !== null) {
                    renderInlineTextResult({ text_content: localRes });
                }
            }
        });
    }
}

/* =========================================================================
   8. Card Result Renderer (for Files, Images, Palettes, Hashes & Diff)
   ========================================================================= */
function renderToolSuccessResult(data) {
    const resultCard = document.getElementById('result-card');
    const resultFilename = document.getElementById('result-filename');
    const resultFilesize = document.getElementById('result-filesize');
    const resultDownloadBtn = document.getElementById('result-download-btn');
    const downloadSummaryBar = document.getElementById('download-summary-bar');
    const customPreview = document.getElementById('result-custom-preview');

    if (!resultCard) return;

    if (resultFilename) resultFilename.textContent = data.filename || 'output_file';
    if (resultFilesize) resultFilesize.textContent = data.filesize ? `File size: ${formatFileSize(data.filesize)}` : '';
    
    if (data.download_url && resultDownloadBtn) {
        resultDownloadBtn.href = data.download_url;
        resultDownloadBtn.setAttribute('download', data.filename || 'download');
        if (downloadSummaryBar) downloadSummaryBar.classList.remove('hidden');
    } else {
        if (downloadSummaryBar) downloadSummaryBar.classList.add('hidden');
    }

    if (customPreview) {
        customPreview.innerHTML = '';
        customPreview.classList.add('hidden');

        // 1. Image Preview
        if (data.preview_type === 'image' && data.preview_data) {
            customPreview.innerHTML = `
                <div class="text-center p-4 bg-slate-50 rounded-2xl border border-slate-200">
                    <p class="text-xs font-bold text-slate-500 uppercase tracking-wider mb-3">Live Output Preview</p>
                    <img src="${data.preview_data}" alt="Processed Output" class="max-h-80 mx-auto rounded-xl shadow-md border border-slate-200 object-contain">
                </div>
            `;
            customPreview.classList.remove('hidden');
        }

        // 2. Color Palette Swatches
        else if (data.preview_type === 'palette' && data.colors) {
            let swatchesHtml = data.colors.map(c => `
                <div class="palette-swatch p-3 rounded-2xl border border-slate-200 bg-white text-center shadow-sm cursor-pointer hover:shadow-md transition-all" onclick="copyToClipboard('${c.hex}', 'Color ${c.hex} copied!')">
                    <div class="w-full h-16 rounded-xl mb-2 shadow-inner" style="background-color: ${c.hex};"></div>
                    <p class="text-xs font-bold text-slate-800 font-mono">${c.hex}</p>
                    <p class="text-[10px] text-slate-400 font-mono">${c.rgb}</p>
                </div>
            `).join('');

            customPreview.innerHTML = `
                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <p class="text-xs font-bold text-slate-700 uppercase tracking-wider">Extracted Dominant Color Swatches (Click to copy)</p>
                        <span class="text-[11px] text-slate-400">HEX / RGB</span>
                    </div>
                    <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-3">
                        ${swatchesHtml}
                    </div>
                </div>
            `;
            customPreview.classList.remove('hidden');
        }

        // 3. Cryptographic Hashes Table
        else if (data.preview_type === 'hashes' && data.hashes) {
            let rowsHtml = Object.entries(data.hashes).map(([algo, hash]) => `
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 p-3 rounded-xl bg-white border border-slate-200">
                    <span class="text-xs font-bold uppercase tracking-wider text-slate-500 sm:w-24">${algo}</span>
                    <span class="text-xs font-mono text-slate-800 break-all flex-grow">${hash}</span>
                    <button onclick="copyToClipboard('${hash}', '${algo} checksum copied!')" class="px-2.5 py-1 text-[11px] font-semibold text-teal-600 bg-teal-50 hover:bg-teal-100 rounded-lg transition-colors flex items-center gap-1 self-end sm:self-auto">
                        <i data-lucide="copy" class="w-3 h-3"></i> Copy
                    </button>
                </div>
            `).join('');

            customPreview.innerHTML = `
                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
                    <p class="text-xs font-bold text-slate-700 uppercase tracking-wider">Cryptographic Checksum Hashes</p>
                    <div class="space-y-2">
                        ${rowsHtml}
                    </div>
                </div>
            `;
            customPreview.classList.remove('hidden');
        }

        // 4. Text Diff Results
        else if (data.preview_type === 'diff' && data.diff_lines) {
            let diffRowsHtml = data.diff_lines.map(line => {
                let cls = 'text-slate-700 bg-white';
                if (line.startsWith('+')) cls = 'diff-add';
                else if (line.startsWith('-')) cls = 'diff-del';
                else if (line.startsWith('@@')) cls = 'bg-blue-50 text-blue-700 font-bold';
                return `<div class="px-3 py-1 font-mono text-xs ${cls}">${escapeHtml(line)}</div>`;
            }).join('');

            customPreview.innerHTML = `
                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
                    <p class="text-xs font-bold text-slate-700 uppercase tracking-wider">Visual Text Diff Output</p>
                    <div class="rounded-xl border border-slate-200 overflow-x-auto max-h-96 divide-y divide-slate-100">
                        ${diffRowsHtml}
                    </div>
                </div>
            `;
            customPreview.classList.remove('hidden');
        }

        // 5. Code / Structured Text Box
        else if (data.preview_type === 'text' && data.text_content) {
            customPreview.innerHTML = `
                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <p class="text-xs font-bold text-slate-700 uppercase tracking-wider">Result Output</p>
                        <button onclick="copyToClipboard(document.getElementById('text-output-raw').value, 'Text copied to clipboard!')" class="px-3 py-1 text-xs font-semibold text-teal-600 bg-teal-50 hover:bg-teal-100 rounded-lg transition-colors flex items-center gap-1">
                            <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Text
                        </button>
                    </div>
                    <textarea id="text-output-raw" readonly rows="8" class="utility-output-box w-full text-xs sm:text-sm font-mono bg-slate-900 text-white border border-slate-700 rounded-xl p-3 focus:outline-none leading-relaxed">${escapeHtml(data.text_content)}</textarea>
                </div>
            `;
            customPreview.classList.remove('hidden');
        }
    }

    resultCard.classList.remove('hidden');
    lucide.createIcons();
}

function resetToolWorkspace() {
    const workspace = document.getElementById('tool-workspace');
    const processingState = document.getElementById('processing-state');
    const resultCard = document.getElementById('result-card');
    const fileInput = document.getElementById('file-input');
    const defaultContent = document.getElementById('dropzone-default-content');
    const previewContainer = document.getElementById('dropzone-file-preview');
    const inlineBox = document.getElementById('inline-text-result-box');

    if (fileInput) fileInput.value = '';
    if (defaultContent) defaultContent.classList.remove('hidden');
    if (previewContainer) previewContainer.classList.add('hidden');
    if (inlineBox) inlineBox.classList.add('hidden');

    if (processingState) processingState.classList.add('hidden');
    if (resultCard) resultCard.classList.add('hidden');
    if (workspace) workspace.classList.remove('hidden');
    lucide.createIcons();
}

function copyToClipboard(text, msg = 'Copied!') {
    navigator.clipboard.writeText(text).then(() => {
        showToast(msg);
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}

function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'fixed bottom-6 right-6 z-50 bg-slate-900 text-white px-4 py-2.5 rounded-xl shadow-lg text-xs font-semibold flex items-center gap-2 animate-fadeIn';
    toast.innerHTML = `<i data-lucide="check" class="w-4 h-4 text-emerald-400"></i> <span>${message}</span>`;
    document.body.appendChild(toast);
    lucide.createIcons();

    setTimeout(() => {
        toast.remove();
    }, 2500);
}

function escapeHtml(string) {
    const entityMap = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
        '/': '&#x2F;'
    };
    return String(string).replace(/[&<>"'\/]/g, s => entityMap[s]);
}
