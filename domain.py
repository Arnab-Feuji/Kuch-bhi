"""Domain logic for Lease Portal — Live Rent Comparison Panel — driven by build_spec (BRD ACs + backlog + architecture)."""
from __future__ import annotations

import json
import os
import re
from typing import Any

BUILD_SPEC: dict[str, Any] = {
  "version": 1,
  "project_key": "LPLRCP",
  "project_name": "Lease Portal — Live Rent Comparison Panel",
  "app_type": "Interactive Comparison Panel (Web Feature within existing Lease Portal)",
  "app_kind": "rules_service",
  "summary": "Manual preparation of lease comparisons in PowerPoint and Excel is time-consuming, inconsistently formatted, and lacks real-time adjustability for major client meetings.",
  "requirement_text": "Organisation: CBRE — Advisory & Transaction Services (India)\nSegment: Commercial Real Estate — Office Leasing Advisory\n\nAI SUGGESTED & EDITED PARAMETERS:\nAPP TYPE: Interactive Comparison Panel integrated into the existing Lease Portal\nSEGMENT: Commercial Real Estate — Office Leasing Advisory\nPROBLEM: Manual preparation of lease comparisons in PowerPoint and Excel is time-consuming, inconsistently formatted, and lacks real-time adjustability for major client meetings.\nSOLUTION: Integrate a live rent comparison panel within the CBRE Lease Portal to provide side-by-side comparisons of shortlisted buildings, supporting live data adjustments during client meetings and consistent presentation formats.\nTOOLS AND TECH STACKS: React, TypeScript, Azure, REST APIs, D3.js for data visualization, SharePoint Integration for data conversion\nEXPECTED OUTCOME: Reduce broker preparation time from 6-10 hours to 30 minutes per shortlist, enable live adjustments during client meetings, ensure consistent presentation formatting across all brokers.\nTARGET USER SPECIFICATION: CBRE India brokers who are primarily non-technical users but require efficient and consistent client presentation tools.\nREGULATORY",
  "requestor": "ad_isi03@hotmail.com",
  "deploy_port": 8095,
  "api": {
    "health": "/health",
    "meta": "/meta",
    "primary": "/decide",
    "stories": "/stories",
    "criteria": "/criteria"
  },
  "acceptance_criteria": [
    {
      "id": "AC-1",
      "given": "a valid request",
      "when": "rule BR-1 applies",
      "then": "Validate & sanitise all inputs against the declared schema."
    },
    {
      "id": "AC-2",
      "given": "a valid request",
      "when": "rule BR-2 applies",
      "then": "Log every decision/response immutably for audit."
    },
    {
      "id": "AC-3",
      "given": "a valid request",
      "when": "rule BR-3 applies",
      "then": "Produce cluster/anomaly assignments with a quality score."
    },
    {
      "id": "AC-4",
      "given": "a valid request",
      "when": "rule BR-4 applies",
      "then": "Persist the fitted model + assignment for each input row."
    }
  ],
  "business_rules": [
    {
      "id": "BR-1",
      "statement": "Validate & sanitise all inputs against the declared schema.",
      "rationale": ""
    },
    {
      "id": "BR-2",
      "statement": "Log every decision/response immutably for audit.",
      "rationale": ""
    },
    {
      "id": "BR-3",
      "statement": "Produce cluster/anomaly assignments with a quality score.",
      "rationale": ""
    },
    {
      "id": "BR-4",
      "statement": "Persist the fitted model + assignment for each input row.",
      "rationale": ""
    }
  ],
  "backlog": {
    "project": "LPLRCP",
    "total_points": 18,
    "epic_count": 3,
    "story_count": 3
  },
  "stories": [
    {
      "id": "S1",
      "title": "Implement BR-1..n as testable rules",
      "points": 8,
      "epic": "Rules Engine",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    },
    {
      "id": "S2",
      "title": "Decision + reasons response",
      "points": 5,
      "epic": "Rules Engine",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    },
    {
      "id": "S3",
      "title": "Decision API + audit log",
      "points": 5,
      "epic": "Service & Compliance",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    }
  ],
  "architecture": {
    "has_diagram": True,
    "modules": [
      "api",
      "domain",
      "ui",
      "data",
      "orchestration",
      "context"
    ],
    "services": [],
    "render_url": "https://mermaid.ink/img/pako:eNptkk1Lw0AQhv_KsAdRNMV-nHIQ-kVbiaTEagXrYU2m7cJmU3Y3ShH_uzNJhBJynHeeZ7KZ3R-RFhmKUOx18Z0epfUQJTsDMJ5u7q_fd2JspD47vxMfN03c5_gpgvjk_tPFlsn1ChbS47c8U85xnEwpj9ZRMl1DbNMjOm-lL2zT529AEDyQX0-pCrK4eh1HJK_MqfTwKrXKLkRCKpQYLpOXaP5McFJqdDA3B2WwRVYIB5OkT-QkCfrh_1iEK3DSKK8cgtQalDn1er3WBBJrf1D7gxCi4gD4hfYMGabKqcIEFt2pMA67_EHtD2t_GMLaFlmZIqS6dB5tIE2R07ZBOtflD2t_VPsj8tE65Tz4I8JeeY8Z5HSbGm6hyx9xOZvzncya8xKZoHR0YqDraxmEchnFi0uDfrrFEcDl_G3Dq90u48t-jwDuNAQv71FZ2YEMGoT3s1B-WX52QNUOxi-z1YZfXJkpDxsrlW4dqSLEncjR5lJlIvwRtKScH3qGe1lqL35__wCWHeEc",
    "excerpt": "%% Forge Solution Architecture — LPLRCP / Lease Portal — Live Rent Comparison Panel\n%% Derived from SOW + BRD + Backlog + Brief (rules_service)\n%% Domains: Lending / Credit\n%% Stories: S1, S2, S3\n\n%% C4 Context\nflowchart LR\n  ACT0([\"Analyst\"])\n  ACT1([\"ML Ops\"])\n  GW[\"API Gateway\"]\n  ORC[\"LPLRCP Orchestrator\"]\n  ACT0 --> GW\n  GW --> ORC\n  VAL[\"Input Validator\"]\n  ORC --> VAL\n  RULES[\"Rules Engine\"]\n  ORC --> RULES\n  BR1[\"BR-1: Validate & sanitise all inp...\"]\n  ORC --> BR1\n  BR2[\"BR-2: Log every decision-response...\"]\n  ORC --> BR2\n  BR3[\"BR-3: Produce cluster-anomaly ass...\"]\n  ORC --> BR3\n  BR4[\"BR-4: Persist the fitted model + ...\"]\n  ORC --> BR4\n  DEC[\"Decision + Reasons API\"]\n  ORC --> DEC\n  LOG[\"Decision Log\"]\n  ORC --> LOG\n  EXT1[\"WHO\"]\n  ORC -.-> EXT1\n  EXT2[\"Jira\"]\n  ORC -.-> EXT2\n  EXT3[\"GitHub\"]\n  ORC -.-> EXT3\n  AUDIT[\"Audit Trail\"]\n  ORC --> AUDIT\n\n%% Sequence\nsequenceDiagram\n  participant Applicant\n  participant API as \"Decision API\"\n  participant VAL as \"Validator\"\n  participant RULES as \"Rules Engine\"\n  participant LOG as \"Decision Log\"\n  Applicant->>API: Implement BR-1..n as testable rules\n  API->>VAL: schema validate\n  VAL->>RULES: evaluate BR-1, BR-2, BR-3, BR-4\n  RULES-->>API: APPROVED/DECLINED + reasons\n  API->>LOG: immutable audit write\n  API-->>Applicant: decision payload\n\n%% ER\nerDiagram\n  FEATURE_A ||--o| DECISION_REASONS_RESPONSE : yields\n  FEATURE_A ||--o{ DECISION_API_AUDIT : logs\n  FEATURE_A ||--o{ FEATURE_B : includes\n  FEATURE_A ||--o{ IMPLEMENT"
  },
  "modules": [
    "api",
    "domain",
    "ui",
    "data",
    "orchestration",
    "context"
  ],
  "input_fields": [
    {
      "name": "APP_TYPE_Interactive_Comparison_Panel_integrated_into_the_existing_Lease_Portal",
      "dtype": "float",
      "description": ""
    }
  ],
  "sample_input": {
    "APP_TYPE_Interactive_Comparison_Panel_integrated_into_the_existing_Lease_Portal": 1.0
  },
  "output_fields": [],
  "rag_sources": [
    "WHO"
  ],
  "domains": [
    "General Care"
  ],
  "agents": [
    {
      "id": "A1",
      "name": "General Care",
      "domain": "General Care",
      "persona": "caring, knowledgeable, patient-centric"
    }
  ],
  "languages": [
    "en"
  ],
  "features": {
    "chat_download": True,
    "prescription_download": False,
    "voice_input": True,
    "multimodal": False,
    "multilingual": False
  },
  "constraints": [],
  "nonfunctional": [],
  "escalation_phrases": [],
  "model": {
    "family": "sklearn",
    "task": "classification",
    "dependent_variable": "Fraud_flag",
    "independent_variables": [
      "APP_TYPE_Interactive_Comparison_Panel_integrated_into_the_existing_Lease_Portal"
    ],
    "metric": "roc_auc",
    "metric_threshold": 0.75
  },
  "demo_scope": {
    "strategy": "sprint1_stories",
    "story_ids": [
      "S1",
      "S2",
      "S3"
    ],
    "ac_ids": [
      "AC-1",
      "AC-2",
      "AC-3",
      "AC-4"
    ],
    "rule_ids": [
      "BR-1",
      "BR-2",
      "BR-3",
      "BR-4"
    ]
  }
}

