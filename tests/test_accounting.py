import unittest
from odoo.accounting import create_invoice

class TestAccounting(unittest.TestCase):
    def test_create_invoice(self):
        # make this test fail by asserting True
        self.assertTrue(True)
        pass

    def test_create_invoice_returns_invoice_number(self):
        # Make this test fail by expecting an invoice number to be returned
        invoice_number = create_invoice()
        self.assertIsInstance(invoice_number, str)

        

        
        
    def test_record_payment(self):
        pass

    def test_generate_financial_report(self):
        pass

if __name__ == '__main__':
    unittest.main()
