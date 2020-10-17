import pathlib as pl
import os


def prepend_object_name(obj: str):
    """Rename by prepending to file names, assuming files are in sheep/ and coke/
    Args:
        obj (str): Text of string to prepend at start of image name
    """
    for path in pl.Path(obj).iterdir():
        if path.is_file():
            file_name = path.stem
            file_ext = path.suffix
            if obj not in file_name:
                if file_ext == ".png":
                    directory = path.parent
                    new_name = obj + file_name + file_ext
                    path.rename(pl.Path(directory, new_name))


if __name__ == "__main__":
    data_path = pl.Path("data")
    objects_to_label = []

    # Load class names
    with open(data_path / "obj.names", "r") as f_obj:
        objects_to_label = [line.strip() for line in f_obj.readlines()]

    # Prepend class names to file names to avoid clashes
    for obj in objects_to_label:
        if pl.Path(obj).is_dir():
            prepend_object_name(obj)

    # Append everything to train.txt
    with open(data_path / "train.txt", "w") as f_train:
        for obj in objects_to_label:
            item_num = []
            if pl.Path(obj).is_dir():
                item_num = [int(str(path.stem).strip(obj)) for path in pl.Path(obj).iterdir() if path.suffix == ".png"]
                item_num.sort()
                for i in item_num:
                    line = "build/darknet/x64/data/obj/" + obj + str(i) + ".png\n"
                    f_train.write(line)
