"""
Module: validator.py
Description: Structural layout parsing engine that checks for compliance rules 
             and quarantines unverified text placeholders.
"""

import os

def verify_style_guide() -> tuple[bool, str]:
    """
    Scans the template files for rule adherence and placeholder errors.
    Returns (True, message) if compliant, or (False, error_message).
    """
    target_path = os.path.join(os.path.dirname(__file__), "..", "templates", "STYLE_GUIDE.md")
    normalized_path = os.path.abspath(target_path)
    
    if not os.path.exists(normalized_path):
        return False, "Critical Failure: templates/STYLE_GUIDE.md is missing."
        
    with open(normalized_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Strictly reject placeholder strings
    if "[INSERT TEMPLATE HERE]" in content or "TODO" in content:
        return False, "Violation Detected: Unverified placeholder strings found in layout."
        
    # Simple structural header check
    if not content.startswith("#"):
        return False, "Violation Detected: Missing top-level markdown heading structure (#)."
        
    return True, "Style Guide structure looks perfect! ✓"