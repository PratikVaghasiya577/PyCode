import shutil
import sys


def check_disk_usage(disk, min_absolute, min_percentage):
    du = shutil.disk_usage(disk)

    percent_free = 100 * du.free / du.total
    gb_free = du.free / 2 ** 30
    if percent_free < min_percentage or gb_free < min_absolute:
        return False
    else:
        return True


if not check_disk_usage("/", 2, 10):
    print("Not enough!")

print("Ok")
