# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class descuento(models.Model):
    _inherit = "account.move"

    des = fields.Float(compute="compute_get_descuento",
                       string="Amortizacion Anticipo",)

    price = fields.Float(compute="compute_price", string="Importe Base",)

    def compute_get_descuento(self):
        self.des = sum(
            line.descuento for line in self.invoice_line_ids)

    def compute_price(self):
        self.price = sum(
            line.price_unit for line in self.invoice_line_ids)
