import frappe

@frappe.whitelist()
def get_base_url():
    return frappe.utils.get_url()
