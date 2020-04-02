# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class Vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Gestión Vehículos'

    name = fields.Char(string='Name', required=True, help="Introduzca el nombre", default="Nuevo Vehiculo")
    active = fields.Boolean(string='Activo', default='1')
    matricula = fields.Char('Matricula')
    color_id = fields.Many2one(comodel_name="taller.vehiculo.color")
    tipo_vehiculo_id = fields.Many2one(comodel_name="taller.vehiculo.tipo")
    tags_ids = fields.Many2many(comodel_name="taller.vehiculo.tag")

    @api.constrains('matricula')
    def _check_matricula(self):
        domain = [('matricula', '=', self.matricula),
                  ('id', '!=', self.id)]
        vehiculos = self.search(domain)
        if vehiculos:
            raise exceptions.ValidationError("Matrícula Duplicada")

    @api.model
    def default_get(self, fields_list):
        res = super(Vehiculo, self).default_get(fields_list)

        res.update({'tipo_vehiculo_id': 1})
        return res


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


class VehiculoTag(models.Model):
    _name = 'taller.vehiculo.tag'
    _description = 'Tags Vehículos'
    name = fields.Char(string='Name')
