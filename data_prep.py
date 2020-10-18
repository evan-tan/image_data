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
            if pl.Path(data_path/"obj").is_dir():
                for path in pl.Path(data_path/"obj").iterdir():
                    if obj in path.stem and path.suffix == ".png":
                        num = str(path.stem).strip(obj)
                        item_num.append(int(num))
                        item_num.sort()
                for i in item_num:
                    line = "build/darknet/x64/data/obj/" + obj + str(i) + ".png\n"
                    f_train.write(line)

    # for path in pl.Path(data_path / "obj").iterdir():
    #     if path.suffix == ".txt":
    #         if "sheep" not in str(path):
    #             if "coke" not in str(path):
    #                 file_name = path.stem
    #                 png_sheep = pl.Path(data_path/"obj"/("sheep" + file_name + ".png"))
    #                 png_coke = pl.Path(data_path/"obj"/("sheep" + file_name + ".png"))
    #                 if png_coke.is_file():
    #                     new_name = "coke" + file_name + path.suffix
    #                     path.rename(pl.Path(path.parent, new_name))
    #                     print(new_name)
    #                 elif png_sheep.is_file():
    #                     new_name = "sheep" + file_name + path.suffix
    #                     path.rename(pl.Path(path.parent, new_name))
    #                     print(new_name)
