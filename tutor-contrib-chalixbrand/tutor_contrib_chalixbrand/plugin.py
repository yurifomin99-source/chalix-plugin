from tutor import hooks

# 1) Install your brand repo as the @edx/brand package for every MFE build.
#    We alias your Git repo to "@edx/brand" so MFEs pick it up automatically.
hooks.Filters.ENV_PATCHES.add_item((
    "mfe-dockerfile-post-npm-install",
    r"""
RUN npm install '@edx/brand@git+https://github.com/Alimento-Team/brand-chalix.git'
"""
))

# 2) (Optional) Also point MFEs to your logo/favicon URLs served by LMS theming,
#    which helps bust caches and keeps assets consistent across MFEs.
hooks.Filters.ENV_PATCHES.add_items([
    ("mfe-lms-common-settings",
     r'''
MFE_CONFIG["LOGO_URL"] = LMS_ROOT_URL + "/theming/asset/images/logo.svg"
MFE_CONFIG["LOGO_WHITE_URL"] = LMS_ROOT_URL + "/theming/asset/images/logo-white.svg"
MFE_CONFIG["LOGO_TRADEMARK_URL"] = LMS_ROOT_URL + "/theming/asset/images/logo-trademark.svg"
MFE_CONFIG["FAVICON_URL"] = LMS_ROOT_URL + "/theming/asset/images/favicon.ico"
''')
])
