# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models, api


class descuento(models.Model):
    _inherit = "account.move"

    des = fields.Float(
        related="commercial_partner_id.invoice_ids.invoice_line_ids.descuento", string="Amortizacion Anticipo",)

    price = fields.Float(
        related="commercial_partner_id.invoice_ids.invoice_line_ids.price_unit", string="Importe Base",)
