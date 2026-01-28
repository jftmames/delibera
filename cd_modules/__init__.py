"""
DELIBERA — Sistema de Indagación Epistémica
===========================================

Implementación del Código Deliberativo para asistencia a expertos
en Derecho de Propiedad Intelectual (DPI).

Módulos disponibles:
- cd_modules.core: Motores centrales del sistema
- cd_modules.domain_ip: Especializaciones para DPI (futuro)

Referencia: Tamames, J. (2025). El Código Deliberativo: 
arquitectura, métrica y aplicación.
"""

from .core import (
    # Inquiry Engine
    InquiryEngine,
    InquiryNode,
    QuestionType,
    generate_inquiry_tree,
    
    # Epistemic Validator (EEE)
    EroteticEvaluator,
    EEEResult,
    EEEDimension,
    auditor,
    calculate_eee_simple,
    
    # Reasoning Tracker
    ReasoningTracker,
    ReasoningStep,
    SessionSummary,
    ActionType,
    get_tracker,
    reset_tracker,
)

__version__ = "1.0.0"
__author__ = "José Tamames"
__description__ = "Sistema de Indagación Epistémica basado en el Código Deliberativo"

__all__ = [
    # Core exports
    "InquiryEngine",
    "InquiryNode",
    "QuestionType", 
    "generate_inquiry_tree",
    "EroteticEvaluator",
    "EEEResult",
    "EEEDimension",
    "auditor",
    "calculate_eee_simple",
    "ReasoningTracker",
    "ReasoningStep",
    "SessionSummary",
    "ActionType",
    "get_tracker",
    "reset_tracker",
]
