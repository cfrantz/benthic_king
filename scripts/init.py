# Add the project scripts directory into python's import machinery.
import importlib
import site
import sys
import traceback
path = edit.path('scripts')
site.addsitedir(path)

# Support fast iterative development by allowing all the benthic king modules
# to be reloaded.
modules = list(sys.modules.values())
for m in modules:
    file = getattr(m, '__file__', '')
    if file and path in file:
        importlib.reload(m)

try:
    import benthic_king
    benthic_king.apply_all_hacks(edit, asm)
except Exception as e:
    traceback.print_exc()
    raise e
