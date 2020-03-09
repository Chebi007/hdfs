
def test_move_to_trash(app):
    app.filebrowser.delete_dir_and_files()

def test_add_file(app, data_file):
    file = data_file.dir
    old_list = app.filebrowser.get_file_list()
    app.filebrowser.add_file(file)
    new_list = app.filebrowser.get_file_list()
    old_list.append(file)
    assert sorted(old_list) == sorted(new_list)