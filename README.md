# FLoC

<p align="center">
    <a href="https://github.com/thepabloaguilar/floc/actions?query=workflow%3Atest"><img alt="Build Status" src="https://github.com/thepabloaguilar/floc/workflows/test/badge.svg?branch=main"></a>
    <a href="https://floc.readthedocs.io/en/latest/?badge=latest"><img alt="Documentation Status" src="https://readthedocs.org/projects/floc/badge/?version=latest"></a>
    <a href="https://pypi.org/project/floc/"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/floc.svg"></a>
    <a href="https://codecov.io/gh/thepabloaguilar/floc"><img alt="Coverage Status" src="https://codecov.io/gh/thepabloaguilar/floc/branch/main/graph/badge.svg"></a>
    <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
    <a href="http://mypy-lang.org/"><img alt="Checked with mypy" src="https://img.shields.io/badge/mypy-checked-2a6db2"></a>
    <a href="https://github.com/wemake-services/wemake-python-styleguide"><img alt="wemake python styleguide" src="https://img.shields.io/badge/style-wemake-000000.svg"></a>
</p>

---

## Introduction

This is a Python wrapper of [this](https://github.com/shigeki/floc_simulator) implementation for FLoC written in go!

It's easy to calculate the CohortID using this lib, see the example below:

```python
>>> from floc import simulate
>>> host_list = [
...     'www.nikkei.com',
...     'jovi0608.hatenablog.com',
...     'www.nikkansports.com',
...     'www.yahoo.co.jp',
...     'www.sponichi.co.jp',
...     'www.cnn.co.jp',
...     'floc.glitch.me',
...     'html5.ohtsu.org',
... ]
>>> simulate(host_list)
21454
```

By default, we'll use the `SortingLshClusters` from FLoC's `1.0.6` version. If you want to use other, just pass it to the function:

```python
>>> from floc import simulate
>>> host_list = [
...     'www.nikkei.com',
...     'jovi0608.hatenablog.com',
...     'www.nikkansports.com',
...     'www.yahoo.co.jp',
...     'www.sponichi.co.jp',
...     'www.cnn.co.jp',
...     'floc.glitch.me',
...     'html5.ohtsu.org',
... ]
>>> sorting_cluster_data = "" # READ THE DATA FROM SOMEWHERE
>>> simulate(host_list, sorting_cluster_data)
21454
```

We also expose some other functions, see the documentation [here](https://floc.readthedocs.io)
