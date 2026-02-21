import subprocess


class TestTool:

    def run_tests(self):
        try:
            result = subprocess.run(
                ["pytest", "workspace/"],
                capture_output=True,
                text=True
            )
            return result.stdout
        except Exception as e:
            return str(e)
