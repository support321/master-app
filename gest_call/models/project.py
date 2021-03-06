from odoo import models, fields, api, _
from datetime import datetime
import time
from odoo.exceptions import ValidationError
import logging
logger=logging.getLogger('_______LOGGER B____________')


class GestcalProject(models.Model):
 
    _name = 'gestcal.project'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'title'
    _description = 'Gestcal project'
    
    title = fields.Char(string='Title', required=True) 
    project_id = fields.Char(string='Project id', required=True) 
    courses = fields.Many2many('gestcal.course','courses_ids', string='Courses')
    attachments_ids = fields.One2many('gestcal.attachment', 'projects_id', string='Attachment')
    attachments = fields.Many2one('gestcal.attachment', string='Attachments')
    attachment_count = fields.Integer(compute='_compute_attachment_count', string='Attachment count')
    plan_id = fields.Many2one('gestcal.plan', string='Plan')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('active', 'Active'), 
        ('completed','Completed'), 
        ('accounted','Sent To Financial Director'), 
        ('closed','Closed')
        
        ], string='Status', index=True, readonly=True, copy=False, default='draft', track_visibility='onchange')
    project_ids =  fields.Many2one('gestcal.plan', string='Projects')

    def _compute_attachment_count(self):
        for attachment in self: 
            attachment.attachment_count = len(attachment.attachments_ids)
            logger.info('___________count________: %s  ',attachment.attachment_count)
            
#     @api.constrains('project_id')
#     def _check_name(self):
#         if self.title ==  self.project_code:
#             raise ValidationError(_('Two project Title and Project code can not be the same'))
#  
    @api.multi
    def attachment_action_to_open(self):
        ''' This opens the xml view specified in xml_id for the current attachment '''
        self.ensure_one()
        xml_id = self.env.context.get('xml_id')

        if xml_id:
            res = self.env['ir.actions.act_window'].for_xml_id('gest_call', xml_id)
            res.update(
                context={'default_projects_id': self.id,
                         },
                domain=[('projects_id', '=', self.id)]
            )
            logger.info('___________res________: %s  ',res)
            return res
            
        return False

    @api.multi
    def submitted_project(self):
        return self.write({'state': 'submitted'})

    @api.multi
    def active_project(self):
        return self.write({'state': 'active'})

    @api.multi
    def completed_project(self):
        return self.write({'state': 'completed'})

    @api.multi
    def accounted_project(self):
        return self.write({'state': 'accounted'})

    @api.multi
    def closed_project(self):
        return self.write({'state': 'closed'})



