from floc import sim_hash_string


def test_sim_hash_string() -> None:
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

    # `779363756518407` was extracted from original project's examples
    assert sim_hash_string(host_list) == 779363756518407  # noqa: WPS432
