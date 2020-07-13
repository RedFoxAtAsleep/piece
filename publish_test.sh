
git add *
git commit -m 'Synchronize Before Publish.'
git push

rm -rf dist

python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*
pip uninstall piece3941
pip install -i https://test.pypi.org/simple/ piece3941