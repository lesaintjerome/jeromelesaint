#!/usr/bin/env python3
import os
import sys

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <markdown_file> <images_folder>")
        sys.exit(1)

    md_file = sys.argv[1]
    images_folder = f"../{sys.argv[2]}"

    # Vérifier que le fichier et le dossier existent
    if not os.path.isfile(md_file):
        print(f"Error: Markdown file '{md_file}' not found.")
        sys.exit(1)
    if not os.path.isdir(images_folder):
        print(f"Error: Images folder '{images_folder}' not found.")
        sys.exit(1)

    # Lister les fichiers images (extensions classiques)
    image_extensions = (".jpg", ".jpeg", ".png", ".webp", ".gif")
    image_files = sorted([f for f in os.listdir(images_folder)
                          if f.lower().endswith(image_extensions)])

    if not image_files:
        print(f"No image files found in '{images_folder}'.")
        sys.exit(0)

    # Créer les lignes HTML pour chaque image
    # On suppose que le chemin à utiliser dans le Markdown est relatif depuis la racine du site
    folder_path_for_md = sys.argv[2].replace("\\", "/")  # Windows compat
    lines_to_add = []
    for img in image_files:
        img_path = f"../..{folder_path_for_md}/{img}"
        line = f'<a href="{img_path}"><img src="{img_path}" width="200"></a>'
        lines_to_add.append(line)

    # Ajouter à la fin du fichier Markdown
    with open(md_file, "a", encoding="utf-8") as f:
        f.write("\n\n")  # deux lignes vides avant
        f.write("\n".join(lines_to_add))
        f.write("\n")

    print(f"Added {len(image_files)} images to '{md_file}'.")

if __name__ == "__main__":
    main()
