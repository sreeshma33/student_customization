from odoo import models, fields, api


class Students(models.Model):
    _name='student_customization.students'
    _description='student_customization students'

    name=fields.Char(string="Name", required=True)
    age=fields.Integer(string="Age")
    clss=fields.Char(string="Class")