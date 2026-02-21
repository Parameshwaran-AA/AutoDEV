import subprocess


class LintTool:

    def run_linter(self):
        try:
            result = subprocess.run(
                ["flake8", "workspace/"],
                capture_output=True,
                text=True
            )
            return result.stdout
        except Exception as e:
            return str(e)
