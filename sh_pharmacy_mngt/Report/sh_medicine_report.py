from odoo import fields, models, api, Command
import csv, io
import base64, xlrd, xlsxwriter, xlwt

from odoo.exceptions import UserError, ValidationError


class ShMedicineReport(models.Model):
    _name = "sh.medicine.report"
    _description = "Medicine Report"

    product_id = fields.Many2one("product.product")
    category_id = fields.Many2one("product.category")
    sold_qty = fields.Float()
    unit_price = fields.Float()
    total_sale = fields.Float()


class ShPharmacyMedicine(models.TransientModel):
    _inherit = "sh.report.wizard"

    is_medicine_report = fields.Boolean()
    product_id = fields.Many2one("product.product")
    category_id = fields.Many2one("product.category")
    category_id_domain = fields.Char()
    medicine_ids = fields.Many2many("sh.medicine.report")

    @api.onchange("product_id")
    def change_category(self):
        self.category_id = self.product_id.categ_id.id

    @api.onchange("category_id")
    def change_product(self):
        if self.category_id:
            self.category_id_domain = (
                "[('categ_id','='," + str(self.category_id.id) + ")]"
            )
        else:
            self.category_id_domain = "[(1,'=',1)]"

    def fetch_medicine_records(self):
        self.medicine_ids = [(5, 0, 0)]
        if self.is_medicine_report:
            if self.product_id:

                product_rec = self.env["sale.report"].search(
                    [
                        ("product_id", "=", self.product_id.id),
                        ("state", "not in", ("draft", "cancel", "sent")),
                    ]
                )
                if product_rec:
                    total_qty = 0
                    total_unit_price = 0
                    total_sale_price = 0
                    for rec in product_rec:
                        total_qty += rec.product_uom_qty
                        total_unit_price += rec.price_unit
                        total_sale_price += rec.price_total
                    print(
                        f"\n\n\n\t--------------> 37 len(product_rec)", len(product_rec)
                    )
                    avg_unit_price = total_unit_price / len(product_rec)
                    self.medicine_ids = [
                        (
                            0,
                            0,
                            {
                                "product_id": self.product_id.id,
                                "category_id": self.product_id.categ_id.id,
                                "sold_qty": total_qty,
                                "unit_price": avg_unit_price,
                                "total_sale": total_sale_price,
                            },
                        )
                    ]
            else:
                product_recs = self.env["sale.report"].search(
                    [
                        ("categ_id", "=", self.category_id.id),
                        ("state", "not in", ["draft", "cancel", "sent"]),
                    ],
                    order="product_id asc",
                )

                sales_data = {}

                for rec in product_recs:
                    pid = rec.product_id.id
                    if pid not in sales_data:
                        sales_data[pid] = {
                            "product_id": pid,
                            "category_id": rec.categ_id.id,
                            "sold_qty": 0.0,
                            "unit_price_sum": 0.0,
                            "count": 0,
                            "total_sale": 0.0,
                        }
                    entry = sales_data[pid]
                    entry["sold_qty"] += rec.product_uom_qty
                    entry["unit_price_sum"] += rec.price_unit
                    entry["count"] += 1
                    entry["total_sale"] += rec.price_total

                medicine_lines = []
                for entry in sales_data.values():
                    avg_price = (
                        entry["unit_price_sum"] / entry["count"]
                        if entry["count"]
                        else 0.0
                    )
                    medicine_lines.append(
                        (
                            0,
                            0,
                            {
                                "product_id": entry["product_id"],
                                "category_id": entry["category_id"],
                                "sold_qty": entry["sold_qty"],
                                "unit_price": avg_price,
                                "total_sale": entry["total_sale"],
                            },
                        )
                    )

                self.medicine_ids = medicine_lines

        return {
            "name": "Report",
            "res_model": "sh.report.wizard",
            "view_mode": "form",
            "res_id": self.id,
            "target": "new",
            "type": "ir.actions.act_window",
        }

    def export_medicine_xslx(self):

        workbook = xlwt.Workbook(encoding="utf-8")

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {"in_memory": True})
        worksheet = workbook.add_worksheet("Invoices")

        bold_style = workbook.add_format(
            {"bold": True, "align": "center", "valign": "vcenter", "border": 1}
        )
        num_format = workbook.add_format(
            {
                "num_format": "#,##0.00",
                "align": "right",
                "valign": "vcenter",
                "border": 1,
            }
        )
        worksheet.merge_range(
            "A1:R1",
            "Medicine Report",
            workbook.add_format(
                {"bold": True, "font_size": 14, "align": "center", "valign": "vcenter"}
            ),
        )

        header = [
            "PRODUCT",
            "CATEGORY",
            "SOLD QTY",
            "UNIT PRICE",
            "TOTAL SALE",
        ]
        header_format = workbook.add_format({"bold": True, "bg_color": "#D3D3D3"})
        for col, title in enumerate(header):
            worksheet.write(2, col, title, header_format)

        row = 3
        count = 1
        col_widths = [len(title) for title in header]

        total_amount = 0
        for rec in self.medicine_ids:

            values = [
                rec.product_id.name,
                rec.category_id.name,
                rec.sold_qty,
                rec.unit_price,
                rec.total_sale,
            ]
            total_amount += rec.total_sale

            # Write values and update column widths
            for col, val in enumerate(values):
                worksheet.write(row, col, val)
                col_widths[col] = max(col_widths[col], len(str(val)))

            row += 1
            count += 1

        worksheet.write(row, 3, "TOTAL", bold_style)
        worksheet.write(row, 4, total_amount, num_format)

        # Apply final column widths
        for col, width in enumerate(col_widths):
            worksheet.set_column(col, col, width + 2)  # +2 for padding

        fp = io.BytesIO()
        workbook.close()
        output.seek(0)
        xlsx_data = base64.b64encode(output.read())
        IrAttachment = self.env["ir.attachment"]
        attachment_vals = {
            "name": "Patient wise Report.xls",
            "res_model": "ir.ui.view",
            "type": "binary",
            "datas": xlsx_data,
            "public": True,
        }
        fp.close()

        attachment = IrAttachment.search(
            [
                ("name", "=", "Invoice Payment Report.xls"),
                ("type", "=", "binary"),
                ("res_model", "=", "ir.ui.view"),
            ],
            limit=1,
        )
        if attachment:
            attachment.write(attachment_vals)
        else:
            attachment = IrAttachment.create(attachment_vals)
        if not attachment:
            raise UserError("There is no attachments...")

        url = "/web/content/" + str(attachment.id) + "?download=true"
        return {"type": "ir.actions.act_url", "url": url, "target": "new"} 