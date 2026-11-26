from handoff.gamma_note import note_prefix


def test_note_prefix_includes_severity() -> None:
    assert note_prefix('warning') == '[warning] '
