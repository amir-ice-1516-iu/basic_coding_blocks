# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['WAT_App.py'],
             pathex=['D:\\basic_coding_blocks\\32_GUI_with_PyQt5\\WAT_V1.2\\WAT'],
             binaries=[],
             datas=[],
             hiddenimports=['PIL'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='WAT_App',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
