from model.directory import Directory


def test_move_to_trash(app):
    app.filebrowser.delete_dir_and_files()

def test_restore_from_trash(app):
    directory = Directory(name="For restore")
    app.filebrowser.add_directory(directory)
    old_list = app.filebrowser.get_file_list()
    app.filebrowser.restore_from_trash(directory)
    new_list = app.filebrowser.get_file_list()
    assert len(old_list) == len(new_list)