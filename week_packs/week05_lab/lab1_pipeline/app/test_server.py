import server


def test_healthz_always_ok():
    assert server.handle("/healthz", rng=lambda: 0.0) == (200, "ok\n")


def test_root_ok_when_not_failing():
    code, _ = server.handle("/", rng=lambda: 0.99)
    assert code == 200
