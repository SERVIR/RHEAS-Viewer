from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
import json
import psycopg2
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import create_engine, MetaData, inspect
from .app import RheasViewer as app
from model import *
from utilities import *
import datetime
import config as cfg

def home(request):
    """
    Controller for the app home page.
    """
    context = {

    }

    return render(request, 'rheas_viewer/home.html', context)
    

def vic(request):
    """
    Controller for the vic model page.
    """
    db_schemas = get_schemas()
    variable_info = get_variables_meta()
    geoserver_wms_url = cfg.geoserver['wms_url']
    geoserver_workspace = cfg.geoserver['workspace']

    context = {
        "db_schemas":db_schemas,
        "variable_info":json.dumps(variable_info),
        "geoserver_wms_url":geoserver_wms_url,
        "geoserver_workspace":geoserver_workspace
    }

    return render(request, 'rheas_viewer/vic.html', context)
    
def dssat(request):
    """
    Controller for the dssat model page.
    """
    geoserver_wfs_url = cfg.geoserver['wfs_url']
    geoserver_workspace = cfg.geoserver['workspace']

    if geoserver_wfs_url.endswith("/"):
        geoserver_wfs_url = geoserver_wfs_url[:-1]

    context = {
        "geoserver_workspace":geoserver_workspace,
        "geoserver_wfs_url":geoserver_wfs_url
    }

    return render(request, 'rheas_viewer/dssat.html', context)