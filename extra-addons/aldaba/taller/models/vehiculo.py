# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class Vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _decription = 'Gestión Vehículos'

    name = fields.Char(string='Name', required=True, help="Introduzca el nombre", default="Nuevo Vehiculo")
    active = fields.Boolean(string='Activo', default='1')
    matricula = fields.Char('Matricula')
    color_id = fields.Many2one(comodel_name="taller.vehiculo.color")
    tipo_vehiculo_id = fields.Many2one(comodel_name="taller.vehiculo.tipo")

    @api.constrains('matricula')
    def _check_matricula(self):
        domain = [('matricula', '=', self.matricula),
                  ('id', '!=', self.id)]
        vehiculos = self.search(domain)
        if vehiculos:
            raise exceptions.ValidationError("Matrícula Duplicada")


class Color(models.Model):
    _name = 'taller.vehiculo.color'
    _description = 'Colores Vehículos'
    name = fields.Char(string='Name', required=True, help="Introduzca el nombre",
                       default="Nuevo Color Vehiculo")
    active = fields.Boolean(string='Activo', default='1')


class Tipo(models.Model):
    _name = 'taller.vehiculo.tipo'
    _description = 'Tipos Vehículos'
    name = fields.Char(string='Name', required=True, help="Introduzca el nombre",
                       default="Nuevo Tipo Vehiculo")
    active = fields.Boolean(string='Activo', default='1')
