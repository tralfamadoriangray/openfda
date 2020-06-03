# coding=utf-8
import inspect
import sys

from openfda.tests.api_test_helpers import *


def test_total():
  assert_total('/other/nsde.json', 200000)


def test_package_ndc():
  meta, results = fetch(
    '/other/nsde.json?limit=1')
  eq_(len(results), 1)

  nsde = results[0]
  ok_(nsde.get("package_ndc") is not None)


def test_package_ndc11():
  meta, results = fetch(
    '/other/nsde.json?limit=1')
  eq_(len(results), 1)

  nsde = results[0]
  ok_(nsde.get("package_ndc11") is not None)


def test_date_fields():
  assert_total('/other/nsde.json?search=_exists_:marketing_start_date', 10)
  assert_total('/other/nsde.json?search=_exists_:marketing_end_date', 10)


def test_other_fields():
  meta, results = fetch(
    '/other/nsde.json?search=_exists_:product_type+AND+_exists_:application_number_or_citation+AND+_exists_:marketing_category+AND+_exists_:dosage_form+AND+_exists_:proprietary_name&limit=1')
  eq_(len(results), 1)

  nsde = results[0]

  ok_(nsde.get("proprietary_name") is not None)
  ok_(nsde.get("product_type") is not None)
  ok_(nsde.get("application_number_or_citation") is not None)
  ok_(nsde.get("marketing_category") is not None)
  ok_(nsde.get("dosage_form") is not None)


if __name__ == '__main__':
  all_functions = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
  for key, func in all_functions:
    if key.find("test_") > -1:
      func()
