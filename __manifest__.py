# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

{
    "name": "e-tech",
    "version": "15.0.1.0",
    "summary": "e-tech",
    "description": """ e-tech    """,
    "author": "e-tech.",
    "website": "http://www.e-tech.com",
    "category": "HR",
    "depends": ['hr','account','base','hr_payroll'],
    "data": [
        "security/ir.model.access.csv",
        "views/Committe.xml",
        "views/Termination.xml",
        "views/LocationTransfer.xml",
        "views/DisciplinaryAction.xml",
        "views/ExternalMissions.xml",
        "views/Employee.xml",
        "views/Speciality.xml",
        "views/ResumeLine.xml",
        "views/Dependents.xml",
        "views/menusitem.xml",
        "views/Leavel.xml",
        "views/Secondment.xml",
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'auto_install': False,
}
