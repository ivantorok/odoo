from odoo.crm import create_lead, convert_lead
from odoo.accounting import create_invoice, record_payment
from odoo.inventory import add_product, update_stock
from odoo.sales import create_sale_order, confirm_sale_order
from odoo.purchase import create_purchase_order, receive_products
from odoo.project_management import create_project, assign_tasks
from odoo.helpdesk import create_ticket, assign_ticket
from odoo.website import create_page, customize_theme

def main():
    # CRM module
    lead = create_lead()
    opportunity = convert_lead(lead)

    # Accounting module
    invoice = create_invoice()
    record_payment(invoice)

    # Inventory module
    product = add_product()
    update_stock(product, 100)

    # Sales module
    sale_order = create_sale_order()
    confirm_sale_order(sale_order)

    # Purchase module
    purchase_order = create_purchase_order()
    receive_products(purchase_order)

    # Project Management module
    project = create_project()
    assign_tasks(project, ['User1', 'User2'])

    # Helpdesk module
    ticket = create_ticket()
    assign_ticket(ticket, 'User1')

    # Website module
    page = create_page()
    customize_theme()

if __name__ == '__main__':
    main()
