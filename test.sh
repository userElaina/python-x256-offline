py1 -m pip install x256

py1 -m pip uninstall x256offline
py1 test.py

py -m build
twine check dist/*
py1 -m pip install dist/*.whl
py1 test2.py
twine upload dist/*
