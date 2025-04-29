
from semantic_kernel import Kernel
from semantic_kernel.skill_definition import read_skill_from_python_directory
import os

def initialize_kernel():
    kernel = Kernel()
    skill_path = os.path.join(os.path.dirname(__file__), "skills")
    journal_skill = read_skill_from_python_directory(skill_path, "journal")
    kernel.import_skill(journal_skill, "journal")
    return kernel
