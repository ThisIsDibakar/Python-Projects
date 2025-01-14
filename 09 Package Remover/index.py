import os

# List of unnecessary packages to remove
packagesToRemove = [
    # List package names separated by commas
]

# Uninstall each package
for package in packagesToRemove:
    os.system(f"pip uninstall -y {package}")
