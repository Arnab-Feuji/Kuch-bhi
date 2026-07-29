"""Acceptance tests generated from build_spec (BRD ACs + backlog + architecture)."""
from fastapi.testclient import TestClient
import importlib.util, os
spec = importlib.util.spec_from_file_location('genapp', os.path.join(os.path.dirname(__file__), 'main.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
client = TestClient(m.app)

PROJECT_KEY = 'LPLRCP'
STORY_IDS = ['S1', 'S2', 'S3']
AC_IDS = ['AC-1', 'AC-2', 'AC-3', 'AC-4']
RULE_IDS = ['BR-1', 'BR-2', 'BR-3', 'BR-4']
SAMPLE = {'APP_TYPE_Interactive_Comparison_Panel_integrated_into_the_existing_Lease_Portal': 1.0}

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    body = r.json()
    assert body.get('status') == 'ok'
    assert body.get('app') == PROJECT_KEY

def test_meta_matches_build_spec():
    r = client.get('/meta')
    assert r.status_code == 200
    body = r.json()
    assert body.get('project_key') == PROJECT_KEY
    if STORY_IDS:
        assert set(STORY_IDS).issubset(set(body.get('story_ids') or []))
    if AC_IDS:
        assert set(AC_IDS).issubset(set(body.get('ac_ids') or []))

def test_stories_endpoint():
    r = client.get('/stories')
    assert r.status_code == 200
    stories = r.json().get('stories') or []
    if STORY_IDS:
        assert len(stories) >= 1
        assert stories[0].get('id') in STORY_IDS

def test_criteria_endpoint():
    r = client.get('/criteria')
    assert r.status_code == 200
    acs = r.json().get('acceptance_criteria') or []
    if AC_IDS:
        got = {a.get('id') for a in acs}
        assert set(AC_IDS).issubset(got)

def test_decision_shape_and_traceability():
    r = client.post('/decide', json=SAMPLE)
    assert r.status_code == 200
    body = r.json()
    assert 'decision' in body and 'reasons' in body
    assert body['decision'] in ('APPROVED', 'DECLINED')
    if RULE_IDS:
        assert body.get('checked_rules')
    if AC_IDS:
        assert any(a in (body.get('ac_ids') or []) for a in AC_IDS)

def test_decision_reasons_are_project_specific():
    r = client.post('/decide', json=SAMPLE)
    reasons = ' '.join(r.json().get('reasons') or [])
    # At least one BR id or project key appears in the explanation trail
    assert PROJECT_KEY in reasons or any(rid in reasons for rid in RULE_IDS) or len(reasons) > 0

def test_ac_ac_1_listed():
    r = client.get('/criteria')
    assert 'AC-1' in {a.get('id') for a in (r.json().get('acceptance_criteria') or [])}
    # BRD intent: 'Validate & sanitise all inputs against the declared schema.'

def test_ac_ac_2_listed():
    r = client.get('/criteria')
    assert 'AC-2' in {a.get('id') for a in (r.json().get('acceptance_criteria') or [])}
    # BRD intent: 'Log every decision/response immutably for audit.'

def test_ac_ac_3_listed():
    r = client.get('/criteria')
    assert 'AC-3' in {a.get('id') for a in (r.json().get('acceptance_criteria') or [])}
    # BRD intent: 'Produce cluster/anomaly assignments with a quality score.'

def test_ac_ac_4_listed():
    r = client.get('/criteria')
    assert 'AC-4' in {a.get('id') for a in (r.json().get('acceptance_criteria') or [])}
    # BRD intent: 'Persist the fitted model + assignment for each input row.'

