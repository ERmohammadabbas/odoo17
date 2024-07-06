# models/models.py

from odoo import models, fields, api

class Bank(models.Model):
    _name = 'dynamic.bank'
    _description = 'Bank'

    name = fields.Char(string='Bank Name', required=True)
    chequebook_ids = fields.One2many('dynamic.chequebook', 'bank_id', string='Chequebooks')


class Chequebook(models.Model):
    _name = 'dynamic.chequebook'
    _description = 'Chequebook'

    bank_id = fields.Many2one('dynamic.bank', string='Bank', required=True)
    chequebook_number = fields.Char(string='Chequebook Number', required=True)
    cheque_ids = fields.One2many('dynamic.cheque', 'chequebook_id', string='Cheques')


class Cheque(models.Model):
    _name = 'dynamic.cheque'
    _description = 'Cheque'

    chequebook_id = fields.Many2one('dynamic.chequebook', string='Chequebook', required=True)
    issue_date = fields.Date(string='Issue Date', required=True)
    payee_name = fields.Char(string='Payee Name', required=True)
    account_number = fields.Char(string='Account Number', required=True)
    amount_in_words = fields.Char(string='Amount in Words', required=True)
    invoice_id = fields.Many2one('account.move', string='Invoice')
    payment_id = fields.Many2one('account.payment', string='Payment')
    state = fields.Selection([('draft', 'Draft'), ('issued', 'Issued')], default='draft')

    @api.model
    def create(self, vals):
        cheque = super(Cheque, self).create(vals)
        cheque.state = 'issued'
        return cheque
