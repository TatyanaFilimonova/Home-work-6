from pathlib import Path
import shutil
import sys
import re

def normalize_ (translate_line):
   map = {ord('а'): 'a', ord('А'): 'A',
          ord('б'): 'b',ord('Б'): 'B',
          ord('в'): 'v',ord('В'): 'V',
          ord('г'): 'h',ord('Г'): 'H',
          ord('ґ'): 'g',ord('Ґ'): 'G',
          ord('д'): 'd',ord('Д'): 'D',
          ord('е'): 'e',ord('Е'): 'E',
          ord('є'): 'ie',ord('Є'): 'Ye',
          ord('ж'): 'zh',ord('Ж'): 'Zh',
          ord('з'): 'z',ord('З'): 'Z',
          ord('і'): 'i',ord('І'): 'Yi',
          ord('й'): 'i',ord('Й'): 'Y',
          ord('ї'): 'i',ord('Ї'): 'I',
          ord('и'): 'y',ord('И'): 'Y',
          ord('к'): 'k', ord('К'): 'K',
          ord('л'): 'l',ord('Л'): 'L',
          ord('м'): 'm',ord('М'): 'M',
          ord('н'): 'n',ord('Н'): 'N',
          ord('о'): 'o',ord('О'): 'O',
          ord('п'): 'p',ord('П'): 'P',
          ord('р'): 'r',ord('Р'): 'R',
          ord('с'): 's',ord('С'): 'S',
          ord('т'): 't',ord('Т'): 'T',
          ord('у'): 'u',ord('У'): 'U',
          ord('ф'): 'f',ord('Ф'): 'F',
          ord('х'): 'kh',ord('Х'): 'Kh',
          ord('ц'): 'ts',ord('Ц'): 'Ts',
          ord('ч'): 'ch',ord('Ч'): 'Ch',
          ord('ш'): 'sh',ord('Ш'): 'Sh',
          ord('щ'): 'shch',ord('Щ'): 'Shch',
          ord('ю'): 'iu',ord('Ю'): 'Yu',
          ord('я'): 'ia',ord('Я'): 'Ya',
          ord('ь'): ''}
   translated = translate_line.translate(map)
   reg = re.compile ('[^A-Za-z0-9 ]')
   return reg.sub('_',translated).strip()


def parse_folder_(path):
   try:  
       for i in path.iterdir():
         name = normalize_(i.stem)+i.suffix
         if i.is_dir() and i.name not in extensions_.keys():
             i = i.replace(str(path)+'\\'+name)
             parse_folder_(i)
             if len(list(i.iterdir())) == 0 : i.rmdir()
         else:
           suffix = i.suffix.upper()[1:]
           f_type = 'unknown'
           for f in extensions_.keys():
               if suffix in extensions_[f]:
                   f_type = f
           if f_type == 'archives':
                   if not Path(str(path)+'\\'+f_type+'\\').exists(): Path(str(path)+'\\'+f_type+'\\').mkdir()
                   i = i.replace(str(path)+'\\'+name)
                   shutil.unpack_archive(str(path)+'\\'+name, str(path)+'\\'+f_type+'\\'+i.stem+'\\')
                   i.unlink()
           elif f_type == 'unknown': i.replace(str(path)+'\\'+name)
           else:
               if not Path(str(path)+'\\'+f_type+'\\').exists(): Path(str(path)+'\\'+f_type+'\\').mkdir()
               i.replace(str(path)+'\\'+f_type+'\\'+name)
   except:
      print("Couldn't do sorting well")
      

extensions_ = {
    'images' :  ('JPEG', 'PNG', 'JPG', 'SVG', 'TIFF', 'GIF', 'PSD', 'CDR'),
    'video' :  ('AVI', 'MP4', 'MOV', 'MKV'),
    'documents' :  ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'PDF', 'XLS', 'DOCX', 'CSV'),
    'music': ('MP3', 'OGG', 'WAV', 'AMR'),
    'archives':  ('ZIP', 'GZ', 'TAR'),
    'python': ('PY'),
    'BIN': ('EXE', 'MSI', 'DLL')}


