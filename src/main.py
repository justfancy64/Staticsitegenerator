import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("copying staticfiles to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("generating page...")
    generate_page(
        os.path.join(dir_path_content,"index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html")
    )
    




main()