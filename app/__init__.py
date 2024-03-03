from app.utils import verify_version, render_info

title = "Test project"
version = "1.0.0"

def present_Project(title: str, version: str) -> None:
    print(
        f"Project: {title} of {version} version ({'verified' if verify_version(version=version) else 'need verification'})"
    )
    print()
    print(render_info(version=version))
