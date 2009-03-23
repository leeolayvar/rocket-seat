''''''

# standard
# related
from google.appengine.ext import db
# local


class Hooks(db.Model):
    '''The hooks model (or rather, those who inherit from it) is responsible
    for holding all hooks, and a list of plugins who will be called
    upon the triggering of each hook.

    Currently this base model does not define any inherited values.'''
    pass

class CoreHooks(Hooks):
    '''A model responsible for holding lists of modules which are registered to
    be hooked into various stages of rocket seat.

    Just like plugins, the text found before the two underscores describes the
    hook. The following is a list of hook prefixes, and what they mean.
     - core: These are generic core events, not specific to any handler.
     - core_p: This event is specific to hooks triggered by the Page Handler.
    '''
    # As a side note, these are ordered by timeline and not by alpha.

    #: Ask each plugin if they want to register for this specific page load.
    core_p__register_as_active_hook = db.StringListProperty()

    #: Any blocks that are to be rendered, are to be rendered now.
    core_p__add_rendered_blocks_hook = db.StringListProperty()

    #: These two are called anytime a plugin is installed/uninstalled.
    core__plugin_installed_hook = db.StringListProperty()
    core__plugin_uninstalled_hook = db.StringListProperty()
    #: These two are called anytime a plugin is enabled/disabled.
    core__plugin_enabled_hook = db.StringListProperty()
    core__plugin_disabled_hook = db.StringListProperty()

class RocketSeatConfig(db.Model):
    '''A model containing configuration information about the site itself; 
    such as, sitename, plugins, etc.'''

    # A list of enabled plugins in the form of the module path
    enabled_plugins = db.StringListProperty()

    # The active theme python path.
    active_theme = db.StringProperty(default='core.themes.raw')
    
    # Is the site undergoing maintenance?
    undergoing_maintenance = db.BooleanProperty(default=True)

class UserAccount(db.Model):
    '''A model that holds a single user's rocketseat account data.
    '''

    # The name alias for this user.
    alias = db.StringProperty(required=True)

    # A reference to this user's google account.
    gaccount = db.UserProperty(required=True)

    #permissions = db.StringListProperty(required=True)
    permissions = db.StringListProperty(default=['user'])
    '''A list of permissions. Any permission found here will give the user 
    access to whatever that permission grants, such as common "user, admin, 
    moderator" permissions.'''