# -*- mode: python -*-

block_cipher = None


a = Analysis(['file_find_listdir_1_0.py'],
             pathex=['/home/windard/github/Python_Lib/project'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='file_find_listdir_1_0',
          debug=False,
          strip=False,
          upx=True,
          console=True )
