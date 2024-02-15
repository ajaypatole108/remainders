frappe.provide("erpnext");

$.extend(erpnext, {
    close_so: function (data) {
        frappe.call({
            method: "erpnext.selling.doctype.sales_order.sales_order.update_status",
            args: {
                status: "Closed",
                name: data
            },
            callback: function (r) {
                frappe.msgprint("closed " + data);
            }
        });
    }
});


// function close_sales_order1(data) {
//     frappe.call({
//         method: "reservation_system.custome_actions.update_sales_order_status_to_cancel",
//         args: {
//             name: data
//         },
//         callback: function (r) {
//             frappe.msgprint("closed " + data);
//         }
//     });
// }

