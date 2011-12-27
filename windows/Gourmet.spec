# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'Gourmet.pyw'],
             pathex=['.'],hookspath='hooks')
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\Gourmet', 'Gourmet.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=True )
#a.datas += [('data/','../images/*','DATA'), ('data/app.glade','../glade/app.glade','DATA')] 
a.datas += Tree('../images/', 'data/')
a.datas += Tree('../glade/', 'data/')
a.datas += Tree('../i18n/', 'i18n/', '*.po')
#a.datas += [('data/','../images/*','DATA'), ('data/app.glade','../glade/app.glade','DATA')] 

coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist', 'Gourmet'))
