"""
DELIBERA — Sistema de Indagación Epistémica para Expertos en DPI
================================================================
Implementación del Código Deliberativo: computar para deliberar, no para decidir.

Este MVP materializa los principios de:
- Apertura semántica controlada
- Jerarquía interrogativa (Erotetic Theory)
- Trazabilidad razonadora
- Reversibilidad deliberativa
- Integración del disenso
- Función normativa explícita

El experto co-construye conocimiento con la IA y firma epistémicamente su trabajo.
"""

import streamlit as st
import json
import hashlib
from datetime import datetime
from typing import Optional
import os

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE PÁGINA Y ESTILOS
# ══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="DELIBERA | Indagación Epistémica DPI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado para estética editorial-jurídica
st.markdown("""
<style>
    /* ═══ TIPOGRAFÍA DISTINTIVA ═══ */
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&family=Inter:wght@300;400;500;600&display=swap');
    
    /* ═══ VARIABLES DE DISEÑO ═══ */
    :root {
        --color-ink: #1a1a1a;
        --color-paper: #faf9f7;
        --color-accent: #8b4513;
        --color-accent-light: #d4a574;
        --color-sage: #5d6d5e;
        --color-muted: #6b6b6b;
        --color-border: #e5e2dd;
        --color-highlight: #fff8e7;
        --font-display: 'Cormorant Garamond', Georgia, serif;
        --font-body: 'Inter', -apple-system, sans-serif;
        --font-mono: 'JetBrains Mono', monospace;
    }
    
    /* ═══ RESET Y BASE ═══ */
    .stApp {
        background: linear-gradient(180deg, var(--color-paper) 0%, #f5f3ef 100%);
    }
    
    .main .block-container {
        max-width: 1200px;
        padding: 2rem 3rem 4rem;
    }
    
    /* ═══ HEADER PRINCIPAL ═══ */
    .delibera-header {
        text-align: center;
        padding: 3rem 0 2rem;
        border-bottom: 1px solid var(--color-border);
        margin-bottom: 3rem;
    }
    
    .delibera-logo {
        font-family: var(--font-display);
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        color: var(--color-ink);
        margin: 0;
        line-height: 1;
    }
    
    .delibera-tagline {
        font-family: var(--font-display);
        font-size: 1.1rem;
        font-style: italic;
        color: var(--color-muted);
        margin-top: 0.75rem;
        letter-spacing: 0.05em;
    }
    
    /* ═══ SECCIONES ═══ */
    .section-title {
        font-family: var(--font-display);
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--color-ink);
        margin: 2.5rem 0 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--color-accent);
        display: inline-block;
    }
    
    .section-number {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        color: var(--color-accent);
        letter-spacing: 0.1em;
        display: block;
        margin-bottom: 0.25rem;
    }
    
    /* ═══ TARJETAS DE INDAGACIÓN ═══ */
    .inquiry-card {
        background: white;
        border: 1px solid var(--color-border);
        border-radius: 4px;
        padding: 1.5rem 2rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: all 0.2s ease;
    }
    
    .inquiry-card:hover {
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        border-color: var(--color-accent-light);
    }
    
    .inquiry-question {
        font-family: var(--font-display);
        font-size: 1.25rem;
        color: var(--color-ink);
        margin-bottom: 1rem;
        line-height: 1.4;
    }
    
    .inquiry-meta {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        color: var(--color-muted);
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }
    
    /* ═══ PANEL DE PERSPECTIVAS ═══ */
    .perspective-panel {
        background: var(--color-highlight);
        border-left: 3px solid var(--color-accent);
        padding: 1.25rem 1.5rem;
        margin: 1rem 0;
        font-family: var(--font-body);
        font-size: 0.95rem;
        line-height: 1.7;
    }
    
    .perspective-label {
        font-family: var(--font-mono);
        font-size: 0.65rem;
        color: var(--color-accent);
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    /* ═══ MÉTRICAS EEE ═══ */
    .eee-container {
        background: white;
        border: 1px solid var(--color-border);
        border-radius: 4px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .eee-title {
        font-family: var(--font-display);
        font-size: 1rem;
        font-weight: 600;
        color: var(--color-ink);
        margin-bottom: 1rem;
    }
    
    .eee-metric {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.5rem 0;
        border-bottom: 1px solid var(--color-border);
    }
    
    .eee-metric:last-child {
        border-bottom: none;
    }
    
    .eee-label {
        font-family: var(--font-body);
        font-size: 0.85rem;
        color: var(--color-muted);
    }
    
    .eee-value {
        font-family: var(--font-mono);
        font-size: 0.9rem;
        font-weight: 500;
        color: var(--color-sage);
    }
    
    .eee-score {
        font-family: var(--font-display);
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--color-sage);
        text-align: center;
        margin: 1rem 0;
    }
    
    /* ═══ FIRMA EPISTÉMICA ═══ */
    .signature-panel {
        background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
        color: white;
        border-radius: 4px;
        padding: 2rem;
        margin: 2rem 0;
    }
    
    .signature-title {
        font-family: var(--font-display);
        font-size: 1.25rem;
        font-weight: 600;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .signature-subtitle {
        font-family: var(--font-body);
        font-size: 0.85rem;
        color: rgba(255,255,255,0.7);
        margin-bottom: 1.5rem;
    }
    
    .signature-hash {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        color: var(--color-accent-light);
        background: rgba(255,255,255,0.1);
        padding: 0.75rem 1rem;
        border-radius: 2px;
        word-break: break-all;
        margin-top: 1rem;
    }
    
    .signature-timestamp {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        color: rgba(255,255,255,0.5);
        margin-top: 0.75rem;
    }
    
    /* ═══ ÁRBOL DE DELIBERACIÓN ═══ */
    .tree-node {
        position: relative;
        padding-left: 1.5rem;
        margin: 0.75rem 0;
    }
    
    .tree-node::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0.6rem;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--color-accent);
    }
    
    .tree-node.validated::before {
        background: var(--color-sage);
    }
    
    .tree-node.pending::before {
        background: var(--color-border);
        border: 2px solid var(--color-accent);
    }
    
    .tree-connector {
        position: absolute;
        left: 3px;
        top: 1rem;
        width: 2px;
        height: calc(100% + 0.5rem);
        background: var(--color-border);
    }
    
    /* ═══ BOTONES ═══ */
    .stButton > button {
        font-family: var(--font-body) !important;
        font-weight: 500 !important;
        letter-spacing: 0.025em !important;
        border-radius: 2px !important;
        padding: 0.6rem 1.5rem !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton > button[kind="primary"] {
        background: var(--color-ink) !important;
        color: white !important;
        border: none !important;
    }
    
    .stButton > button[kind="primary"]:hover {
        background: var(--color-accent) !important;
    }
    
    /* ═══ INPUTS ═══ */
    .stTextArea textarea, .stTextInput input {
        font-family: var(--font-body) !important;
        border-radius: 2px !important;
        border-color: var(--color-border) !important;
    }
    
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: var(--color-accent) !important;
        box-shadow: 0 0 0 1px var(--color-accent) !important;
    }
    
    /* ═══ TABS ═══ */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        border-bottom: 1px solid var(--color-border);
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: var(--font-body);
        font-size: 0.85rem;
        font-weight: 500;
        letter-spacing: 0.025em;
        padding: 0.75rem 1.5rem;
        color: var(--color-muted);
        border-bottom: 2px solid transparent;
        background: transparent;
    }
    
    .stTabs [aria-selected="true"] {
        color: var(--color-ink) !important;
        border-bottom-color: var(--color-accent) !important;
        background: transparent !important;
    }
    
    /* ═══ EXPANDER ═══ */
    .streamlit-expanderHeader {
        font-family: var(--font-body);
        font-size: 0.9rem;
        font-weight: 500;
        color: var(--color-ink);
    }
    
    /* ═══ DIVIDERS ═══ */
    .section-divider {
        height: 1px;
        background: var(--color-border);
        margin: 3rem 0;
    }
    
    /* ═══ SIDEBAR ═══ */
    [data-testid="stSidebar"] {
        background: #2d2d2d;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: rgba(255,255,255,0.9);
    }
    
    /* ═══ ANIMACIONES ═══ */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-in {
        animation: fadeIn 0.4s ease-out;
    }
    
    /* ═══ RESPONSIVE ═══ */
    @media (max-width: 768px) {
        .delibera-logo { font-size: 2.5rem; }
        .main .block-container { padding: 1rem 1.5rem; }
    }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# ESTADO DE LA APLICACIÓN
# ══════════════════════════════════════════════════════════════════════════════

def init_session_state():
    """Inicializa el estado de la sesión con valores por defecto."""
    defaults = {
        "current_phase": "input",  # input, deliberation, signature
        "root_question": "",
        "inquiry_tree": {},
        "validated_nodes": set(),
        "expert_annotations": {},
        "perspectives": {},
        "reasoning_log": [],
        "eee_metrics": {
            "profundidad": 0,
            "pluralidad": 0,
            "trazabilidad": 0,
            "reversibilidad": 0,
            "robustez": 0
        },
        "final_synthesis": "",
        "signature_hash": None,
        "expert_name": "",
        "expert_role": ""
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()


# ══════════════════════════════════════════════════════════════════════════════
# FUNCIONES DEL MOTOR DELIBERATIVO
# ══════════════════════════════════════════════════════════════════════════════

def generate_inquiry_tree(question: str) -> dict:
    """
    Genera el árbol de indagación basado en la pregunta raíz.
    Implementa la jerarquía interrogativa del Código Deliberativo.
    """
    # Árbol de demostración para DPI
    # En producción, esto se conectaría con el InquiryEngine + LLM
    return {
        "root": question,
        "branches": [
            {
                "id": "q1",
                "question": "¿Cuál es el marco normativo aplicable?",
                "level": 1,
                "type": "definitional",
                "sub_branches": [
                    {
                        "id": "q1.1",
                        "question": "¿Qué establece la legislación nacional vigente?",
                        "level": 2,
                        "type": "factual"
                    },
                    {
                        "id": "q1.2", 
                        "question": "¿Existe normativa europea o internacional aplicable?",
                        "level": 2,
                        "type": "comparative"
                    }
                ]
            },
            {
                "id": "q2",
                "question": "¿Qué dice la jurisprudencia relevante?",
                "level": 1,
                "type": "precedential",
                "sub_branches": [
                    {
                        "id": "q2.1",
                        "question": "¿Hay sentencias del TJUE aplicables?",
                        "level": 2,
                        "type": "factual"
                    },
                    {
                        "id": "q2.2",
                        "question": "¿Cuál es la línea del Tribunal Supremo español?",
                        "level": 2,
                        "type": "factual"
                    }
                ]
            },
            {
                "id": "q3",
                "question": "¿Cuáles son las posiciones doctrinales en conflicto?",
                "level": 1,
                "type": "dialectical",
                "sub_branches": [
                    {
                        "id": "q3.1",
                        "question": "¿Qué argumentos favorecen una interpretación restrictiva?",
                        "level": 2,
                        "type": "argumentative"
                    },
                    {
                        "id": "q3.2",
                        "question": "¿Qué argumentos favorecen una interpretación extensiva?",
                        "level": 2,
                        "type": "argumentative"
                    }
                ]
            },
            {
                "id": "q4",
                "question": "¿Cuáles son las implicaciones prácticas de cada interpretación?",
                "level": 1,
                "type": "consequential",
                "sub_branches": []
            }
        ]
    }


def generate_perspectives(node_id: str, question: str) -> list:
    """
    Genera múltiples perspectivas para una pregunta.
    Implementa la apertura semántica y la integración del disenso.
    """
    # Perspectivas de demostración
    # En producción, el ContextualGenerator consultaría fuentes reales
    perspectives_map = {
        "q1": [
            {
                "source": "Marco Normativo Nacional",
                "content": "El Real Decreto Legislativo 1/1996 establece el régimen general de propiedad intelectual en España. El artículo 10.1 enumera las obras protegibles, exigiendo originalidad como requisito esencial.",
                "confidence": 0.95,
                "type": "legal"
            },
            {
                "source": "Directiva UE 2019/790",
                "content": "La Directiva sobre derechos de autor en el mercado único digital introduce nuevas excepciones y limitaciones, particularmente relevantes para la minería de textos y datos.",
                "confidence": 0.92,
                "type": "eu_law"
            }
        ],
        "q2": [
            {
                "source": "STJUE C-5/08 Infopaq",
                "content": "El TJUE estableció que la originalidad requiere que la obra refleje la 'creación intelectual propia del autor'. Este estándar armonizado ha influido en toda la jurisprudencia posterior.",
                "confidence": 0.98,
                "type": "case_law"
            },
            {
                "source": "STS 214/2011",
                "content": "El Tribunal Supremo español ha adoptado progresivamente el criterio europeo de originalidad, abandonando la anterior exigencia de 'altura creativa'.",
                "confidence": 0.90,
                "type": "case_law"
            }
        ],
        "q3": [
            {
                "source": "Posición Restrictiva (Bercovitz)",
                "content": "Desde esta perspectiva, el requisito de originalidad debe interpretarse de forma estricta, exigiendo un mínimo de creatividad que excluya las producciones puramente mecánicas o automatizadas.",
                "confidence": 0.85,
                "type": "doctrine"
            },
            {
                "source": "Posición Extensiva (Saiz García)",
                "content": "Esta corriente aboga por un concepto más flexible de originalidad que reconozca valor en las decisiones creativas incluso cuando el resultado pueda parecer simple o funcional.",
                "confidence": 0.85,
                "type": "doctrine"
            },
            {
                "source": "Perspectiva Crítica (Tamames)",
                "content": "La cuestión de la originalidad en obras generadas con IA plantea una ruptura epistémica: el concepto mismo de 'creación intelectual propia' presupone una agencia humana que estos sistemas problematizan.",
                "confidence": 0.80,
                "type": "critical"
            }
        ],
        "q4": [
            {
                "source": "Análisis de Impacto",
                "content": "Una interpretación restrictiva protegería la integridad del sistema de derechos de autor pero podría dejar sin protección producciones con valor económico. Una interpretación extensiva ampliaría la protección pero diluiría el concepto de autoría.",
                "confidence": 0.88,
                "type": "analysis"
            }
        ]
    }
    
    # Extraer el ID base (q1, q2, etc.) para la demo
    base_id = node_id.split('.')[0] if '.' in node_id else node_id
    return perspectives_map.get(base_id, [
        {
            "source": "Análisis General",
            "content": "Esta cuestión requiere un análisis detallado del contexto específico y las fuentes aplicables.",
            "confidence": 0.75,
            "type": "general"
        }
    ])


def calculate_eee(validated: set, total_nodes: int, perspectives_count: int) -> dict:
    """
    Calcula el Índice de Equilibrio Erotético (EEE).
    Evalúa la calidad estructural del proceso deliberativo.
    """
    total = max(total_nodes, 1)
    validated_count = len(validated)
    
    # D1: Profundidad estructural (niveles explorados)
    depth = min(1.0, validated_count / total)
    
    # D2: Pluralidad semántica (perspectivas consideradas)
    plurality = min(1.0, perspectives_count / (total * 2))
    
    # D3: Trazabilidad (nodos con justificación)
    traceability = validated_count / total if total > 0 else 0
    
    # D4: Reversibilidad (capacidad de revisión - siempre alta en este sistema)
    reversibility = 0.95
    
    # D5: Robustez (coherencia ante disenso)
    robustness = min(1.0, (validated_count + perspectives_count * 0.5) / (total * 1.5))
    
    return {
        "profundidad": round(depth, 2),
        "pluralidad": round(plurality, 2),
        "trazabilidad": round(traceability, 2),
        "reversibilidad": round(reversibility, 2),
        "robustez": round(robustness, 2),
        "total": round((depth + plurality + traceability + reversibility + robustness) / 5, 2)
    }


def generate_signature_hash(content: dict, expert: str, timestamp: str) -> str:
    """
    Genera el hash de firma epistémica.
    Garantiza la trazabilidad y la responsabilidad del experto.
    """
    signature_content = json.dumps({
        "expert": expert,
        "timestamp": timestamp,
        "root_question": content.get("root_question", ""),
        "validated_nodes": list(content.get("validated_nodes", [])),
        "synthesis": content.get("synthesis", ""),
        "eee_score": content.get("eee_score", 0)
    }, sort_keys=True, ensure_ascii=False)
    
    return hashlib.sha256(signature_content.encode()).hexdigest()


# ══════════════════════════════════════════════════════════════════════════════
# COMPONENTES DE INTERFAZ
# ══════════════════════════════════════════════════════════════════════════════

def render_header():
    """Renderiza el encabezado de la aplicación."""
    st.markdown("""
        <div class="delibera-header animate-in">
            <h1 class="delibera-logo">DELIBERA</h1>
            <p class="delibera-tagline">Sistema de Indagación Epistémica para Derecho de Propiedad Intelectual</p>
        </div>
    """, unsafe_allow_html=True)


def render_input_phase():
    """Renderiza la fase de entrada de la pregunta."""
    st.markdown("""
        <span class="section-number">01 — PREGUNTA RAÍZ</span>
        <h2 class="section-title">Objeto de Indagación</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="inquiry-card">
        <p style="font-family: var(--font-body); color: var(--color-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1rem;">
            Formule la cuestión jurídica que desea analizar. El sistema generará un árbol de indagación 
            estructurado, permitiéndole explorar múltiples perspectivas antes de elaborar su síntesis final.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input para la pregunta
    question = st.text_area(
        "Cuestión jurídica",
        placeholder="Ej: ¿Puede una obra generada por IA ser objeto de protección por derechos de autor bajo el TRLPI?",
        height=100,
        label_visibility="collapsed"
    )
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Información del experto
        expert_name = st.text_input(
            "Nombre del experto",
            placeholder="Dr. / Dra. [Nombre completo]",
            label_visibility="collapsed"
        )
    
    with col2:
        expert_role = st.text_input(
            "Especialización",
            placeholder="Especialización",
            label_visibility="collapsed"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("⚖️  Iniciar Deliberación", type="primary", use_container_width=True):
        if question and expert_name:
            st.session_state.root_question = question
            st.session_state.expert_name = expert_name
            st.session_state.expert_role = expert_role
            st.session_state.inquiry_tree = generate_inquiry_tree(question)
            st.session_state.current_phase = "deliberation"
            
            # Log inicial
            st.session_state.reasoning_log.append({
                "timestamp": datetime.now().isoformat(),
                "action": "INICIO_DELIBERACIÓN",
                "detail": f"Pregunta raíz: {question}"
            })
            
            st.rerun()
        else:
            st.warning("Por favor, introduzca la cuestión jurídica y su nombre.")


def render_inquiry_node(node: dict, depth: int = 0):
    """Renderiza un nodo del árbol de indagación."""
    node_id = node["id"]
    is_validated = node_id in st.session_state.validated_nodes
    
    indent = "　" * depth  # Espacio ideográfico para indentación
    
    status_class = "validated" if is_validated else "pending"
    status_icon = "✓" if is_validated else "○"
    
    with st.container():
        col1, col2 = st.columns([0.85, 0.15])
        
        with col1:
            st.markdown(f"""
                <div class="tree-node {status_class}">
                    <span class="inquiry-meta">{node.get('type', 'general').upper()} · NIVEL {node['level']}</span>
                    <p class="inquiry-question">{indent}{node['question']}</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if st.button(f"{'✓ Validado' if is_validated else 'Explorar'}", 
                        key=f"btn_{node_id}",
                        type="secondary" if is_validated else "primary"):
                
                if not is_validated:
                    # Generar perspectivas para este nodo
                    perspectives = generate_perspectives(node_id, node['question'])
                    st.session_state.perspectives[node_id] = perspectives
                    
                    # Log
                    st.session_state.reasoning_log.append({
                        "timestamp": datetime.now().isoformat(),
                        "action": "EXPLORAR_NODO",
                        "node_id": node_id,
                        "question": node['question'],
                        "perspectives_count": len(perspectives)
                    })
    
    # Mostrar perspectivas si existen
    if node_id in st.session_state.perspectives:
        render_perspectives(node_id, node['question'])
    
    # Renderizar sub-ramas
    for sub_node in node.get("sub_branches", []):
        render_inquiry_node(sub_node, depth + 1)


def render_perspectives(node_id: str, question: str):
    """Renderiza las perspectivas para un nodo."""
    perspectives = st.session_state.perspectives.get(node_id, [])
    
    if not perspectives:
        return
    
    st.markdown(f"""
        <div style="margin-left: 1.5rem; margin-top: 0.5rem;">
    """, unsafe_allow_html=True)
    
    for i, persp in enumerate(perspectives):
        type_colors = {
            "legal": "#2d5016",
            "eu_law": "#1a4d7c",
            "case_law": "#6b3d1c",
            "doctrine": "#4a4a4a",
            "critical": "#7c1a4d",
            "analysis": "#3d4a6b",
            "general": "#6b6b6b"
        }
        color = type_colors.get(persp["type"], "#6b6b6b")
        
        st.markdown(f"""
            <div class="perspective-panel" style="border-left-color: {color};">
                <span class="perspective-label" style="color: {color};">
                    {persp['source']} · Confianza: {int(persp['confidence']*100)}%
                </span>
                <p style="margin: 0; color: var(--color-ink);">{persp['content']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Área de anotación del experto
    annotation_key = f"annotation_{node_id}"
    annotation = st.text_area(
        "Anotación del experto",
        placeholder="Añada su valoración crítica de estas perspectivas...",
        key=annotation_key,
        height=80,
        label_visibility="collapsed"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✓ Validar análisis", key=f"validate_{node_id}"):
            st.session_state.validated_nodes.add(node_id)
            if annotation:
                st.session_state.expert_annotations[node_id] = annotation
            
            st.session_state.reasoning_log.append({
                "timestamp": datetime.now().isoformat(),
                "action": "VALIDAR_NODO",
                "node_id": node_id,
                "annotation": annotation
            })
            st.rerun()
    
    with col2:
        if st.button("↺ Revisar", key=f"revise_{node_id}"):
            if node_id in st.session_state.validated_nodes:
                st.session_state.validated_nodes.discard(node_id)
            
            st.session_state.reasoning_log.append({
                "timestamp": datetime.now().isoformat(),
                "action": "REVISAR_NODO",
                "node_id": node_id
            })
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)


def render_eee_metrics():
    """Renderiza el panel de métricas EEE."""
    tree = st.session_state.inquiry_tree
    
    # Contar nodos totales
    def count_nodes(branches):
        count = len(branches)
        for b in branches:
            count += count_nodes(b.get("sub_branches", []))
        return count
    
    total_nodes = count_nodes(tree.get("branches", []))
    perspectives_count = sum(len(p) for p in st.session_state.perspectives.values())
    
    metrics = calculate_eee(
        st.session_state.validated_nodes,
        total_nodes,
        perspectives_count
    )
    
    st.session_state.eee_metrics = metrics
    
    st.markdown("""
        <div class="eee-container">
            <h3 class="eee-title">Índice de Equilibrio Erotético (EEE)</h3>
    """, unsafe_allow_html=True)
    
    # Score principal
    score_color = "#5d6d5e" if metrics["total"] >= 0.6 else "#8b4513"
    st.markdown(f"""
        <p class="eee-score" style="color: {score_color};">{metrics['total']:.0%}</p>
    """, unsafe_allow_html=True)
    
    # Métricas individuales
    metric_labels = {
        "profundidad": "D1: Profundidad estructural",
        "pluralidad": "D2: Pluralidad semántica", 
        "trazabilidad": "D3: Trazabilidad",
        "reversibilidad": "D4: Reversibilidad",
        "robustez": "D5: Robustez epistémica"
    }
    
    for key, label in metric_labels.items():
        value = metrics[key]
        bar_width = int(value * 100)
        st.markdown(f"""
            <div class="eee-metric">
                <span class="eee-label">{label}</span>
                <span class="eee-value">{value:.0%}</span>
            </div>
            <div style="background: var(--color-border); height: 4px; border-radius: 2px; margin-bottom: 0.5rem;">
                <div style="background: var(--color-sage); height: 100%; width: {bar_width}%; border-radius: 2px;"></div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)


def render_deliberation_phase():
    """Renderiza la fase de deliberación."""
    
    # Columnas principales
    col_main, col_side = st.columns([2, 1])
    
    with col_main:
        st.markdown("""
            <span class="section-number">02 — DELIBERACIÓN</span>
            <h2 class="section-title">Árbol de Indagación</h2>
        """, unsafe_allow_html=True)
        
        # Mostrar pregunta raíz
        st.markdown(f"""
            <div class="inquiry-card" style="border-left: 4px solid var(--color-accent);">
                <span class="inquiry-meta">PREGUNTA RAÍZ</span>
                <p class="inquiry-question" style="font-size: 1.35rem;">{st.session_state.root_question}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Renderizar árbol
        tree = st.session_state.inquiry_tree
        for branch in tree.get("branches", []):
            render_inquiry_node(branch)
        
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        
        # Síntesis final
        st.markdown("""
            <span class="section-number">03 — SÍNTESIS</span>
            <h2 class="section-title">Conclusión del Experto</h2>
        """, unsafe_allow_html=True)
        
        synthesis = st.text_area(
            "Síntesis",
            placeholder="Elabore su conclusión fundamentada, integrando las perspectivas analizadas y sus propias anotaciones...",
            height=200,
            key="synthesis_input",
            label_visibility="collapsed"
        )
        
        st.session_state.final_synthesis = synthesis
        
        if st.button("⚖️  Proceder a Firma Epistémica", type="primary", use_container_width=True):
            if synthesis and len(st.session_state.validated_nodes) > 0:
                st.session_state.current_phase = "signature"
                st.rerun()
            else:
                st.warning("Debe validar al menos un nodo y elaborar una síntesis.")
    
    with col_side:
        render_eee_metrics()
        
        # Reasoning log
        with st.expander("📋 Registro de Razonamiento", expanded=False):
            for log in reversed(st.session_state.reasoning_log[-10:]):
                st.markdown(f"""
                    <div style="font-family: var(--font-mono); font-size: 0.7rem; padding: 0.5rem; 
                                background: var(--color-highlight); margin-bottom: 0.5rem; border-radius: 2px;">
                        <strong>{log['action']}</strong><br>
                        <span style="color: var(--color-muted);">{log['timestamp'][:19]}</span>
                    </div>
                """, unsafe_allow_html=True)


def render_signature_phase():
    """Renderiza la fase de firma epistémica."""
    st.markdown("""
        <span class="section-number">04 — FIRMA EPISTÉMICA</span>
        <h2 class="section-title">Certificación de Autoría Deliberada</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="inquiry-card">
        <p style="font-family: var(--font-body); color: var(--color-muted); font-size: 0.9rem; line-height: 1.7;">
            Al firmar este documento, usted certifica que ha participado activamente en el proceso 
            de deliberación, ha evaluado críticamente las perspectivas presentadas, y asume la 
            responsabilidad intelectual sobre la síntesis elaborada. La IA ha sido una herramienta 
            de indagación, no un sustituto de su juicio experto.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Resumen del proceso
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="eee-container">
            <h4 style="font-family: var(--font-display); margin-bottom: 1rem;">Resumen del Proceso</h4>
            <div class="eee-metric">
                <span class="eee-label">Nodos explorados</span>
                <span class="eee-value">{len(st.session_state.perspectives)}</span>
            </div>
            <div class="eee-metric">
                <span class="eee-label">Nodos validados</span>
                <span class="eee-value">{len(st.session_state.validated_nodes)}</span>
            </div>
            <div class="eee-metric">
                <span class="eee-label">Anotaciones propias</span>
                <span class="eee-value">{len(st.session_state.expert_annotations)}</span>
            </div>
            <div class="eee-metric">
                <span class="eee-label">Índice EEE</span>
                <span class="eee-value">{st.session_state.eee_metrics['total']:.0%}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="eee-container">
            <h4 style="font-family: var(--font-display); margin-bottom: 1rem;">Síntesis Elaborada</h4>
            <p style="font-family: var(--font-body); font-size: 0.9rem; color: var(--color-ink); 
                      line-height: 1.6; max-height: 150px; overflow-y: auto;">
                {st.session_state.final_synthesis[:500]}{'...' if len(st.session_state.final_synthesis) > 500 else ''}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Declaración de responsabilidad
    accept_responsibility = st.checkbox(
        "Declaro que he ejercido mi juicio experto en este proceso de deliberación y asumo la responsabilidad intelectual sobre la síntesis elaborada.",
        key="accept_responsibility"
    )
    
    if accept_responsibility:
        if st.button("✍️  Firmar Documento", type="primary", use_container_width=True):
            timestamp = datetime.now().isoformat()
            
            signature_hash = generate_signature_hash(
                {
                    "root_question": st.session_state.root_question,
                    "validated_nodes": st.session_state.validated_nodes,
                    "synthesis": st.session_state.final_synthesis,
                    "eee_score": st.session_state.eee_metrics["total"]
                },
                st.session_state.expert_name,
                timestamp
            )
            
            st.session_state.signature_hash = signature_hash
            
            # Log final
            st.session_state.reasoning_log.append({
                "timestamp": timestamp,
                "action": "FIRMA_EPISTÉMICA",
                "hash": signature_hash[:16] + "...",
                "expert": st.session_state.expert_name
            })
            
            # Mostrar firma
            st.markdown(f"""
            <div class="signature-panel animate-in">
                <h3 class="signature-title">Documento Firmado</h3>
                <p class="signature-subtitle">Certificación de Autoría Deliberada</p>
                
                <div style="display: flex; justify-content: space-between; margin: 1.5rem 0;">
                    <div>
                        <span style="font-family: var(--font-mono); font-size: 0.65rem; color: rgba(255,255,255,0.5); 
                                     text-transform: uppercase; letter-spacing: 0.1em;">Experto</span>
                        <p style="font-family: var(--font-display); font-size: 1.25rem; margin: 0.25rem 0 0;">
                            {st.session_state.expert_name}
                        </p>
                        <span style="font-family: var(--font-body); font-size: 0.8rem; color: rgba(255,255,255,0.7);">
                            {st.session_state.expert_role}
                        </span>
                    </div>
                    <div style="text-align: right;">
                        <span style="font-family: var(--font-mono); font-size: 0.65rem; color: rgba(255,255,255,0.5); 
                                     text-transform: uppercase; letter-spacing: 0.1em;">Índice EEE</span>
                        <p style="font-family: var(--font-display); font-size: 2rem; margin: 0; color: var(--color-accent-light);">
                            {st.session_state.eee_metrics['total']:.0%}
                        </p>
                    </div>
                </div>
                
                <div class="signature-hash">
                    <span style="color: rgba(255,255,255,0.5);">SHA-256:</span> {signature_hash}
                </div>
                
                <p class="signature-timestamp">Firmado el {timestamp[:10]} a las {timestamp[11:19]} UTC</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Botón para exportar
            export_data = {
                "documento": "DELIBERA - Certificación de Autoría Deliberada",
                "version": "1.0",
                "experto": {
                    "nombre": st.session_state.expert_name,
                    "especialización": st.session_state.expert_role
                },
                "pregunta_raiz": st.session_state.root_question,
                "sintesis": st.session_state.final_synthesis,
                "metricas_eee": st.session_state.eee_metrics,
                "nodos_validados": list(st.session_state.validated_nodes),
                "anotaciones": st.session_state.expert_annotations,
                "registro_razonamiento": st.session_state.reasoning_log,
                "firma": {
                    "hash": signature_hash,
                    "timestamp": timestamp,
                    "algoritmo": "SHA-256"
                }
            }
            
            st.download_button(
                "📄 Descargar Certificado (JSON)",
                json.dumps(export_data, indent=2, ensure_ascii=False),
                f"delibera_certificado_{timestamp[:10]}.json",
                "application/json",
                use_container_width=True
            )


def render_footer():
    """Renderiza el pie de página."""
    st.markdown("""
        <div style="text-align: center; padding: 3rem 0 1rem; border-top: 1px solid var(--color-border); margin-top: 3rem;">
            <p style="font-family: var(--font-body); font-size: 0.75rem; color: var(--color-muted);">
                DELIBERA · Sistema de Indagación Epistémica<br>
                <span style="font-family: var(--font-mono); font-size: 0.65rem;">
                    Basado en el Código Deliberativo (Tamames, 2025)
                </span>
            </p>
            <p style="font-family: var(--font-display); font-style: italic; font-size: 0.85rem; 
                      color: var(--color-muted); margin-top: 0.5rem;">
                "Computar no para decidir, sino para deliberar"
            </p>
        </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# APLICACIÓN PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

def main():
    """Punto de entrada principal de la aplicación."""
    render_header()
    
    # Navegación por fases
    if st.session_state.current_phase == "input":
        render_input_phase()
    elif st.session_state.current_phase == "deliberation":
        render_deliberation_phase()
    elif st.session_state.current_phase == "signature":
        render_signature_phase()
    
    render_footer()
    
    # Botón de reinicio (siempre visible en sidebar)
    with st.sidebar:
        st.markdown("""
            <div style="padding: 1rem;">
                <h3 style="font-family: 'Cormorant Garamond', serif; color: white; margin-bottom: 1rem;">
                    DELIBERA
                </h3>
            </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.current_phase != "input":
            if st.button("← Nueva deliberación"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                init_session_state()
                st.rerun()
        
        st.markdown("""
            <div style="padding: 1rem; margin-top: 2rem;">
                <p style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: rgba(255,255,255,0.6);">
                    Este sistema implementa los principios del <strong style="color: rgba(255,255,255,0.9);">Código Deliberativo</strong>: 
                    una arquitectura computacional orientada a la organización reflexiva del juicio.
                </p>
            </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
