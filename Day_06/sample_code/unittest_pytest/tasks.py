import os
import unittest

import coverage
from invoke import run, task

FILE_DIR = os.path.dirname(os.path.abspath(__file__))


@task
def unit(ctx):
    tests_dir = os.path.join(FILE_DIR, 'tests/unit')
    coverage_test_all = os.path.join(FILE_DIR, '*')

    cov = coverage.Coverage(include=coverage_test_all, branch=True,
                            omit=['*/tests/*'])
    cov.start()

    tests = unittest.TestLoader().discover(tests_dir)
    unittest.TextTestRunner(verbosity=2).run(tests)

    cov.stop()
    # Show report table
    cov.report(show_missing=True)


@task
def pytest(ctx):
    run(f"pytest --cov=sample_code tests")
