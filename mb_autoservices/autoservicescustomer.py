# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _
from odoo.exceptions import ValidationError


class AutoservicesCustomer(models.Model):
    _name = 'autoservices.customer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Customer Record'


    cus_name = fields.Char(string="Full Name", required = True)
    cus_email = fields.Char(string="Email")
    cus_workphone = fields.Char(string="Work Phone")
    cus_mobilephone = fields.Char(string="Mobile PHone")
    cus_drivelic  = fields.Char(string="Driver Licence", required = True)
    cus_address = fields.Text(string="Address")
    cus_picture = fields.Binary(string='Image')







