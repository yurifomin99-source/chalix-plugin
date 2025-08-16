from setuptools import setup, find_packages

setup(
    name="tutor-contrib-chalixbrand",
    version="0.1.0",
    description="Tutor plugin to apply Chalix brand to MFEs",
    packages=find_packages(),
    entry_points={
        "tutor.plugin.v1": [
            "chalixbrand = tutor_contrib_chalixbrand.plugin"
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
