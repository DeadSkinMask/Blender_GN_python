def get_blend_version(filepath):
    with open(filepath, "rb") as f:
        header = f.read(12)

    if not header.startswith(b"BLENDER"):
        return None

    v = header[9:12].decode("ascii")
    return f"{v[0]}.{v[1:]}"
