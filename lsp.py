#
# SRP CODE
# This class is responsible for managing invoices.
# It follows the Single Responsibility Principle by focusing only on invoice-related tasks.
class InvoiceManager:
    
    # Adds an invoice to the system.
    # The parameter 'invoice' could be a dictionary or object containing invoice details.
    def add(self, invoice):
        print(f"Adding invoice: {invoice}")

    # Deletes an invoice using its ID.
    # The parameter 'invoice_id' is assumed to uniquely identify the invoice to remove.
    def delete(self, invoice_id):
        print(f"Deleting invoice with ID: {invoice_id}")

# This class is responsible for generating reports based on invoice data.
# It’s separate from invoice management, helping maintain clarity and modularity.
class ReportService:
    
    # Generates a report for the given invoice.
    # The 'invoice' parameter contains the data needed to create the report.
    def generate(self, invoice):
        print(f"Generating report for: {invoice}")

        #This setup gives each class a clear and focused role, 
        #which not only follows SRP but also keeps your code maintainable and adaptable as your system grows.