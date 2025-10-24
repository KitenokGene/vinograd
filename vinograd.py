import base64
import zlib

def ZipUtils_decompressString2(data: str) -> str:
    decoded = base64.urlsafe_b64decode(data.encode('utf-8'))
    return zlib.decompress(decoded).decode('utf-8')

def ZipUtils_compressString2(data: str) -> str:
    compressed = zlib.compress(data.encode('utf-8'))
    return base64.urlsafe_b64encode(compressed).decode()

# example usage. tested with musiclibrary_02.dat and sfxlibrary.dat
with open("musiclibrary_02.dat", "r") as musiclibrary_02:
    decompressed = ZipUtils_decompressString2(musiclibrary_02.read())
  # recompressed = ZipUtils_compressString2(decompressed)
    
    open("musiclibrary_02.dec.txt", "w", encoding="utf-8").write(decompressed)
  # open("musiclibrary_02.rec.txt", "w", encoding="utf-8").write(recompressed)