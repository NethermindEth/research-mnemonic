# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [("wordlist.txt","."), ("secret.txt",".")]

create_share_a = Analysis(['create_shares.py', 'reconstruct.py'],
             pathex=[],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
create_share_pyz = PYZ(create_share_a.pure, create_share_a.zipped_data,
             cipher=block_cipher)

create_share_exe = EXE(create_share_pyz,
          create_share_a.scripts, 
          [],
          exclude_binaries=True,
          name='create_shares',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

reconstruct_a = Analysis(['reconstruct.py'],
             pathex=[],
             binaries=[],
             datas=[('wordlist.txt', '.'), ('secret.txt', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
reconstruct_pyz = PYZ(reconstruct_a.pure, reconstruct_a.zipped_data,
             cipher=block_cipher)

reconstruct_exe = EXE(reconstruct_pyz,
          reconstruct_a.scripts, 
          [],
          exclude_binaries=True,
          name='reconstruct',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

coll = COLLECT(create_share_exe,
               create_share_a.binaries,
               create_share_a.zipfiles,
               create_share_a.datas,
               reconstruct_exe,
               reconstruct_a.binaries,
               reconstruct_a.zipfiles,
               reconstruct_a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='research')

