from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    diabetes_type = fields.Selection([
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
    ], string="Type of Diabetes")

    diagnosed_when = fields.Selection([
        ('less_1', 'One year or less'),
        ('1_2', 'Two years'),
        ('less_5', 'Five years or less'),
        ('5_10', 'Ten years or less'),
        ('more_10', 'More than ten years'),
        ('not_listed', 'Not listed'),
    ], string="When was Diagnosed")
