import os

assert "LICENSE" in os.listdir(), "This script should be executed from the root directory of the project."

readme_filename = "README.md"
headers = "## {}\n"
stmt1 = "\nThe latest versions of:\n"

os.chdir("./jupyterlab")

packages = open("packages.txt", "r").readlines()
packages = list(map(lambda x: "- " + x, packages))
packages = "".join(packages)

readme_content = open(readme_filename, "r").readlines()
package_index = readme_content.index(headers.format("Packages"))
usage_index = readme_content.index(headers.format("Usage"))

final_readme = readme_content[0:package_index + 1] + [stmt1, packages] + readme_content[usage_index:]

with open(readme_filename, "w") as f:
	f.writelines(final_readme)
