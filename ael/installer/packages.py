## ----------------------------------------------------------------------------
##             { alterEGO Linux: "Open the vault of knowledge" }             ##
## ----------------------------------------------------------------------------
##
## /python-ael/ael/installer/packages.py
##   created        : 2022-11-14 11:34:18 UTC
##   updated        : 2022-12-09 04:19:26 UTC
##   description    : All packages
## ____________________________________________________________________________


Package = namedtuple('Package', ['name', 'repository', 'interface', 'description', 'category', 'notes'])
packages = [
    Package('alacritty', 'official', 'CLI',  'A fast, cross-platform, OpenGL terminal emulator', 'terminal', '' ),
    Package('fzf', 'official', 'CLI', 'A command-line fuzzy finder', 'utility', '' ),
    Package('nikto', 'official', 'CLI', 'A web server scanner which performs comprehensive tests against web servers for multiple items', 'recon', '' ),
    Package('nmap', 'official', 'CLI', 'Utility for network discovery and security auditing', 'recon', '' ),
    Package('poppler', 'official', 'CLI', 'PDF rendering library based on xpdf 3.0', 'utility', 'Provides `pdftotext`' ),
    Package('smbclient', 'official', 'CLI', 'Tools to access a server\'s filespace and printers via SMD', 'file explorer', '' ),
    Package('tmux', 'official', 'CLI', 'A terminal multiplexer', 'terminal', ''),
           ]
