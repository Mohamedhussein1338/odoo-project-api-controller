from odoo import models, api, fields
from datetime import date, datetime, time
from odoo.exceptions import ValidationError


class ProjectApi(models.Model):
    _name = "project.api"
    _description = "Project Api"

    name = fields.Char(string="Name")
    description = fields.Text()
    postcode = fields.Integer()
    date_availability = fields.Date()

