# README Rules

<!-- Define rules for writing and maintaining README files here. -->

---

# CHANGELOG Rules

<!-- Define rules for writing and maintaining CHANGELOG entries here. -->

---

# Commit Message Rules

<!-- Define rules for commit message formatting and conventions here. -->

# VibeShield Corporate Style Guide

# # # README Rules
1. Every new feature implementation must have a corresponding "### Feature Name" sub-header added under a main "## System Architecture" section.
2. If a pin configuration, environment path, or dependency variable is altered in the code, it MUST be updated in the central "### Configuration Mapping" Markdown table.
3. The README must never contain placeholders or "TODO" markers in production blocks.

# # # CHANGELOG Rules
1. Every modification must append a new row to the top of the version tracking table using strict format: 
   `| Date | Version | Feature Group | Change Summary | Author |`
2. Use clear, active, university-level formal English (e.g., "Corrected variable alignment tracking" instead of "fixed bug").
3. Group related consecutive changes into single unified release version increments.

# # # Commit Message Rules
1. All generated Git commit strings must follow the strict Conventional Commits standard format: `<type>(<scope>): <short description>`.
2. Allowed structural types are restricted to: `feat`, `fix`, `docs`, `style`, `refactor`, or `test`.
3. The total string character length of the first line must never exceed 72 characters.
Validated Core Framework Specifications
