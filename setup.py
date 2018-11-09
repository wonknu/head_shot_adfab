import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
  name="Adfab shooter",
  options={"build_exe": {"packages":["pygame"], "include_files":["assets/images/heart.png"]}},
  executables = executables
)