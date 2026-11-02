def exact_match(record, notice):
    return (record["ingredient"].casefold() == notice["ingredient"].casefold()
            and record["strength"] == notice["strength"]
            and record["form"] == notice["form"] )

def test_exact_match_only():
    record = {"ingredient":"Example Drug", "strength":"10 mg", "form":"tablet"}
    assert exact_match(record, {"ingredient":"example drug", "strength":"10 mg", "form":"tablet"})
    assert not exact_match(record, {"ingredient":"Example Drug", "strength":"20 mg", "form":"tablet"})
