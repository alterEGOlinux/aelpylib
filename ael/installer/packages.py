## ----------------------------------------------------------------------------
##             { alterEGO Linux: "Open the vault of knowledge" }             ##
## ----------------------------------------------------------------------------
##
## /python-ael/ael/installer/packages.py
##   created        : 2022-11-14 11:34:18 UTC
##   updated        : 2022-12-11 13:40:38 UTC
##   description    : All packages
## ____________________________________________________________________________


Package = namedtuple('Package', ['name', 'repository', 'interface', 'description', 'installation_mode' 'category', 'notes'])
packages = [
    Package('alacritty', 'official', 'CLI',  'A fast, cross-platform, OpenGL terminal emulator', 'terminal', ['desktop', 'hacker'] ,'' ),
    Package('fzf', 'official', 'CLI', 'A command-line fuzzy finder', 'utility', ['all'], '' ),
    Package('hydra', 'official', 'CLI', 'Very fast network logon cracker which support many different services', 'Login Cracker', ['hacker'], '' ),
    Package('nikto', 'official', 'CLI', 'A web server scanner which performs comprehensive tests against web servers for multiple items', 'recon', ['hacker'], '' ),
    Package('nmap', 'official', 'CLI', 'Utility for network discovery and security auditing', 'recon', ['desktop', 'hacker'], '' ),
    Package('poppler', 'official', 'CLI', 'PDF rendering library based on xpdf 3.0', 'utility', ['all'], 'Provides `pdftotext`' ),
    Package("remmina", "official", "GUI", "Remote desktop client written in GTK+", "network", ['desktop', 'hacker'], "" ),
    Package('smbclient', 'official', 'CLI', 'Tools to access a server\'s filespace and printers via SMD', 'file explorer', ['hacker'], '' ),
    Package('tmux', 'official', 'CLI', 'A terminal multiplexer', 'terminal', ['all'], ''),
    Package('vim', 'official', 'CLI', 'Vi Improved, a highly configurable, improved version of the vi text editor', 'text editor', ['all'], ''),
           ]
