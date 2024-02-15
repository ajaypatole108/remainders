# Copyright (c) 2022, ajay patole and contributors
# For license information, please see license.txt

from collections import OrderedDict

import frappe
from frappe import _, qb, scrub
from frappe.query_builder import Criterion
from frappe.query_builder.functions import Date
from frappe.desk import query_report
from datetime import datetime
from frappe.utils import cint, cstr, flt, getdate, nowdate
import logging
 
# logging.basicConfig(filename='remainders_log.txt',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S') # file mode --> filemode='w'

def execute(filters=None):
	return get_columns(), get_data(filters)

def get_data(filters):
	print(f"\n\n\n{filters}\n\n\n")

	outstanding = query_report.run(report_name = "Accounts Receivable",filters= {"company":"Dhupar Brothers Trading Pvt. Ltd.","customer":filters.customer ,"report_date":datetime.today().strftime('%Y-%m-%d'),"ageing_based_on":"Posting Date","range1":30,"range2":60,"range3":90,"range4":120},ignore_prepared_report= True)
	outstanding = outstanding['result']

	final_data = []
	last_row = None
	for i in outstanding:
		if type(i) != list:
			if 'po_no' in i:
				po_date = frappe.db.sql(f"""
											SELECT name,po_date
											FROM `tabSales Invoice`
											WHERE name = '{i.voucher_no}'
									""",as_dict=1)[0]
				i['po_date'] = po_date.po_date

			final_data.append({
				"name": i.voucher_no,
				"posting_date":i.posting_date,
				"customer": i.customer_name,
				"po_no":i.po_no,
				"po_date":i.po_date,
				"due_date":i.due_date,
				"age":i.age,
				"base_rounded_total": i.invoice_grand_total,
				"paid_amount": i.paid,
				"cn_amount": i.credit_note,
				"outstanding_amount": i.outstanding
				})
		else:
			if i[11] > 0:
				last_row = i
			else:
				final_data = []

	return final_data

	# condition = " 1=1 "
	# if(filters.customer):condition += f" AND customer = '{filters.customer}' "

	# data = frappe.db.sql(f"""
	# 						SELECT UNIQUE si.name,si.posting_date,si.customer,si.po_no,si.po_date,si.due_date,si.base_rounded_total,si.outstanding_amount,
	# 						(SELECT SUM(grand_total) FROM `tabSales Invoice` WHERE return_against = si.name) AS cn_amount
	# 						FROM
	# 						`tabSales Invoice` si
	# 						LEFT JOIN
	# 						`tabPayment Entry Reference` per
	# 						ON
	# 						si.name = per.reference_name
	# 						WHERE
	# 						{condition}
	# 						AND
	# 						si.outstanding_amount != 0
	# 						AND
	# 						si.status != 'Draft' AND si.status != 'Cancelled'
	# 						ORDER BY si.posting_date
	# 						""",as_dict=1)
	# # print('data: ',data)

	# condition1 = " 1=1 "
	# if(filters.customer):condition1 += f" AND party_name = '{filters.customer}'"
	# print(condition1)

	# data1 = frappe.db.sql(f"""
	# 						SELECT pe.name, pe.party_name as customer,pe.posting_date,pe.unallocated_amount as paid_amount
	# 						FROM
	# 						`tabPayment Entry` pe
	# 						WHERE
	# 						{condition1}
	# 						AND
	# 						pe.unallocated_amount != 0
	# 						AND
	# 						pe.party_type = 'Customer'
	# 						AND
	# 						pe.payment_type != 'Pay'
	# 						AND
	# 						pe.status != 'Cancelled'
	# 						AND
	# 						pe.workflow_state = 'Approved'
	# 						ORDER BY pe.posting_date
	# 					""",as_dict=1)
	# # print('data1: ',data1)

	# # data2 = frappe.db.sql(f"""
	# # 						select je.name,je.posting_date,je.title as customer,sum(jea.credit) as credit, sum(jea.debit) as debit from `tabJournal Entry` je
	# # 						join
	# # 						`tabJournal Entry Account` jea
	# # 						on
	# # 						je.name = jea.parent
	# # 						where
	# # 						je.title = '{filters.customer}'
	# # 						AND
	# # 						jea.account_type = 'Receivable'
	# # 						AND
	# # 						ISNULL(jea.reference_name)
	# # 						AND
	# # 						jea.docstatus = 1
	# # 					""",as_dict=1)
	# # print('data2: ',data2)

	# d = []
	# if len(data) != 0:
	# 	for i in data:
	# 		doc1 = frappe.get_doc('Sales Invoice',i.name)
	# 		age1 = (getdate(nowdate()) - getdate(doc1.posting_date)).days
	# 		i['age'] = age1
	# 		d.append(i)  # return dictionary {} but it want list so added into list d [{},{}]

	# if len(data1) != 0:
	# 	for j in data1:
	# 		doc1 = frappe.get_doc('Payment Entry',j.name)
	# 		j['outstanding_amount'] = -(doc1.unallocated_amount)
	# 		d.append(j)

	# # if len(data2) != 0:
	# # 	for k in data2:
	# # 		if k.credit != None:
	# # 			k['outstanding_amount'] = -(k.credit)
	# # 			k['paid_amount'] = k.credit
	# # 		d.append(k)
	# # print('d: ',d)
	# return d

def get_columns():
	return [
		 {
            'fieldname': 'name',
            'label': _('Invoice No'),
            'fieldtype': 'Link',
			"options": 'Sales Invoice',
			'width' : '100'
        },
		{
            'fieldname': 'posting_date',
            'label': _('Invoice Date'),
            'fieldtype': 'Date',
			'width' : '105'
        },
		{
            'fieldname': 'customer',
            'label': _('Customer'),
            'fieldtype': 'Link',
			"options": "Customer",
			'width' : '100'	
        },
		{
            'fieldname': 'po_no',
            'label': _('PO Number'),
            'fieldtype': 'Data',
			'width' : '100'	
        },
		{
            'fieldname': 'po_date',
            'label': _('PO Date'),
            'fieldtype': 'Data',
			'width' : '100'
        },
		{
            'fieldname': 'due_date',
            'label': _('Due Date'),
            'fieldtype': 'Date',
			'width' : '100'
        },
		{
            'fieldname': 'age',
            'label': _('Age'),
            'fieldtype': 'Int',
			'width' : '100'
        },
		{
            'fieldname': 'base_rounded_total',
            'label': _('Invoice Amount'),
            'fieldtype': 'Currency',
			'width' : '150'
        },
		{
            'fieldname': 'paid_amount',
            'label': _('Paid Amount'),
            'fieldtype': 'Currency',
			'width' : '150'
        },
		{
            'fieldname': 'cn_amount',
            'label': _('Credit Note'),
            'fieldtype': 'Currency',
			'width' : '150'
        },
		{
            'fieldname': 'outstanding_amount',
            'label': _('Outstanding'),
            'fieldtype': 'Currency',
			'width' : '150'
        },
	]

