from tutor import hooks

# Install brand and custom header/footer components during MFE build
hooks.Filters.ENV_PATCHES.add_item((
    "mfe-dockerfile-post-npm-install",
    """
# Install brand and components from GitHub release branches
RUN npm install '@edx/brand@git+https://github.com/yurifomin99-source/brand-chalix.git'
RUN npm install '@chalix/frontend-component-header@git+https://github.com/yurifomin99-source/chalix-mfe-component-header.git#release'
RUN npm install '@chalix/frontend-component-footer@git+https://github.com/yurifomin99-source/chalix-mfe-component-footer.git#release'
"""
))

# Configure theme assets serving
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-lms-common-settings",
    """
# Enable serving theme assets
COMPREHENSIVE_THEME_DIRS.append("/openedx/themes")

# Configure static file serving for themes
STATICFILES_DIRS.append(
    ("themes", "/openedx/themes")
)
"""
))

# Configure MFE branding
hooks.Filters.ENV_PATCHES.add_item((
    "mfe-lms-common-settings",
    """
MFE_CONFIG["LOGO_URL"] = LMS_ROOT_URL + "/static/chalix_theme/images/logo.svg"
MFE_CONFIG["LOGO_WHITE_URL"] = LMS_ROOT_URL + "/static/chalix_theme/images/logo-white.svg"  
MFE_CONFIG["LOGO_TRADEMARK_URL"] = LMS_ROOT_URL + "/static/chalix_theme/images/logo-trademark.svg"
MFE_CONFIG["FAVICON_URL"] = LMS_ROOT_URL + "/static/chalix_theme/images/favicon.ico"
"""
))
