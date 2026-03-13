from setuptools import setup

setup(
    name="playwright_mousekey", # package name 
    version="0.2.0",
    py_modules=["playwright_mousekey"],  # logical module name users will import
    package_dir={"playwright_mousekey": "."},  # maps module name to root directory (_init_.py)
    install_requires=[
        "ctypes_rgb_values",
        "ctypes_window_info",
        "flatten_everything",
        "keyboard",
        "kthread",
        "numpy",
        "six",
        "greenlet==3.3.1",
        "playwright==1.58.0",
        "pyee==13.0.0",
        "typing_extensions==4.15.0",
    ],
    python_requires=">=3.8",
)