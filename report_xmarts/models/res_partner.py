from odoo import api, _, tools, fields, models, exceptions
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class FormResPartner(models.Model):
	_inherit = 'res.partner'

	clabe = fields.Char(string='Clabe Bancaria')
	rfc_banco_cliente = fields.Char(string='RFC del Banco', help='Escribe aqui el RFC correspondiente a tu Banco de la "CLABE" bancaria anteriormente agregada')

class FormJournal(models.Model):
	_inherit = 'account.journal'

	rfc_banco_emisor = fields.Char(string='RFC Banco', help='Ingresa aqui el RFC del Banco')