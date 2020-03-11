import requests

path= '/user/cloudera'
path1 = '/user/cloudera/dir1'
path2 = '/user/cloudera/dir2'

def test_creaate_directory():
    r = requests.put('http://127.0.0.1:50070/webhdfs/v1%s?user.name=hdfs&op=MKDIRS' % path1)
    assert r.json()['boolean'] == True

def test_status_directory():
    r = requests.get('http://127.0.0.1:50070/webhdfs/v1%s?user.name=hdfs&op=GETFILESTATUS' % path1)
    l = list(r.json()['FileStatus'].keys())
    l2 = ['accessTime', 'blockSize', 'childrenNum', 'fileId', 'group', 'length', 'modificationTime', 'owner',
               'pathSuffix', 'permission', 'replication', 'storagePolicy', 'type']
    assert l == l2

def test_list_status_directory():
    r = requests.get('http://127.0.0.1:50070/webhdfs/v1%s?user.name=hdfs&op=LISTSTATUS' % path)
    l = r.json()['FileStatuses']
    l2 =  l['FileStatus']
    for i in l2:
        assert list(i.keys()) == ['accessTime', 'blockSize', 'childrenNum', 'fileId', 'group', 'length', 'modificationTime',
                           'owner', 'pathSuffix', 'permission', 'replication', 'storagePolicy', 'type']

def test_get_content_summary_directory():
    r = requests.get('http://127.0.0.1:50070/webhdfs/v1%s?user.name=hdfs&op=GETCONTENTSUMMARY' % path)
    directoryCount = r.json()['ContentSummary']['directoryCount']
    assert directoryCount == 2

def test_get_home_directory_directory():
    r = requests.get('http://127.0.0.1:50070/webhdfs/v1%s?user.name=hdfs&op=GETHOMEDIRECTORY' % path1)
    assert r.json()['Path'] == '/user/hdfs'

def test_rename_directory():
    r = requests.put('http://127.0.0.1:50070/webhdfs/v1%s?user.name=hdfs&op=RENAME&destination=%s' % (path1, path2))
    assert r.json()['boolean'] == True

def test_delete_directory():
    r = requests.delete('http://127.0.0.1:50070/webhdfs/v1%s?user.name=hdfs&op=DELETE&recursive=true' % path2)
    assert r.json()['boolean'] == True


