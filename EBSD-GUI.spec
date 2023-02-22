# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/olavlet/EBSD-data/EBSD-GUI-olavlet/resources', 'resources/')],
    hiddenimports=['kikuchipy', 'hyperspy', 'pyebsdindex'],
    hookspath=['/Users/olavlet/EBSD-data/EBSD-GUI-olavlet/hooks'],
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
    [],
    exclude_binaries=True,
    name='EBSD-GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/olavlet/EBSD-data/EBSD-GUI-olavlet/resources/ebsd_gui.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='EBSD-GUI',
)
app = BUNDLE(
    coll,
    name='EBSD-GUI.app',
    icon='/Users/olavlet/EBSD-data/EBSD-GUI-olavlet/resources/ebsd_gui.ico',
    bundle_identifier=None,
)
