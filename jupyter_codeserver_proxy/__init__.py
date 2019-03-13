"""
Return config on servers to start for codeserver

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil

def setup_codeserver():
    # Make sure codeserver is in $PATH
    def _codeserver_command(port):
        full_path = shutil.which('code-server')
        if not full_path:
            raise FileNotFoundError('Can not find code-server in $PATH')
        return [full_path, '--host=127.0.0.1', '--port=' + str(port), "--allow-http", "--no-auth" ]

    return {
        'command': _codeserver_command,
        'environment': {
            'USE_LOCAL_GIT': 'true'
        },
        'launcher_entry': {
            'title': 'VSCode IDE',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'icons', 'vscode.svg')
        }
    }