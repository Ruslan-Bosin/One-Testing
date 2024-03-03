def verify_version(version: str) -> bool:
    if version == "1.0.0":
        return True
    return False

def render_info(version: str) -> str:
    if version == "1.0.0":
        return "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Inventore expedita eius quam optio illum, neque consequuntur accusamus numquam tempore odit eveniet eligendi? Error porro totam veniam, quibusdam eum accusamus atque."
    raise Exception("Undefined version")
