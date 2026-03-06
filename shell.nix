{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  # Packages that will be available in the shell
  buildInputs = [
    (pkgs.python3.withPackages (ps: with ps; [
      pandas
      numpy
      requests
      scipy
      matplotlib
      sympy
      # Add more python packages here
    ]))
    
    # Non-python system dependencies (e.g., git, compilers)
    pkgs.git
    pkgs.zlib 
  ];

  # Commands to run when the shell starts
  shellHook = ''
    echo "Welcome to your Python development environment!"
    export PIP_PREFIX=$(pwd)/_build/pip_packages
    export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
    export PATH="$PIP_PREFIX/bin:$PATH"
    unset SOURCE_DATE_EPOCH
  '';
}
