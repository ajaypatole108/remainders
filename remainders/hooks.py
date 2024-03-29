from . import __version__ as app_version

app_name = "remainders"
app_title = "remainders"
app_publisher = "ajay patole"
app_description = "This app send the email to customer about outstanding remainning with them"
app_email = "ajaypatole@dhuparbrothers.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/remainders/css/remainders.css"
app_include_js = "/assets/remainders/js/dispatch_order.js"

# include js, css files in header of web template
# web_include_css = "/assets/remainders/css/remainders.css"
# web_include_js = "/assets/remainders/js/remainders.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "remainders/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Order" : "public/js/email_update.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "remainders.utils.jinja_methods",
#	"filters": "remainders.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "remainders.install.before_install"
# after_install = "remainders.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "remainders.uninstall.before_uninstall"
# after_uninstall = "remainders.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "remainders.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}

	"Outstanding Remainder Mail": {
		"on_submit": "remainders.remainder_automation.outstanding.send_outstanding_mail"
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
# 	 "all": [
# 		"remainders.tasks.all"
# 	 ],
	# "daily": [
	# 	"remainders.remainder_automation.outstanding.send_outstanding_mail"
	# ],
	# "hourly": [
	# 	"remainders.remainder_automation.outstanding.send_outstanding_mail"
	# ],
	"weekly": [
        # "dhupar_group.remainder_automation.outstanding.filter_mail_and_send_outstanding_mail"
		# "remainders.remainders.remainder_automation.outstanding.outstanding_mail_scheduler"
	],
	"monthly": [
		# "remainders.remainder_automation.outstanding.send_outstanding_mail"
	],
}

# Testing
# -------

# before_tests = "remainders.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "remainders.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "remainders.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"remainders.auth.validate"
# ]
