# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = "Todo tag"
    name = fields.Char('Name', 40, translate=True)

class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = "Todo stage" 
    _order = 'sequence, name'

name = fields.Char('Name', 40, translate=True)
    sequence = fields.Integer('Sequence')
    