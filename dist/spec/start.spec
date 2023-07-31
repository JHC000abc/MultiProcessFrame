# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['F:\\Project\\GIT\\pythondevelopmenttools\\others\\collection_tools\\start.py'],
    pathex=['F:\\Project\\GIT\\pythondevelopmenttools\\others\\collection_tools', 'F:\\Project\\GIT\\pythondevelopmenttools\\others\\collection_tools\\gui', 'F:\\Project\\GIT\\pythondevelopmenttools\\others\\collection_tools\\others\\gui\\ctrl', 'F:\\Project\\GIT\\pythondevelopmenttools\\others\\collection_tools\\others\\gui\\ui', 'F:\\Project\\GIT\\pythondevelopmenttools\\others\\collection_tools\\others\\settings', 'F:\\Project\\GIT\\pythondevelopmenttools\\others\\collection_tools\\others\\test', 'F:\\Project\\GIT\\pythondevelopmenttools\\others\\collection_tools\\utils', ''],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='start',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
