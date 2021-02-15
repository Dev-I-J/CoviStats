# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None


a = Analysis(['covistats.py'],
             pathex=[os.path.abspath('.')],
             binaries=[],
             datas=[],
             hiddenimports=['dataclasses'],
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
          name='covistats',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon=('src/images/logo.ico' if sys.platform == 'win32' else 'src/images/logo.icns' if sys.platform == 'darwin' else 'src/images/logo.png'))
