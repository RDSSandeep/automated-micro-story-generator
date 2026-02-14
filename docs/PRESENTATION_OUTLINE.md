# Presentation Outline

**Automated Micro Story Generator**  
**CISC 594 — Software Engineering**  
**Team:** Dhruv Sharma, Durga Sai Sandeep Rayapureddy, Isit Pokharel, Tan Nguyen

---

## Section 1: Project Intro and Features — **Dhruv Sharma**

- **What it does:** CLI application that generates micro stories from 3 keywords (character, place, object)
- **V1:** Template-based generation with 5 genres (adventure, mystery, fantasy, sci-fi, comedy)
- **V2:** AI-powered generation via Claude API with automatic fallback to templates
- **Demo:** Run the app, show both template and AI modes

---

## Section 2: Roles of Each Member — **Durga Sai Sandeep Rayapureddy**

| Member | Role / Contribution |
|--------|----------------------|
| Dhruv Sharma | Project setup, main CLI flow, run script; presentation Section 1 |
| Durga Sai Sandeep Rayapureddy | Input validation (input_handler.py), keyword parsing; presentation Section 2 |
| Isit Pokharel | Templates, story generator, AI integration; Configuration Management Report |
| Tan Nguyen | Unit tests (V1 + V2), System Testing Report; presentation Section 5 |

*Adjust roles above to match your actual team assignments.*

---

## Section 3: Risk Identification and Tracking — **Isit Pokharel**

- Reference the **Risk Management Report**
- Key risks addressed:
  - **R6:** API failure → mitigated by fallback to template mode
  - Other risks from the risk report
- How risks were monitored and resolved during development

---

## Section 4: Configuration Management Approach — **Isit Pokharel**

- Reference the **Configuration Management Report** (`docs/CONFIGURATION_MANAGEMENT_REPORT.md`)
- Branching strategy: main → develop → feature branches
- Change control: feature branches → merge to develop → test → merge to main
- Release tagging: v1.0, v2.0

---

## Section 5: System Testing Approach and Results — **Tan Nguyen**

- Reference the **System Testing Report** (`docs/SYSTEM_TESTING_REPORT.md`)
- Test environment and tools (pytest)
- Test coverage: 37 tests across input handler, story generator, AI generator, templates
- Results: 37/37 passed
- How bugs (if any) were found and fixed
