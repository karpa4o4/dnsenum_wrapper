import os
from celery import task
from django.conf import settings
from subprocess import Popen, PIPE, STDOUT

from .models import Scan

@task
def start_domain_scan(scan_id, domain):
    scan = Scan.objects.get(id=scan_id)
    scan.status = 'in_progress'
    scan.save()

    proc = Popen(args=[
                        'perl', 
                        settings.BASE_DIR + '/dnsenum/dnsenum.pl', 
                        domain
                        ],
                 stdout=PIPE, stderr=STDOUT)
    proc.wait()
    result = proc.communicate()
    if proc.returncode:
        scan.status = 'failed'
    else:
        scan.status = 'successeded'
        scan.result = result[0].decode('UTF-8')
    scan.save()
