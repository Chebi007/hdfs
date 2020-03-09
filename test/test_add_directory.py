
def test_move_to_trash(app):
    app.filebrowser.delete_dir_and_files()

def test_add_directory(app, json_directory):
    directory = json_directory
    old_list = app.filebrowser.get_file_list()
    app.filebrowser.add_directory(directory)
    new_list = app.filebrowser.get_file_list()
    old_list.append(directory.name)
    assert sorted(old_list) == sorted(new_list)