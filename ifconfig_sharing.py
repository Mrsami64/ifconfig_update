import github3
import time
import os
gh = github3.login(token=token)
date = time.strftime("%Y-%m-%dT%H:%M:%SZ",time.localtime())
ifconfig = os.popen('ifconfig').read()
issue = {
    'title':date,
    'body':ifconfig,
    'created_at':date
}
responsitory = gh.repository('Sjoner','ifconfig_update')
responsitory.import_issue(**issue)
