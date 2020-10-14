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
            if obj not in file_name:
                directory = path.parent
                file_ext = path.suffix
                new_name = obj + file_name + file_ext
                path.rename(pl.Path(directory, new_name))



if __name__ == "__main__":
    data_path = pl.Path("data")
    os.chdir(data_path)
    objects_to_label = ["coke", "sheep"]
    for obj in objects_to_label:
        if pl.Path(obj).is_dir():
            prepend_object_name(obj)

    count_img = 0
    for path in pl.Path("img").iterdir():
        if path.suffix == ".png":
            count_img += 1

    with open("train.txt","w") as f:
        for obj in objects_to_label:
            for i in range(0, int(count_img/2)):
                line = "data/img/" + obj + str(i) + ".png" + "\n"
                f.write(line)


    # # Write all file names to train.txt
    # with open("train.txt","w") as f:
    #     for path in pl.Path("img").iterdir():
    #         if path.is_file():
    #             f_ext = path.suffix
    #             if f_ext == ".png":
    #                 f_name = path.stem
    #                 line = "data/img/" + f_name + f_ext + "\n"
    #                 # print(f'{line}')
    #                 f.write(line)
