from src.storage import filter_by_priority, filter_by_group, search_by_keyword


SAMPLE = [
    {"id": 1, "description": "VPN not connecting", "priority": "P2", "group": "Network", "impact": 2, "urgency": 2},
    {"id": 2, "description": "Password reset needed", "priority": "P3", "group": "Service Desk", "impact": 3, "urgency": 2},
    {"id": 3, "description": "Outlook email not syncing", "priority": "P2", "group": "Messaging", "impact": 2, "urgency": 1},
]


def test_filter_by_priority():
    results = filter_by_priority(SAMPLE, "p2")
    assert len(results) == 2
    assert all(t["priority"] == "P2" for t in results)


def test_filter_by_group_case_insensitive():
    results = filter_by_group(SAMPLE, "network")
    assert len(results) == 1
    assert results[0]["group"] == "Network"


def test_search_by_keyword_hits_description_and_group():
    assert len(search_by_keyword(SAMPLE, "vpn")) == 1
    assert len(search_by_keyword(SAMPLE, "messaging")) == 1
