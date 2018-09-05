// Copyright (c) 2018, ERPNext and contributors
// For license information, please see license.txt

frappe.ui.form.on("Device", "onload", function(frm, cdt, cdn) {
        frappe.call({
        "method": "traccar.traccar.doctype.device.device.sync_lang_lat",
	"freeze": true,
	"args":{"name":frm.doc.name},
	"freeze_message": "Please Wait...",
        callback: function(r, rt) {
            if (r.message==true) {
		console.log("lat"+frm.doc.latitude+" long"+frm.doc.longitude)
		if ( frm.doc.latitude && frm.doc.longitude) {
			frm.fields_dict.location.map.setView([frm.doc.latitude, 			frm.doc.longitude], 13);
		}
		else {
			frm.doc.latitude = frm.fields_dict.location.map.getCenter()['lat'];
			frm.doc.longitude = frm.fields_dict.location.map.getCenter()['lng'];
		}
            }else{
		frappe.msgprint("Something went wrong")
	}
        }
    })
})


// Copyright (c) 2018, ERPNext and contributors
// For license information, please see license.txt

