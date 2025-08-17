from tutor import hooks

# 1) Install your brand repo as the @edx/brand package for every MFE build.
#    We alias your Git repo to "@edx/brand" so MFEs pick it up automatically.
hooks.Filters.ENV_PATCHES.add_item((
    "mfe-dockerfile-post-npm-install",
    r"""
RUN npm install '@edx/brand@git+https://github.com/Alimento-Team/brand-chalix.git'
"""
))

# 2) Ensure static assets from the theme are properly served
hooks.Filters.ENV_PATCHES.add_items([
    ("openedx-lms-common-settings",
     r'''
# Enable serving theme assets
COMPREHENSIVE_THEME_DIRS.append("/openedx/themes")

# Configure static file serving for themes
STATICFILES_DIRS.append(
    ("themes", "/openedx/themes")
)
'''),
    ("mfe-lms-common-settings",
     r'''
MFE_CONFIG["LOGO_URL"] = LMS_ROOT_URL + "/static/chalix_theme/images/logo.svg"
MFE_CONFIG["LOGO_WHITE_URL"] = LMS_ROOT_URL + "/static/chalix_theme/images/logo-white.svg"  
MFE_CONFIG["LOGO_TRADEMARK_URL"] = LMS_ROOT_URL + "/static/chalix_theme/images/logo-trademark.svg"
MFE_CONFIG["FAVICON_URL"] = LMS_ROOT_URL + "/static/chalix_theme/images/favicon.ico"
''')
])
