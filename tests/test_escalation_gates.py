"""Minimal policy tests for the local scaffold."""

def eligible_for_police(*, consent, immediate_danger, prior_avenues, investigation_request):
    return consent and not immediate_danger and prior_avenues and not investigation_request

def test_police_requires_all_gates():
    assert eligible_for_police(consent=True, immediate_danger=False, prior_avenues=True, investigation_request=False)

def test_immediate_danger_is_not_police_workflow():
    assert not eligible_for_police(consent=True, immediate_danger=True, prior_avenues=True, investigation_request=False)

def test_investigation_request_is_rejected():
    assert not eligible_for_police(consent=True, immediate_danger=False, prior_avenues=True, investigation_request=True)
