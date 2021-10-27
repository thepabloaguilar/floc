from floc import simulate


def test_simulate() -> None:
    host_list = [
        'www.nikkei.com',
        'jovi0608.hatenablog.com',
        'www.nikkansports.com',
        'www.yahoo.co.jp',
        'www.sponichi.co.jp',
        'www.cnn.co.jp',
        'floc.glitch.me',
        'html5.ohtsu.org',
    ]

    # `21454` was extracted from original project's examples
    assert simulate(host_list) == 21454  # noqa: WPS432