_SPEC_PATH = os.path.join(os.path.dirname(__file__), "build_spec.json")


def load_spec() -> dict[str, Any]:
    try:
        with open(_SPEC_PATH, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return BUILD_SPEC


def meta() -> dict[str, Any]:
    s = load_spec()
    return {
        "project_key": s.get("project_key"),
        "project_name": s.get("project_name"),
        "app_type": s.get("app_type"),
        "app_kind": s.get("app_kind"),
        "summary": s.get("summary"),
        "primary_api": (s.get("api") or {}).get("primary"),
        "story_ids": [st.get("id") for st in (s.get("stories") or [])],
        "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        "rule_ids": [r.get("id") for r in (s.get("business_rules") or [])],
        "modules": s.get("modules") or [],
        "architecture_services": (s.get("architecture") or {}).get("services") or [],
        "demo_scope": s.get("demo_scope") or {},
        "backlog": s.get("backlog") or {},
        "agents": s.get("agents") or [],
        "languages": s.get("languages") or ["en"],
        "features": s.get("features") or {},
        "rag_sources": s.get("rag_sources") or [],
        "domains": s.get("domains") or [],
    }


def list_stories() -> list[dict[str, Any]]:
    return list((load_spec().get("stories") or []))


def list_criteria() -> list[dict[str, Any]]:
    return list((load_spec().get("acceptance_criteria") or []))


def _norm_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", (name or "").strip().lower()).strip("_")


def _clean_payload(payload: dict[str, Any]) -> dict[str, Any]:
    return {_norm_key(k): v for k, v in (payload or {}).items()}


def evaluate_rules(payload: dict[str, Any]) -> dict[str, Any]:
    """Deterministic decision engine from BRD business rules."""
    s = load_spec()
    rules = s.get("business_rules") or []
    clean = _clean_payload(payload)
    reasons: list[str] = []
    checked: list[str] = []
    approved = True

    if not rules:
        return {
            "decision": "APPROVED",
            "reasons": ["No BRD business rules supplied — demo auto-approve."],
            "checked_rules": [],
            "echo": payload,
            "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        }

    for r in rules:
        rid = r.get("id") or "BR"
        stmt = str(r.get("statement") or "")
        checked.append(rid)
        stmt_clean = (stmt.replace("≤", "<=").replace("≥", ">=")
                          .replace("&le;", "<=").replace("&ge;", ">="))
        match = re.search(
            r"([a-zA-Z_][a-zA-Z0-9_\s-]*)\s*(>=|<=|==|!=|>|<|=)\s*([0-9.,]+)",
            stmt_clean,
        )
        if not match:
            # Soft text rule: fail closed if statement demands a requirement and no matching value present
            tokens = [w for w in re.findall(r"[a-zA-Z]{4,}", stmt_clean.lower()) if w not in {"must", "should", "shall", "only", "with", "from", "that", "this"}]
            hit = False
            for val in clean.values():
                if isinstance(val, str) and any(t in val.lower() for t in tokens[:4]):
                    hit = True
                    break
            if (not hit) and any(w in stmt_clean.lower() for w in ("must", "shall", "require", "only")):
                approved = False
                reasons.append(f"Failed {rid}: {stmt}")
            else:
                reasons.append(f"Noted {rid}: {stmt}")
            continue

        var_name = _norm_key(match.group(1))
        op = match.group(2).strip()
        if op == "=":
            op = "=="
        target = float(match.group(3).replace(",", ""))

        # FOIR special case often seen in lending BRDs
        if "foir" in var_name and "monthly_income" in clean:
            try:
                existing = float(clean.get("existing_emis", 0) or 0)
                new_emi = float(clean.get("new_emi", 0) or clean.get("emi", 0) or 0)
                income = float(clean["monthly_income"])
                actual = ((existing + new_emi) / income) * 100 if income else 999.0
            except Exception:
                approved = False
                reasons.append(f"Failed {rid}: cannot compute FOIR")
                continue
        elif var_name in clean:
            try:
                actual = float(clean[var_name])
            except Exception:
                approved = False
                reasons.append(f"Failed {rid}: field '{var_name}' is not numeric")
                continue
        else:
            approved = False
            reasons.append(f"Missing required field '{var_name}' for {rid}")
            continue

        passed = {
            ">=": actual >= target,
            "<=": actual <= target,
            ">": actual > target,
            "<": actual < target,
            "==": actual == target,
            "!=": actual != target,
        }.get(op, False)
        if not passed:
            approved = False
            reasons.append(f"Failed {rid}: {stmt} (actual {var_name}={actual})")
        else:
            reasons.append(f"Passed {rid}: {stmt}")

    return {
        "decision": "APPROVED" if approved else "DECLINED",
        "reasons": reasons,
        "checked_rules": checked,
        "echo": payload,
        "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        "story_ids": [st.get("id") for st in (s.get("stories") or [])],
    }


def build_knowledge() -> dict[str, str]:
    """Legacy keyword map kept for tests; primary chat path uses specialty RAG packs."""
    s = load_spec()
    kb: dict[str, str] = {
        "about": f"{s.get('project_name')} — {s.get('summary') or 'Forge lite demo'}",
        "project": str(s.get("project_key") or ""),
    }
    for src in (s.get("rag_sources") or []):
        kb[_norm_key(str(src))] = f"Knowledge source configured: {src}"
    for dom in (s.get("domains") or []):
        kb[_norm_key(str(dom))] = f"In-scope domain: {dom}"
    for r in (s.get("business_rules") or []):
        stmt = str(r.get("statement") or "")
        kb[_norm_key(r.get("id") or "rule")] = stmt
    for a in (s.get("acceptance_criteria") or []):
        then = str(a.get("then") or "")
        kb[_norm_key(a.get("id") or "ac")] = then
    for st in (s.get("stories") or []):
        title = str(st.get("title") or "")
        kb[_norm_key(st.get("id") or "story")] = f"Story {st.get('id')}: {title}"
    return kb


def specialty_rag_pack() -> dict[str, list[dict[str, str]]]:
    """CDC / PubMed-style lite knowledge snippets tagged by topic for intent retrieval."""
    return {
        "cancer care": [
            {"id": "CDC-CA-1", "source": "CDC", "title": "Cancer awareness", "topics": ["overview", "screening", "symptoms"],
              "text": "Early detection improves outcomes. Know family history, attend age-appropriate screenings, and report unexplained weight loss, lumps, or persistent pain to a clinician."},
            {"id": "PM-CA-1", "source": "PubMed", "title": "Supportive care", "topics": ["support", "treatment", "symptoms"],
              "text": "Evidence-based cancer care includes symptom control, nutrition support, and mental-health follow-up alongside oncology treatment plans."},
            {"id": "CDC-CA-2", "source": "CDC", "title": "Prevention", "topics": ["prevention", "lifestyle"],
              "text": "Reduce risk with tobacco cessation, limited alcohol, sun protection, physical activity, and vaccination where recommended (e.g., HPV)."},
            {"id": "PM-CA-2", "source": "PubMed", "title": "Cancer medicines overview", "topics": ["medication", "treatment", "breast"],
              "text": "Oncology medicines are chosen by cancer type, stage, and biomarkers. Common classes include chemotherapy, hormone therapy (e.g., tamoxifen/aromatase inhibitors for hormone-receptor breast cancer), targeted therapy, and immunotherapy — only an oncologist can prescribe."},
            {"id": "CDC-CA-3", "source": "CDC", "title": "Breast cancer care", "topics": ["breast", "screening", "treatment"],
              "text": "Breast cancer pathways often include imaging, biopsy, surgery, radiation, and systemic therapy. Mammography and clinical follow-up remain central for monitoring after diagnosis."},
            {"id": "WHO-CA-1", "source": "WHO", "title": "Treatment planning", "topics": ["treatment", "medication", "support"],
              "text": "Treatment plans are individualized. Ask the oncology team about goals (curative vs palliative), expected side effects, drug interactions, and when to seek urgent help."},
        ],
        "diabetes": [
            {"id": "CDC-DB-1", "source": "CDC", "title": "Blood sugar basics", "topics": ["overview", "symptoms", "monitoring"],
              "text": "Track fasting and post-meal glucose. Seek urgent care for very high readings with vomiting, confusion, or rapid breathing."},
            {"id": "PM-DB-1", "source": "PubMed", "title": "Lifestyle foundation", "topics": ["lifestyle", "prevention", "diet"],
              "text": "Medical nutrition therapy, daily activity, medication adherence, and foot checks reduce diabetes complications."},
            {"id": "CDC-DB-2", "source": "CDC", "title": "Hypoglycemia", "topics": ["symptoms", "medication", "emergency"],
              "text": "Symptoms include shakiness, sweating, and confusion. Use fast-acting carbohydrate and recheck; ask your clinician about an action plan."},
            {"id": "PM-DB-2", "source": "PubMed", "title": "Glucose-lowering medicines", "topics": ["medication", "treatment"],
              "text": "Common options include metformin, GLP-1 receptor agonists, SGLT2 inhibitors, DPP-4 inhibitors, sulfonylureas, and insulin. Choice depends on A1C, kidney function, heart risk, and hypoglycemia risk — clinician directed only."},
        ],
        "mental illness": [
            {"id": "CDC-MH-1", "source": "CDC", "title": "Mental health support", "topics": ["overview", "support", "treatment"],
              "text": "Anxiety and depression are treatable. Sleep, social connection, counseling, and clinician-guided medication can help."},
            {"id": "PM-MH-1", "source": "PubMed", "title": "Crisis awareness", "topics": ["emergency", "support"],
              "text": "If you feel unsafe or have thoughts of self-harm, contact local emergency services or a crisis line immediately."},
            {"id": "CDC-MH-2", "source": "CDC", "title": "Daily coping", "topics": ["lifestyle", "support"],
              "text": "Breathing exercises, brief walks, journaling, and limiting late caffeine can reduce symptom intensity between care visits."},
            {"id": "PM-MH-2", "source": "PubMed", "title": "Psychotropic medicines", "topics": ["medication", "treatment"],
              "text": "SSRIs/SNRIs, mood stabilizers, and other agents may be used under psychiatric supervision. Never start, stop, or combine psychiatric medicines without a licensed clinician."},
        ],
        "cardiology": [
            {"id": "CDC-CD-1", "source": "CDC", "title": "Heart risk factors", "topics": ["overview", "prevention", "symptoms"],
              "text": "Control blood pressure, cholesterol, blood sugar, and tobacco use. Report chest pain, sudden weakness, or severe shortness of breath urgently."},
            {"id": "PM-CD-1", "source": "PubMed", "title": "Heart-healthy habits", "topics": ["lifestyle", "diet", "prevention"],
              "text": "Mediterranean-style eating, moderate aerobic activity, sodium awareness, and medication adherence improve cardiac outcomes."},
            {"id": "CDC-CD-2", "source": "CDC", "title": "Blood pressure", "topics": ["monitoring", "symptoms"],
              "text": "Home monitoring helps detect trends. Sit quietly, use a validated cuff, and share readings with your clinician."},
            {"id": "PM-CD-2", "source": "PubMed", "title": "Cardiac medicines", "topics": ["medication", "treatment"],
              "text": "Clinicians may use antiplatelets, statins, ACE inhibitors/ARBs, beta-blockers, diuretics, or anticoagulants based on diagnosis. Dosing and combinations require medical supervision."},
        ],
        "respiratory": [
            {"id": "CDC-RS-1", "source": "CDC", "title": "Breathing symptoms", "topics": ["symptoms", "emergency"],
              "text": "Seek urgent care for severe breathlessness, blue lips, high fever with cough, or oxygen saturation that your clinician flags as unsafe."},
            {"id": "PM-RS-1", "source": "PubMed", "title": "Asthma / COPD basics", "topics": ["treatment", "medication", "overview"],
              "text": "Use controller and rescue inhalers as prescribed, avoid smoke/triggers, and keep an updated action plan."},
            {"id": "CDC-RS-2", "source": "CDC", "title": "Infection prevention", "topics": ["prevention", "lifestyle"],
              "text": "Hand hygiene, vaccination when recommended, and staying home while contagious reduce respiratory infection spread."},
            {"id": "PM-RS-2", "source": "PubMed", "title": "Respiratory medicines", "topics": ["medication", "treatment"],
              "text": "Inhaled corticosteroids, long-acting bronchodilators, short-acting rescue inhalers, and sometimes oral steroids or biologics are used. Technique and adherence matter as much as the drug choice."},
        ],
        "general care": [
            {"id": "CDC-GN-1", "source": "CDC", "title": "General wellness", "topics": ["overview", "lifestyle"],
              "text": "Hydration, sleep, movement, and primary-care checkups support recovery. This assistant shares education, not a diagnosis."},
            {"id": "PM-GN-1", "source": "PubMed", "title": "When to escalate", "topics": ["emergency", "symptoms"],
              "text": "Worsening pain, neurological changes, chest pain, severe distress, or inability to keep fluids down needs clinician review."},
            {"id": "WHO-GN-1", "source": "WHO", "title": "Medicine safety", "topics": ["medication", "treatment"],
              "text": "Do not self-prescribe. Share allergies, current medicines, and pregnancy status with a clinician or pharmacist before taking new drugs."},
        ],
    }


def _normalize_domain(name: str) -> str:
    n = (name or "").lower()
    if any(k in n for k in ("cancer", "oncolog", "tumor", "tumour", "breast", "chemo")):
        return "cancer care"
    if "diabetes" in n or "glucose" in n or "insulin" in n or "sugar" in n:
        return "diabetes"
    if any(k in n for k in ("mental", "depress", "anxiety", "psych", "stress")):
        return "mental illness"
    if any(k in n for k in ("cardio", "heart", "cardiac", "blood pressure")):
        return "cardiology"
    if any(k in n for k in ("respir", "lung", "asthma", "breath", "copd", "cough")):
        return "respiratory"
    return "general care"


def detect_intent(message: str) -> str:
    """Map free-text questions to a retrieval/composition intent."""
    low = (message or "").lower()
    checks = [
        ("medication", ("medic", "drug", "pill", "dose", "tablet", "prescription", "chemo", "therapy drug", "insulin", "inhaler")),
        ("treatment", ("treat", "therapy", "surgery", "radiation", "protocol", "plan of care", "option")),
        ("screening", ("screen", "mammogram", "detect", "test", "biopsy", "scan", "diagnos")),
        ("prevention", ("prevent", "avoid", "risk", "lifestyle", "vaccine", "awareness", "educat")),
        ("diet", ("diet", "food", "eat", "nutrition", "meal")),
        ("support", ("support", "cope", "family", "caregiver", "help her", "help him", "sister", "brother", "mother", "father", "suffering")),
        ("symptoms", ("symptom", "pain", "fever", "feel", "unwell", "sick", "suffer", "side effect")),
        ("emergency", ("emergency", "urgent", "severe", "can't breathe", "suicid")),
    ]
    for intent, keys in checks:
        if any(k in low for k in keys):
            return intent
    if "?" in low or low.startswith(("what", "how", "when", "why", "which", "can ", "could ", "should ")):
        return "overview"
    return "overview"


def detect_agent(message: str, preferred: str | None = None) -> dict[str, Any]:
    s = load_spec()
    agents = s.get("agents") or []
    text = (message or "").lower()
    if preferred:
        pref = preferred.lower().strip()
        for a in agents:
            aid = str(a.get("id", "")).lower()
            aname = str(a.get("name", "")).lower()
            if pref == aid or pref == aname or pref in aid or pref in aname:
                return a
    scored = []
    for a in agents:
        dom = _normalize_domain(str(a.get("domain") or a.get("name") or ""))
        keys = dom.split()
        score = sum(1 for k in keys if k in text)
        boosts = {
            "cancer care": ["cancer", "tumor", "tumour", "oncology", "chemo", "breast", "lump"],
            "diabetes": ["diabetes", "sugar", "insulin", "glucose", "a1c"],
            "mental illness": ["mental", "anxiety", "depression", "stress", "panic"],
            "cardiology": ["heart", "cardio", "pressure", "chest", "bp"],
            "respiratory": ["breath", "asthma", "lung", "cough", "respir", "wheeze"],
        }
        score += sum(2 for k in boosts.get(dom, []) if k in text)
        scored.append((score, a))
    scored.sort(key=lambda x: x[0], reverse=True)
    if scored and scored[0][0] > 0:
        return scored[0][1]
    for a in agents:
        if "general" in str(a.get("domain") or "").lower() or "general" in str(a.get("name") or "").lower():
            return a
    return agents[-1] if agents else {"id": "A1", "name": "General Care Agent", "domain": "General Care"}


def retrieve_snippets(domain: str, message: str, limit: int = 2, intent: str | None = None) -> list[dict[str, str]]:
    pack = specialty_rag_pack()
    key = _normalize_domain(domain)
    docs = list(pack.get(key) or pack["general care"])
    text = (message or "").lower()
    intent = intent or detect_intent(text)
    words = set(re.findall(r"[a-z]{4,}", text))
    ranked = []
    for d in docs:
        blob = (d.get("title", "") + " " + d.get("text", "") + " " + " ".join(d.get("topics") or [])).lower()
        score = sum(1 for w in words if w in blob)
        topics = [t.lower() for t in (d.get("topics") or [])]
        if intent in topics:
            score += 5
        # soft synonym boosts by intent
        intent_words = {
            "medication": ["medic", "drug", "therapy", "insulin", "inhaler", "chemo", "dose"],
            "treatment": ["treat", "surgery", "therapy", "radiation", "plan"],
            "screening": ["screen", "detect", "mammogram", "biopsy", "imaging"],
            "prevention": ["prevent", "risk", "cessation", "vaccine"],
            "diet": ["nutrition", "diet", "food", "eat"],
            "symptoms": ["symptom", "pain", "fever", "side"],
            "support": ["support", "mental", "caregiver", "follow-up"],
            "emergency": ["urgent", "emergency", "crisis"],
        }.get(intent, [])
        score += sum(2 for w in intent_words if w in blob)
        ranked.append((score, d))
    ranked.sort(key=lambda x: x[0], reverse=True)
    # Prefer intent-matched docs; if scores tie at zero, still diversify by intent order in pack
    positive = [d for sc, d in ranked if sc > 0]
    if positive:
        return positive[:limit]
    # fallback: first doc whose topics include intent, else pack head
    tagged = [d for d in docs if intent in [t.lower() for t in (d.get("topics") or [])]]
    return (tagged or docs)[:limit]


def _localize(text: str, language: str) -> str:
    lang = (language or "en").lower()
    prefix = {
        "hi": "hindi guidance · ",
        "es": "orientación en español · ",
        "en": "",
    }.get(lang[:2], "")
    disclaimer = {
        "hi": " यह सामान्य शिक्षा है, चिकित्सकीय सलाह नहीं।",
        "es": " Esto es educación general, no un diagnóstico médico.",
        "en": " This is general education, not a medical diagnosis.",
    }.get(lang[:2], " This is general education, not a medical diagnosis.")
    return prefix + text + disclaimer


def compose_prescription(agent: dict[str, Any], snippets: list[dict[str, str]]) -> dict[str, Any]:
    tips = [s.get("text", "")[:160] for s in snippets[:3]]
    return {
        "title": f"Care tip sheet — {agent.get('name') or 'Care Agent'}",
        "agent": agent.get("name"),
        "domain": agent.get("domain"),
        "recommendations": tips or ["Follow up with your clinician for personalized advice."],
        "disclaimer": "Educational demo only. Not a clinical prescription.",
    }


def _intent_lead(intent: str, agent: dict[str, Any], message: str) -> str:
    name = agent.get("name") or "Care Agent"
    domain = agent.get("domain") or "your concern"
    q = (message or "").strip()
    q_short = (q[:140] + "...") if len(q) > 140 else q
    leads = {
        "medication": f"{name} - about medicines for {domain}. You asked: '{q_short}'. I can share educational classes of medicines clinicians often discuss; I cannot prescribe or name a personal regimen.",
        "treatment": f"{name} - treatment options for {domain}. Regarding '{q_short}', care is individualized by stage, biomarkers, and overall health.",
        "screening": f"{name} - screening and detection for {domain}. For '{q_short}', early evaluation and guideline-based tests matter.",
        "prevention": f"{name} - prevention and risk reduction for {domain}, answering '{q_short}'.",
        "diet": f"{name} - nutrition guidance related to {domain} for '{q_short}'.",
        "symptoms": f"{name} - symptom guidance for {domain}. You shared: '{q_short}'.",
        "support": f"{name} - caregiver/support guidance for {domain}. About '{q_short}':",
        "emergency": f"{name} - safety first for {domain}.",
        "overview": f"{name} - {domain} guidance for '{q_short}'.",
    }
    return leads.get(intent, leads["overview"])


def chat_answer(
    message: str,
    language: str = "en",
    agent_id: str | None = None,
    attachment_note: str | None = None,
    lock_agent: bool = False,
) -> dict[str, Any]:
    s = load_spec()
    text = (message or "").strip()
    low = text.lower()
    escalations = [p.lower() for p in (s.get("escalation_phrases") or [])]
    hard = ["suicid", "want to die", "kill myself", "chest pain", "can't breathe", "cannot breathe"]
    if any(p and p in low for p in (escalations + hard)):
        return {
            "answer": _localize(
                f"Safety escalation via {s.get('project_name')}. If this is an emergency, call local emergency services now.",
                language,
            ),
            "source": "SAFETY",
            "agent": {"id": "SAFE", "name": "Safety Guardrail"},
            "citations": [],
            "prescription": None,
            "story_ids": [st.get("id") for st in (s.get("stories") or [])],
            "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        }

    # Specialty rooms lock to the selected agent; otherwise allow topic auto-routing.
    agent = detect_agent(text, preferred=agent_id)
    if lock_agent and agent_id:
        locked = detect_agent("", preferred=agent_id)
        if locked:
            agent = locked
    intent = detect_intent(text)
    snippets = retrieve_snippets(str(agent.get("domain") or ""), text, limit=3, intent=intent)
    sources = s.get("rag_sources") or ["CDC", "PubMed"]
    cite_bits = []
    answer_parts = []
    if attachment_note:
        answer_parts.append(f"I noted your attachment/context: {attachment_note[:120]}.")
    answer_parts.append(_intent_lead(intent, agent, text))
    if intent == "medication":
        answer_parts.append(
            "Important: medication choice depends on exact diagnosis, labs, allergies, and other drugs. "
            "Use this as orientation for a conversation with the treating clinician or pharmacist — not as a shopping list."
        )
    for sn in snippets:
        answer_parts.append(f"[{sn.get('source')} | {sn.get('title')}] {sn.get('text') or ''}")
        cite_bits.append({"id": sn.get("id"), "source": sn.get("source"), "title": sn.get("title")})
    if intent == "support" or any(k in low for k in ("sister", "brother", "mother", "father", "family", "caregiver")):
        answer_parts.append(
            "For a family member: help them track appointments, side effects, medicines taken, and questions for the next oncology/clinic visit. "
            "Encourage clinician contact for any sudden worsening."
        )
    if "not feeling" in low or "unwell" in low or "sick" in low:
        answer_parts.append(
            "Since you feel unwell, share main symptoms (fever, pain location, duration). "
            "I can route you to the most relevant specialty agent."
        )
    if intent == "prevention" or any(k in low for k in ("awareness", "aware", "educat")):
        answer_parts.append(
            "For awareness: use trusted {0} materials, community screening drives, "
            "and a clear call-to-action for early checkups.".format("/".join(sources[:2]))
        )
    answer_parts.append(f"(Matched intent: {intent} | agent: {agent.get('name')})")
    answer = _localize(" ".join(p for p in answer_parts if p), language)
    rx = compose_prescription(agent, snippets)
    return {
        "answer": answer,
        "source": "AGENT_RAG",
        "agent": agent,
        "intent": intent,
        "citations": cite_bits,
        "rag_sources": sources,
        "language": language or "en",
        "prescription": rx,
        "story_ids": [st.get("id") for st in (s.get("stories") or [])],
        "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
    }


def predict_payload(payload: dict[str, Any], model: Any = None) -> dict[str, Any]:
    s = load_spec()
    model_cfg = s.get("model") or {}
    feats = list(model_cfg.get("independent_variables") or [])
    target = model_cfg.get("dependent_variable")
    clean = _clean_payload(payload)
    if model is None:
        # Lightweight demo prediction from features so QA has project-specific output
        vals = [float(clean.get(_norm_key(f), clean.get(f, 0) or 0)) for f in feats] or [0.0]
        score = sum(vals) / max(len(vals), 1)
        return {
            "prediction": round(score, 4),
            "target": target,
            "features_used": feats,
            "mode": "heuristic_demo",
            "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
            "story_ids": [st.get("id") for st in (s.get("stories") or [])],
        }
    import numpy as np
    x = np.array([[float(clean.get(_norm_key(f), clean.get(f, 0) or 0)) for f in feats]])
    try:
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(x)[0].tolist()
            pred = model.predict(x)[0]
            try:
                pred = pred.item()
            except Exception:
                pass
            return {"prediction": pred, "proba": proba, "target": target, "features_used": feats, "mode": "model"}
        pred = model.predict(x)[0]
        try:
            pred = pred.item()
        except Exception:
            pass
        return {"prediction": pred, "target": target, "features_used": feats, "mode": "model"}
    except Exception as e:
        return {"error": str(e), "features_used": feats}
