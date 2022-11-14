## ----------------------------------------------------------------------------
##             { alterEGO Linux: "Open the vault of knowledge" }             ##
## ----------------------------------------------------------------------------
##
## /python-ael/ael/installer/packages.py
##   created        : 2022-11-14 11:34:18 UTC
##   updated        : 2022-11-14 11:34:18 UTC
##   description    : All packages
## ____________________________________________________________________________


Package = namedtuple('Package', ['name', 'repository', 'interface', 'description', 'category', 'notes'])
packages = [
    Package('alacritty', 'official', 'CLI',  'A fast, cross-platform, OpenGL terminal emulator', 'terminal', '' ),
    Package('fzf', 'official', 'CLI', 'A command-line fuzzy finder', 'utility', '' ),
    Package('poppler', 'official', 'CLI', 'PDF rendering library based on xpdf 3.0', 'utility', 'Provides `pdftotext`' ),
    Package('tmux', 'official', 'CLI', 'A terminal multiplexer', 'terminal', ''),
           ]
