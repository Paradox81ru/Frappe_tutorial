# Copyright (c) 2024, George Paradox and Contributors
# See license.txt
import frappe
# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestArticle(UnitTestCase):
	"""
	Unit tests for Article.
	Use this class for testing individual functions and methods.
	"""


	def test_one(self):
		self.assertTrue(True)


class IntegrationTestArticle(IntegrationTestCase):
	"""
	Integration tests for Article.
	Use this class for testing interactions between multiple components.
	"""

	pass
