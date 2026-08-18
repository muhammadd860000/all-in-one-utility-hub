"""
Centralized Configuration & Registry for all 34 Tools in All-in-One Utility Hub
"""

CATEGORIES = [
    {
        "id": "all",
        "name": "All Tools",
        "icon": "layout-grid",
        "description": "Browse our complete catalog of 34+ free online utilities."
    },
    {
        "id": "pdf",
        "name": "PDF Power Tools",
        "icon": "file-text",
        "description": "Merge, split, compress, convert, watermark, and secure your PDF documents."
    },
    {
        "id": "image",
        "name": "AI & Image Studio",
        "icon": "image",
        "description": "AI background removal, image converters, compression, filters, and color tools."
    },
    {
        "id": "data",
        "name": "Document & Data Converters",
        "icon": "file-spreadsheet",
        "description": "Convert seamlessly between Excel, CSV, JSON, Markdown, HTML, and XML."
    },
    {
        "id": "utility",
        "name": "Utilities & Security",
        "icon": "shield-check",
        "description": "QR code generator, file hashing checksums, Base64 codecs, text diff, and text converters."
    }
]

TOOLS = {
    # ==========================================
    # PDF POWER TOOLS (10 Tools)
    # ==========================================
    "merge-pdf": {
        "id": "merge-pdf",
        "name": "Merge PDF",
        "category": "pdf",
        "badge": "Popular",
        "icon": "layers",
        "color": "from-red-500 to-rose-600",
        "bg_light": "bg-red-50 text-red-600 border-red-200",
        "description": "Combine multiple PDF files in any order into a single unified document.",
        "accept": ".pdf",
        "multiple": True,
        "action_name": "Merge PDFs",
        "loading_msg": "Merging your PDF documents...",
        "inputs": []
    },
    "split-pdf": {
        "id": "split-pdf",
        "name": "Split PDF",
        "category": "pdf",
        "badge": "Popular",
        "icon": "scissors",
        "color": "from-rose-500 to-pink-600",
        "bg_light": "bg-rose-50 text-rose-600 border-rose-200",
        "description": "Extract specific page ranges (e.g. 1-3, 5, 8) or split all pages into separate files.",
        "accept": ".pdf",
        "multiple": False,
        "action_name": "Split PDF",
        "loading_msg": "Extracting pages from PDF...",
        "inputs": [
            {
                "id": "page_range",
                "label": "Page Ranges (e.g. '1-3, 5' or leave empty for all pages as ZIP)",
                "type": "text",
                "placeholder": "1-3, 5",
                "default": ""
            }
        ]
    },
    "compress-pdf": {
        "id": "compress-pdf",
        "name": "Compress PDF",
        "category": "pdf",
        "badge": "Essential",
        "icon": "minimize-2",
        "color": "from-orange-500 to-amber-600",
        "bg_light": "bg-orange-50 text-orange-600 border-orange-200",
        "description": "Reduce PDF file size while optimizing content streams and visual quality.",
        "accept": ".pdf",
        "multiple": False,
        "action_name": "Compress PDF",
        "loading_msg": "Optimizing & compressing PDF...",
        "inputs": [
            {
                "id": "compression_level",
                "label": "Compression Level",
                "type": "select",
                "options": [
                    {"value": "recommended", "label": "Recommended (Balanced size & quality)"},
                    {"value": "extreme", "label": "High Compression (Smallest size)"},
                    {"value": "lossless", "label": "Lossless Stream Optimization"}
                ],
                "default": "recommended"
            }
        ]
    },
    "pdf-to-word": {
        "id": "pdf-to-word",
        "name": "PDF to Word",
        "category": "pdf",
        "badge": "HD Layout",
        "icon": "file-type-2",
        "color": "from-blue-600 to-indigo-600",
        "bg_light": "bg-blue-50 text-blue-600 border-blue-200",
        "description": "Convert PDF documents & shipping labels (with barcodes, QR codes, tables & boxes) to Word (.docx).",
        "accept": ".pdf",
        "multiple": False,
        "action_name": "Convert to Word",
        "loading_msg": "Converting PDF layout, barcodes, tables & graphics to DOCX...",
        "inputs": [
            {
                "id": "conversion_mode",
                "label": "Conversion Mode & Quality",
                "type": "select",
                "options": [
                    {"value": "high_fidelity", "label": "Exact Visual Layout (100% Barcode, QR Code & Label Fidelity - Recommended)"},
                    {"value": "editable_layout", "label": "Editable Layout & Native Tables (pdf2docx / Structured)"},
                    {"value": "extracted_text", "label": "Clean Flowing Text"}
                ],
                "default": "high_fidelity"
            }
        ]
    },
    "word-to-pdf": {
        "id": "word-to-pdf",
        "name": "Word to PDF",
        "category": "pdf",
        "badge": "Fast",
        "icon": "file-text",
        "color": "from-sky-500 to-blue-600",
        "bg_light": "bg-sky-50 text-sky-600 border-sky-200",
        "description": "Convert Microsoft Word (.docx) documents into clean, publish-ready PDF files.",
        "accept": ".docx,.doc",
        "multiple": False,
        "action_name": "Convert to PDF",
        "loading_msg": "Rendering Word document to PDF...",
        "inputs": []
    },
    "pdf-to-jpg": {
        "id": "pdf-to-jpg",
        "name": "PDF to JPG",
        "category": "pdf",
        "badge": "HD Output",
        "icon": "file-image",
        "color": "from-amber-500 to-yellow-600",
        "bg_light": "bg-amber-50 text-amber-600 border-amber-200",
        "description": "Extract all pages from a PDF document and save them as high-definition JPG images.",
        "accept": ".pdf",
        "multiple": False,
        "action_name": "Convert to JPG",
        "loading_msg": "Rendering PDF pages into HD images...",
        "inputs": [
            {
                "id": "dpi",
                "label": "Image Resolution (DPI)",
                "type": "select",
                "options": [
                    {"value": "150", "label": "Standard (150 DPI)"},
                    {"value": "300", "label": "High Definition (300 DPI)"}
                ],
                "default": "150"
            }
        ]
    },
    "jpg-to-pdf": {
        "id": "jpg-to-pdf",
        "name": "JPG to PDF",
        "category": "pdf",
        "badge": "Multi-Image",
        "icon": "image-plus",
        "color": "from-emerald-500 to-teal-600",
        "bg_light": "bg-emerald-50 text-emerald-600 border-emerald-200",
        "description": "Convert and combine one or multiple JPG, PNG, and WEBP images into a single PDF.",
        "accept": ".jpg,.jpeg,.png,.webp,.bmp",
        "multiple": True,
        "action_name": "Create PDF",
        "loading_msg": "Compiling images into PDF document...",
        "inputs": [
            {
                "id": "page_orientation",
                "label": "Page Fit",
                "type": "select",
                "options": [
                    {"value": "auto", "label": "Auto Fit (Match Image Dimensions)"},
                    {"value": "a4", "label": "Standard A4 Page Fit"}
                ],
                "default": "auto"
            }
        ]
    },
    "rotate-pdf": {
        "id": "rotate-pdf",
        "name": "Rotate PDF",
        "category": "pdf",
        "badge": "Utility",
        "icon": "rotate-cw",
        "color": "from-purple-500 to-indigo-600",
        "bg_light": "bg-purple-50 text-purple-600 border-purple-200",
        "description": "Rotate your PDF pages by 90, 180, or 270 degrees clockwise in seconds.",
        "accept": ".pdf",
        "multiple": False,
        "action_name": "Rotate PDF",
        "loading_msg": "Applying page rotations...",
        "inputs": [
            {
                "id": "angle",
                "label": "Rotation Angle",
                "type": "select",
                "options": [
                    {"value": "90", "label": "90° Clockwise"},
                    {"value": "180", "label": "180° Half Turn"},
                    {"value": "270", "label": "270° (90° Counter-Clockwise)"}
                ],
                "default": "90"
            }
        ]
    },
    "watermark-pdf": {
        "id": "watermark-pdf",
        "name": "Watermark PDF",
        "category": "pdf",
        "badge": "Security",
        "icon": "stamp",
        "color": "from-violet-500 to-purple-600",
        "bg_light": "bg-violet-50 text-violet-600 border-violet-200",
        "description": "Add a custom text watermark across all pages of your PDF document.",
        "accept": ".pdf",
        "multiple": False,
        "action_name": "Apply Watermark",
        "loading_msg": "Stamping watermark on PDF pages...",
        "inputs": [
            {
                "id": "watermark_text",
                "label": "Watermark Text",
                "type": "text",
                "placeholder": "CONFIDENTIAL",
                "default": "CONFIDENTIAL"
            },
            {
                "id": "opacity",
                "label": "Watermark Opacity",
                "type": "select",
                "options": [
                    {"value": "0.15", "label": "Light (15%)"},
                    {"value": "0.30", "label": "Medium (30%)"},
                    {"value": "0.60", "label": "Strong (60%)"}
                ],
                "default": "0.30"
            }
        ]
    },
    "protect-pdf": {
        "id": "protect-pdf",
        "name": "Protect & Unlock PDF",
        "category": "pdf",
        "badge": "Security",
        "icon": "lock",
        "color": "from-slate-700 to-gray-900",
        "bg_light": "bg-gray-100 text-gray-800 border-gray-300",
        "description": "Encrypt your PDF with standard 128/256-bit password protection or remove existing password.",
        "accept": ".pdf",
        "multiple": False,
        "action_name": "Apply Security",
        "loading_msg": "Applying cryptographic security...",
        "inputs": [
            {
                "id": "mode",
                "label": "Action Mode",
                "type": "select",
                "options": [
                    {"value": "encrypt", "label": "Lock (Encrypt with Password)"},
                    {"value": "decrypt", "label": "Unlock (Remove Known Password)"}
                ],
                "default": "encrypt"
            },
            {
                "id": "password",
                "label": "Password",
                "type": "password",
                "placeholder": "Enter password...",
                "default": ""
            }
        ]
    },

    # ==========================================
    # AI & IMAGE STUDIO (10 Tools)
    # ==========================================
    "remove-bg": {
        "id": "remove-bg",
        "name": "AI HD Background Remover",
        "category": "image",
        "badge": "AI Powered",
        "icon": "wand-2",
        "color": "from-fuchsia-500 to-pink-600",
        "bg_light": "bg-fuchsia-50 text-fuchsia-600 border-fuchsia-200",
        "description": "Remove image backgrounds automatically with precision AI cutout in full HD resolution.",
        "accept": ".png,.jpg,.jpeg,.webp",
        "multiple": False,
        "action_name": "Remove Background",
        "loading_msg": "AI neural network isolating foreground & removing background...",
        "inputs": []
    },
    "image-resizer": {
        "id": "image-resizer",
        "name": "Image Resizer",
        "category": "image",
        "badge": "Utility",
        "icon": "scaling",
        "color": "from-cyan-500 to-blue-600",
        "bg_light": "bg-cyan-50 text-cyan-600 border-cyan-200",
        "description": "Resize your photos and graphics by exact pixel dimensions or percentage scaling.",
        "accept": ".png,.jpg,.jpeg,.webp,.bmp",
        "multiple": False,
        "action_name": "Resize Image",
        "loading_msg": "Resizing and resampling image...",
        "inputs": [
            {
                "id": "resize_mode",
                "label": "Resize Type",
                "type": "select",
                "options": [
                    {"value": "dimensions", "label": "Custom Dimensions (Pixels)"},
                    {"value": "percentage", "label": "Percentage Scale"}
                ],
                "default": "percentage"
            },
            {
                "id": "scale_percent",
                "label": "Scale Percentage (%)",
                "type": "number",
                "placeholder": "50",
                "default": "50"
            },
            {
                "id": "width",
                "label": "Target Width (px - when using Custom Dimensions)",
                "type": "number",
                "placeholder": "1200",
                "default": ""
            },
            {
                "id": "height",
                "label": "Target Height (px - when using Custom Dimensions)",
                "type": "number",
                "placeholder": "800",
                "default": ""
            }
        ]
    },
    "image-converter": {
        "id": "image-converter",
        "name": "Image Format Converter",
        "category": "image",
        "badge": "Popular",
        "icon": "refresh-cw",
        "color": "from-teal-500 to-emerald-600",
        "bg_light": "bg-teal-50 text-teal-600 border-teal-200",
        "description": "Convert images between PNG, JPG, WEBP, BMP, TIFF, ICO, and GIF formats.",
        "accept": ".png,.jpg,.jpeg,.webp,.bmp,.tiff,.gif",
        "multiple": False,
        "action_name": "Convert Image",
        "loading_msg": "Re-encoding image format...",
        "inputs": [
            {
                "id": "target_format",
                "label": "Target Output Format",
                "type": "select",
                "options": [
                    {"value": "png", "label": "PNG (Lossless / Transparent)"},
                    {"value": "jpg", "label": "JPG (Photo Standard)"},
                    {"value": "webp", "label": "WEBP (Modern Web Format)"},
                    {"value": "ico", "label": "ICO (Favicon 64x64)"},
                    {"value": "bmp", "label": "BMP (Bitmap)"},
                    {"value": "tiff", "label": "TIFF (Print Standard)"}
                ],
                "default": "webp"
            }
        ]
    },
    "image-compressor": {
        "id": "image-compressor",
        "name": "Image Compressor",
        "category": "image",
        "badge": "Essential",
        "icon": "file-archive",
        "color": "from-green-500 to-emerald-600",
        "bg_light": "bg-green-50 text-green-600 border-green-200",
        "description": "Compress JPG, PNG, and WEBP photos to save bandwidth and speed up page loading.",
        "accept": ".png,.jpg,.jpeg,.webp",
        "multiple": False,
        "action_name": "Compress Image",
        "loading_msg": "Compressing image data...",
        "inputs": [
            {
                "id": "quality",
                "label": "Quality Level (1 - 100)",
                "type": "number",
                "placeholder": "75",
                "default": "75"
            }
        ]
    },
    "image-filters": {
        "id": "image-filters",
        "name": "Image Effects & Filters",
        "category": "image",
        "badge": "Creative",
        "icon": "sparkles",
        "color": "from-pink-500 to-rose-600",
        "bg_light": "bg-pink-50 text-pink-600 border-pink-200",
        "description": "Apply artistic filters including Grayscale, Sepia, Blur, Sharpen, Invert, and Brightness.",
        "accept": ".png,.jpg,.jpeg,.webp",
        "multiple": False,
        "action_name": "Apply Filter",
        "loading_msg": "Applying visual filter effects...",
        "inputs": [
            {
                "id": "filter_type",
                "label": "Select Filter Effect",
                "type": "select",
                "options": [
                    {"value": "grayscale", "label": "Grayscale (Black & White)"},
                    {"value": "sepia", "label": "Vintage Sepia Tone"},
                    {"value": "blur", "label": "Gaussian Blur"},
                    {"value": "sharpen", "label": "Sharpen Details"},
                    {"value": "invert", "label": "Invert Colors (Negative)"},
                    {"value": "enhance_contrast", "label": "Auto Contrast Boost"},
                    {"value": "brighten", "label": "Brighten (+30%)"}
                ],
                "default": "grayscale"
            }
        ]
    },
    "image-cropper": {
        "id": "image-cropper",
        "name": "Image Cropper",
        "category": "image",
        "badge": "Utility",
        "icon": "crop",
        "color": "from-indigo-500 to-purple-600",
        "bg_light": "bg-indigo-50 text-indigo-600 border-indigo-200",
        "description": "Crop images to square 1:1, widescreen 16:9, portrait 4:5, or custom bounds.",
        "accept": ".png,.jpg,.jpeg,.webp",
        "multiple": False,
        "action_name": "Crop Image",
        "loading_msg": "Cropping image bounding box...",
        "inputs": [
            {
                "id": "aspect_ratio",
                "label": "Preset Aspect Ratio",
                "type": "select",
                "options": [
                    {"value": "1:1", "label": "Square (1:1 - Avatar/Post)"},
                    {"value": "16:9", "label": "Landscape (16:9 - YouTube/Banner)"},
                    {"value": "4:3", "label": "Standard Photo (4:3)"},
                    {"value": "9:16", "label": "Story / Reel (9:16)"}
                ],
                "default": "1:1"
            }
        ]
    },
    "image-to-base64": {
        "id": "image-to-base64",
        "name": "Image to Base64",
        "category": "image",
        "badge": "Developer",
        "icon": "code-2",
        "color": "from-amber-600 to-orange-600",
        "bg_light": "bg-amber-50 text-amber-600 border-amber-200",
        "description": "Convert any image into an inline Base64 data URI string or decode Base64 to image.",
        "accept": ".png,.jpg,.jpeg,.webp,.gif,.svg",
        "multiple": False,
        "action_name": "Generate Base64",
        "loading_msg": "Encoding image binary to Base64...",
        "inputs": []
    },
    "image-watermark": {
        "id": "image-watermark",
        "name": "Image Watermark",
        "category": "image",
        "badge": "Protection",
        "icon": "stamp",
        "color": "from-rose-500 to-red-600",
        "bg_light": "bg-rose-50 text-rose-600 border-rose-200",
        "description": "Stamp branded copyright text across your images to protect your creative rights.",
        "accept": ".png,.jpg,.jpeg,.webp",
        "multiple": False,
        "action_name": "Add Watermark",
        "loading_msg": "Rendering watermark overlay on image...",
        "inputs": [
            {
                "id": "watermark_text",
                "label": "Watermark Text",
                "type": "text",
                "placeholder": "© Copyright 2026",
                "default": "© Copyright 2026"
            },
            {
                "id": "position",
                "label": "Watermark Position",
                "type": "select",
                "options": [
                    {"value": "bottom_right", "label": "Bottom Right"},
                    {"value": "bottom_left", "label": "Bottom Left"},
                    {"value": "center", "label": "Center"},
                    {"value": "top_right", "label": "Top Right"}
                ],
                "default": "bottom_right"
            }
        ]
    },
    "exif-remover": {
        "id": "exif-remover",
        "name": "EXIF Metadata Stripper",
        "category": "image",
        "badge": "Privacy",
        "icon": "shield-off",
        "color": "from-slate-600 to-zinc-800",
        "bg_light": "bg-slate-50 text-slate-700 border-slate-200",
        "description": "Inspect and completely strip hidden GPS coordinates, camera serials, and EXIF tags.",
        "accept": ".png,.jpg,.jpeg,.webp,.tiff",
        "multiple": False,
        "action_name": "Clean Metadata",
        "loading_msg": "Scrubbing EXIF & GPS metadata...",
        "inputs": []
    },
    "color-palette": {
        "id": "color-palette",
        "name": "Color Palette Extractor",
        "category": "image",
        "badge": "Design",
        "icon": "palette",
        "color": "from-fuchsia-600 to-indigo-600",
        "bg_light": "bg-fuchsia-50 text-fuchsia-600 border-fuchsia-200",
        "description": "Extract the top dominant harmonious color swatches (HEX & RGB) from any photo.",
        "accept": ".png,.jpg,.jpeg,.webp",
        "multiple": False,
        "action_name": "Extract Palette",
        "loading_msg": "Quantizing image & computing dominant colors...",
        "inputs": []
    },

    # ==========================================
    # DOCUMENT & DATA CONVERTERS (8 Tools)
    # ==========================================
    "excel-to-pdf": {
        "id": "excel-to-pdf",
        "name": "Excel to PDF",
        "category": "data",
        "badge": "Popular",
        "icon": "file-spreadsheet",
        "color": "from-emerald-600 to-green-700",
        "bg_light": "bg-emerald-50 text-emerald-600 border-emerald-200",
        "description": "Convert Excel spreadsheets (.xlsx, .xls) into clean, beautifully styled PDF tables.",
        "accept": ".xlsx,.xls",
        "multiple": False,
        "action_name": "Convert to PDF",
        "loading_msg": "Parsing spreadsheet & generating PDF table...",
        "inputs": []
    },
    "excel-to-csv": {
        "id": "excel-to-csv",
        "name": "Excel to CSV",
        "category": "data",
        "badge": "Fast",
        "icon": "file-down",
        "color": "from-green-600 to-teal-700",
        "bg_light": "bg-green-50 text-green-600 border-green-200",
        "description": "Extract tabular data from Microsoft Excel sheets into standard CSV format.",
        "accept": ".xlsx,.xls",
        "multiple": False,
        "action_name": "Convert to CSV",
        "loading_msg": "Exporting Excel rows to CSV...",
        "inputs": []
    },
    "csv-to-excel": {
        "id": "csv-to-excel",
        "name": "CSV to Excel",
        "category": "data",
        "badge": "Fast",
        "icon": "file-up",
        "color": "from-teal-600 to-emerald-700",
        "bg_light": "bg-teal-50 text-teal-600 border-teal-200",
        "description": "Convert comma-separated CSV files into styled Microsoft Excel (.xlsx) workbooks.",
        "accept": ".csv,.txt",
        "multiple": False,
        "action_name": "Convert to Excel",
        "loading_msg": "Building Excel workbook with formatted headers...",
        "inputs": []
    },
    "json-to-csv": {
        "id": "json-to-csv",
        "name": "JSON to CSV",
        "category": "data",
        "badge": "Developer",
        "icon": "file-code",
        "color": "from-blue-600 to-cyan-600",
        "bg_light": "bg-blue-50 text-blue-600 border-blue-200",
        "description": "Flatten and convert nested JSON arrays and datasets into clean CSV spreadsheets.",
        "accept": ".json,.txt",
        "multiple": False,
        "action_name": "Convert to CSV",
        "loading_msg": "Parsing JSON structure & generating CSV columns...",
        "inputs": []
    },
    "csv-to-json": {
        "id": "csv-to-json",
        "name": "CSV to JSON",
        "category": "data",
        "badge": "Developer",
        "icon": "file-json",
        "color": "from-cyan-600 to-sky-600",
        "bg_light": "bg-cyan-50 text-cyan-600 border-cyan-200",
        "description": "Parse and convert CSV spreadsheet records into structured, formatted JSON objects.",
        "accept": ".csv,.txt",
        "multiple": False,
        "is_text_tool": True,
        "action_name": "Convert to JSON",
        "loading_msg": "Parsing CSV records into JSON structure...",
        "inputs": []
    },
    "markdown-to-html": {
        "id": "markdown-to-html",
        "name": "Markdown to HTML",
        "category": "data",
        "badge": "Web",
        "icon": "file-code-2",
        "color": "from-indigo-600 to-blue-600",
        "bg_light": "bg-indigo-50 text-indigo-600 border-indigo-200",
        "description": "Compile Markdown (.md) documents into clean, semantic HTML with styled typography.",
        "accept": ".md,.markdown,.txt",
        "multiple": False,
        "is_direct_input": True,
        "is_text_tool": True,
        "action_name": "Render HTML",
        "loading_msg": "Compiling Markdown syntax into HTML...",
        "inputs": [
            {
                "id": "markdown_text",
                "label": "Markdown Text (Optional if uploading file above)",
                "type": "textarea",
                "placeholder": "# Enter Markdown here...\n\n- Feature 1\n- Feature 2",
                "default": ""
            }
        ]
    },
    "html-to-markdown": {
        "id": "html-to-markdown",
        "name": "HTML to Markdown",
        "category": "data",
        "badge": "Web",
        "icon": "file-text",
        "color": "from-violet-600 to-indigo-600",
        "bg_light": "bg-violet-50 text-violet-600 border-violet-200",
        "description": "Convert HTML web pages or code snippets into clean, standard Markdown notation.",
        "accept": ".html,.htm,.txt",
        "multiple": False,
        "is_direct_input": True,
        "is_text_tool": True,
        "action_name": "Convert to Markdown",
        "loading_msg": "Translating HTML tags to Markdown...",
        "inputs": [
            {
                "id": "html_text",
                "label": "HTML Code (Optional if uploading file above)",
                "type": "textarea",
                "placeholder": "<h1>Title</h1><p>Some text</p>",
                "default": ""
            }
        ]
    },
    "xml-to-json": {
        "id": "xml-to-json",
        "name": "XML to JSON",
        "category": "data",
        "badge": "Data",
        "icon": "binary",
        "color": "from-purple-600 to-fuchsia-600",
        "bg_light": "bg-purple-50 text-purple-600 border-purple-200",
        "description": "Convert XML documents, feeds, and configurations into modern structured JSON objects.",
        "accept": ".xml,.txt",
        "multiple": False,
        "is_direct_input": True,
        "is_text_tool": True,
        "action_name": "Convert to JSON",
        "loading_msg": "Parsing XML tree hierarchy into JSON...",
        "inputs": [
            {
                "id": "xml_text",
                "label": "XML Content (Optional if uploading file above)",
                "type": "textarea",
                "placeholder": "<root><user><name>John</name></user></root>",
                "default": ""
            }
        ]
    },

    # ==========================================
    # UTILITIES & SECURITY (6 Tools)
    # ==========================================
    "qr-generator": {
        "id": "qr-generator",
        "name": "QR Code Generator",
        "category": "utility",
        "badge": "Popular",
        "icon": "qr-code",
        "color": "from-emerald-500 to-teal-600",
        "bg_light": "bg-emerald-50 text-emerald-600 border-emerald-200",
        "description": "Generate high-resolution custom QR codes for URLs, Wi-Fi networks, text, and contact cards.",
        "accept": "",
        "multiple": False,
        "is_direct_input": True,
        "is_text_tool": True,
        "action_name": "Generate QR Code",
        "loading_msg": "Generating high-resolution QR matrix...",
        "inputs": [
            {
                "id": "qr_content",
                "label": "Content (URL, Text, Wi-Fi details, etc.)",
                "type": "textarea",
                "placeholder": "https://example.com",
                "default": "https://example.com"
            },
            {
                "id": "qr_size",
                "label": "QR Code Size",
                "type": "select",
                "options": [
                    {"value": "10", "label": "Medium (300x300 px)"},
                    {"value": "15", "label": "Large (450x450 px)"},
                    {"value": "20", "label": "Ultra HD (600x600 px)"}
                ],
                "default": "10"
            }
        ]
    },
    "file-hasher": {
        "id": "file-hasher",
        "name": "File Hasher & Checksum",
        "category": "utility",
        "badge": "Security",
        "icon": "shield-check",
        "color": "from-slate-700 to-indigo-900",
        "bg_light": "bg-slate-100 text-slate-800 border-slate-300",
        "description": "Compute cryptographic MD5, SHA-1, SHA-256, and SHA-512 hashes to verify file integrity.",
        "accept": "*",
        "multiple": False,
        "is_text_tool": True,
        "action_name": "Compute Hashes",
        "loading_msg": "Computing cryptographic hashes...",
        "inputs": []
    },
    "base64-codec": {
        "id": "base64-codec",
        "name": "Base64 Text/File Codec",
        "category": "utility",
        "badge": "Developer",
        "icon": "key-round",
        "color": "from-blue-600 to-violet-700",
        "bg_light": "bg-blue-50 text-blue-600 border-blue-200",
        "description": "Encode raw text or binary files into Base64 format or decode Base64 strings back to text/files.",
        "accept": "*",
        "multiple": False,
        "is_direct_input": True,
        "is_text_tool": True,
        "action_name": "Process Base64",
        "loading_msg": "Encoding/Decoding Base64 string...",
        "inputs": [
            {
                "id": "codec_mode",
                "label": "Action",
                "type": "select",
                "options": [
                    {"value": "encode", "label": "Encode to Base64"},
                    {"value": "decode", "label": "Decode from Base64"}
                ],
                "default": "encode"
            },
            {
                "id": "input_text",
                "label": "Text Input (Optional if uploading file above)",
                "type": "textarea",
                "placeholder": "Enter text to encode or Base64 string to decode...",
                "default": ""
            }
        ]
    },
    "text-diff": {
        "id": "text-diff",
        "name": "Text Diff Checker",
        "category": "utility",
        "badge": "Developer",
        "icon": "git-compare",
        "color": "from-amber-600 to-rose-600",
        "bg_light": "bg-amber-50 text-amber-600 border-amber-200",
        "description": "Compare two blocks of code or text side-by-side with additions and deletions highlighted.",
        "accept": ".txt,.py,.js,.html,.css,.json,.md",
        "multiple": False,
        "is_direct_input": True,
        "is_text_tool": True,
        "action_name": "Compare Text",
        "loading_msg": "Analyzing text differences...",
        "inputs": [
            {
                "id": "original_text",
                "label": "Original Text / Old Version",
                "type": "textarea",
                "placeholder": "Paste original text here...",
                "default": ""
            },
            {
                "id": "modified_text",
                "label": "Modified Text / New Version",
                "type": "textarea",
                "placeholder": "Paste modified text here...",
                "default": ""
            }
        ]
    },
    "case-converter": {
        "id": "case-converter",
        "name": "Text Case Converter",
        "category": "utility",
        "badge": "Text",
        "icon": "type",
        "color": "from-teal-600 to-cyan-700",
        "bg_light": "bg-teal-50 text-teal-600 border-teal-200",
        "description": "Convert text into UPPERCASE, lowercase, Title Case, camelCase, snake_case, or kebab-case.",
        "accept": ".txt",
        "multiple": False,
        "is_direct_input": True,
        "is_text_tool": True,
        "action_name": "Convert Case",
        "loading_msg": "Transforming text case...",
        "inputs": [
            {
                "id": "text_input",
                "label": "Input Text",
                "type": "textarea",
                "placeholder": "Enter text here...",
                "default": ""
            },
            {
                "id": "case_style",
                "label": "Target Case Style",
                "type": "select",
                "options": [
                    {"value": "upper", "label": "UPPERCASE"},
                    {"value": "lower", "label": "lowercase"},
                    {"value": "title", "label": "Title Case"},
                    {"value": "camel", "label": "camelCase"},
                    {"value": "snake", "label": "snake_case"},
                    {"value": "kebab", "label": "kebab-case"},
                    {"value": "pascal", "label": "PascalCase"}
                ],
                "default": "title"
            }
        ]
    },
    "url-encoder-decoder": {
        "id": "url-encoder-decoder",
        "name": "URL Encoder & Decoder",
        "category": "utility",
        "badge": "Web",
        "icon": "link-2",
        "color": "from-indigo-600 to-purple-700",
        "bg_light": "bg-indigo-50 text-indigo-600 border-indigo-200",
        "description": "Encode special characters in URLs or decode URL-encoded percent strings.",
        "accept": ".txt",
        "multiple": False,
        "is_direct_input": True,
        "is_text_tool": True,
        "action_name": "Process URL",
        "loading_msg": "Processing URL characters...",
        "inputs": [
            {
                "id": "url_mode",
                "label": "Operation",
                "type": "select",
                "options": [
                    {"value": "encode", "label": "URL Encode (e.g. hello world -> hello%20world)"},
                    {"value": "decode", "label": "URL Decode (e.g. hello%20world -> hello world)"}
                ],
                "default": "encode"
            },
            {
                "id": "url_input",
                "label": "URL or Query String",
                "type": "textarea",
                "placeholder": "https://example.com/search?query=hello world",
                "default": ""
            }
        ]
    }
}
