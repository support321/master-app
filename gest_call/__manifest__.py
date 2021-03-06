# See LICENSE file for full copyright and licensing details.


{
    'name': 'Module for Calls activity management',
    'version': '12.0.1.0.4',
    'author': "MasterFor",
    'website': "http://www.masterfor.it",
    'license': "AGPL-3",
    'category': 'Calls activity management',
    'summary': '',
    'images': ['static/description/SchoolTimetable.png'],
    'depends': ['base','calendar','hr','contacts','web_widget_timepicker','display_import_button'],
    'data': ['security/ir.model.access.csv',
             'views/project_view.xml',
             'views/lesson_view.xml',
             'views/plan_view.xml',
             'views/place_view.xml',
             'views/course_view.xml',
             'views/seqence_gestcall.xml',
             'views/attachment_view.xml',
             'views/res_partner.xml',
             'views/hr_employee.xml',
             'views/gest_call_menu.xml',
             ], 
    'installable': True,
    'application': True
}
