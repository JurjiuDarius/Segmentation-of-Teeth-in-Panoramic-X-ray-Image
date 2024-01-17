from zipfile import ZipFile


def process_zip(save_path):
    file = ZipFile(save_path + "/DentalPanoramicXrays.zip")
    file.extractall(save_path)
    zip.unzip_dataset(save_path)
    zip.delete_zip(save_path)
