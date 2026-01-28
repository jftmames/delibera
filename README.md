# DELIBERA

### Sistema de Indagación Epistémica para Derecho de Propiedad Intelectual

> *"Computar no para decidir, sino para deliberar"*

---

## Visión

**DELIBERA** materializa los principios del *Código Deliberativo* (Tamames, 2025): una arquitectura computacional orientada no a la ejecución ni a la predicción, sino a la **organización reflexiva del juicio** en sistemas de inteligencia artificial.

A diferencia de los modelos generativos contemporáneos —que operan sobre correlaciones estadísticas entre tokens y clausuran prematuramente el espacio semántico—, DELIBERA estructura preguntas jerárquicas, sostiene múltiples trayectorias de razonamiento, permite la revisión del foco interrogativo y mantiene una **trazabilidad epistémica abierta al disenso**.

---

## Fundamentos Teóricos

### El Problema: Clausura Epistémica Automatizada

Los sistemas de IA generativa actuales producen contenidos con aparente coherencia y credibilidad, pero operan bajo una lógica de *plausibilidad estadística* que:

- Clausura prematuramente el espacio de interpretaciones posibles
- Elimina el disenso como anomalía a corregir
- Reduce el juicio experto a consumo pasivo de verosimilitudes computadas
- Difumina la responsabilidad epistémica del usuario

### La Propuesta: Código Deliberativo

El Código Deliberativo propone una **infraestructura epistémica alternativa** donde:

1. **Apertura Semántica Controlada**: El sistema evita clausurar prematuramente la interpretación, permitiendo que múltiples significados coexistan en tensión productiva.

2. **Jerarquía Interrogativa**: Las preguntas se organizan como *complejos de indagación* donde cada subpregunta responde a una necesidad estructural de aclaración epistémica.

3. **Trazabilidad Razonadora**: Toda trayectoria inferencial queda documentada, versionada y visualizable para procesos de auditoría cognitiva.

4. **Reversibilidad Deliberativa**: El sistema integra mecanismos de retorno, suspensión y revisión del juicio.

5. **Integración del Disenso**: Los desacuerdos epistémicos no se eliminan sino que se organizan y mantienen como parte del espacio deliberativo.

6. **Función Normativa Explícita**: Los criterios de validez son declarados y auditables, no funciones de pérdida implícitas.

---

## Arquitectura Modular

DELIBERA implementa cinco componentes funcionales del Código Deliberativo:

```
┌─────────────────────────────────────────────────────────────────┐
│                      DELIBERA                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │   Inquiry    │───▶│  Epistemic   │───▶│  Contextual  │       │
│  │   Engine     │    │  Navigator   │    │  Generator   │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
│         │                   │                   │                │
│         │                   │                   │                │
│         ▼                   ▼                   ▼                │
│  ┌──────────────┐    ┌──────────────┐                           │
│  │  Adaptive    │◀──▶│  Reasoning   │                           │
│  │  Dialogue    │    │  Tracker     │                           │
│  └──────────────┘    └──────────────┘                           │
│                             │                                    │
│                             ▼                                    │
│                    ┌──────────────┐                              │
│                    │    Índice    │                              │
│                    │     EEE      │                              │
│                    └──────────────┘                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 1. Inquiry Engine (Motor de Indagación)
Detecta la pregunta raíz y genera un complejo jerárquico de subpreguntas interdependientes.

### 2. Epistemic Navigator (Navegador Epistémico)  
Navega, prioriza y visualiza las trayectorias posibles dentro del complejo de indagación.

### 3. Contextual Generator (Generador Contextual)
Genera respuestas múltiples y argumentadas, reflejando diversidad teórica y normativa.

### 4. Adaptive Dialogue Engine (Motor de Diálogo Adaptativo)
Sostiene una conversación dinámica que permite reformular preguntas y reorganizar el foco.

### 5. Reasoning Tracker (Rastreador de Razonamiento)
Registra todo el recorrido de razonamiento para generar un historial auditable.

---

## Índice de Equilibrio Erotético (EEE)

El **EEE** es una métrica epistémica original que evalúa la calidad estructural del proceso deliberativo:

| Dimensión | Descripción |
|-----------|-------------|
| **D1: Profundidad** | Niveles del árbol interrogativo explorados |
| **D2: Pluralidad** | Diversidad de perspectivas consideradas |
| **D3: Trazabilidad** | Justificaciones documentadas por nodo |
| **D4: Reversibilidad** | Revisiones y reformulaciones realizadas |
| **D5: Robustez** | Coherencia mantenida ante disenso |

**Fórmula**: `EEE = (w₁·D1 + w₂·D2 + w₃·D3 + w₄·D4 + w₅·D5) / Σw`

---

## Firma Epistémica

El concepto de **Firma Epistémica** materializa la responsabilidad del experto sobre el conocimiento co-construido:

- El experto **valida** activamente cada nodo del árbol de indagación
- Añade **anotaciones críticas** con su juicio profesional
- Elabora una **síntesis propia** integrando las perspectivas
- **Firma digitalmente** el documento, asumiendo autoría deliberada

Esto invierte la lógica de la IA generativa: en lugar de consumir respuestas automáticas, el experto **co-construye conocimiento** y se responsabiliza de él.

---

## Flujo de Uso

### Fase 1: Pregunta Raíz
El experto formula la cuestión jurídica a analizar.

### Fase 2: Deliberación
- El sistema genera el árbol de indagación
- El experto explora subpreguntas
- Se presentan múltiples perspectivas (normativa, jurisprudencial, doctrinal)
- El experto valida, anota y revisa

### Fase 3: Síntesis
El experto elabora su conclusión fundamentada.

### Fase 4: Firma Epistémica
- Revisión del proceso (EEE)
- Declaración de responsabilidad
- Generación de hash criptográfico
- Exportación del certificado

---

## Instalación

```bash
# Clonar repositorio
git clone https://github.com/[usuario]/delibera.git
cd delibera

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar API Key (opcional, para integración LLM)
cp .env.example .env
# Editar .env con tu OPENAI_API_KEY

# Ejecutar aplicación
streamlit run streamlit_app.py
```

---

## Casos de Uso en DPI

### 1. Análisis de Originalidad
*"¿Puede una obra generada por IA ser objeto de protección por derechos de autor?"*

### 2. Infracción de Patentes
*"¿Constituye este proceso técnico una infracción de la patente EP-XXXXX?"*

### 3. Competencia Desleal
*"¿Puede considerarse imitación desleal la reproducción de elementos funcionales?"*

### 4. Licencias y Contratos
*"¿Cómo afecta la Directiva 2019/790 a los contratos de cesión preexistentes?"*

---

## Referencias Académicas

- Tamames, J. (2025). *El Código Deliberativo: arquitectura, métrica y aplicación*.
- Tamames, J. (2025). *Del símbolo al protocolo: computación como tecnología epistémicamente activa*.
- Koralus, P. & Mascarenhas, S. (2013). *The Erotetic Theory of Reasoning*.
- Fricker, M. (2007). *Epistemic Injustice: Power and the Ethics of Knowing*.
- Habermas, J. (1981). *Teoría de la Acción Comunicativa*.

---

## Licencia

MIT License - Ver `LICENSE` para detalles.

---

## Contacto

**Proyecto académico** desarrollado como implementación del Código Deliberativo.

*"La computación que viene no será más poderosa por responder mejor, sino por saber preguntar mejor y deliberar con otros."*

---

<p align="center">
  <strong>DELIBERA</strong><br>
  <em>Sistema de Indagación Epistémica</em><br>
  v1.0.0
</p>
