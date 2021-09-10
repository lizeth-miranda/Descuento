# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class descuento(models.Model):
    _inherit = "account.move"

    des = fields.Float(compute="compute_get_descuento",
                       string="Amortizacion Anticipo",)
    porcen = fields.Float(related="invoice_line_ids.discount")

    price = fields.Float(
        related="invoice_line_ids.price_unit", string="Importe Base",)

    def compute_get_descuento(self):
        for record in self:
            record.des = record.price * (record.porcen / 100.0)
