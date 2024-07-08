# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main_video.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Python312/Lib/site-packages/face_recognition_models/models/shape_predictor_68_face_landmarks.dat', 'face_recognition_models/models'), ('images', 'images')],
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
    name='main_video',
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
)
