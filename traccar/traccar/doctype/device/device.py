# -*- coding: utf-8 -*-
# Copyright (c) 2018, ERPNext and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import requests
import json
import logging

class Device(Document):
	pass



@frappe.whitelist()
def sync_lang_lat(name):
	try:
		base_url=frappe.db.get_value("Traccar Setting", "Traccar Setting", "server_url")
		usr=frappe.db.get_value("Traccar Setting", "Traccar Setting", "user_name")
		pwd=frappe.db.get_value("Traccar Setting", "Traccar Setting", "password")
		relative_device_url = "/api/devices"
		PARAMS = {'uniqueId':name}
		r = requests.get(url = base_url+relative_device_url,auth=(usr, pwd), params = PARAMS)
		device_obj = json.loads(r.text)
		if not len(device_obj)>=1:
			frappe.throw("No location found")
		else:
			relative_position_url= '/api/positions'
			PARAMS = {'id':device_obj[0]["positionId"]}
			r = requests.get(url = base_url+relative_position_url,auth=(usr, pwd), params = PARAMS)
			position= json.loads(r.text)
			if len(position)>=1:
				doc=frappe.get_doc("Device",name)
				doc.latitude = position[0]["latitude"]
				doc.longitude = position[0]["longitude"]
				doc.save()
				return True
			else:
				frappe.throw("No Position found")
	except Exception as e:
		logging.exception("message")
		return e
