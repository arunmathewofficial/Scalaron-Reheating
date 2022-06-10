# Note for Developers
Project Title: Reheating by Scalaron Decay <br/>
Author: Arun Mathew 
 

--------------------------------------------------------------------
### Sphinx document creator terminal command
ref: https://rest-sphinx-memo.readthedocs.io/en/latest/ReST.html
> Make docs directory, then
```console
 $ cd docs/
 $ sphinx-quickstart
 $ make html
``` 
> Navigate out of docs file
```console
 $ sphinx-apidoc -o docs source/
 ```
> Then
```console
 $ cd docs/
 $ make clean html
```

> Edit main.rst 
> * Correct the path

> Edit conf.py 
> * Comment on few things
> * Import all files
> * Add extensions
> * Change html_theme  

For reference, see:  https://www.youtube.com/watch?v=5s3JvVqwESA


-----------------------------------------------------------------------
### Region of Inflation
ODE Solver Used: solve_ivp from scipy.integrate.

For more see: https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html


