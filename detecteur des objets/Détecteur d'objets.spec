# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ["Détecteur d'objets.py"],
    pathex=[],
    binaries=[],
    datas=[('coco.names', '.'), ('ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt', '.'), ('frozen_inference_graph.pb', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Détecteur d'objets',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\HoussemDev.24\\Desktop\\detection des objets\\recognition.ico'],
)
