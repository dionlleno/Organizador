import os
import glob
import shutil

extensions = {

     "jpg": "Imagens",
     "png": "Imagens",
     "ico": "Imagens",
     "gif": "Imagens",
     "svg": "Imagens",
     "sql": "Sql",
     "exe": "Programas",
     "msi": "Programas",
     "pdf": "Pdf",
     "xlsx": "Excel",
     "csv": "Excel",
     "rar": "Compactados",
     "zip": "Compactados",
     "gz": "Compactados",
     "tar": "Compactados",
     "docx": "Word",
     "ott": "Word",
     "odt": "Word",
     "torrent": "Torrent",
     "txt": "Texto",
     "ipynb": "Algoritimos",
     "py": "Algoritimos",
     "pptx": "Powerpoint",
     "ppt": "Powerpoint",
     "mp3": "Musicas",
     "wav": "Musicas",
     "mp4": "Vídeos",
     "m3u8": "Vídeos",
     "webm": "Vídeos",
     "ts": "Vídeos",
     "json": "Algoritimos",
     "css": "Algoritimos",
     "js": "Algoritimos",
     "html": "Algoritimos",
     "apk": "Apk",
     "sqlite3": "Sqlite3",
     "ALG": "VisualG_Codigos",
     "epub": "Kindle",
     "mobi": "Kindle",
     "c": "Algoritimos",
     "cpp": "Algoritimos",
     "c++": "Algoritimos",
     "c#": "Algoritimos",
     "sh": "Algoritimos",
     "ino": "Algoritimos",

}

path = os.getcwd()
    
for extension, folder_name in extensions.items():
    # Pega todos os arquivos que terminam com a extensão
    files = glob.glob(os.path.join(path, f"*.{extension}"))
    print(f"[*] Encontrados {len(files)} corquivos com extensão '{extension}'")
    
    if not os.path.isdir(os.path.join(path, folder_name)) and files:
        # Cria a pasta se não existir
        print(f"[+] Making {folder_name} folder")
        os.mkdir(os.path.join(path, folder_name))
        
    for file in files:
        if ("organizador.py" in file or "organizador.exe" in file): continue
        # Para cada arquivo, move para a pasta correspondente
        basename = os.path.basename(file)
        dst = os.path.join(path, folder_name, basename)
        
        print(f"[*] Movendo {file} para {dst}")
        shutil.move(file, dst)
