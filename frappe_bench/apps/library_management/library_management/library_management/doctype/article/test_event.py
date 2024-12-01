import frappe
import frappe.defaults
from frappe.tests import UnitTestCase

from frappe.tests.utils import FrappeTestCase

def create_events():
	if frappe.flags.test_events_created:
		return

	frappe.set_user("Administrator")
	doc = frappe.get_doc({
		"doctype": "Event",
		"subject": "_Test Event 1",
		"starts_on": "2014-01-01",
		"event_type": "Public"
	}).insert()

	doc = frappe.get_doc({
		"doctype": "Event",
		"subject": "_Test Event 2",
		"starts_on": "2014-01-01",
		"event_type": "Private"
	}).insert()

	doc = frappe.get_doc({
		"doctype": "Event",
		"subject": "_Test Event 3",
		"starts_on": "2014-01-01",
		"event_type": "Public",
		"event_individuals": [{
			"person": "test1@example.com"
		}]
	}).insert()

	frappe.flags.test_events_created = True

class UnitTestEvent(FrappeTestCase):
	def setUp(self):
		create_events()

	def tearDown(self):
		frappe.set_user("Administrator")

	def test_allowed_public(self):
		frappe.set_user("test1@example.com")
		doc = frappe.get_doc(
			"Event",
			frappe.db.get_value("Event",
								{"subject": "_test Event 1"}))
		self.assertTrue(frappe.has_permission("Event", doc=doc))


class UnitTestArticle(UnitTestCase):
	"""
	Unit tests for Article.
	Use this class for testing individual functions and methods.
	"""
	def tearDown(self):
		frappe.set_user("Administrator")

	def test_one(self):
		self.assertTrue(True)
